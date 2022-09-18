from datetime import datetime
import sys


print("***************WELCOME TO SUNDARAM TRAVELS***************")
print("___________________________________________________________\n")
print("\n----------ACCOUNT CREATION----------")
name = input("\n Enter your Full name: ").upper()
phone= input(" Enter your phone number: ")
gender=str(input("Gender   (M/F): "))
age= input("Enter your age :")
class travel():
    def __init__(self ,name,phone,gender,age ):
        self.name= name
        self.phone= phone
        self.gender=gender
        self.age=age

    def bus(self):
        location = ["Tirunelveli to chennai","Tirunelveli to madurai","Tirunelveli to Coimbatore","Tirunelveli to Nagarkovil","Tirunelveli to Kanyakumari"]
        cost_bus = [1000,780,650,250,300]
        print("""  
                   Now Available Route
                  ---------------------
                1. Tirunelveli to chennai 
                2. Tirunelveli to madurai 
                3. Tirunelveli to Coimbatore
                4. Tirunelveli to Nagarkovil
                5. Tirunelveli to Kanyakumari """)
        route=int(input(f"\nEnter your choice:"))
        if route==1:
            x=datetime.now()
            print(" Travel From",location[0],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_bus[0],
            "\n Bus Time :10.15pm"
            "\n Your Reporting Time is: 10.00pm")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************BUS TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[0],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_bus[0],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_bus[0]*ticket )
            else :
                print("Thank you")
        elif route==2:
            x=datetime.now()
            print(" Travel From",location[1],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_bus[1],
            "\n Bus Time :9.15pm"
            "\n Your Reporting Time is: 9.00pm")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************BUS TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[1],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_bus[1],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_bus[1]*ticket )
            else :
                print("Thank you")
        elif route==3:
            x=datetime.now()
            print(" Travel From",location[2],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_bus[2],
            "\n Bus Time :8.15pm"
            "\n Your Reporting Time is: 8.00pm")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************BUS TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[2],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_bus[2],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_bus[2]*ticket )
            else :
                print("Thank you")
        elif route==4:
            x=datetime.now()
            print(" Travel From",location[3],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_bus[3],
            "\n Bus Time :10.15pm"
            "\n Your Reporting Time is: 10.00pm")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************BUS TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[3],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_bus[3],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_bus[3]*ticket )
            else :
                print("Thank you")
        elif route==5:
            x=datetime.now()
            print(" Travel From",location[4],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_bus[4],
            "\n Bus Time :10.15pm"
            "\n Your Reporting Time is: 10.00pm")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(F" ",
                " **************BUS TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[4],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_bus[4],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_bus[4]*ticket )
            else :
                print("Thank you")

        else:
            print("Please Enter valid number:")
            route=int(input(f"\nEnter your choice:"))
            exit()
        
    def train(self):
        location = ["Tirunelveli to chennai","Tirunelveli to madurai","Tirunelveli to Coimbatore"]
        cost_train = [550,340,350]
        print("""  
                Now Available Train Route
                  ---------------------
                1. Tirunelveli to chennai 
                2. Tirunelveli to madurai 
                3. Tirunelveli to Coimbatore
                 """)
        route=int(input(f"\nEnter your choice:"))
        if route==1:
            x=datetime.now()
            print(" Travel From",location[0],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_train[0],
            "\n Train Time :8.15pm"
            "\n Your Reporting Time is: 8.00pm")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************TRAIN TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[0],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_train[0],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_train[0]*ticket )
            else :
                print("Thank you")
        elif route==2:
            x=datetime.now()
            print(" Travel From",location[1],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_train[1],
            "\n Bus Time :9.15am"
            "\n Your Reporting Time is: 9.00am")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************TRAIN TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[1],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_train[1],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_train[1]*ticket )
            else :
                print("Thank you")
        elif route==3:
            x=datetime.now()
            print(" Travel From",location[2],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_train[2],
            "\n Bus Time :8.15am"
            "\n Your Reporting Time is: 8.00am")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************TRAIN TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[2],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_train[2],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_train[2]*ticket )
            else :
                print("Thank you")
        else:
            print("Please Enter valid number:")
            route=int(input(f"\nEnter your choice:"))
            exit()
    def flight(self):
        location = ["Thoothukudi to Chennai","Thoothukudi to coimbatore","Thoothukudi to madurai"]
        cost_Flight = [2000,1500,800]
        print("""  
                Now Available Domestic Route
                  ---------------------
                1. Thoothukudi to chennai 
                2. Thoothukudi to  coimbatore
                3. Thoothukudi to madurai
                 """)
        route=int(input(f"\nEnter your choice:"))
        if route==1:
            x=datetime.now()
            print(" Travel From",location[0],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_Flight[0],
            "\n Train Time :8.15pm"
            "\n Your Reporting Time is: 8.00pm")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************TRAIN TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[0],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_Flight[0],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_Flight[0]*ticket )
            else :
                print("Thank you")
        elif route==2:
            x=datetime.now()
            print(" Travel From",location[1],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_Flight[1],
            "\n Bus Time :9.15am"
            "\n Your Reporting Time is: 9.00am")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************TRAIN TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[1],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_Flight[1],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_Flight[1]*ticket )
            else :
                print("Thank you")
        elif route==3:
            x=datetime.now()
            print(" Travel From",location[2],
            "\n Your Minimum Bus Fare Amount is : Rs.",cost_Flight[2],
            "\n Bus Time :8.15am"
            "\n Your Reporting Time is: 8.00am")
            booking=str(input(f"\nDo you want ticket ? (y/n) : ")).lower().strip()
            if booking== "y":
                day=input("Enter your trip date by given format (DD/MM/YY):")
                ticket= int(input (f"Enter the no. of ticket by digit :"))
                print(f" ",
                " **************TRAIN TICKET**************",
                "\n Ticket Booked Time:",x,
                "\n Passenger        :",self.name,"(",self.age,self.gender,")",
                "\n Phone number     :",self.phone,
                "\n  From ", location[2],
                "\n Trip date        :",day,
                "\n Ticket rate per head : ",cost_Flight[2],
                "\n Number of Ticket :",ticket,
                "__________________________________"
                "\n Total Amount     :",cost_Flight[2]*ticket )
            else :
                print("Thank you")
        else:
            print("Please Enter valid number:")
            route=int(input(f"\nEnter your choice:"))
            exit()
travel = travel(name,phone,gender,age)

while True:
    print("""
        1.Bus
        2.Train
        3.Flight""")

    trans = input("\nSelect your Travel mode (1/2/3):").lower().strip()
    if trans == 1:
        travel.bus()
    elif trans == 2:
        travel.train()
    elif trans == 3:
        travel.flight()    
    else:
        print(" please select correct travel type\n")