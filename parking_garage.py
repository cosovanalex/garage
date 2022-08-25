# There are 200 spots available in the parking lot
# Cost of parking/hours is 3$

# Create the idea of a very basic Parking Garage
class Garage:
    pass

    def __init__(self, tickets = [], parking_spaces = [], current_ticket = {"paid" : False}):
        self.tickets = [x for x in range(1,201)]
        self.parking_spaces = [x for x in range(1,201)]
        self.current_ticket = {}       
    
    def takeTicket(self):
        print(f"There are {len(self.parking_spaces)} parking spots available.")
        print("\nPlease take your ticket! The cost of parking is 3$/hr.")
        self.parking_spaces = self.parking_spaces[:-1]
        self.tickets = self.tickets[:-1]

    def pay(self):
        hours = input("How many hours did you use the parking garage for? ")
        price = int(hours) * 3
        print(f"The total cost for parking is {price}$.")
        payment = input("Would you like to pay? - yes/no ")
        if payment == 'yes':
            self.current_ticket = {'paid': True}
            price = int(hours) * 3
            print(f"The total cost for parking is {price}$.")
            print("Thank you! Your ticket is paid. Please have the spot available in the next 15 minutes.")
             # for n in range(len(self.parking_spaces), 200):
            #     self.parking_spaces.append(n)
            # for n in range(len(self.tickets), 200):
            #     self.tickets.append(n)    
        elif payment == 'no':
            self.current_ticket = {'paid': False}
            print("Sorry, but you can't leave without paying.")     
        else:
            self.current_ticket = {'paid': False}
            print("You need to insert a valid amount.")

    def leaveGarage(self):
        if self.current_ticket == {'paid': True}:
            for n in range(len(self.parking_spaces), 200):
                self.parking_spaces.append(n)
            for n in range(len(self.tickets), 200):
                self.tickets.append(n)   
            print("Thank you! Have a nice day!")
        elif self.pay:
            pass
       

ex_1 = Garage()

def run():
    while True:
        response = input("What would you like to do? ticket/pay/leave ")
        if response.lower() == 'ticket':
            ex_1.takeTicket()
        
        elif response.lower() == 'pay':
            ex_1.pay()

        elif response.lower() == 'leave':
            ex_1.leaveGarage()
        
        else:
            print("You need to enter a valid option.")

run()