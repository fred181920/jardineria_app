from odoo import fields, models, api
from odoo.exceptions import Warning, ValidationError


class Herramientas(models.Model):
    _name = 'jardineria.herramientas'
    _description = 'Herramientas'
    name = fields.Char('Nombre', required=True)
    description = fields.Html('Descripción')
    fuel_type = fields.Selection(
        [('nothing', 'Ninguno'), ('electric', 'Eléctrico'), ('gasoil', 'Gasolina')], 'Consumo', default='nothing', required=True)
    leasable = fields.Boolean('¿Es alquilable?', default=False)
    price = fields.Float('Precio', required=True)
    stock = fields.Integer('Stock', required=True)
    leasable_price = fields.Float('Precio de alquiler por hora', required=True)
    fabrication_date = fields.Date('Fecha de fabricación')
    image = fields.Binary('Foto')
    brand_ids = fields.Many2many('jardineria.marcas', string='Marca')
    seller_ids = fields.Many2many('res.partner', string='Vendedor', required=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.user.company_id.currency_id)
    AVAILABLE_PRIORITIES = [
        ('0', 'Muy poco valorado'),
        ('1', 'Muy malo'),
        ('2', 'Malo'),
        ('3', 'Bueno'),
        ('4', 'Muy Bueno'), ('5', 'Excelente')]
    stars = fields.Selection(AVAILABLE_PRIORITIES, select=True, string="Estrellas")

    @api.constrains('stock')
    def _checkea_el_stock_(self):
        for herramientas in self:
            if herramientas.stock < 0:
                raise ValidationError('El stock no puede ser negativo' % herramientas.price)

    @api.constrains('price')
    def _checkea_el_price_(self):
        for herramientas in self:
            if herramientas.price <= 0.0:
                raise ValidationError('%s is an invalid price' % herramientas.price)

    @api.constrains('leasable_price')
    def _check_leaseable_and_leasable_price(self):
        for herramientas in self:
            if herramientas.leasable == True:
                if herramientas.leasable_price <= 0.0:
                    raise ValidationError('%s is an invalid leasable price' % herramientas.leasable_price)



