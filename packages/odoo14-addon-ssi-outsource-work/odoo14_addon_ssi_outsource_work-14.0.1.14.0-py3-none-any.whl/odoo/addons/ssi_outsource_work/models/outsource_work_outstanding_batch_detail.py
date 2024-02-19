# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class OutsourceWorkOutstandingBatchDetail(models.Model):
    _name = "outsource_work_outstanding_batch_detail"
    _description = "Outsource Work Outstanding Batch Detail"

    batch_id = fields.Many2one(
        string="# Batch",
        comodel_name="outsource_work_outstanding_batch",
        required=True,
        ondelete="cascade",
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
    )
    outstanding_id = fields.Many2one(
        string="# Outstanding",
        comodel_name="outsource_work_outstanding",
        readonly=True,
    )

    def _create_outstanding(self):
        self.ensure_one()
        Outstanding = self.env["outsource_work_outstanding"]
        outstanding = Outstanding.create(self._prepare_outstanding_data())
        self.write(
            {
                "outstanding_id": outstanding.id,
            }
        )
        outstanding.action_populate()
        outstanding.action_compute_tax()

    def _prepare_outstanding_data(self):
        self.ensure_one()
        batch = self.batch_id
        return {
            "partner_id": self.partner_id.id,
            "batch_id": batch.id,
            "type_id": batch.type_id.id,
            "currency_id": batch.currency_id.id,
            "date": batch.date,
            "date_due": batch.date_due,
            "date_start": batch.date_start,
            "date_end": batch.date_end,
            "payable_journal_id": batch.type_id.payable_journal_id.id,
            "payable_account_id": batch.type_id.payable_account_id.id,
            "analytic_account_id": batch.analytic_account_id
            and batch.analytic_account_id.id
            or False,
        }
