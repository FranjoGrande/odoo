# -*- coding: utf-8 -*-
{
    'name': 'Piscigranja',
    'version': '0.1',
    'summary': 'Gestión de piscigranjas',
    'description': 'Módulo para la gestión integral de piscigranjas.',
    'author': 'Codex',
    'depends': ['base', 'mail'],
    'data': [
        'security/piscigranja_security.xml',
        'security/piscigranja_rules.xml',
        'security/ir.model.access.csv',
        'views/piscigranja_menus.xml',
        'views/cycle_views.xml',
        'views/feed_views.xml',
        'views/health_views.xml',
        'views/environment_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
