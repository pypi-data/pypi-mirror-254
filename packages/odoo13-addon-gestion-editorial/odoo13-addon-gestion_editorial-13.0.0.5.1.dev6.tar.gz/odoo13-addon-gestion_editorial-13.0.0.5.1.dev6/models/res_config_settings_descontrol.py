from odoo import fields, models

class EditorialResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_editorial_ddaa = fields.Boolean(string="Módulo derechos de autoría",
                                           related='company_id.module_editorial_ddaa',
                                           readonly=False)

    product_category_ddaa_id = fields.Many2one(related='company_id.product_category_ddaa_id', readonly=False)

    product_categories_genera_ddaa_ids = fields.Many2many(related='company_id.product_categories_genera_ddaa_ids', readonly=False)
