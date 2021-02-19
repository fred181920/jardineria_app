from odoo import fields, models, api
from odoo.exceptions import Warning, ValidationError

class Servicios(models.Model):
    _name = 'jardineria.servicios'
    _description = 'Servicios'
    name = fields.Char('Nombre', required=True)
    age = fields.Integer('Edad', required=True)
    gender = fields.Selection([('hombre','Hombre'),('mujer','Mujer')],'Sexo', required=True)
    specialty = fields.Html('Especialidades', required=True)
    price = fields.Float('Precio/Hora', required=True)
    image = fields.Binary('Foto')
    cv = fields.Binary('Currículum')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.user.company_id.currency_id)
    AVAILABLE_PRIORITIES = [
        ('0', 'Muy poco valorado'),
        ('1', 'Muy malo'),
        ('2', 'Malo'),
        ('3', 'Bueno'),
        ('4', 'Muy Bueno'), ('5', 'Excelente')]
    stars = fields.Selection(AVAILABLE_PRIORITIES, select=True, string="Estrellas")

    @api.constrains('price')
    def _checkea_el_price_(self):
        for servicios in self:
            if servicios.price <= 0:
                raise ValidationError('%s is an invalid price' % servicios.price)

    @api.constrains('age')
    def _checkea_el_price_(self):
        for servicios in self:
            if servicios.age < 18:
                raise ValidationError('%s is an invalid age' % servicios.age)