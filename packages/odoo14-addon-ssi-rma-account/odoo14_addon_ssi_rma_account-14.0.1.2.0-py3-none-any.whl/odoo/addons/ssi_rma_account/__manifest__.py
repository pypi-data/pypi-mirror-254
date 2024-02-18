# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "RMA + Accounting Integration",
    "version": "14.0.1.2.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["ssi_rma", "ssi_financial_accounting"],
    "data": [
        "data/rma_policy_field_data.xml",
        "data/rma_policy_data.xml",
        "views/rma_operation_views.xml",
        "views/rma_customer_views.xml",
        "views/rma_supplier_views.xml",
        # "data/rma_policy_field_data.xml",
        # "data/rma_policy_data.xml",
    ],
    "demo": [],
    "images": [],
}
