# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class FleetVehicle(models.Model):
    _inherit = "fleet_vehicle"

    driver_selection_method = fields.Selection(
        string="Driver Selection Method",
        selection=[("manual", "Manual"), ("domain", "Domain")],
        default="manual",
    )
    driver_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="rel_fleet_vehicle_2_driver",
        column1="vehicle_id",
        column2="driver_id",
        string="Drivers",
    )
    driver_domain = fields.Text(default=[])
    allowed_driver_ids = fields.Many2many(
        string="Allowed Drivers",
        comodel_name="res.partner",
        compute="_compute_allowed_driver_ids",
        store=False,
        compute_sudo=True,
    )
    codriver_selection_method = fields.Selection(
        string="Co-Driver Selection Method",
        selection=[("manual", "Manual"), ("domain", "Domain")],
        default="manual",
    )
    codriver_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="rel_fleet_vehicle_2_codriver",
        column1="vehicle_id",
        column2="codriver_id",
        string="Co-Drivers",
    )
    codriver_domain = fields.Text(default=[])
    allowed_codriver_ids = fields.Many2many(
        string="Allowed Co-Drivers",
        comodel_name="res.partner",
        compute="_compute_allowed_codriver_ids",
        store=False,
        compute_sudo=True,
    )

    @api.depends(
        "driver_selection_method",
        "driver_ids",
        "driver_domain",
    )
    def _compute_allowed_driver_ids(self):
        for record in self:
            result = []
            if record.driver_selection_method == "manual":
                result = record.driver_ids.ids
            elif record.driver_selection_method == "domain":
                criteria = safe_eval(record.driver_domain, {})
                result = self.env["res.partner"].search(criteria).ids
            record.allowed_driver_ids = result

    @api.depends(
        "codriver_selection_method",
        "codriver_ids",
        "codriver_domain",
    )
    def _compute_allowed_codriver_ids(self):
        for record in self:
            result = []
            if record.codriver_selection_method == "manual":
                result = record.codriver_ids.ids
            elif record.codriver_selection_method == "domain":
                criteria = safe_eval(record.codriver_domain, {})
                result = self.env["res.partner"].search(criteria).ids
            record.allowed_codriver_ids = result
