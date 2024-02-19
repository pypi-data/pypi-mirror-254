# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models


class LoanCollateralType(models.Model):
    _name = "loan_collateral_type"
    _inherit = ["mixin.master_data"]
    _description = "Loan Collateral Type"
