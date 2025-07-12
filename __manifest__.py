{
    'name': 'Student Management',
    'version': '16.0.1.0.0',
    'category': 'Education',
    'summary': 'Manage students and courses',
    'description': """
        Student Management Module
        =========================
        This module provides functionality to manage students and courses including:
        * Student registration and management
        * Course management
        * Student-Course relationships
        * Access control with Student Manager group
        * Public website display of confirmed students
    """,
    'author': 'Kyle Sin Lynn',
    'license': 'AGPL-3',
    'depends': ['base', 'website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/menu.xml',
        'templates/website_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
