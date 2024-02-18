# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RMAPolicy(models.Model):
    _name = "rma_policy"
    _inherit = ["rma_policy"]

    refund_policy_ok = fields.Boolean(
        string="Available on Refund Policy",
    )
