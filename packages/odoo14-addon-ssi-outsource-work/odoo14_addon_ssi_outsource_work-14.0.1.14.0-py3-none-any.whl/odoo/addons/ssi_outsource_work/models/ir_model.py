# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class IrModel(models.Model):
    _name = "ir.model"
    _inherit = "ir.model"

    outsource_work_aa_selection_method = fields.Selection(
        string="Outsource Work Analytic Account Selection Method",
        selection=[
            ("fixed", "Fixed"),
            ("python", "Python Code"),
        ],
        default="fixed",
    )
    outsource_work_aa_ids = fields.Many2many(
        string="Outsource Work Analytic Accounts",
        comodel_name="account.analytic.account",
        relation="rel_model_2_outsource_work_aa",
        column1="model_id",
        column2="analytic_account_id",
    )
    outsource_work_python_code = fields.Text(
        string="Python Code",
        default="""# Available variables:
#  - env: Odoo Environment on which the action is triggered.
#  - document: record on which the action is triggered; may be void.
#  - result: Return result, the value is list of Analytic Accounts.
result = []""",
        copy=True,
    )
    # Pricelist
    outsource_work_pricelist_selection_method = fields.Selection(
        string="Outsource Work Pricelist Selection Method",
        selection=[
            ("fixed", "Fixed"),
            ("python", "Python Code"),
        ],
        default="fixed",
        required=False,
    )
    outsource_work_pricelist_ids = fields.Many2many(
        string="Allowed Outsource Work Pricelists",
        comodel_name="product.pricelist",
        relation="rel_model_2_outsource_work_pricelist",
        column1="model_id",
        column2="pricelist_id",
    )
    outsource_work_pricelist_python_code = fields.Text(
        string="Python Code for Outsource Work Pricelist",
        default="""# Available variables:
#  - env: Odoo Environment on which the action is triggered.
#  - document: record on which the action is triggered; may be void.
#  - result: Return result, the value is list of Analytic Accounts.
result = []""",
        copy=True,
    )
    # Usage
    outsource_work_usage_selection_method = fields.Selection(
        string="Outsource Work Usage Selection Method",
        selection=[
            ("fixed", "Fixed"),
            ("python", "Python Code"),
        ],
        default="fixed",
        required=False,
    )
    outsource_work_usage_ids = fields.Many2many(
        string="Allowed Outsource Work Usages",
        comodel_name="product.usage_type",
        relation="rel_model_2_outsource_work_usage",
        column1="model_id",
        column2="usage_id",
    )
    outsource_work_usage_python_code = fields.Text(
        string="Python Code for Outsource Work Usage",
        default="""# Available variables:
#  - env: Odoo Environment on which the action is triggered.
#  - document: record on which the action is triggered; may be void.
#  - result: Return result, the value is list of Analytic Accounts.
result = []""",
        copy=True,
    )
