acc_bal=input("Enter your acc balance")

if(int(acc_bal) > 100000 and int(acc_bal) < 200000):
    acc_bal = acc-bal-25000
    print("We have dedacted Ksh 25000 from your acc")
elif(int(acc_bal) > 500000 and int(acc_bal) < 100000):
     acc_bal=acc_bal-(0.3*acc_bal)
     print("We have deducted Ksh 30 percentfrom your account")
elif(int(acc_bal) > 100000):
     acc_bal-1000000
     print("We have deducted 15000 from your account")