# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : MasterData : HR',
    'version': '17.0.0.0.2',
    'summary': 'Master-data extracted from CDB for HR domain.',
    'description': 'Extracted from Clear-DB. Test-env master data. Edit the CSVs in data/ to add/remove rows before install.',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'BugFix-HR',
        'Jinasena_MasterData_Common',
    ],
    'data': [
        'data/hr.department.csv',
        'data/hr.job.csv',
        'data/hr.employee.csv',
        'data/hr.contract.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
