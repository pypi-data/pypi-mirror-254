# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.addons.ssi_decorator import ssi_decorator


class LoanMixin(models.AbstractModel):
    _name = "loan.mixin"
    _inherit = [
        "mixin.currency",
        "mixin.company_currency",
        "mixin.transaction_confirm",
        "mixin.transaction_ready",
        "mixin.transaction_open",
        "mixin.transaction_done",
        "mixin.transaction_cancel",
    ]
    _description = "Loan Mixin"

    _exchange_date_field = "date"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "ready"
    _approval_state = "confirm"
    _after_approved_method = "action_ready"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True

    # Attributes related to add element on form view automatically
    _automatically_insert_multiple_approval_page = True
    _automatically_insert_open_policy_fields = False
    _automatically_insert_open_button = False
    _automatically_insert_done_policy_fields = False
    _automatically_insert_done_button = False

    _statusbar_visible_label = "draft,confirm,ready,open,done"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "cancel_ok",
        "restart_ok",
        "done_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "action_done",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_open",
        "dom_done",
        "dom_cancel",
    ]

    # Sequence attribute
    _create_sequence_state = "ready"

    date = fields.Date(
        string="Date Transaction",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    date_cutoff = fields.Date(
        string="Date Cut-Off",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        readonly=True,
        domain=[
            "|",
            "&",
            ("parent_id", "=", False),
            ("is_company", "=", False),
            ("is_company", "=", True),
        ],
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    request_date = fields.Date(
        string="Request Date",
        required=True,
        default=fields.Date.today(),
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    type_id = fields.Many2one(
        string="Loan Type",
        comodel_name="loan.type",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    currency_id = fields.Many2one(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    rate_inverted = fields.Boolean(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    rate = fields.Monetary(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.model
    def _default_direction(self):
        return "out"

    direction = fields.Selection(
        string="Direction",
        selection=[
            ("in", "In"),
            ("out", "Out"),
        ],
        default=lambda self: self._default_direction(),
    )
    loan_amount = fields.Monetary(
        string="Loan Amount",
        required=True,
        readonly=True,
        currency_field="currency_id",
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    maximum_loan_amount = fields.Float(
        string="Maximum Loan Amount",
        readonly=True,
        copy=False,
    )
    interest = fields.Float(
        string="Interest (p.a)",
        readonly=True,
        required=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    maximum_installment_period = fields.Integer(
        string="Maximum Installment Period",
        readonly=True,
        copy=False,
    )
    manual_loan_period = fields.Integer(
        string="Loan Period",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        required=True,
    )
    first_payment_date = fields.Date(
        string="First Payment Date",
        readonly=True,
        required=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    move_realization_id = fields.Many2one(
        string="Realization Journal Entry",
        comodel_name="account.move",
        readonly=True,
        copy=False,
    )
    move_line_header_id = fields.Many2one(
        string="Realization Move Line Header",
        comodel_name="account.move.line",
        readonly=True,
        copy=False,
    )

    @api.depends(
        "move_line_header_id",
        "move_line_header_id.matched_debit_ids",
        "move_line_header_id.matched_credit_ids",
    )
    def _compute_realized(self):
        for record in self:
            result = False

            if record.move_line_header_id.reconciled:
                result = True

            record.realized = result

    realized = fields.Boolean(
        string="Realized",
        compute="_compute_realized",
        store=True,
    )
    payment_schedule_ids = fields.One2many(
        string="Payment Schedules",
        comodel_name="loan.payment_schedule_mixin",
        inverse_name="loan_id",
        copy=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.depends(
        "payment_schedule_ids",
        "payment_schedule_ids.principle_amount",
        "payment_schedule_ids.interest_amount",
        "payment_schedule_ids.principle_payment_state",
    )
    def _compute_total(self):
        for loan in self:
            loan.total_principle_amount = (
                loan.total_interest_amount
            ) = loan.total_manual_principle_amount = 0.0
            if loan.payment_schedule_ids:
                for schedule in loan.payment_schedule_ids:
                    if schedule.principle_payment_state == "manual":
                        loan.total_manual_principle_amount += schedule.principle_amount
                    else:
                        loan.total_principle_amount += schedule.principle_amount
                    loan.total_interest_amount += schedule.interest_amount

    total_manual_principle_amount = fields.Monetary(
        string="Total Manual Principle Amount",
        compute="_compute_total",
        store=True,
        currency_field="currency_id",
    )
    total_principle_amount = fields.Monetary(
        string="Total Principle Amount",
        compute="_compute_total",
        store=True,
        currency_field="currency_id",
    )
    total_interest_amount = fields.Monetary(
        string="Total Interest Amount",
        compute="_compute_total",
        store=True,
        currency_field="currency_id",
    )

    @api.depends(
        "payment_schedule_ids",
        "payment_schedule_ids.principle_payment_state",
        "payment_schedule_ids.interest_payment_state",
    )
    def _compute_paid(self):
        for record in self:
            result = True

            if len(record.payment_schedule_ids) == 0:
                result = False

            for payment in record.payment_schedule_ids:
                if payment.principle_payment_state not in ["paid", "manual"] or (
                    payment.interest_amount
                    and payment.interest_payment_state not in ["paid", "manual"]
                ):
                    result = False
                    break
            record.paid = result

    paid = fields.Boolean(
        string="Paid",
        compute="_compute_paid",
        store=True,
    )
    collateral_ids = fields.One2many(
        string="Collaterals",
        comodel_name="loan.collateral_mixin",
        inverse_name="loan_id",
        copy=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("ready", "Ready to Process"),
            ("open", "In Progress"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
            ("reject", "Rejected"),
        ],
        default="draft",
        copy=False,
    )

    @api.model
    def _get_policy_field(self):
        res = super(LoanMixin, self)._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "open_ok",
            "ready_ok",
            "done_ok",
            "cancel_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.onchange("type_id")
    def onchange_maximum_loan_amount(self):
        self.maximum_loan_amount = 0.0
        if self.type_id:
            self.maximum_loan_amount = self.type_id.maximum_loan_amount

    @api.onchange("type_id")
    def onchange_maximum_installment_period(self):
        self.maximum_installment_period = 0.0
        if self.type_id:
            self.maximum_installment_period = self.type_id.maximum_installment_period

    @api.onchange("type_id")
    def onchange_interest(self):
        self.interest = 0.0
        if self.type_id:
            self.interest = self.type_id.interest_amount

    @api.onchange(
        "date",
    )
    def onchange_rate(self):
        self.onchange_rate_mixin()

    def action_compute_payment(self):
        for record in self.sudo():
            record._compute_payment()

    def _compute_payment(self):
        self.ensure_one()
        schedule_object_name = self.payment_schedule_ids._name

        obj_payment = self.env[schedule_object_name]
        obj_loan_type = self.env["loan.type"]

        self.payment_schedule_ids.unlink()

        payment_datas = obj_loan_type._compute_interest(
            self.loan_amount,
            self.interest,
            self.manual_loan_period,
            self.first_payment_date,
            self.type_id.interest_method,
        )

        for payment_data in payment_datas:
            payment_data.update({"loan_id": self.id})
            obj_payment.create(payment_data)

    def _create_realization_move(self):
        self.ensure_one()
        obj_move = self.env["account.move"]
        obj_line = self.env["account.move.line"]

        move = obj_move.create(self._prepare_realization_move())

        move_line_header = obj_line.with_context(check_move_validity=False).create(
            self._prepare_header_move_line(move)
        )

        for schedule in self.payment_schedule_ids.filtered(
            lambda r: r.principle_payment_state != "manual"
        ):
            schedule._create_principle_receivable_move_line(move)

        debit = credit = 0.0
        for line in move.line_ids:
            debit += line.debit
            credit += line.credit

        if debit != credit:
            amount = debit - credit
            obj_line.with_context(check_move_validity=False).create(
                self._prepare_rounding_move_line(move, amount)
            )

        move.action_post()

        return move.id, move_line_header.id

    def _prepare_realization_move(self):
        self.ensure_one()
        res = {
            "name": "/",
            "journal_id": self._get_realization_journal().id,
            "date": self.date_cutoff and self.date_cutoff or self.date,
            "ref": self.name,
            "currency_id": self.currency_id.id,
        }
        return res

    def _get_realization_journal(self):
        self.ensure_one()
        journal = self.type_id.realization_journal_id

        if not journal:
            msg = _("No realization journal defined")
            raise UserError(msg)

        return journal

    def _prepare_header_move_line(self, move):
        self.ensure_one()
        name = _("%s loan realization") % (self.name)
        debit, credit, amount_currency = self._get_realization_move_line_header_amount()
        res = {
            "move_id": move.id,
            "name": name,
            "account_id": self._get_realization_account().id,
            "debit": debit,
            "credit": credit,
            "partner_id": self.partner_id.id,
            "currency_id": self.currency_id.id,
            "amount_currency": amount_currency,
        }
        return res

    def _get_realization_move_line_header_amount(self):
        self.ensure_one()
        debit = credit = amount_currency = 0.0

        total_principle_amount = self._convert_amount_to_company_currency(
            self.total_principle_amount
        )

        if self.direction == "out":
            credit = total_principle_amount
            amount_currency = -1.0 * self.total_principle_amount
        else:
            debit = total_principle_amount
            amount_currency = self.total_principle_amount
        return debit, credit, amount_currency

    def _get_realization_account(self):
        self.ensure_one()
        account = self.type_id.account_realization_id

        if not account:
            msg = _("No realization account defined")
            raise UserError(msg)

        return account

    def _get_rounding_amount(self, amount):
        debit = credit = amount_currency = 0.0

        rounding_amount = self._convert_amount_to_company_currency(abs(amount))

        if rounding_amount < 0.0:
            credit = rounding_amount
            amount_currency = -1.0 * abs(amount)
        else:
            debit = rounding_amount
            amount_currency = abs(amount)
        return debit, credit, amount_currency

    def _prepare_rounding_move_line(self, move, amount):
        self.ensure_one()
        name = _("%s loan rounding") % (self.name)
        debit, credit, amount_currency = self._get_rounding_amount(amount)
        res = {
            "move_id": move.id,
            "name": name,
            "account_id": self._get_rounding_account().id,
            "debit": debit,
            "credit": credit,
            "partner_id": self.partner_id.id,
            "currency_id": self.currency_id.id,
            "amount_currency": amount_currency,
        }
        return res

    def _get_rounding_account(self):
        self.ensure_one()
        account = self.type_id.account_rounding_id

        if not account:
            msg = _("No rounding account defined")
            raise UserError(msg)

        return account

    def _prepare_ready_data(self):
        self.ensure_one()
        _super = super(LoanMixin, self)
        result = _super._prepare_ready_data()
        if not self.move_realization_id:
            move_id, move_line_header_id = self._create_realization_move()
            result.update(
                {
                    "move_realization_id": move_id,
                    "move_line_header_id": move_line_header_id,
                }
            )
        return result

    def _prepare_cancel_data(self, cancel_reason=False):
        self.ensure_one()
        _super = super(LoanMixin, self)
        result = _super._prepare_cancel_data()
        if self.move_realization_id:
            move = self.move_realization_id
            self.write(
                {
                    "move_realization_id": False,
                    "move_line_header_id": False,
                }
            )
            move.with_context(force_delete=True).unlink()
        return result

    def _check_interest_realization_move(self):
        self.ensure_one()

        result = True
        schedules = self.payment_schedule_ids.filtered(
            lambda r: r.interest_move_line_id
        )

        if len(schedules) > 0:
            error_msg = """You cannot cancel loan with realized interest.

        Unrealized all interest first
            """
            result = False
            raise ValidationError(_(error_msg))

        return result

    def _check_payment(self):
        self.ensure_one()

        result = True
        schedules = self.payment_schedule_ids.filtered(
            lambda r: r.principle_payment_state in ["partial", "paid"]
            or r.interest_payment_state in ["partial", "paid"]
        )

        if len(schedules) > 0:
            error_msg = """You cannot cancel loan with paid principle or interest.

        Cancel all principle or interest payment
            """
            result = False
            raise ValidationError(_(error_msg))

        return result

    def _check_loan_realization(self):
        self.ensure_one()

        result = True
        if self.realized:
            error_msg = """You cannot cancel realized loan

        Cancel loan realization entry
            """
            result = False
            raise ValidationError(_(error_msg))

        return result

    def action_cancel(self, cancel_reason=False):
        _super = super(LoanMixin, self)

        for record in self.sudo():
            record._check_interest_realization_move()
            record._check_payment()
            record._check_loan_realization()

        _super.action_cancel(cancel_reason)

    @ssi_decorator.pre_confirm_check()
    def _check_total_principle_amount(self):
        self.ensure_one()
        if self.total_principle_amount != self.loan_amount:
            total_principle_amount = '{:0,.2f}'.format(self.total_principle_amount)
            loan_amount = '{:0,.2f}'.format(self.loan_amount)
            raise ValidationError(_(
                f'Total principal amount ({total_principle_amount}) '
                f'different with loan amount ({loan_amount}).'))
