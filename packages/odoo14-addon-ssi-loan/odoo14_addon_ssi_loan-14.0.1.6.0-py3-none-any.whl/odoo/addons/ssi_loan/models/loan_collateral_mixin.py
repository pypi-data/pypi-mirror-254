# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class LoanCollateralMixin(models.AbstractModel):
    _name = "loan.collateral_mixin"
    _description = "Loan Collateral Mixin"
    _order = "sequence, id, loan_id"

    loan_id = fields.Many2one(
        string="# Loan",
        comodel_name="loan.mixin",
        ondelete="cascade",
        copy=False,
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="loan_collateral_type",
        required=True,
    )
    name = fields.Char(
        string="Collateral Name",
        required=True,
    )
