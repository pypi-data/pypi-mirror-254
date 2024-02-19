# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class OutsourceWorkOutstanding(models.Model):
    _name = "outsource_work_outstanding"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_confirm",
        "mixin.transaction_pricelist",
        "mixin.date_duration",
    ]
    _description = "Outsource Work Outstanding"
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

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        domain=[
            ("is_company", "=", False),
            ("parent_id", "=", False),
        ],
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    batch_id = fields.Many2one(
        string="# Batch",
        comodel_name="outsource_work_outstanding_batch",
        readonly=True,
        ondelete="restrict",
    )
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
    work_ids = fields.One2many(
        string="Outstanding Works",
        comodel_name="outsource_work",
        inverse_name="outstanding_id",
        readonly=True,
        copy=True,
    )
    tax_ids = fields.One2many(
        string="Taxes",
        comodel_name="outsource_work_outstanding_tax",
        inverse_name="outstanding_id",
        readonly=True,
        states={
            "open": [
                ("readonly", False),
            ],
        },
        copy=True,
    )

    @api.depends(
        "work_ids",
        "work_ids.price_subtotal",
        "work_ids.price_tax",
        "work_ids.price_total",
        "tax_ids",
        "tax_ids.tax_amount",
    )
    def _compute_total(self):
        for record in self:
            amount_untaxed = amount_tax = 0.0
            for work in record.work_ids:
                amount_untaxed += work.price_subtotal

            for tax in record.tax_ids:
                amount_tax += tax.tax_amount

            record.amount_untaxed = amount_untaxed
            record.amount_tax = amount_tax
            record.amount_total = amount_untaxed + amount_tax

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

    # Accounting
    payable_journal_id = fields.Many2one(
        string="Payable Journal",
        comodel_name="account.journal",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    payable_account_id = fields.Many2one(
        string="Payable Account",
        comodel_name="account.account",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    move_id = fields.Many2one(
        string="# Invoice",
        comodel_name="account.move",
        readonly=True,
    )
    payable_move_line_id = fields.Many2one(
        string="Payable Journal Item",
        comodel_name="account.move.line",
        readonly=True,
        ondelete="set null",
        copy=False,
    )

    @api.depends(
        "payable_move_line_id",
        "payable_move_line_id.matched_debit_ids",
        "payable_move_line_id.matched_credit_ids",
    )
    def _compute_reconciled(self):
        for record in self:
            result = False
            if record.payable_move_line_id.reconciled:
                result = True
            record.reconciled = result

    reconciled = fields.Boolean(
        string="Reconciled",
        compute="_compute_reconciled",
        store=True,
    )

    @api.depends(
        "amount_total",
        "state",
        "payable_move_line_id",
        "payable_move_line_id.reconciled",
        "payable_move_line_id.amount_residual",
        "payable_move_line_id.amount_residual_currency",
    )
    def _compute_residual(self):
        for document in self:
            realized = 0.0
            residual = document.amount_total
            currency = document.currency_id
            if document.payable_move_line_id:
                move_line = document.payable_move_line_id
                if not currency:
                    residual = -1.0 * move_line.amount_residual
                else:
                    residual = -1.0 * move_line.amount_residual_currency
                realized = document.amount_total - residual
            document.amount_realized = realized
            document.amount_residual = residual

    amount_realized = fields.Monetary(
        string="Paid",
        compute="_compute_residual",
        store=True,
        currency_field="currency_id",
    )
    amount_residual = fields.Monetary(
        string="Residual",
        compute="_compute_residual",
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
        res = super(OutsourceWorkOutstanding, self)._get_policy_field()
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

    @api.onchange(
        "type_id",
    )
    def onchange_payable_journal_id(self):
        self.payable_journal_id = False
        if self.type_id:
            self.payable_journal_id = self.type_id.payable_journal_id

    @api.onchange(
        "type_id",
    )
    def onchange_payable_account_id(self):
        self.payable_account_id = False
        if self.type_id:
            self.payable_account_id = self.type_id.payable_account_id

    @ssi_decorator.post_done_action()
    def _post_done_acion_20_create_aml(self):
        self.ensure_one()
        move = (
            self.env["account.move"]
            .with_context(check_move_validity=False)
            .create(self._prepare_account_move_data())
        )
        self.write(
            {
                "move_id": move.id,
            }
        )
        self._create_receivable_aml()
        self._create_work_aml()
        self._create_tax_aml()
        self.move_id.action_post()

    def _create_receivable_aml(self):
        self.ensure_one()
        AML = self.env["account.move.line"]
        aml = AML.with_context(check_move_validity=False).create(
            self._prepare_payable_aml_data()
        )
        self.write(
            {
                "payable_move_line_id": aml.id,
            }
        )

    def _prepare_payable_aml_data(self):
        self.ensure_one()
        debit, credit, amount_currency = self._get_payable_amount(self.currency_id)
        data = {
            "name": self.name,
            "move_id": self.move_id.id,
            "partner_id": self.partner_id.id,
            "account_id": self.payable_account_id.id,
            "debit": debit,
            "credit": credit,
            "currency_id": self.currency_id.id,
            "amount_currency": amount_currency,
            "date_maturity": self.date_due,
        }
        return data

    def _get_payable_amount(self, currency):
        self.ensure_one()
        debit = credit = amount = amount_currency = 0.0
        move_date = self.date

        amount_currency = self.amount_total
        amount = currency.with_context(date=move_date).compute(
            amount_currency,
            self.company_id.currency_id,
        )

        if amount < 0.0:
            debit = abs(amount)
        else:
            credit = abs(amount)

        return debit, credit, amount_currency

    def _create_work_aml(self):
        self.ensure_one()
        for work in self.work_ids:
            work._create_aml()

    def _create_tax_aml(self):
        self.ensure_one()
        for tax in self.tax_ids:
            tax._create_aml()

    def _disconnect_invoice(self):
        self.ensure_one()
        self.write(
            {
                "invoice_id": False,
            }
        )

    def _get_payable_journal(self):
        self.ensure_one()
        return self.payable_journal_id

    def _get_payable_account(self):
        self.ensure_one()
        return self.payable_account_id

    def _prepare_account_move_data(self):
        self.ensure_one()
        journal = self._get_payable_journal()
        return {
            "date": self.date,
            "name": self.name,
            "journal_id": journal.id,
            "ref": self.name,
        }

    @ssi_decorator.post_cancel_action()
    def _post_delete_acion_10_delete_invoice(self):
        self.ensure_one()
        if self.move_id:
            invoice = self.move_id
            self.write(
                {
                    "move_id": False,
                }
            )
            invoice.unlink()

    def action_populate(self):
        for record in self:
            record._populate()

    def action_clear_work(self):
        for record in self:
            record._clear_work()

    def _clear_work(self):
        self.ensure_one()
        self.work_ids.write({"outstanding_id": False})

    def _populate(self):
        self.ensure_one()
        Work = self.env["outsource_work"]
        criteria = self._prepare_populate_domain()
        Work.search(criteria).write(
            {
                "outstanding_id": self.id,
            }
        )

    def _prepare_populate_domain(self):
        self.ensure_one()
        result = [
            ("partner_id", "=", self.partner_id.id),
            ("date", ">=", self.date_start),
            ("date", "<=", self.date_end),
            ("outstanding_id", "=", False),
            ("currency_id", "=", self.currency_id.id),
            ("state", "=", "done"),
        ]
        if self.analytic_account_id:
            result.append(("analytic_account_id", "=", self.analytic_account_id.id))
        return result

    def action_compute_tax(self):
        for record in self:
            record._recompute_tax()

    def _recompute_tax(self):
        self.ensure_one()
        taxes_grouped = self.get_taxes_values()
        self.tax_ids.unlink()
        tax_lines = []
        for tax in taxes_grouped.values():
            tax_lines.append((0, 0, tax))
        self.write({"tax_ids": tax_lines})

    def get_taxes_values(self):
        tax_grouped = {}
        cur = self.currency_id
        round_curr = cur.round
        for work in self.work_ids:
            price_unit = work.price_unit
            taxes = work.tax_ids.compute_all(price_unit, cur, work.quantity)["taxes"]
            for tax in taxes:
                val = self._prepare_tax_line_vals(work, tax)
                key = self.get_grouping_key(val)

                if key not in tax_grouped:
                    tax_grouped[key] = val
                    tax_grouped[key]["base_amount"] = round_curr(val["base_amount"])
                else:
                    tax_grouped[key]["tax_amount"] += val["tax_amount"]
                    tax_grouped[key]["base_amount"] += round_curr(val["base_amount"])
        return tax_grouped

    def get_grouping_key(self, tax_line):
        self.ensure_one()
        return (
            str(tax_line["tax_id"])
            + "-"
            + str(tax_line["account_id"])
            + "-"
            + str(tax_line["analytic_account_id"])
        )

    def _prepare_tax_line_vals(self, line, tax):
        vals = {
            "outstanding_id": self.id,
            "tax_id": tax["id"],
            "tax_amount": tax["amount"],
            "base_amount": tax["base"],
            "manual": False,
            "account_id": tax["account_id"],
            "analytic_account_id": line.analytic_account_id.id,
        }
        return vals

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
