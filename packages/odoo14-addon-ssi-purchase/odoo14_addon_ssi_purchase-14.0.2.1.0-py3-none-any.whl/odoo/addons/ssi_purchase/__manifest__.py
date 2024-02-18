# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase",
    "version": "14.0.2.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "purchase",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/purchase_order_type.xml",
        "views/res_partner_views.xml",
        "views/purchase_order_views.xml",
        "views/product_product_views.xml",
        "views/purchase_order_type_views.xml",
    ],
    "demo": [],
}
