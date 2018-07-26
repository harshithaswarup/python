import datetime
class Temperature:
    def get_date(self):
        for x in range(1):
            x=int(input("enter a year:"))
            y=int(input("enter a month:"))
            z=int(input("enter the day:"))
            date1=datetime.date(x,y,z)
            date=date1.strftime('%d/%m/%y')
            print date
        return date,date1


    def  get_temprtr(self,date,date1):
        temp_list=[]
        fin_dict={}
        for temp_val in range(3):
            temp_val=raw_input("enter the temperature either in F or C:")
            degree=int(temp_val[:-1])
            i_convention=temp_val[-1]
            o_convention=temp_val[-1]
            if i_convention.upper() == "F":
                res = int(round((degree - 32) * 5 / 9))
                temp_list.append(res)
                o_convention = "Celsius"
            else:
                temp_list.append(temp_val)
                print temp_list
        key=date1
        fin_dict.setdefault(date,[])
        fin_dict[date].append(temp_list)
        fin_dict[date]=[temp_list]
        print fin_dict
        return fin_dict

    def min_max_temp(self,fin_dict,date):
        x=int(input("enter a year:"))
        y=int(input("enter a month:"))
        z=int(input("enter the day:"))
        date_input=datetime.date(x,y,z)
        date_2=date_input.strftime('%d/%m/%y')
        if (date_2==date):
            print "the maximum temp is:",max(fin_dict[date][0])
            print "the minimum temp is:",min(fin_dict[date][0])
        else:
            print "the temp for the date is not available"
        
t=Temperature()
date,date1=t.get_date()
fin_dict=t.get_temprtr(date,date1)
t.min_max_temp(fin_dict,date)

