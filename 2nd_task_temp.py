import datetime
class Temperature:
    def get_date(self):
            x=int(input("enter a year:"))
            y=int(input("enter a month:"))
            z=int(input("enter the day:"))
            date1=datetime.date(x,y,z)
            date=date1.strftime('%d/%m/%y')
            print date
            return date


    def  get_temprtr(self,date):
        self.temp_list=[]
        fin_dict={}
        for temp_val in range(3):
            temp_val=raw_input("enter the temperature either in F or C:")
            degree=int(temp_val[:-1])
            i_convention=temp_val[-1]
            o_convention=temp_val[-1]
            if i_convention.upper() == "F":
                res = int(round((degree - 32) * 5 / 9))
                self.temp_list.append(res)
                o_convention = "Celsius"
            else:
                self.temp_list.append(temp_val)
        key=date
        fin_dict.setdefault(date,[])
        fin_dict[date].append(self.temp_list)
        fin_dict[date]=[self.temp_list]
        print fin_dict
        return fin_dict

    def to_display_temp(self,fin_dict,date):
        x=int(input("enter a year:"))
        y=int(input("enter a month:"))
        z=int(input("enter the day:"))
        date_input=datetime.date(x,y,z)
        date_2=date_input.strftime('%d/%m/%y')
        if (date_2==date):
            print "enter 1 for max temp and 2 for min temp in degree celsius"
            choice_list=[1,2,3]
            for user_input in range(2):
                user_input=int(input("enter your choice:"))
                if(user_input==choice_list[0]):
                    print "the maximum temp is:",max(fin_dict[date][0])
                elif(user_input==choice_list[1]):
                    print "the minimum temp is:",min(fin_dict[date][0])
        else:
            print "the temp for the date is not available"
        #date=t.get_date()
        #fin_dict=t.get_temprtr(date)
            
        
t=Temperature()
date=t.get_date()
fin_dict=t.get_temprtr(date)
t.to_display_temp(fin_dict,date)

