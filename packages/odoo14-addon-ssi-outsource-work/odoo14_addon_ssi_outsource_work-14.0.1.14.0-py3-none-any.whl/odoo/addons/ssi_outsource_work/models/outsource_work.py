# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval

from odoo.addons.ssi_decorator import ssi_decorator


class OutsourceWork(models.Model):
    _name = "outsource_work"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_confirm",
        "mixin.product_line_account",
    ]
    _description = "Outsource Work"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True

    # Attributes related to add element on form view automatically
    _automatically_insert_multiple_approval_page = True
    _statusbar_visible_label = "draft,confirm,done,rejected"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "cancel_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
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

    # Sequence attribute
    _create_sequence_state = "done"

    @api.model
    def _default_model_id(self):
        model = False
        obj_ir_model = self.env["ir.model"]
        model_name = self.env.context.get("outsource_work_model", False)
        if model_name:
            criteria = [("model", "=", model_name)]
            model = obj_ir_model.search(criteria)
        return model

    model_id = fields.Many2one(
        string="Document Type",
        comodel_name="ir.model",
        index=True,
        required=True,
        ondelete="cascade",
        default=lambda self: self._default_model_id(),
        readonly=True,
    )
    model_name = fields.Char(
        related="model_id.model",
        index=True,
        store=True,
    )
    work_object_id = fields.Many2oneReference(
        string="Document ID",
        index=True,
        required=True,
        readonly=False,
        model_field="model_name",
    )

    @api.model
    def _selection_target_model(self):
        return [(model.model, model.name) for model in self.env["ir.model"].search([])]

    @api.depends(
        "model_id",
        "work_object_id",
    )
    def _compute_work_object_reference(self):
        for document in self:
            result = False
            if document.model_id and document.work_object_id:
                result = "%s,%s" % (document.model_name, document.work_object_id)
            document.work_object_reference = result

    work_object_reference = fields.Reference(
        string="Document Reference",
        compute="_compute_work_object_reference",
        store=True,
        selection="_selection_target_model",
    )

    @api.model
    def _default_date(self):
        return fields.Date.today()

    date = fields.Date(
        string="Date",
        required=True,
        default=lambda self: self._default_date(),
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        index=True,
        required=True,
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="outsource_work_type",
        index=True,
        required=True,
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        related="type_id.product_id",
        store=True,
    )

    @api.depends(
        "model_id",
    )
    def _compute_allowed_analytic_account_ids(self):
        for document in self:
            result = []
            if document.model_id:
                model = document.model_id
                if model.outsource_work_aa_selection_method == "fixed":
                    if model.outsource_work_aa_ids:
                        result = model.outsource_work_aa_ids.ids
                elif model.outsource_work_aa_selection_method == "python":
                    analytic_account_ids = self._evaluate_analytic_account(model)
                    if analytic_account_ids:
                        result = analytic_account_ids
            document.allowed_analytic_account_ids = result

    allowed_analytic_account_ids = fields.Many2many(
        string="Allowed Analytic Accounts",
        comodel_name="account.analytic.account",
        compute="_compute_allowed_analytic_account_ids",
        store=False,
    )
    allowed_pricelist_ids = fields.Many2many(
        string="Allowed Pricelist",
        comodel_name="product.pricelist",
        compute="_compute_allowed_pricelist_ids",
    )

    @api.depends(
        "model_id",
    )
    def _compute_allowed_usage_ids(self):
        Usage = self.env["product.usage_type"]
        for document in self:
            result = []
            if document.model_id:
                model = document.model_id
                if model.outsource_work_usage_selection_method == "fixed":
                    if model.outsource_work_usage_ids:
                        result += model.outsource_work_usage_ids.ids
                elif model.outsource_work_usage_selection_method == "python":
                    usage_ids = self._evaluate_worklog_usage(model)
                    if usage_ids:
                        result = usage_ids
                if len(result) > 0:
                    criteria = [
                        ("id", "in", result),
                    ]
                    result = Usage.search(criteria).ids
            document.allowed_usage_ids = result

    allowed_usage_ids = fields.Many2many(
        string="Allowed Usage",
        comodel_name="product.usage_type",
        compute="_compute_allowed_usage_ids",
    )

    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    outstanding_id = fields.Many2one(
        string="# Outstanding",
        comodel_name="outsource_work_outstanding",
        readonly=True,
    )
    reconciled = fields.Boolean(
        related="outstanding_id.reconciled",
        store=True,
    )
    batch_id = fields.Many2one(
        string="# Outstanding Batch",
        related="outstanding_id.batch_id",
        store=True,
    )
    account_move_line_id = fields.Many2one(
        string="Journal Item",
        comodel_name="account.move.line",
        readonly=True,
        copy=False,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
            ("reject", "Rejected"),
        ],
        default="draft",
        copy=False,
    )

    @api.depends(
        "model_id",
        "currency_id",
    )
    def _compute_allowed_pricelist_ids(self):
        Pricelist = self.env["product.pricelist"]
        for document in self:
            result = []
            if document.model_id:
                model = document.model_id
                if model.outsource_work_pricelist_selection_method == "fixed":
                    if model.outsource_work_pricelist_ids:
                        result += model.outsource_work_pricelist_ids.ids
                elif model.outsource_work_pricelist_selection_method == "python":
                    pricelist_ids = self._evaluate_worklog_pricelist(model)
                    if pricelist_ids:
                        result = pricelist_ids
                if len(result) > 0:
                    criteria = [
                        ("id", "in", result),
                        ("currency_id", "=", document.currency_id.id),
                    ]
                    result = Pricelist.search(criteria).ids
            document.allowed_pricelist_ids = result

    @api.model
    def _get_policy_field(self):
        res = super(OutsourceWork, self)._get_policy_field()
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

    def _get_localdict(self):
        self.ensure_one()
        object = self.env[self.model_name]
        document = object.browse(self.work_object_id)
        return {
            "env": self.env,
            "document": document,
        }

    def _evaluate_analytic_account(self, model):
        self.ensure_one()
        res = False
        localdict = self._get_localdict()
        try:
            safe_eval(
                model.outsource_work_python_code, localdict, mode="exec", nocopy=True
            )
            if "result" in localdict:
                res = localdict["result"]
        except Exception as error:
            msg_err = _("Error evaluating conditions.\n %s") % error
            raise UserError(msg_err)
        return res

    def _evaluate_worklog_usage(self, model):
        self.ensure_one()
        res = False
        localdict = self._get_localdict()
        try:
            safe_eval(
                model.outsource_work_usage_python_code,
                localdict,
                mode="exec",
                nocopy=True,
            )
            if "result" in localdict:
                res = localdict["result"]
        except Exception as error:
            msg_err = _("Error evaluating conditions.\n %s") % error
            raise UserError(msg_err)
        return res

    @api.onchange(
        "product_id",
    )
    def onchange_name(self):
        pass

    @api.onchange(
        "model_id",
    )
    def onchange_analytic_account_id(self):
        self.analytic_account_id = False
        if len(self.allowed_analytic_account_ids) > 0:
            self.analytic_account_id = self.allowed_analytic_account_ids[0]._origin.id

    @api.onchange(
        "model_id",
        "allowed_usage_ids",
    )
    def onchange_usage_id(self):
        self.usage_id = False
        if self.allowed_usage_ids:
            usage_type_id = self.allowed_usage_ids._origin[0]
            self.usage_id = usage_type_id.id

    def _create_aml(self):
        self.ensure_one()
        AML = self.env["account.move.line"]
        aml = AML.with_context(check_move_validity=False).create(
            self._prepare_aml_data()
        )
        self.write(
            {
                "account_move_line_id": aml.id,
            }
        )

    def _prepare_aml_data(self):
        self.ensure_one()
        outstanding = self.outstanding_id
        aa_id = self.analytic_account_id and self.analytic_account_id.id or False
        debit, credit, amount_currency = self._get_aml_amount(outstanding.currency_id)
        return {
            "move_id": outstanding.move_id.id,
            "product_id": self.product_id.id,
            "name": self.name,
            "partner_id": outstanding.partner_id.id,
            "account_id": self.account_id.id,
            "quantity": self.uom_quantity,
            "product_uom_id": self.uom_id.id,
            "price_unit": self.price_unit,
            "debit": debit,
            "credit": credit,
            "currency_id": outstanding.currency_id.id,
            "amount_currency": amount_currency,
            "analytic_account_id": aa_id,
        }

    def _get_aml_amount(self, currency):
        self.ensure_one()
        debit = credit = amount = amount_currency = 0.0
        outstanding = self.outstanding_id
        move_date = outstanding.date

        amount_currency = self.price_subtotal
        amount = currency.with_context(date=move_date).compute(
            amount_currency,
            outstanding.currency_id,
        )

        if amount > 0.0:
            debit = abs(amount)
        else:
            credit = abs(amount)

        return debit, credit, amount_currency

    @ssi_decorator.pre_cancel_check()
    def _01_check_outstanding(self):
        self.ensure_one()
        if self.outstanding_id:
            error_message = _(
                """
            Context: Cancel outsource work
            Database ID: %s
            Problem: Outsource work already have an outstanding
            Solution: Cancel outsource work outstanding
            """
                % (self.id)
            )
            raise UserError(error_message)

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
