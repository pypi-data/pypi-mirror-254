# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class OutsourceWorkOutstandingType(models.Model):
    _name = "outsource_work_outstanding_type"
    _inherit = ["mixin.master_data"]
    _description = "Outsource Work Outstanding Type"

    payable_journal_id = fields.Many2one(
        string="Payable Journal",
        comodel_name="account.journal",
        company_dependent=True,
    )
    payable_account_id = fields.Many2one(
        string="Payable Account",
        comodel_name="account.account",
        company_dependent=True,
    )
