#   Kristen Anderson
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = (input('Enter start date (MM/DD/YYYY): '))
    todate = (input('Enter end date MM/DD/YYYY): '))
    return fromdate, todate
    #write the code to input fromdate and todate and return the values from the function.  
    #Prompt the user for the dates in the following format: mm/dd/yyyy
    #no validations are needed for this input, we will assume the dates are entered correctly




def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay


def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    # the following code creates a for loop to read through EmpDetailList and assign values in list to variables
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]

        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst




        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        # the following line of code assigns TotEmployees totals to dictionary 
        EmpTotals["TotEmp"] = TotEmployees
        # write code to assign TotHours, TotGrossPay, TotTax, and TotNetPay to corresponding dictionary item
        EmpTotals["hours"] = TotHours 
        EmpTotals["grosspay"] = TotGrossPay
        EmpTotals["incometax"] = TotTax
        EmpTotals["netpay"] = TotNetPay





def PrintTotals(EmpTotals):    
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    # write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary
    print(f'Total Number of Hours: {EmpTotals["hours"]}')
    print(f'Total Amount of Gross Pay: {EmpTotals["grosspay"]}')
    print(f'Total Amount of Tax: {EmpTotals["incometax"]}')
    print(f'Total Amount of Net Pay: {EmpTotals["netpay"]}')
    





if __name__ == "__main__":
    
 

    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        

        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]

        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail


        #the following code appends the list EmpDetail to the list EmpDetailList
        EmpDetailList.append(EmpDetail)


    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)




