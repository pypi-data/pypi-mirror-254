# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class OutsourceWorkOutstandingBatch(models.Model):
    _name = "outsource_work_outstanding_batch"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_confirm",
        "mixin.transaction_pricelist",
        "mixin.date_duration",
    ]
    _description = "Outsource Work Outstanding Batch"
    _approval_from_state = "draft"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    # Mixin duration attribute
    _date_start_readonly = True
    _date_end_readonly = True
    _date_start_required = True
    _date_end_required = True
    _date_start_states_list = ["draft"]
    _date_start_states_readonly = ["draft"]
    _date_end_states_list = ["draft"]
    _date_end_states_readonly = ["draft"]

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True

    # Attributes related to add element on form view automatically
    _automatically_insert_multiple_approval_page = True

    _statusbar_visible_label = "open,draft,confirm,done"

    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "cancel_ok",
        "restart_ok",
        "done_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "action_done",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_done",
        "dom_cancel",
    ]

    _create_sequence_state = "done"

    pricelist_id = fields.Many2one(
        required=False,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="outsource_work_outstanding_type",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    date_due = fields.Date(
        string="Date Due",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    detail_ids = fields.One2many(
        string="Outstanding Details",
        comodel_name="outsource_work_outstanding_batch_detail",
        inverse_name="batch_id",
        readonly=True,
        copy=True,
    )
    amount_untaxed = fields.Monetary(
        string="Untaxed",
        required=False,
        compute="_compute_total",
        store=True,
        currency_field="currency_id",
    )
    amount_tax = fields.Monetary(
        string="Tax",
        required=False,
        compute="_compute_total",
        store=True,
        currency_field="currency_id",
    )
    amount_total = fields.Monetary(
        string="Total",
        required=False,
        compute="_compute_total",
        store=True,
        currency_field="currency_id",
    )
    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        copy=False,
        default="draft",
        required=True,
        readonly=True,
    )

    @api.model
    def _get_policy_field(self):
        res = super(OutsourceWorkOutstandingBatch, self)._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "done_ok",
            "cancel_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.depends(
        "detail_ids",
        "detail_ids.outstanding_id",
        "detail_ids.outstanding_id.amount_untaxed",
        "detail_ids.outstanding_id.amount_tax",
        "detail_ids.outstanding_id.amount_total",
    )
    def _compute_total(self):
        for record in self:
            amount_untaxed = amount_tax = amount_total = 0.0
            for detail in record.detail_ids:
                amount_untaxed += detail.outstanding_id.amount_untaxed
                amount_tax += detail.outstanding_id.amount_tax
                amount_total += detail.outstanding_id.amount_total

            record.amount_untaxed = amount_untaxed
            record.amount_tax = amount_tax
            record.amount_total = amount_untaxed + amount_tax

    def action_populate(self):
        for record in self:
            record._populate()

    def action_clear(self):
        for record in self:
            record._unlink_detail()

    @ssi_decorator.post_confirm_action()
    def _post_confirm_action_10_confirm_outstanding(self):
        self.ensure_one()
        for detail in self.detail_ids:
            outstanding = detail.outstanding_id
            outstanding.action_populate()
            if outstanding.confirm_ok:
                outstanding.action_confirm()

    @ssi_decorator.post_approve_action()
    def _post_approve_action_10_approve_outstanding(self):
        self.ensure_one()
        for detail in self.detail_ids:
            outstanding = detail.outstanding_id
            if outstanding.approve_ok:
                outstanding.action_approve_approval()

    @ssi_decorator.post_reject_action()
    def _post_reject_action_10_reject_outstanding(self):
        self.ensure_one()
        for detail in self.detail_ids:
            outstanding = detail.outstanding_id
            if outstanding.reject_ok:
                outstanding.action_reject_approval()

    @ssi_decorator.post_restart_action()
    def _post_restart_action_10_restart_outstanding(self):
        self.ensure_one()
        for detail in self.detail_ids:
            outstanding = detail.outstanding_id
            if outstanding.restart_ok:
                outstanding.action_restart()

    @ssi_decorator.post_cancel_action()
    def _post_cancel_action_10_cancel_outstanding(self):
        self.ensure_one()
        for detail in self.detail_ids:
            outstanding = detail.outstanding_id
            if outstanding.cancel_ok:
                outstanding.action_cancel(self.cancel_reason_id)

    def _populate(self):
        self.ensure_one()
        Work = self.env["outsource_work"]
        Detail = self.env["outsource_work_outstanding_batch_detail"]
        self._unlink_detail()
        criteria = self._prepare_populate_domain()
        works = Work.search(criteria)
        partners = works.mapped("partner_id")
        for partner in partners:
            Detail.create(
                {
                    "batch_id": self.id,
                    "partner_id": partner.id,
                }
            )
        for detail in self.detail_ids:
            detail._create_outstanding()

    def _unlink_detail(self):
        self.ensure_one()
        for detail in self.detail_ids:
            detail.outstanding_id.unlink()
        self.detail_ids.unlink()

    def _prepare_populate_domain(self):
        self.ensure_one()
        result = [
            ("date", ">=", self.date_start),
            ("date", "<=", self.date_end),
            ("outstanding_id", "=", False),
            ("currency_id", "=", self.currency_id.id),
            ("state", "=", "done"),
        ]
        if self.analytic_account_id:
            result.append(("analytic_account_id", "=", self.analytic_account_id.id))
        return result

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
