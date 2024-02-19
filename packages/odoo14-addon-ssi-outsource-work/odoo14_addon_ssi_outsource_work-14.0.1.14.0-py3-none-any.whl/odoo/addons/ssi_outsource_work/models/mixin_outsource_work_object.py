# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from lxml import etree

from odoo import api, fields, models


class MixinOutsourceWorkObject(models.AbstractModel):
    _name = "mixin.outsource_work_object"
    _description = "Outsource Work Object Mixin"

    _work_log_create_page = False
    _work_log_page_xpath = "//page[1]"
    _work_log_template_position = "before"

    outsource_work_ids = fields.One2many(
        string="Outsource Work Logs",
        comodel_name="outsource_work",
        inverse_name="work_object_id",
        domain=lambda self: [("model_name", "=", self._name)],
        auto_join=True,
        readonly=False,
    )

    @api.model
    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        res = super().fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        if view_type == "form" and self._outsource_work_create_page:
            doc = etree.XML(res["arch"])
            node_xpath = doc.xpath(self._work_log_page_xpath)
            if node_xpath:
                str_element = self.env["ir.qweb"]._render(
                    "ssi_outsource_work.outsource_work_template"
                )
                for node in node_xpath:
                    new_node = etree.fromstring(str_element)
                    if self._work_log_template_position == "after":
                        node.addnext(new_node)
                    elif self._work_log_template_position == "before":
                        node.addprevious(new_node)

            View = self.env["ir.ui.view"]

            if view_id and res.get("base_model", self._name) != self._name:
                View = View.with_context(base_model_name=res["base_model"])
            new_arch, new_fields = View.postprocess_and_fields(doc, self._name)
            res["arch"] = new_arch
            new_fields.update(res["fields"])
            res["fields"] = new_fields
        return res

    @api.depends(
        "outsource_work_ids",
        "outsource_work_ids.analytic_account_id",
    )
    def _compute_allowed_analytic_account_ids(self):
        for document in self:
            document.allowed_analytic_account_ids = []

    allowed_analytic_account_ids = fields.Many2many(
        string="Analytic Accounts",
        comodel_name="account.analytic.account",
        compute="_compute_allowed_analytic_account_ids",
    )

    def unlink(self):
        outsource_works = self.mapped("outsource_work_ids")
        outsource_works.unlink()
        return super(MixinOutsourceWorkObject, self).unlink()
