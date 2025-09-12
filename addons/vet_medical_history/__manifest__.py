{
    'name': 'Veterinary Medical History',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Gestiona historias médicas de pacientes veterinarios',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vet_medical_views.xml',
    ],
    'application': True,
}
