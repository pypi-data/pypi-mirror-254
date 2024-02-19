# Talaios coop.
# Original code by: Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# # License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_use_product_description_per_so_line = fields.Boolean(
        string="Allows you to use only the product name in the sales order line description",
        implied_group="only_name_on_sale_order_line_description."
        "group_use_product_description_per_so_line",
        help="Allows you to use only product name on the sales order line description.",
    )
