import datetime 

list_expenses = []
list_incomes = []
list_savings = []

class Expenses:
	def __init__(self, cat, subcat, amount, date):
		self.cat = cat
		self.subcat = subcat
		self.amount = amount
		self.date = date

	def add_amount(self, new_amount):
		self.amount += new_amount


def add_element(selection):
	''' Add an element in the budget '''
	if selection == 'E':
		new_expense = input("Which expense to add? ")
		exp_amount = int(input("What is the amount of your expense? "))
		exp_date = int(input("When did you make the expense? (yyyymmdd) "))

		list_expenses.append(Expenses('Expense', new_expense, exp_amount, exp_date)) 

		'''
		new = True 

		for items in list_expenses:
			if list_expenses[item].subcat == new_expense:
				list_expenses[item].add_amount(exp_amount)
				list_expenses[item].date = exp_date
				new = False
				break

		if new == True:
			list_expenses.append(Expenses('Expense', new_expense, exp_amount, exp_date)) 
		'''

	if selection == 'I':
		new_inc = input("Which income to add? ")
		inc_amount = int(input("What is the amount of your income? "))
		inc_date = int(input("When did you receive the income? (yyyymmdd) "))

		list_incomes.append(Expenses('Income', new_inc, inc_amount, inc_date)) 

	if selection == 'S': 
		new_sav = input("Which saving to add? ")
		sav_amount = int(input("What is the amount of your saving? "))
		sav_date = int(input("When did you make the saving? (yyyymmdd) "))

		list_savings.append(Expenses('Savings', new_sav, sav_amount, sav_date)) 

def netflow():
	totalsum = 0

	for item in list_incomes: 
		totalsum += item.amount
	for item in list_expenses: 
		totalsum -= item.amount

	return totalsum

def table(currency):
	''' Create a table to display the budget '''
	print("Household budget:")

	print("Incomes         \t Amount | Date")
	for item in list_incomes:
		print("{:<15} \t {:<4}{} | {:8}".format(item.subcat, item.amount, currency, item.date))

	print("\n")

	print("Savings         \t Amount | Date")
	for item in list_savings:
		print("{:<15} \t {:<4}{} | {:8}".format(item.subcat, item.amount, currency, item.date))

	print("\n")

	print("Expenses         \t Amount | Date")
	for item in list_expenses:
		print("{:<15} \t {:<4}{} | {:8}".format(item.subcat, item.amount, currency, item.date))

	totalsum = netflow()
	print("Total net flow (Incomes - Expenses) \t {}{}".format(totalsum, currency))

#salary = Expenses('Income','Salary', 2500, datetime.date.today())
#table(10, income, salary)

complete = True

currency = input("What is your currency? ")

while complete: 
	selection = input("What do you want to add in your budget? An expense (E), an income (I) or a saving (S): ")
	add_element(selection)

	display_table = input("Do you want to see your entire household bugdet? Yes (Y) or no (N): ")
	if display_table == 'Y':
		table(currency)

	keepgoing = input("Do you want to add something else in your budget? Yes (Y) or no (N): ")
	if keepgoing != 'Y':
		complete = False

