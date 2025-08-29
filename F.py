# ==================== BUS CLASS ====================
class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            return True
        return False


# ==================== PASSENGER CLASS ====================
class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


# ==================== ADMIN CLASS ====================
class Admin:
    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    def login(self, user, pwd):
        return self.username == user and self.password == pwd


# ==================== BUS SYSTEM CLASS ====================
class BusSystem:
    FARE = 500   # fixed fare

    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin()
        self.admin_logged_in = False

    # ---------- Admin Features ----------
    def add_bus(self, number, route, seats):
        if self.admin_logged_in:
            bus = Bus(number, route, seats)
            self.buses.append(bus)
            print(f"✅ Bus {number} added successfully.")
        else:
            print("❌ Only admin can add buses. Please login first.")

    def admin_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.admin.login(username, password):
            self.admin_logged_in = True
            print("✅ Admin login successful.")
        else:
            print("❌ Invalid credentials.")

    def admin_menu(self):
        while self.admin_logged_in:
            print("\n---- Admin Menu ----")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                number = input("Enter bus number: ")
                route = input("Enter route: ")
                seats = int(input("Enter total seats: "))
                self.add_bus(number, route, seats)

            elif choice == "2":
                self.show_buses()

            elif choice == "3":
                self.admin_logged_in = False
                print("🚪 Logged out.")
            else:
                print("❌ Invalid choice.")

    # ---------- User Features ----------
    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.number == bus_number:
                if bus.book_seat():
                    passenger = Passenger(name, phone, bus)
                    self.passengers.append(passenger)
                    print(f"✅ Ticket booked for {name} on Bus {bus.number} ({bus.route})")
                    print(f"Fare: ৳{self.FARE}")
                    return
                else:
                    print("❌ No seats available.")
                    return
        print("❌ Bus not found.")

    def show_buses(self):
        if not self.buses:
            print("⚠️ No buses available.")
            return
        print("\n---- Bus List ----")
        for bus in self.buses:
            print(f"Bus {bus.number} | Route: {bus.route} | Seats: {bus.total_seats} | Available: {bus.available_seats()}")


# ==================== MAIN PROGRAM ====================
def main():
    system = BusSystem()

    while True:
        print("\n===== Bangladesh Bus Ticket Booking System =====")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.admin_login()
            if system.admin_logged_in:
                system.admin_menu()

        elif choice == "2":
            if not system.buses:
                print("⚠️ No buses available yet.")
                continue
            system.show_buses()
            bus_number = input("Enter bus number: ")
            name = input("Enter your name: ")
            phone = input("Enter your phone: ")
            system.book_ticket(bus_number, name, phone)

        elif choice == "3":
            system.show_buses()

        elif choice == "4":
            print("👋 Thank you for using the system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
