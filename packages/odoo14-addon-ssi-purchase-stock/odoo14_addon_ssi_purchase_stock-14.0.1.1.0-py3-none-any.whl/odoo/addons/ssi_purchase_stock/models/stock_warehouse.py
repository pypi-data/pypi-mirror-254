# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class StockWarehouse(models.Model):
    _name = "stock.warehouse"
    _inherit = ["stock.warehouse"]

    purchase_user_ids = fields.Many2many(
        string="Purchase Users",
        comodel_name="res.users",
        relation="rel_warehouse_2_purchase_user",
        column1="warehouse_id",
        column2="user_id",
    )
