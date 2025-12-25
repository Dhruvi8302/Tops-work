class BusReservation:
    def __init__(self):
        self.routes = {
            1: {"route": "Mumbai to Pune", "price": 500, "seats": []},
            2: {"route": "Delhi to Jaipur", "price": 600, "seats": []},
            3: {"route": "Bangalore to Mysore", "price": 450, "seats": []}
        }
        self.tickets = {} #store booked tickets 
        self.ticket_id = 1

    def showRoutes(self):
        print("\n=== Available Routes ===")
        for route_id, info in self.routes.items():
            print(f"{route_id}. {info['route']} - ₹{info['price']} (Booked Seats: {len(info['seats'])}/40)")

    def bookTicket(self):
        name = input("Enter Passenger Name: ")

        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("Invalid Age!")
            return

        mobile = input("Enter Mobile Number: ")
        if len(mobile) != 10 or not mobile.isdigit():
            print("Invalid Mobile Number!")
            return

        self.showRoutes() #calling the method to check 
        try:
            route_id = int(input("Select Route Number: "))
        except ValueError:
            print("Invalid Choice!")
            return

        if route_id not in self.routes:
            print("Route does not exist!")
            return

        if len(self.routes[route_id]["seats"]) >= 40:   # Seat Availability Check
            print("No seats available on this route!")
            return

        seat_no = len(self.routes[route_id]["seats"]) + 1    # Assign Seat & Ticket ID
        self.routes[route_id]["seats"].append(seat_no)

        ticket_id = self.ticket_id
        self.ticket_id += 1

        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": self.routes[route_id]["route"],
            "price": self.routes[route_id]["price"],
            "seat": seat_no
        }

        print("\n Ticket Booked Successfully!")
        print(f"Ticket ID: {ticket_id}, Seat: {seat_no}")
        print(f"Route: {self.routes[route_id]['route']}, Price: ₹{self.routes[route_id]['price']}")

    def viewTicket(self):
        try:
            ticket_id = int(input("Enter Ticket ID: "))
        except ValueError:
            print("Invalid Ticket ID!")
            return

        if ticket_id in self.tickets:
            print("\n=== Ticket Details ===")
            data = self.tickets[ticket_id]
            for key, value in data.items():
                print(f"{key.title()} : {value}")
        else:
            print("No ticket found with this ID!")

    def cancelTicket(self):
        try:
            ticket_id = int(input("Enter Ticket ID to Cancel: "))
        except ValueError:
            print("Invalid Ticket ID!")
            return

        if ticket_id in self.tickets:
            route = self.tickets[ticket_id]["route"]

            # Remove seat number from that route
            for r_id, info in self.routes.items():
                if info["route"] == route:
                    seat_no = self.tickets[ticket_id]["seat"]
                    info["seats"].remove(seat_no)

            del self.tickets[ticket_id]
            print(" Ticket Cancelled Successfully!")
        else:
            print("Ticket not found!")

obj = BusReservation()
while True:

    print("\n===== BUS RESERVATION SYSTEM =====")
    print("1. Show Routes")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue  

    match ch:
        case 1:
            obj.showRoutes()
        case 2:
            obj.bookTicket()
        case 3:
            obj.viewTicket()
        case 4:
            obj.cancelTicket()
        case 5:
            print("Exiting System...")
            break
        case _:
            print("Invalid Choice!")