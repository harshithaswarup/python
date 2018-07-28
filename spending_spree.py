class Money:
    def get_balance(self):
        balance=1000.00
        print "The balance amount you have is:$",balance
        return balance

    def get_cost(self,balance):
       for y in range(5):
           item_cost=float(input("Enter the cost of the item you want to buy:$"))
           print "Are you sure to buy the item which costs:$ ",item_cost,"?"
           x=raw_input("enter Yes or No:")
           user_choice=["yes","no"]
           if(item_cost>balance):
               print "Sorry you don't have sufficient balance to buy the item!!"
               debt_amt=item_cost-balance
               print "You owe :$",debt_amt
           elif(x==user_choice[0]):
               balance-=item_cost
               print "The remaining money available to spend :$",balance
           else:
               print "The available balance is:$",balance
               
m=Money()
balance=m.get_balance()
m.get_cost(balance)
