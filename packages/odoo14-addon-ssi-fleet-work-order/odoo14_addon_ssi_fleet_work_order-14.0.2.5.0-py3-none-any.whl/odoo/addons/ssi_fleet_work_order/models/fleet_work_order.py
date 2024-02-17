# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError

from odoo.addons.ssi_decorator import ssi_decorator


class FleetWorkOrder(models.Model):
    _name = "fleet_work_order"
    _description = "Fleet Work Order"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_ready",
        "mixin.transaction_confirm",
        "mixin.partner",
    ]

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "ready"
    _approval_state = "confirm"
    _after_approved_method = "action_ready"

    # Attributes related to add element on form view automatically
    _automatically_insert_view_element = True
    _automatically_insert_multiple_approval_page = True

    _statusbar_visible_label = "draft,confirm,ready,open,done"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "ready_ok",
        "open_ok",
        "done_ok",
        "cancel_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "action_open",
        "action_done",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_ready",
        "dom_open",
        "dom_done",
        "dom_reject",
        "dom_cancel",
    ]

    # Sequence attribute
    _create_sequence_state = "ready"

    type_id = fields.Many2one(
        comodel_name="fleet_work_order_type",
        string="Type",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        default=fields.Date.context_today,
        states={"draft": [("readonly", False)]},
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    contact_id = fields.Many2one(
        comodel_name="res.partner",
        string="Contact",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    vehicle_id = fields.Many2one(
        comodel_name="fleet_vehicle",
        string="Vehicle",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    allowed_vehicle_ids = fields.Many2many(
        comodel_name="fleet_vehicle",
        related="type_id.allowed_vehicle_ids",
        store=False,
        string="Allowed Vehicles",
    )
    driver_id = fields.Many2one(
        comodel_name="res.partner",
        string="Driver",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    allowed_driver_ids = fields.Many2many(
        related="vehicle_id.allowed_driver_ids", store=False, string="Allowed Drivers"
    )
    codriver_id = fields.Many2one(
        comodel_name="res.partner",
        string="Co-Driver",
        required=False,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    allowed_codriver_ids = fields.Many2many(
        related="vehicle_id.allowed_codriver_ids",
        store=False,
        string="Allowed Co-Drivers",
    )
    estimated_date_depart = fields.Datetime(
        string="Estimated Departure Date",
        readonly=True,
        required=True,
        states={"draft": [("readonly", False)]},
    )
    estimated_date_arrive = fields.Datetime(
        string="Estimated Arrival Date",
        readonly=True,
        required=True,
        states={"draft": [("readonly", False)]},
    )
    real_date_depart = fields.Datetime(
        string="Real Departure Date",
        readonly=True,
        states={"ready": [("readonly", False)]},
    )
    real_date_arrive = fields.Datetime(
        string="Real Arrival Date",
        readonly=True,
        states={"open": [("readonly", False)]},
    )
    start_odometer = fields.Float(
        string="Start Odometer", readonly=True, states={"ready": [("readonly", False)]}
    )
    end_odometer = fields.Float(
        string="End Odometer", readonly=True, states={"open": [("readonly", False)]}
    )
    route_template_id = fields.Many2one(
        comodel_name="fleet_work_order_route_template",
        string="Route Template",
        readonly=True,
        required=True,
        states={"draft": [("readonly", False)]},
    )
    allowed_route_template_ids = fields.Many2many(
        comodel_name="fleet_work_order_route_template",
        related="type_id.allowed_route_template_ids",
        store=False,
        string="Allowed Route Templates",
    )
    allowed_location_ids = fields.Many2many(
        comodel_name="res.partner",
        related="route_template_id.allowed_location_ids",
        store=False,
        string="Allowed Locations",
    )
    route_ids = fields.One2many(
        comodel_name="fleet_work_order.route",
        inverse_name="work_order_id",
        string="Routes",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    total_distance = fields.Float(
        string="Total Distance", compute="_compute_total_distance", store=True
    )

    @api.model
    def _get_policy_field(self):
        res = super(FleetWorkOrder, self)._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "reject_ok",
            "restart_approval_ok",
            "ready_ok",
            "open_ok",
            "done_ok",
            "cancel_ok",
            "restart_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.onchange("type_id")
    def onchange_vehicle_id(self):
        self.vehicle_id = False

    @api.onchange("vehicle_id")
    def onchange_driver_id(self):
        self.driver_id = False

    @api.onchange("vehicle_id")
    def onchange_codriver_id(self):
        self.codriver_id = False

    @api.onchange("type_id")
    def onchange_route_template_id(self):
        self.route_template_id = False

    def _prepare_route_data(self, route):
        self.ensure_one()
        result = {
            "work_order_id": self.id,
            "sequence": route.sequence,
            "start_location_id": route.start_location_id.id,
            "end_location_id": route.end_location_id.id,
            "distance": route.distance,
        }
        return result

    @api.onchange("route_template_id")
    def onchange_route_ids(self):
        self.route_ids = [(5, 0, 0)]
        if self.route_template_id:
            template = self.route_template_id
            if template.route_ids:
                routes = []
                for route in template.route_ids:
                    res = self._prepare_route_data(route)
                    routes.append((0, 0, res))
                self.route_ids = routes

    @api.depends("route_ids", "route_ids.distance")
    def _compute_total_distance(self):
        for record in self:
            record.total_distance = 0.0
            for route in self.route_ids:
                record.total_distance += route.distance

    @ssi_decorator.pre_open_check()
    def _30_check_real_depart_time(self):
        self.ensure_one()
        if not self.real_date_depart:
            error_message = """
                Context: Confirm fleet work order
                Database ID: %s
                Problem: Real date depart is empty
                Solution: Fill real date depart
                """ % (
                self.id
            )
            raise UserError(_(error_message))

    @ssi_decorator.pre_open_check()
    def _30_check_starting_odometer(self):
        self.ensure_one()
        if not self.start_odometer:
            error_message = """
                Context: Confirm fleet work order
                Database ID: %s
                Problem: Start odometer is empty
                Solution: Fill start odometer
                """ % (
                self.id
            )
            raise UserError(_(error_message))

    @ssi_decorator.pre_done_check()
    def _30_check_real_arrive_time(self):
        self.ensure_one()
        if not self.real_date_arrive:
            error_message = """
                Context: Finish fleet work order
                Database ID: %s
                Problem: Real date arrive is empty
                Solution: Fill real date arrive
                """ % (
                self.id
            )
            raise UserError(_(error_message))

    @ssi_decorator.pre_done_check()
    def _30_check_ending_odometer(self):
        self.ensure_one()
        if not self.end_odometer:
            error_message = """
                Context: Finish fleet work order
                Database ID: %s
                Problem: End odometer is empty
                Solution: Fill end odometer
                """ % (
                self.id
            )
            raise UserError(_(error_message))

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
