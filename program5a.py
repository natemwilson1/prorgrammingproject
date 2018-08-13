# -------------------------------------------------------------------
# Author:   Nate Wilson
# Name:     Program5a
#
# Description:
# This program reads data from a document named Billing.txt that is
# created by program3 and produces a management report that includes
# The employees name, hourly rate, hours work for week 1-4, and a total
# invoice due.  It also provides a report on total billable hours,
# average billable hours, and a total billing due for all employees.
# -------------------------------------------------------------------

import module5


def main():


    # constants and variables

    listAllBillableHours = [] # a list of all billable hours
    numberOfEmployees = 0     # an accumulator of employees
    totalAmountDue = 0        # sum of all amount due
    employeeName = ''         # employees name string
    hourlyRate = 0            # employees hourly rate
    listEmployeeWeeklyHours =[] # list of weekly hours for each employee
    Billing = 0               # file variable
    totalHours_AvarageHours = () # tuple of employee total and average hours
    totalAllHours_AverageAllhours = () # tuple of all total and average hours
    totalAllHours = 0            # sum of all employees hours
    averageAllHours = 0          # average of all employees hours
    mostHours = 0               # max hours worked 
    leastHours = 0             # min hours worked


    # print the begining of the display
    print()
    print('Employee','\t\tRate','\tWeek1','\tWeek2','\tWeek3',
    '\tWeek4','\tTotal',sep='')

    # opens the Billing.txt file in read mode

    Billing = open('Billing.txt', 'r')
    
    # read first line for employee name string

    employeeName = module5.readNextString(Billing)
    
    # while loop to read all records

    while employeeName != '':
        
        numberOfEmployees += 1
        hourlyRate = module5.readNextFloat(Billing)
        listEmployeeWeeklyHours = module5.readFloatsToList(Billing,4)
        listAllBillableHours.extend(listEmployeeWeeklyHours)
        week1 = listEmployeeWeeklyHours[0]
        week2 = listEmployeeWeeklyHours[1]
        week3 = listEmployeeWeeklyHours[2]
        week4 = listEmployeeWeeklyHours[3]
        totalHours_AvarageHours = module5.calcTotalHours(listEmployeeWeeklyHours,4)
        totalBillableHours = totalHours_AvarageHours[0]
        invoiceDataList = module5.calcInvoiceTotal(totalBillableHours, hourlyRate)
        amountDue = invoiceDataList[0]
        totalAmountDue += amountDue
        
        # display record for each employee

        print(employeeName,'\t\t',hourlyRate,'\t',week1,'\t',week2,
        '\t',week3,'\t',week4,'\t','$',format(amountDue,',.2f'),sep='')

        # check for next employee

        employeeName = module5.readNextString(Billing)

    # close file

    Billing.close()

    totalAllHours_AverageAllhours = module5.calcTotalHours(listAllBillableHours,numberOfEmployees)
    totalAllHours = totalAllHours_AverageAllhours[0]
    averageAllHours = totalAllHours_AverageAllhours[1]
    leastHours = min(listAllBillableHours)
    mostHours = max(listAllBillableHours)


    # displays the additional control data

    print()
    print('Total Billable Due: $', format(totalAmountDue, ',.2f'),sep='')
    print('Total Billable Hours:', format(totalAllHours, '.2f'))
    print('Average Billable Hours:', format(averageAllHours,'.2f'))
    print('Least hours worked:', format(leastHours,'.2f'))
    print('Most hours worked:', format(mostHours,'.2f'))
    









