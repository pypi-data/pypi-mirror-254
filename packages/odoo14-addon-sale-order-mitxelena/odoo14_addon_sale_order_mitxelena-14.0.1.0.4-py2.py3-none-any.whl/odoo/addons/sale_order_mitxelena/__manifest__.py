{
    'name': 'Sale Order Mitxelena Custom',
    'version': '14.0.1.0.4',
    'category': 'Sales',
    'summary': 'Customization for sale order',
    'depends': ['sale', 
                'base'],
    'data': [
        'views/sale_order_line_views.xml',
        'security/ir.model.access.csv',
        'reports/sale_order_report_template.xml',
        'reports/mitxelena_standar_layout.xml',
        'reports/mitxelena_sale_order_template.xml',
        'wizard/sale_order_report_wizard_view.xml'
    ],
    'installable': True,
}