#-------------------------------------------------------------------------------
# Author:      Nate Wilson
# Name:        module5
#
# Description: This module includes the functions required for program4.
#-------------------------------------------------------------------------------

# -------------------------------------------------------------------
# readEmployeeName - gets validates and returns a user inputted name
# -------------------------------------------------------------------
def readEmployeeName():
    employee_name = input('Enter the employee name: ')
    while employee_name == '':
        print('Employee name must be entered!')
        print()
        employee_name = input('Enter the employee name: ')
    return employee_name

# -------------------------------------------------------------------
# readHourlyRate - gets validates and returns a user inputted houry rate
# -------------------------------------------------------------------
def readHourlyRate():
    while True:
        try:
            hourly_rate = float(input('Enter employee hourly rate: $'))
            while hourly_rate < 20:
                print('Invalid Hourly Rate, must be at least $20.00/hour.”')
                print()
                hourly_rate = float(input('Hourly rate: $'))
        except ValueError:
            print('Please enter numerical value for rate!')
            print()
            continue
        break
    return hourly_rate

# -------------------------------------------------------------------
# readWeeklyHours - gets validates and returns user inputted weekly hours
# -------------------------------------------------------------------
def readWeeklyHours(week_number):
    while True:
        try:
            weekly_hours = float(input('Enter hours worked for week {}: '.format(week_number)))
            while weekly_hours < 35 or weekly_hours > 80:
                print('Invalid number of hours, must be between 35 and 80.')
                print()
                weekly_hours = float(input('Enter hours worked for week {}: '.format(week_number)))
        except ValueError:
            print('Please enter numerical value for hours worked!')
            print()
            continue
        break
    return weekly_hours

# -------------------------------------------------------------------
# resetBillingFile - destroys and creates a new Billing.txt file
# -------------------------------------------------------------------
def resetBillingFile():
    Billing = open('Billing.txt','w')
    Billing.close()

# -------------------------------------------------------------------
# writeBillingRecord - writes recquired emplyee data to Billing.txt
# -------------------------------------------------------------------
def writeBillingRecord(name,hourly_rate,list_of_hours):
    Billing = open('Billing.txt','a')
    Billing.write(name+'\n')
    Billing.write(str(hourly_rate)+'\n')
    for hours in list_of_hours:
        Billing.write(str(hours)+'\n')
    Billing.close()

# -------------------------------------------------------------------
# calcInvoiceTotal - calculates the total invoice
# -------------------------------------------------------------------
def calcInvoiceTotal(total_hours_worked, hourly_rate):
    overtime_rate = float((hourly_rate*0.05) + hourly_rate)
    
    if total_hours_worked > 160:
        regular_pay = float(160* hourly_rate)
        overtime_hours = float(total_hours_worked-160)
        overtime_pay = float(overtime_hours * overtime_rate)
        amount_due = float(regular_pay + overtime_pay)
    else:
        regular_pay = float(total_hours_worked*hourly_rate)
        overtime_hours = 0
        overtime_pay = 0
        overtime_invoice = 0
        amount_due = regular_pay
    return [ amount_due, overtime_rate, overtime_hours, 
    overtime_pay,regular_pay]


# -------------------------------------------------------------------
# accumulateWeeklyBillingAmounts - reads weekly billing hours and 
# returns a list
# -------------------------------------------------------------------
def accumulateWeeklyBillingAmounts():
    billinghours = []
    for week in range(1,5):
        hours = readWeeklyHours(week)
        billinghours.append(hours)
    return billinghours

# -------------------------------------------------------------------
# calcTotalhours - calculates the total hours and returns a list containing total hours
# and average hours
# -------------------------------------------------------------------
def calcTotalHours(list_of_hours,total_for_average):
    sum_of_hours = 0
    for hours in list_of_hours:
        sum_of_hours += hours
    average = sum_of_hours/total_for_average
    return sum_of_hours, average

# -------------------------------------------------------------------
# readNextString - reads string and strips \n character
# -------------------------------------------------------------------
def readNextString(file_variable):
    _string = file_variable.readline()
    _string = _string.rstrip('\n')
    return _string
# -------------------------------------------------------------------
# readNextFloat - reads string and converts to float
# -------------------------------------------------------------------
def readNextFloat(file_variable):
    _float = float(readNextString(file_variable))
    return _float

# -------------------------------------------------------------------
# readFloatsToList - reads floats and returns a list a specified length
# -------------------------------------------------------------------
def readFloatsToList(file_variable,size_of_list):
    listoffloats = []
    for _float in range(size_of_list):
        _float = readNextFloat(file_variable)
        listoffloats.append(_float)
    return listoffloats

