from odoo import models, fields, api, exceptions
from .. import constants

class EditorialProducts(models.Model):
    """ Extend product product for editorial management """

    _description = "Editorial Core Products"
    _inherit = 'product.product'

    on_hand_qty = fields.Float(compute='_compute_on_hand_qty', string='A mano')
    liquidated_qty = fields.Float(compute='_compute_liquidated_qty', string='Liquidados')
    owned_qty = fields.Float(compute='_compute_owned_qty', string='En propiedad')
    in_distribution_qty = fields.Float(compute='_compute_in_distribution_qty', string='En distribución')

    def get_all_child_locations(self, location_id):
        location = self.env['stock.location'].browse(location_id)
        child_locations = location.child_ids
        location_ids = [location.id] + [child.id for child in child_locations]
        
        for child_location in child_locations:
            location_ids += self.get_all_child_locations(child_location.id)

        return location_ids

    def get_product_quantity_in_location(self, location_id):
        location_ids = self.get_all_child_locations(location_id)

        quants = self.env['stock.quant'].search([
            ('product_id', '=', self.id), 
            ('location_id', 'in', location_ids)
        ])

        quantity = sum(quant.quantity for quant in quants)
        return quantity

    def _compute_on_hand_qty(self):
        for product in self:
            product.on_hand_qty = product.get_product_quantity_in_location(constants.LOCATION_ID_STOCK)

    def _compute_liquidated_qty(self):
        for product in self:
            product.liquidated_qty = product.get_product_quantity_in_location(constants.LOCATION_ID_CUSTOMERS)

    def _compute_owned_qty(self):
        for product in self:
            product.owned_qty = product.on_hand_qty + product.in_distribution_qty

    def _compute_in_distribution_qty(self):
        for product in self:
            product.in_distribution_qty = product.get_product_quantity_in_location(constants.LOCATION_ID_DEPOSITO)


