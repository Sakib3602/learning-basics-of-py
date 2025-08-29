# =================== USER CLASS ===================
class USER:
    def __init__(self, name, email, number, address):
        self.name = name
        self.email = email
        self.number = number
        self.address = address

# =================== EMPLOYEE CLASS ===================
class Employee(USER):
    def __init__(self, name, email, number, address, age, salary, designation):
        super().__init__(name, email, number, address)
        self.age = age
        self.salary = salary
        self.designation = designation

# =================== RESTAURANT CLASS ===================
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.allEmployees = []  # list to store Employee objects

    def add_employee(self, name, email, number, address, age, salary, designation):
        emp = Employee(name, email, number, address, age, salary, designation)
        self.allEmployees.append(emp)
        print(f"{name} is added to {self.name}!")

    def view_employees(self):
        print(f"Employees in {self.name}:")
        for emp in self.allEmployees:
            print(emp.name, emp.email, emp.number, emp.address, emp.age, emp.salary, emp.designation)

# =================== ADMIN CLASS ===================
class Admin(USER):
    def __init__(self, name, email, number, address):
        super().__init__(name, email, number, address)


    def add_employee(self, restaurant, name, email, number, address, age, salary, designation):
        restaurant.add_employee(name, email, number, address, age, salary, designation)

    # Admin tells Restaurant to show employees
    def view_employees(self, restaurant):
        restaurant.view_employees()
# ======================= Menu ======================
class Menu:
    def __init__(self):
        self.allMenu = [] 
    def add_item(self,item):
        self.allMenu.append(item)
    
    def findItem(self,item):
        for x in self.allMenu:
            if x["name"].lower() == item.lower():
                print(f"Item Available {x}")
                return item
            else :
                return None
    def remove_item(self,item):
        for x in self.allMenu:
            if x["name"].lower() == item.lower():
                self.allMenu.remove(x)
                print(f"Item removed {x}")
            else :
                return f'Item not find'
    def show_item(self):
        print("**************** Menu ***********************")
        print("Name\tPrice\tQuantity")
        for x in self.allMenu:
            print(f"{x['name']}\t{x['price']}\t{x['quantity']}")


# =================== DEMO ===================
r1 = Restaurant("Food Village")  # Create restaurant
ad = Admin("Sakib", "sakib@op.com", 12345678, "Dhaka")  # Create Admin

ad.add_employee(r1, "Shofic", "pokil@lo.com", 2334532, "Foridpur", 29, 12000, "Chef")
ad.add_employee(r1, "Motin", "moti@lo.com", 2334532, "Kalampur", 34, 15000, "Waiter")

ad.view_employees(r1)

pizza = Menu()
burger = Menu()
pizza.add_item({"name" : "Pizza", "price" : 2342, "Quantity" : 10})
burger.add_item({"name" : "burger", "price" : 22, "Quantity" : 10})

pizza.findItem("pizza")

menu = Menu()

# Add items
menu.add_item({"name": "Burger", "price": 150, "quantity": 10})
menu.add_item({"name": "Pizza", "price": 300, "quantity": 5})
menu.add_item({"name": "Pasta", "price": 200, "quantity": 7})

menu.show_item()


