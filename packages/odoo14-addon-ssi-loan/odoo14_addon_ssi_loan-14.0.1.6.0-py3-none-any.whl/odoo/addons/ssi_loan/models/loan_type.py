# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from dateutil import relativedelta

from odoo import api, fields, models


class LoanType(models.Model):
    _name = "loan.type"
    _inherit = ["mixin.master_data"]
    _description = "Loan Type"

    name = fields.Char(
        string="Loan Type",
    )
    direction = fields.Selection(
        string="Direction",
        selection=[
            ("in", "In"),
            ("out", "Out"),
        ],
        required=True,
    )
    interest_method = fields.Selection(
        string="Interest Method",
        selection=[
            ("anuity", "Anuity"),
            ("flat", "Flat"),
            ("effective", "Effective"),
        ],
        required=True,
        default="anuity",
        company_dependent=True,
    )
    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency",
        required=True,
    )
    interest_amount = fields.Float(
        string="Interest Amount",
        company_dependent=True,
    )
    maximum_loan_amount = fields.Float(
        string="Maximum Loan Amount",
        required=True,
        company_dependent=True,
    )
    maximum_installment_period = fields.Integer(
        string="Maximum Installment Period",
        company_dependent=True,
    )
    realization_journal_id = fields.Many2one(
        string="Realization Journal",
        comodel_name="account.journal",
        company_dependent=True,
        domain=[
            ("type", "=", "general"),
        ],
    )
    account_realization_id = fields.Many2one(
        string="Realization Account",
        comodel_name="account.account",
        company_dependent=True,
        help="Account that will server as cross-account for realization.\n\n"
        "It will use as debit account for loan in or "
        "credit account for loan out",
    )
    account_rounding_id = fields.Many2one(
        string="Rounding Account",
        comodel_name="account.account",
        company_dependent=True,
    )
    interest_journal_id = fields.Many2one(
        string="Interest Journal",
        comodel_name="account.journal",
        company_dependent=True,
    )
    account_interest_id = fields.Many2one(
        string="Interest Account",
        comodel_name="account.account",
        company_dependent=True,
    )
    account_interest_income_id = fields.Many2one(
        string="Interest Income Account",
        comodel_name="account.account",
        company_dependent=True,
    )
    short_account_principle_id = fields.Many2one(
        string="Short-Term Principle Account",
        comodel_name="account.account",
        company_dependent=True,
    )
    long_account_principle_id = fields.Many2one(
        string="Long-Term Principle Account",
        comodel_name="account.account",
        company_dependent=True,
    )

    @api.depends(
        "direction",
    )
    def _compute_allowed_additional_item(self):
        LoanAdditionalItem = self.env["loan.additional_item"]
        for record in self:
            result = []
            if record.direction == "out":
                criteria = [
                    ("loan_out_ok", "=", True),
                ]
            elif record.direction == "in":
                criteria = [
                    ("loan_in_ok", "=", True),
                ]
            else:
                criteria = False

            if criteria:
                result = LoanAdditionalItem.search(criteria).ids

            record.allowed_additional_item_ids = result

    allowed_additional_item_ids = fields.Many2many(
        string="Allowed Additional Items",
        comodel_name="loan.additional_item",
        compute="_compute_allowed_additional_item",
    )

    additional_item_ids = fields.Many2many(
        string="Additional Items",
        comodel_name="loan.additional_item",
        relation="rel_loan_type_2_additional_item",
        column1="type_id",
        column2="additional_item_id",
    )

    @api.model
    def _compute_interest(
        self, loan_amount, interest, period, first_payment_date, interest_method
    ):
        if interest_method == "flat":
            return self._compute_flat(loan_amount, interest, period, first_payment_date)
        elif interest_method == "effective":
            return self._compute_effective(
                loan_amount, interest, period, first_payment_date
            )
        elif interest_method == "anuity":
            return self._compute_anuity(
                loan_amount, interest, period, first_payment_date
            )

    @api.model
    def _compute_flat(self, loan_amount, interest, period, first_payment_date):
        result = []

        principle_amount = loan_amount / period
        interest_amount = (loan_amount * (interest / 100.00)) / 12.0
        first_payment_date = next_payment_date = fields.Date.to_date(first_payment_date)
        for _loan_period in range(1, period + 1):
            res = {
                "schedule_date": fields.Date.to_string(next_payment_date),
                "principle_amount": principle_amount,
                "interest_amount": interest_amount,
            }
            result.append(res)
            next_payment_date = next_payment_date + relativedelta.relativedelta(
                months=+1,
                day=first_payment_date.day,
            )
        return result

    @api.model
    def _compute_effective(self, loan_amount, interest, period, first_payment_date):
        result = []
        principle_amount = loan_amount / float(period)
        interest_dec = interest / 100.00
        first_payment_date = next_payment_date = fields.Date.to_date(first_payment_date)
        for loan_period in range(1, period + 1):
            period_before = loan_period - 1
            interest_amount = (
                (loan_amount - (period_before * principle_amount))
                * interest_dec
                / 12.00
            )
            res = {
                "schedule_date": fields.Date.to_string(next_payment_date),
                "principle_amount": principle_amount,
                "interest_amount": interest_amount,
            }
            result.append(res)
            next_payment_date = next_payment_date + relativedelta.relativedelta(
                months=+1,
                day=first_payment_date.day,
            )
        return result

    @api.model
    def _compute_anuity(self, loan_amount, interest, period, first_payment_date):
        result = []
        interest_decimal = interest / 100.00
        total_principle_amount = 0.0
        fixed_principle_amount = loan_amount * (
            (interest_decimal / 12.0)
            / (1.0 - (1.0 + (interest_decimal / 12.00)) ** -float(period))
        )
        first_payment_date = next_payment_date = fields.Date.to_date(first_payment_date)
        for _loan_period in range(1, period + 1):
            interest_amount = (
                (loan_amount - total_principle_amount) * interest_decimal / 12.00
            )
            principle_amount = fixed_principle_amount - interest_amount
            res = {
                "schedule_date": fields.Date.to_string(next_payment_date),
                "principle_amount": principle_amount,
                "interest_amount": interest_amount,
            }
            result.append(res)
            total_principle_amount += principle_amount
            next_payment_date = next_payment_date + relativedelta.relativedelta(
                months=+1,
                day=first_payment_date.day,
            )
        return result
