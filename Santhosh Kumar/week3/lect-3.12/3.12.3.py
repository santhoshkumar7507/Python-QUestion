emp_id=input('Enter the Employee Id:')
while(emp_id!="-1"):
    trade=int(input("Enter the trade amount:"))
    profit_loss = 0
    while(trade !=0):
        profit_loss = profit_loss + trade
        trade = int(input('Enter the trade amount:'))
    print(f'profit/loss for employee {emp_id} is {profit_loss}')
    empID = input('/nEnter employeeID: ')