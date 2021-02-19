{
	'name': 'Jardinería aplicacion',
	'description': 'Manejar las ventas de jardinería',
	'author': 'Daniel Reis',
	'depends': ['base'],
	'application': True,

	'data': [
		'security/ir.model.access.csv',
		'views/herramientas_view.xml',
		'views/jardineria_menu.xml',
        'views/semillas_view.xml',
		'views/servicios_view.xml',
	],
	'demo':[
		'data/herramientas_demo.xml',
		'data/semillas_demo.xml',
		'data/servicios_demo.xml',
	]

}