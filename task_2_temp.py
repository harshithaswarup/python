import datetime
class Temperature:
    def get_date(self):
            x=int(input("enter a year:"))
            y=int(input("enter a month:"))
            z=int(input("enter the day:"))
            date1=datetime.date(x,y,z)
            date=date1.strftime('%d/%m/%y')
            return date


    def  get_temprtr(self,date):
        for temp_val in range(3):
            temp_val=raw_input("enter the temperature either in F or C:")
            degree=int(temp_val[:-1])
            i_convention=temp_val[-1]
            if i_convention.upper() == "F":
                res = int(round((degree - 32) * 5 / 9))
        return res,temp_val
    
    def add_temp(self,res,temp_val):
        temp_list=[]
        temp_list.append(res)
        temp_list.append(temp_val)
        fin_dict={}
        key=date
        fin_dict.setdefault(date,[])
        fin_dict[date].append(temp_list)
        fin_dict[date]=[temp_list]
        return fin_dict

    def get_user_date(self):
        x=int(input("enter a year:"))
        y=int(input("enter a month:"))
        z=int(input("enter the day:"))
        date_input=datetime.date(x,y,z)
        date_2=date_input.strftime('%d/%m/%y')
        return date_2
    
    def display_temp(self,date_2,fin_dict,date):
        if (date_2==date):
            print "enter 1 for max temp and 2 for min temp in degree celsius"
            choice_list=[1,2]
            for user_input in range(2):
                user_input=int(input("enter your choice:"))
                if(user_input==choice_list[0]):
                    print max(fin_dict[date][0])
                elif(user_input==choice_list[1]):
                   print min(fin_dict[date][0])
        
t=Temperature()
date=t.get_date()
res,temp_val=t.get_temprtr(date)
fin_dict=t.add_temp(res,temp_val)
date_2=t.get_user_date()
t.display_temp(date_2,fin_dict,date)
