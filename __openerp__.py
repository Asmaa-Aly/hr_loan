
{
	'name' : 'Loan',
	'version' : '0.1',
	'author' : 'Asmaa Aly',
	'category' : 'Human Resources',
	'description' : """

	""",

	'depends' : ['hr', 'hr_payroll', 'account'],
	'data': [
		'sequences/hr_loan_sequence.xml',
		'datas/hr_payroll_data.xml',
		'views/hr_loan_view.xml',
		'views/hr_payroll_view.xml',
		#'views/board_hr_loan_statistical_view.xml',
	],

	'installable': True,
	'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
