'''In this program, I have implemented OOPs concept to keep record of different types of vehicles.'''
class Vehicle:
    # Setting up class attributes(variables):
    type="Car"
    mileage="20kmpl"
    colour="Red"
    company="TATA"

    # Setting up class methods:

    # method to return type of vehicle 
    def vehichleType(self):
        print(f"The vehicle is of type {self.type}")
    # method to return milage of vehicle 
    def vehichleMileage(self):
        print(f"The mileage of vehicle is {self.mileage}")
    # method to return color of vehicle
    def vehichleColour(self):
        print(f"The colour of the vehicle is {self.colour}")
    # method to return company of vehicle
    def vehichleCompany(self):
        print(f"The company of vehicle is {self.company}")
    # method to give entire info of vehicle at once:
    def complete_info(self):
        print(f"The vehicle is of type {self.type} which is of colour {self.colour} and gives mileage of {self.mileage} and is of {self.company} company.")

# Creating object 1:
Vehicle1= Vehicle()
Vehicle1.type="Bike"
Vehicle1.mileage="60kmpl"
Vehicle1.colour="Yellow"
Vehicle1.company="Hero"

# Creating object 2:
Vehicle2= Vehicle()
Vehicle2.type="Truck"
Vehicle2.mileage="16kmpl"
Vehicle2.colour="Orange"
Vehicle2.company="Mahindra"

# Creating object 3:
Vehicle3= Vehicle()
Vehicle3.type="E-Rickshaw"
Vehicle3.mileage="70km per charge"
Vehicle3.colour="White"
Vehicle3.company="Ceeon"

# Creating object 4:
Vehicle4= Vehicle()
Vehicle4.type="Van"
Vehicle4.mileage="22kmpl"
Vehicle4.colour="White"
Vehicle4.company="Maruti"

# Creating object 5:
Vehicle5= Vehicle()
Vehicle5.type="Tempo"
Vehicle5.mileage="24kmpl"
Vehicle5.colour="Yellow and Black"
Vehicle5.company="Force Motors Ltd."

#Calling methods
Vehicle1.vehichleType()
Vehicle2.vehichleColour()
Vehicle3.vehichleMileage()
Vehicle4.vehichleCompany()
Vehicle5.complete_info()
