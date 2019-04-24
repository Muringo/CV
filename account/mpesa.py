class account:
     def __init__(self,first_name,last_name,balance):
     	self.first_name = first_name
     	self.last_name = last_name
     	self.balance = balance


     def welcome(self):
     	return "Hello, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)


     def deposit(self,current_balance):
          deposit=current_balance
          self.balance=self.balance+current_balance
          return "Hello, {} {} your new balance is {}".format(self.first_name,self.last_name,current_balance)

     def withdraw(self,x):
          withdraw=x
          if x > self.balance:
               return "not successful"
          else:
               self.balance=self.balance-x
               return "Hello {} {} you have withdrawn {}".format(self.first_name,self.last_name,x)

     def showbalance(self):
          showbalance=self.balance
          return "Hello {} {} your immediate balance is {}".format(self.first_name,self.last_name,self.balance)


























































     