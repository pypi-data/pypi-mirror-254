# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RMAOperation(models.Model):
    _name = "rma_operation"
    _description = "RMA Operation"
    _inherit = ["mixin.master_data"]

    direction = fields.Selection(
        string="Direction",
        selection=[
            ("customer", "RMA Customer"),
            ("supplier", "RMA Supplier"),
        ],
        required=True,
        default="customer",
    )
    receipt_policy_id = fields.Many2one(
        comodel_name="rma_policy",
        string="Receipt Policy",
        domain="[('receipt_policy_ok', '=', True)]",
        required=True,
        ondelete="restrict",
    )
    delivery_policy_id = fields.Many2one(
        comodel_name="rma_policy",
        string="Delivery Policy",
        domain="[('delivery_policy_ok', '=', True)]",
        required=True,
        ondelete="restrict",
    )
    rma_supplier_policy_id = fields.Many2one(
        comodel_name="rma_policy",
        string="RMA Supplier Policy",
        domain="[('rma_supplier_policy_ok', '=', True)]",
        required=True,
        ondelete="restrict",
    )
    allowed_route_template_ids = fields.Many2many(
        comodel_name="rma_route_template",
        string="Allowed Route Template",
        relation="rel_rma_operation_2_rma_route_template",
    )
    default_route_template_id = fields.Many2one(
        comodel_name="rma_route_template",
        string="Default Route Template",
        ondelete="restrict",
    )
