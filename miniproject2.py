bank_accounts={}
def create_account():
    account_number=input("enter number:")
    if account_number in bank_accounts:
        print("account already exists")
    else:
        name=input("enter holder name:")
        bank_accounts[account_number]={"name": name, "balance": 0}
        print(f"account created for {name}. with account number {account_number}")
        print(bank_accounts)

def deposit():
    account_number=input("enter number:")
    if account_number in bank_accounts:
        amount=float(int(input("enter amount to deposit:")))
        if amount>0:
            bank_accounts[account_number]["balance"]+=amount
            print(f"deposit amount {amount}.current balance:{bank_accounts[account_number]['balance']}")
        else:
         print("invalid amount")


    else:
      print("invalid account number")

def withdraw():
   account_number=input("enter number:")
   if account_number in bank_accounts:
      amount=float(int(input("enter amount to withdraw:")))
      if 0<amount<=bank_accounts[account_number]["balance"]:
         bank_accounts[account_number]["balance"]-=amount
         print(f"withdraw amount {amount} current balance:{bank_accounts[account_number]["balance"]}")
      else:
         print("invalid amount")

def check_balance():
   account_number=input("enter account number:")
   if account_number in bank_accounts:
      print(f"holder name: {bank_accounts[account_number]['name']}")
      print(f"balance check: {bank_accounts[account_number]['balance']}")
   else:
      print("invalid account number")
def bank():
      while True:
         print("=====bank menu=====")
         print("1.create account")
         print("2.deposit")
         print("3.withdraw")
         print("4.check balance")
         print("5.exit")
         choice=input("enter your choice:")
         if choice=="1":
          create_account()
         elif choice=="2":
          deposit()
         elif choice=="3":
          withdraw()
         elif choice=="4":
            check_balance()
         elif choice=="5":
            print("thank you for using our services")
         
bank()
