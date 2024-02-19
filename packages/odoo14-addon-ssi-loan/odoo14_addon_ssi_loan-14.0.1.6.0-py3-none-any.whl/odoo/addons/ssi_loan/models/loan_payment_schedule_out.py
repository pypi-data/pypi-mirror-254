# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LoanPaymentScheduleOut(models.Model):
    _name = "loan.payment_schedule_out"
    _inherit = ["loan.payment_schedule_mixin"]
    _description = "Loan Out Payment Schedule"

    loan_id = fields.Many2one(
        comodel_name="loan.out",
    )
    principle_move_id = fields.Many2one(
        comodel_name="account.move",
        related="principle_move_line_id.move_id",
    )
    interest_move_id = fields.Many2one(
        comodel_name="account.move",
        related="interest_move_line_id.move_id",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        related="loan_id.partner_id",
        store=True,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="loan_id.currency_id",
        store=False,
    )
    state = fields.Selection(
        related="loan_id.state",
        store=True,
    )
    additional_item_ids = fields.One2many(
        comodel_name="loan.payment_schedule_out_additional_item",
    )
