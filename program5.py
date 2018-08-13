# -------------------------------------------------------------------
# Author:   Nate Wilson
# Name:     Program5
#
# Description:
# Program that gathers employee information
# and creates an billing invoice for the  month.
# program3 adds the ability to enter more than one emplyee as
# well as adding user input validation and creates a file in which
# the employee data is stored
# -------------------------------------------------------------------

import module5

def main():

    print()
    
    # initialize conditional variable for loop

    keep_going = 'y'

    # initialize variables

    hourlyRate = 0         #employees hourly rate
    employeeName = 0       #employees name string
    hoursList = []         #list of employees weekly hours 
    totalBillableHours = 0    #sum of list of billable hours 
    averageWeeklyHours = 0    #average of list of weekly hours  
    invoiceDataList = 0       # list of data pertaining billing     
    regularWorkWeek = 160     # constant 40 hour work week * 4  
    amountDue = 0             # total billable for invoice  
    overtimeHours = 0         # the amount of hours worked over 160  
    regularPay = 0            # amount billable under 160 hours  
    overtimePay = 0           # amount billable over 160 hours  

    # reset billing.txt file

    module5.resetBillingFile()

    # initialize main loop

    while keep_going == 'y':

        # gathers the user input using functions defined
        # in module5

        employeeName = module5.readEmployeeName()
        hourlyRate = module5.readHourlyRate()
        hoursList = module5.accumulateWeeklyBillingAmounts()

        # append the user data to the Billing.txt file

        module5.writeBillingRecord(employeeName, hourlyRate, hoursList)

        # performs required calculations and assigns to variables

        totalHours_averageHours = module5.calcTotalHours(hoursList,4)
        totalBillableHours = totalHours_averageHours[0]
        averageWeeklyHours = totalHours_averageHours[1]
        invoiceDataList = module5.calcInvoiceTotal(totalBillableHours, hourlyRate)
        amountDue = invoiceDataList[0]
        overtimeRate = invoiceDataList[1]
        overtimeHours = invoiceDataList[2]
        overtimePay = invoiceDataList[3]
        regularPay = invoiceDataList[4]
       
       # prints a formatted billing invoice

        print()
        print()
        print('-'*60)
        if totalBillableHours > regularWorkWeek:
           print(employeeName,'worked',format(overtimeHours, '.2f'),
            'hours of overtime.')
           print()
        else:
            print(employeeName, 'worked no overtime.')
            print()
        print('Invoice')
        print('Resource:',employeeName,'\tAverage weekly hours:',
        format(averageWeeklyHours,'.2f'))
        print()
        print('Total billable hours: ',format(totalBillableHours,'.2f'),
        '\trate: $',format(hourlyRate,'.2f'),sep = '')
        if totalBillableHours > regularWorkWeek:
            print('Overtime hours: ',format(overtimeHours,'.2f'),
            ' @ $',format(overtimeRate, '.2f'),'\t=$', format(overtimePay,',.2f'),sep='')
            print('Regular hours: ',format(regularWorkWeek,'.2f'),
            ' @ $',format(hourlyRate, '.2f'),'\t=$', format(regularPay,',.2f'),sep='')
            print('Amount Due: $', format(amountDue, ',.2f'),sep = '')
        else:
            print('Amount Due: $', format(amountDue, ',.2f'),sep = '')
        print('-'*60)
        keep_going = input('Would you like to add another employee?\nEnter "y" for yes or any other key to close: ')




