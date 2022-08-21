import datetime
now = datetime.datetime.now()
class shop:
    def __init__(self, stock = 90):
        self.stock = stock

    def show_stock(self):
            print("\n\nThere are ",self.stock," Bikes Available.\n")   

    def validate_user_input(self, n):

        if n <= 0:
            print("Enter a valid number!")
        
        elif n > self.stock:
            print (" Sorry We Only have ",self.stock," Bikes Left in Stock.")

        else:
            print("\n\n\nChoose how much time you want to rent the bikes for...\n\n1.Hourly = Rs300 Per Hour.\n2.Daily = Rs1000 Per Day.\n3.Weekl = Rs5000 Per Week.\n\n")

    
    def rent_bike_hourly(self,no_of_bikes ):

        print("\nYou have rented ",no_of_bikes," Bike(s) on Hourly Basis at ",now.ctime(),"\nRs 300 will be deducted from your account hourly")
  
    def rent_bike_daily(self,no_of_bikes):

        print("\nYou have rented ",no_of_bikes," Bike(s) on Daily Basis at ",now.ctime(),"\nRs 1000 will be deducted from your account daily")

    def rent_bike_weekly(self,no_of_bikes):

        print("\nYou have rented ",no_of_bikes," Bike(s) on Daily Basis at ",now.ctime(),"\nRs 5000 will be deducted from your account weekly")


while True:
    obj = shop()
    obj.show_stock()
    user_input = int(input("Enter the Number of Bikes you want to rent\n"))
    obj.validate_user_input(user_input)
    rent_basis = int(input())

    if rent_basis == 1:
        obj.rent_bike_hourly(user_input)
        print ("\nThank You!\nWe Hope You Enjoy our Services.")

    elif rent_basis == 2:
        obj.rent_bike_daily(user_input)
        print ("\nThank You!\nWe Hope You Enjoy our Services.")

    elif rent_basis == 3:
        obj.rent_bike_weekly(user_input)
        print ("\nThank You!\nWe Hope You Enjoy our Services.")

    else :
        print("Please Choose a Valid Plan!")