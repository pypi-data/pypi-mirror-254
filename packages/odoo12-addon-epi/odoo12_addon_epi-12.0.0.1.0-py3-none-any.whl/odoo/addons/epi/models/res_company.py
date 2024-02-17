from odoo import models, fields


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"


    footer_doc_policy_text = fields.Html(
        string="Footer doc policy text", translate=True
    )
