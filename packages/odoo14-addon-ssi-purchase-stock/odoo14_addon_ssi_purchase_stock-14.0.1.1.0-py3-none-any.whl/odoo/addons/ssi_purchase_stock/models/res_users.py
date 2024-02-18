# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResUsers(models.Model):
    _name = "res.users"
    _inherit = ["res.users"]

    warehouse_purchase_ids = fields.Many2many(
        string="Purchase Users",
        comodel_name="stock.warehouse",
        relation="rel_warehouse_2_purchase_user",
        column2="warehouse_id",
        column1="user_id",
    )
