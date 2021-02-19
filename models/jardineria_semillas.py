from odoo import fields, models, api
from odoo.exceptions import Warning, ValidationError
class Semillas(models.Model):
    _name = 'jardineria.semillas'
    _description = 'Semillas'
    name = fields.Char('Nombre', required=True)
    weight = fields.Float('Peso', required=True)
    price = fields.Float('Precio', required=True)
    description = fields.Char('Descripcion', required=True)
    image = fields.Binary('Imagen')
    stock = fields.Integer('Stock', required=True)
    brand_ids = fields.Many2many('jardineria.marcas', string='Marca')
    seller_ids = fields.Many2many('res.partner', string='Vendedor')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.user.company_id.currency_id)

    @api.constrains('stock')
    def _checkea_el_stock_(self):
        for semillas in self:
            if semillas.stock < 0:
                raise ValidationError('%s is an invalid price' % semillas.stock)

    @api.constrains('price')
    def _checkea_el_price_(self):
        for semillas in self:
            if semillas.price <= 0.0:
                raise ValidationError('%s is an invalid price' % semillas.price)

    @api.constrains('weight')
    def _checkea_el_weight_(self):
        for semillas in self:
            if semillas.weight <= 0.0:
                raise ValidationError("Te weight cannot be 0g")


