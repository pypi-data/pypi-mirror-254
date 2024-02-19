# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class ProjectOutsourceWorkAcceptance(models.Model):
    _name = "project_outsource_work_acceptance"
    _inherit = [
        "mixin.transaction_confirm",
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.outsource_work_object",
        "mixin.transaction_pricelist",
    ]
    _description = "Project Outsource Work Acceptance"
    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_done_button = False
    _automatically_insert_done_policy_fields = False

    # Attributes related to add element on form view automatically
    _automatically_insert_multiple_approval_page = True
    _outsource_work_create_page = True
    _statusbar_visible_label = "draft,confirm,done"
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

    date = fields.Date(
        string="Date Acceptance",
        required=True,
        readonly=True,
        states={
            "draft": [("readonly", False)],
        },
    )
    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        required=True,
        ondelete="cascade",
        readonly=True,
        states={
            "draft": [("readonly", False)],
        },
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
    reconciled = fields.Boolean(
        string="Reconciled",
        compute="_compute_reconciled",
        store=True,
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("done", "Done"),
            ("reject", "Rejected"),
            ("cancel", "Cancelled"),
        ],
    )

    @api.depends(
        "outsource_work_ids",
        "outsource_work_ids.price_subtotal",
        "outsource_work_ids.price_tax",
        "outsource_work_ids.price_total",
    )
    def _compute_total(self):
        for record in self:
            amount_untaxed = amount_tax = amount_total = 0.0
            for work in record.outsource_work_ids:
                amount_untaxed += work.price_subtotal
                amount_tax += work.price_tax
                amount_total += work.price_total

            record.amount_untaxed = amount_untaxed
            record.amount_tax = amount_tax
            record.amount_total = amount_total

    @api.depends(
        "outsource_work_ids",
        "outsource_work_ids.reconciled",
    )
    def _compute_reconciled(self):
        for record in self:
            result = True

            if len(record.outsource_work_ids) == 0:
                result = False

            for work in record.outsource_work_ids:
                if not work.reconciled:
                    result = False

            record.reconciled = result

    @api.model
    def _get_policy_field(self):
        res = super(ProjectOutsourceWorkAcceptance, self)._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "cancel_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.onchange(
        "project_id",
    )
    def onchange_policy_template_id(self):
        template_id = self._get_template_policy()
        self.policy_template_id = template_id

    @ssi_decorator.post_confirm_action()
    def _confirm_outsource_work(self):
        self.ensure_one()
        for work in self.outsource_work_ids:
            if work.confirm_ok:
                work.action_confirm()

    @ssi_decorator.post_cancel_action()
    def _cancel_outsource_work(self):
        self.ensure_one()
        for work in self.outsource_work_ids:
            if work.cancel_ok:
                work.action_cancel(self.cancel_reason_id)

    @ssi_decorator.post_restart_action()
    def _restart_outsource_work(self):
        self.ensure_one()
        for work in self.outsource_work_ids:
            if work.restart_ok:
                work.action_restart()

    @ssi_decorator.post_approve_action()
    def _approve_outsource_work(self):
        self.ensure_one()
        for work in self.outsource_work_ids:
            if work.approve_ok:
                work.action_approve_approval()

    @ssi_decorator.post_reject_action()
    def _reject_outsource_work(self):
        self.ensure_one()
        for work in self.outsource_work_ids:
            if work.reject_ok:
                work.action_reject_approval()
