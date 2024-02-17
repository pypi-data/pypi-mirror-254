# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetWorkOrderRouteTemplateRoute(models.Model):
    _name = "fleet_work_order_route_template.route"
    _description = "Fleet Work Order Route Template - Route"
    _order = "sequence, id"

    template_id = fields.Many2one(
        comodel_name="fleet_work_order_route_template",
        string="Template",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(string="Sequence", default=10, required=True)
    start_location_id = fields.Many2one(
        comodel_name="res.partner",
        string="Start Location",
        required=True,
        ondelete="restrict",
    )
    end_location_id = fields.Many2one(
        comodel_name="res.partner",
        string="End Location",
        required=True,
        ondelete="restrict",
    )
    distance = fields.Float(string="Distance", default=0.0, required=True)
