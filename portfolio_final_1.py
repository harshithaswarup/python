import urllib
class Portfolio:
    def retrieve_stock_price(self,x):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&outputsize=full&apikey=demo"
        #response = urllib.urlopen(url)
        #data = json.loads(response.read())
        #MS_price=data['Time Series (15min)']['2018-07-16 16:00:00']['2. high']
        MS_price= 50.0
        return MS_price
        
    def get_stock_value(self,stock_price,stock_count):
        count = float(stock_price) * float(stock_count)
        return count
    
    def get_stock_details(self):

        getFile=raw_input("enter the file:")
        #C:\Users\Harshitha\Desktop\pgrm\portfolio.txt
        file=open(getFile,"r")
        final = [];
        for line in file:
            a=line.split(',')
            onlineValue = 0.0
            for b in range(len(a)):
                oneLine = a[b].strip().split("-")
                count = 0.0
                for line in range(len(oneLine)-1):
                    stock_price =  s.retrieve_stock_price(oneLine[line])
                    stock_count =  oneLine[line+1].strip()
                    
                    val = s.get_stock_value(stock_price,stock_count)
                    print val
                onlineValue += val
            print "the values of the stocks are:", onlineValue
            final.append(onlineValue)

        for i in  final:
            final.sort(reverse=True)
            print "the stock values in decreasing order is:",final
                    
                
s=Portfolio()
s.retrieve_stock_price("GOOG")
stock_count=s.get_stock_details()


