import datetime
class shop:
    def __init__(self, stock):
        self.stock = stock

    def show_stock(self):
            print("\n\n\n\nThere are ",self.stock," Bikes Available.\n")   
            return self.stock

    def rent_bike(self, no_of_bikes ):

        if user_input < 0 :
            print ("Please Enter a Positive Value!")
            return None

        elif user_input > self.stock :
            print ("Sorry... only ",self.stock," bike are available.")
            return None

        else:

            rent_type = int(input("\n\n\nChoose how much time you want to rent the bikes for...\n\n1.Hourly = Rs300 Per Hour.\n2.Daily = Rs1000 Per Day.\n3.Weekl = Rs5000 Per Week.\n\n"))

            if rent_type == 1:

                no_of_hours = int(input("\n\nEnter the Number of Hours\n"))
                print ("\nYour Total is Rs", no_of_hours * 300)

            elif rent_type == 2:

                no_of_days = int(input("\n\nEnter the Number of Days\n"))
                print ("\nYour Total is Rs", no_of_days * 1000)

            elif rent_type == 3:
                no_of_weeks = int(input("\n\nEnter the Number of Weeks\n"))
                print ("\nYour Total is Rs", no_of_weeks * 5000)   

            else:
                print("Please Enter a Valide Plan!")

        self.stock = self.stock - no_of_bikes
        return self.stock    

while True:
    obj = shop(100)
    obj.show_stock()
    user_input = int(input("Enter the Number of Bikes you want to rent\n"))
    obj.rent_bike(user_input)
    
