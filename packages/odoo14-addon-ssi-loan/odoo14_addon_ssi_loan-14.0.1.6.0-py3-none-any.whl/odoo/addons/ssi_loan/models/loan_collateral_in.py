# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LoanCollateralIn(models.Model):
    _name = "loan_in.collateral"
    _inherit = ["loan.collateral_mixin"]
    _description = "Loan Collateral In"

    loan_id = fields.Many2one(
        comodel_name="loan.in",
    )
