# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LoanOut(models.Model):
    _name = "loan.out"
    _inherit = ["loan.mixin"]
    _description = "Loan Out"

    type_id = fields.Many2one(
        domain=[
            ("direction", "=", "out"),
        ],
    )
    direction = fields.Selection(
        related="type_id.direction",
        store=True,
    )
    payment_schedule_ids = fields.One2many(
        comodel_name="loan.payment_schedule_out",
    )
    collateral_ids = fields.One2many(
        comodel_name="loan_out.collateral",
    )
