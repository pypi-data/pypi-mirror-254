# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase + Inventory Integration",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "purchase",
        "stock",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir_rule_data.xml",
        "views/stock_warehouse_views.xml",
    ],
    "demo": [],
}
