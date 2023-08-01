'''In this program, I have implemented OOPs concept to keep record of different types of vehicles.'''
class Vehicle:
    # Setting up attributes using constructor:
    def __init__(self, typ, milg, clr, cpy):
        self.type="Car"
        self.mileage="20kmpl"
        self.colour="Red"
        self.company="TATA"

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
Vehicle1= Vehicle("Bike","60kmpl","Yellow","Hero")

# Creating object 2:
Vehicle2= Vehicle("Truck","16kmpl","Orange","Mahindra")

# Creating object 3:
Vehicle3= Vehicle("E-Rickshaw","70km per charge","White","Ceeon")

# Creating object 4:
Vehicle4= Vehicle("Van","22kmpl","White","Maruti")

# Creating object 5:
Vehicle5= Vehicle("Tempo","24kmpl","Yellow and Black","Force Motors Ltd.")

#Calling methods
Vehicle1.vehichleType()
Vehicle2.vehichleColour()
Vehicle3.vehichleMileage()
Vehicle4.vehichleCompany()
Vehicle5.complete_info()
