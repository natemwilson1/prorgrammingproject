import program5
import program5a

QUIT = '0'
ENTER_BILLING_DATA = '1'
ADHOC_BILLING_REPORT = '2'


def displayMenu():
	print()
	print('*'*60)
	print('Billing System Menu:')
	print('\t0 - End')
	print('\t1 - Enter billing data')
	print('\t2 - Display adhoc billing report')

def main():
	option = ''
	while option != QUIT:
		displayMenu()
		option = input('Option ==> ')
		print('*'*60)
		if option == ENTER_BILLING_DATA:
			program5.main()
		elif option == ADHOC_BILLING_REPORT:
			program5a.main()
		elif option == QUIT:
			print('Exiting program...')
		else:
			print('Please enter an available option.')
main()
