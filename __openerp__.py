# -*- coding: utf-8 -*-
# Part of asmaa. See LICENSE file for full copyright and licensing details.

{
    'name': 'Loan Management',
    'version': '1.1',
    'category': 'Human Resources',
    'sequence': 75,
    'summary': 'Payroll, Loan Request, Employees Details',
    'description': """
Loan Management
==========================

This application enables you to manage Loan Requests of your company's staff 

You can manage:
---------------
* Employee Loan Requests
* HR Payroll
    """,
	'author': 'Asmaa Aly',
    'depends': [
        'hr_payroll',
        'hr',
		'account',
    ],
    'data': [
		'sequences/hr_loan_sequence.xml',
	    'datas/hr_payroll_data.xml',
        'views/hr_loan_view.xml',
		'views/hr_payroll_view.xml',
    ],
}
