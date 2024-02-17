# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class FleetWorkOrderType(models.Model):
    _name = "fleet_work_order_type"
    _description = "Fleet Work Order Type"
    _inherit = ["mixin.master_data"]

    vehicle_selection_method = fields.Selection(
        string="Vehicle Selection Method",
        selection=[("manual", "Manual"), ("domain", "Domain")],
        default="manual",
    )
    vehicle_ids = fields.Many2many(
        comodel_name="fleet_vehicle",
        relation="rel_fleet_wo_type_2_vehicle",
        column1="type_id",
        column2="vehicle_id",
        string="Vehicles",
    )
    vehicle_domain = fields.Text(
        string="Vehicle Domain",
        default=[],
    )
    allowed_vehicle_ids = fields.Many2many(
        string="Allowed Vehicles",
        comodel_name="fleet_vehicle",
        compute="_compute_allowed_vehicle_ids",
        store=False,
        compute_sudo=True,
    )
    route_template_selection_method = fields.Selection(
        string="Route Template Selection Method",
        selection=[("manual", "Manual"), ("domain", "Domain")],
        default="manual",
    )
    route_template_ids = fields.Many2many(
        comodel_name="fleet_work_order_route_template",
        relation="rel_fleet_wo_type_2_route_template",
        column1="type_id",
        column2="route_template_id",
        string="Route Templates",
    )
    route_template_domain = fields.Text(
        string="Route Template Domain",
        default=[],
    )
    allowed_route_template_ids = fields.Many2many(
        string="Allowed Route Templates",
        comodel_name="fleet_work_order_route_template",
        compute="_compute_allowed_route_template_ids",
        store=False,
        compute_sudo=True,
    )

    @api.depends(
        "vehicle_selection_method",
        "vehicle_ids",
        "vehicle_domain",
    )
    def _compute_allowed_vehicle_ids(self):
        for record in self:
            result = []
            if record.vehicle_selection_method == "manual":
                result = record.vehicle_ids.ids
            elif record.vehicle_selection_method == "domain":
                criteria = safe_eval(record.vehicle_domain, {})
                result = self.env["fleet_vehicle"].search(criteria).ids
            record.allowed_vehicle_ids = result

    @api.depends(
        "route_template_selection_method",
        "route_template_ids",
        "route_template_domain",
    )
    def _compute_allowed_route_template_ids(self):
        for record in self:
            result = []
            if record.route_template_selection_method == "manual":
                result = record.route_template_ids.ids
            elif record.route_template_selection_method == "domain":
                criteria = safe_eval(record.route_template_domain, {})
                result = (
                    self.env["fleet_work_order_route_template"].search(criteria).ids
                )
            record.allowed_route_template_ids = result
