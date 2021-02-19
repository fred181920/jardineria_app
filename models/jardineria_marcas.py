from odoo import fields, models
class Marcas(models.Model):
    _name = 'jardineria.marcas'
    _description = 'Marcas'
    name = fields.Char('Nombre', required=True)
    tool_ids = fields.Many2many('jardineria.herramientas', string='Herramientas')
    seed_ids = fields.Many2many('jardineria.semillas', string='Semillas')
