# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class LoanPaymentScheduleAdditionalItemMixin(models.AbstractModel):
    _name = "loan.payment_schedule_additional_item_mixin"
    _description = "Loan Payment Schedule Additional Item Mixin"

    schedule_id = fields.Many2one(
        string="Schedule",
        comodel_name="loan.payment_schedule_mixin",
        ondelete="cascade",
        copy=False,
    )
    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency",
        related="schedule_id.loan_id.currency_id",
        store=True,
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
        required=True,
    )
    additional_item_id = fields.Many2one(
        string="Additional Item",
        comodel_name="loan.additional_item",
        ondelete="restrict",
        required=True,
    )
    amount = fields.Monetary(
        string="Amount",
        required=True,
        currency_field="currency_id",
    )
    journal_id = fields.Many2one(
        string="Journal",
        comodel_name="account.journal",
        required=True,
    )
    reconcilliation_account_id = fields.Many2one(
        string="Reconcilliation Account",
        comodel_name="account.account",
        required=True,
    )
    contra_reconcilliation_account_id = fields.Many2one(
        string="Contra-Reconcilliation Account",
        comodel_name="account.account",
        required=True,
    )
    move_line_id = fields.Many2one(
        string="Move Line",
        comodel_name="account.move.line",
        readonly=True,
        ondelete="restrict",
    )
    move_id = fields.Many2one(
        string="# Accounting Entry",
        comodel_name="account.move",
        related="move_line_id.move_id",
        readonly=True,
        store=True,
        ondelete="restrict",
    )

    @api.depends(
        "move_line_id",
        "move_line_id.matched_debit_ids",
        "move_line_id.matched_credit_ids",
    )
    def _compute_state(self):
        for record in self:
            move_line = record.move_line_id

            if not move_line:
                record.state = "unpaid"
            elif (
                not move_line.reconciled
                and not move_line.matched_debit_ids
                and not move_line.matched_credit_ids
            ):
                record.state = "unpaid"
            elif not move_line.reconciled:
                record.state = "partial"
            elif move_line.reconciled:
                record.state = "paid"

    state = fields.Selection(
        string="State",
        selection=[
            ("unpaid", "Unpaid"),
            ("partial", "Partial Paid"),
            ("paid", "Paid"),
        ],
        compute="_compute_state",
        store=True,
        copy=False,
        compute_sudo=True,
    )

    @api.onchange(
        "schedule_id",
        "additional_item_id",
    )
    def onchange_journal_id(self):
        self.journal_id = False
        if self.schedule_id and self.additional_item_id:
            loan_type = self.schedule_id.loan_id.type_id
            if loan_type.direction == "out":
                self.journal_id = self.additional_item_id.receivable_journal_id
            elif loan_type.direction == "in":
                self.journal_id = self.additional_item_id.payable_journal_id

    @api.onchange(
        "schedule_id",
        "additional_item_id",
    )
    def onchange_reconcilliation_account_id(self):
        self.reconcilliation_account_id = False
        if self.schedule_id and self.additional_item_id:
            loan_type = self.schedule_id.loan_id.type_id
            if loan_type.direction == "out":
                self.reconcilliation_account_id = (
                    self.additional_item_id.receivable_account_id
                )
            elif loan_type.direction == "in":
                self.reconcilliation_account_id = (
                    self.additional_item_id.payable_account_id
                )

    @api.onchange(
        "schedule_id",
        "additional_item_id",
    )
    def onchange_contra_reconcilliation_account_id(self):
        self.contra_reconcilliation_account_id = False
        if self.schedule_id and self.additional_item_id:
            loan_type = self.schedule_id.loan_id.type_id
            if loan_type.direction == "out":
                self.contra_reconcilliation_account_id = (
                    self.additional_item_id.contra_receivable_account_id
                )
            elif loan_type.direction == "in":
                self.contra_reconcilliation_account_id = (
                    self.additional_item_id.contra_payable_account_id
                )

    def action_create_accounting_entry(self):
        for record in self:
            record._create_accounting_entry()

    def action_delete_accounting_entry(self):
        for record in self:
            record._delete_accounting_entry()

    def _delete_accounting_entry(self):
        self.ensure_one()
        move = self.move_id
        self.write(
            {
                "move_line_id": False,
            }
        )
        move.with_context(force_delete=True).unlink()

    def _create_accounting_entry(self):
        self.ensure_one()
        AccountMove = self.env["account.move"]
        move = AccountMove.create(self._prepare_account_move())
        reconcilliation_ml = self._create_reconcilliation_ml(move)
        self._create_contra_reconcilliation_ml(move)
        self.write(
            {
                "move_line_id": reconcilliation_ml.id,
            }
        )

    def _prepare_account_move(self):
        self.ensure_one()
        return {
            "name": "/",
            "journal_id": self.journal_id.id,
            "date": self.schedule_id.schedule_date,
            "ref": self.schedule_id.loan_id.id,
        }

    def _create_reconcilliation_ml(self, move):
        self.ensure_one()
        AccountMoveLine = self.env["account.move.line"]
        return AccountMoveLine.with_context(check_move_validity=False).create(
            self._prepare_reconcilliation_ml(move)
        )

    def _create_contra_reconcilliation_ml(self, move):
        self.ensure_one()
        AccountMoveLine = self.env["account.move.line"]
        return AccountMoveLine.with_context(check_move_validity=False).create(
            self._prepare_contra_reconcilliation_ml(move)
        )

    def _prepare_ml(
        self,
        move,
        name,
        account,
        debit,
        credit,
        currency,
        amount_currency,
        partner,
        date_maturity=False,
    ):
        self.ensure_one()
        res = {
            "move_id": move.id,
            "name": name,
            "account_id": account.id,
            "credit": credit,
            "debit": debit,
            "currency_id": currency.id,
            "amount_currency": amount_currency,
            "date_maturity": date_maturity or False,
            "partner_id": partner and partner.id or False,
        }
        return res

    def _get_reconcilliation_ml_amount(self):
        self.ensure_one()
        direction = self.schedule_id.loan_id.type_id.direction
        schedule = self.schedule_id
        loan = schedule.loan_id
        debit = credit = 0.0
        amount = self.currency_id._convert(
            from_amount=self.amount,
            to_currency=loan.company_currency_id,
            company=loan.company_id,
            date=schedule.schedule_date,
        )

        if direction == "out":
            debit = amount
            amount_currency = self.amount
        elif direction == "in":
            credit = amount
            amount_currency = -1.0 * self.amount

        return debit, credit, amount_currency

    def _prepare_reconcilliation_ml(self, move):
        self.ensure_one()
        debit, credit, amount_currency = self._get_reconcilliation_ml_amount()
        return self._prepare_ml(
            move=move,
            name=self.additional_item_id.name,
            account=self.reconcilliation_account_id,
            debit=debit,
            credit=credit,
            currency=self.currency_id,
            amount_currency=amount_currency,
            partner=self.schedule_id.loan_id.partner_id,
            date_maturity=self.schedule_id.schedule_date,
        )

    def _get_contra_reconcilliation_ml_amount(self):
        self.ensure_one()
        direction = self.schedule_id.loan_id.type_id.direction
        schedule = self.schedule_id
        loan = schedule.loan_id
        debit = credit = 0.0
        amount = self.currency_id._convert(
            from_amount=self.amount,
            to_currency=loan.company_currency_id,
            company=loan.company_id,
            date=schedule.schedule_date,
        )

        if direction == "in":
            debit = amount
            amount_currency = self.amount
        elif direction == "out":
            credit = amount
            amount_currency = -1.0 * self.amount

        return debit, credit, amount_currency

    def _prepare_contra_reconcilliation_ml(self, move):
        self.ensure_one()
        debit, credit, amount_currency = self._get_contra_reconcilliation_ml_amount()
        return self._prepare_ml(
            move=move,
            name=self.additional_item_id.name,
            account=self.contra_reconcilliation_account_id,
            debit=debit,
            credit=credit,
            currency=self.currency_id,
            amount_currency=amount_currency,
            partner=self.schedule_id.loan_id.partner_id,
            date_maturity=False,
        )