class EditorialTemplateProducts(models.Model):
    """ Extend product template for editorial management """

    _description = "Editorial Template Products"
    _inherit = 'product.template'
    # we inherited product.template model which is Odoo/OpenERP built in model and edited several fields in that model.
    isbn_number = fields.Char(string="ISBN", copy=False, required=False,
                              help="International Standard Book Number \
                              (ISBN)")
    purchase_ok = fields.Boolean('Can be Purchased', default=False)
    author_name = fields.Many2many("res.partner", string="Autores", required=False,
                                   help="Nombre del autor", domain="[('is_author','=',True)]")
    on_hand_qty = fields.Float(compute='_compute_on_hand_qty', string='A mano')
    liquidated_qty = fields.Float(compute='_compute_liquidated_qty', string='Liquidados')
    owned_qty = fields.Float(compute='_compute_owned_qty', string='En propiedad')
    in_distribution_qty = fields.Float(compute='_compute_in_distribution_qty', string='En distribución')

    def _compute_on_hand_qty(self):
        for template in self:
            on_hand_qty = 0.0
            for product in template.product_variant_ids:
                on_hand_qty += product.get_product_quantity_in_location(constants.LOCATION_ID_STOCK)
            template.on_hand_qty = on_hand_qty

    def _compute_liquidated_qty(self):
        for template in self:
            liquidated_qty = 0.0
            for product in template.product_variant_ids:
                liquidated_qty += product.get_product_quantity_in_location(constants.LOCATION_ID_CUSTOMERS)
            template.liquidated_qty = liquidated_qty

    def _compute_owned_qty(self):
        for template in self:
            template.owned_qty = template.on_hand_qty + template.in_distribution_qty

    def _compute_in_distribution_qty(self):
        for template in self:
            in_distribution_qty = 0.0
            for product in template.product_variant_ids:
                in_distribution_qty += product.get_product_quantity_in_location(constants.LOCATION_ID_DEPOSITO)
            template.in_distribution_qty = in_distribution_qty

    @api.constrains("isbn_number")
    def check_is_isbn13(self):
        for record in self:
            if record.isbn_number:
                n = record.isbn_number.replace("-", "").replace(" ", "")
                if len(n) != 13:
                    raise exceptions.ValidationError("El ISBN debe tener 13 dígitos")
                product = sum(int(ch) for ch in n[::2]) + sum(
                    int(ch) * 3 for ch in n[1::2]
                )
                if product % 10 != 0:
                    raise exceptions.ValidationError(
                        "El ISBN %s no es válido." % record.isbn_number
                    )
        # all records passed the test, don't return anything

    # DDAA: Derechos de autoría
    # Cuando se selecciona la categoría "All / Libros" (con id 5), se establecen los valores por defecto:
    # Producto que se puede vender y comprar y es almacenable.
    @api.onchange("categ_id")
    def _onchange_uom(self):
        if self.categ_id:
            if self.categ_id.id == 5:  # categoria Libro
                self.sale_ok = True
                self.purchase_ok = True
                self.type = "product"
            elif self.categ_id.id == 11:  # categoria Libro Digital
                self.sale_ok = True
                self.purchase_ok = True
                self.type = "consu"
            if (
                self.env.company.module_editorial_ddaa
                and self.env.company.is_category_genera_ddaa_or_child(self.categ_id)
            ):
                self.genera_ddaa = True
            else:
                self.genera_ddaa = False

    @api.onchange("categ_id")
    def _compute_view_show_fields(self):
        if self.env.company.module_editorial_ddaa:
            self.view_show_genera_ddaa_fields = (
                self.env.company.is_category_genera_ddaa_or_child(self.categ_id)
            )
            self.view_show_ddaa_fields = (
                self.categ_id == self.env.company.product_category_ddaa_id
            )
        else:
            self.view_show_genera_ddaa_fields = False
            self.view_show_ddaa_fields = False

    # DDAA: Derechos de autoría
    # Check one2one relation. Here between "producto_referencia" y "derecho_autoria"
    #
    # Note: we are creating the relationship between the templates.
    # Therefore, when we add the product to a stock.picking or a sale or purchase, we are actually adding the product  and not the template.
    # Please use product_tmpl_id to access the template of a product.
    producto_referencia = fields.One2many(
        "product.template",
        "derecho_autoria",
        string="Libro de referencia",
        help="Este campo se utiliza para relacionar el derecho de autoría con el libro",
    )

    # prod_ref = fields.Many2one("product.template", compute='compute_autoria', inverse='autoria_inverse', string="prod ref",
    #                             required=False)

    @api.model
    def _derecho_autoria_domain(self):
        return [("categ_id", "=", self.env.company.product_category_ddaa_id.id)]

    derecho_autoria = fields.Many2one(
        "product.template",
        domain=_derecho_autoria_domain,
        string="Producto ddaa",
        help="Este campo se utiliza para relacionar el derecho de autoría con el libro",
    )

    receptora_derecho_autoria = fields.Many2many(
        "res.partner",
        "receptora_autoria_product_template",
        "product_id",
        "partner_id",
        copy=False,
        string="Receptor derechos autoría",
        help="Nombre de la receptora de derechos de autoría",
    )

    genera_ddaa = fields.Boolean("Genera derechos de autoría", default=False)

    # @api.depends('producto_referencia')
    # def compute_autoria(self):
    #     if len(self.derecho_autorias) > 0:
    #         self.derecho_autoria = self.derecho_autorias[0]

    # def autoria_inverse(self):
    #     if len(self.derecho_autorias) > 0:
    #         # delete previous reference
    #         ddaa = self.env['product.template'].browse(self.derecho_autorias[0].id)
    #         ddaa.producto_referencia = False
    #     # set new reference
    #     self.derecho_autoria.producto_referencia = self

    view_show_genera_ddaa_fields = fields.Boolean(
        "Muestra los campos asociados a categorías que generan ddaa",
        compute="_compute_view_show_fields",
        default=False,
    )
    view_show_ddaa_fields = fields.Boolean(
        "Muestra los campos asociados a la categoría ddaa",
        compute="_compute_view_show_fields",
        default=False,
    )

    # DDAA: Derechos de autoría
    # Se crea un producto asociado con la categoría que representa los DDAA
    @api.model_create_multi
    def create(self, vals_list):
        templates = super(EditorialTemplateProducts, self).create(vals_list)
        company = self.env.company
        if company.module_editorial_ddaa:
            vals = vals_list[0]
            category_id = self.env["product.category"].browse(vals.get("categ_id"))
            if (
                company.is_category_genera_ddaa_or_child(category_id)
                and vals.get("genera_ddaa") == True
            ):
                self.env["product.template"].create(
                    {
                        "name": "DDAA de " + vals.get("name"),
                        "categ_id": company.product_category_ddaa_id.id,
                        "list_price": vals.get("list_price") * 0.1,
                        "type": "service",
                        "sale_ok": False,
                        "purchase_ok": True,
                        "author_name": vals.get("author_name"),
                        "receptora_derecho_autoria": vals.get("author_name"),
                        "producto_referencia": [templates.id],
                        "derecho_autoria": False,
                    }
                )
        return templates
