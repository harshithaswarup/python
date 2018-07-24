import urllib, json
class Portfolio:
    def get_stock_details(self):
        self.stock_name=[]
        self.stock_count=[]
        getFile=raw_input("enter the file:")
        #C:\Users\Harshitha\Desktop\pgrm\portfolio.txt
        file = open(getFile,"r")
        for line in file:
            print str(line)
            a=line.split(',')
            for b in a:
                c=b.strip().split('-')
                self.stock_name.append(c[0])
                self.stock_count.append(c[1])
                # the values are converted into int
                self.stock_count=map(int,self.stock_count)
                
    def retrieve_stock_price(self,x):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&outputsize=full&apikey=demo"
        url_1=url.replace("MSFT",x)
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        self.MS_price=data['Time Series (15min)']['2018-07-16 16:00:00']['2. high']
        self.GOOG_price=data['Time Series (15min)']['2018-07-16 15:45:00']['2. high']
        self.INFY_price=data['Time Series (15min)']['2018-07-16 15:30:00']['2. high']
        self.AMZN_price=data['Time Series (15min)']['2018-07-16 15:15:00']['2. high']
        
    def get_stock_value(self):
        self.stock_value_1=[(float(self.stock_count[0])*float(self.GOOG_price))+(float(self.stock_count[1])*float(self.MS_price))]
        print "the stock value of 1st person:",self.stock_value_1
        self.stock_value_2=[(float(self.stock_count[2])*float(self.INFY_price))+(float(self.stock_count[3])*float(self.GOOG_price))+(float(self.stock_count[4])*float(self.MS_price))]
        print "stock value of 2nd person:",self.stock_value_2
        self.stock_value_3=[(float(self.stock_count[5])*float(self.GOOG_price))+(float(self.stock_count[6])*float(self.AMZN_price))+(float(self.stock_count[7])*float(self.MS_price))]
        print "stock value of 3rd person:",self.stock_value_3
        

    def to_display_values(self):
        list_stock_value=[]
        list_stock_value.append(self.stock_value_1)
        list_stock_value.append(self.stock_value_2)
        list_stock_value.append(self.stock_value_3)
        list_stock_value.sort(reverse=True)
        print "the stock value in decreasing order is:",list_stock_value
        

s=Portfolio()
s.get_stock_details()
s.retrieve_stock_price("GOOG")
s.get_stock_value()
s.to_display_values()
