class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Shop:
    def __init__(self):
        self.prod = []  # list of products

    def add_product(self, product):
        self.prod.append(product)  # add Product object

    def buy_prod(self, product_name):
        x = product_name.lower()
        for p in self.prod:
            if p.name.lower() == x:
                print(f"🎉 {p.name} bought successfully at price {p.price}")
                return
        print(f"❌ Product '{product_name}' not available in shop.")


# Example usage
shop = Shop()
shop.add_product(Product("T Shirt", 500))
shop.add_product(Product("Pent", 800))

shop.buy_prod("lungi")      # ✅ success
# shop.buy_prod("Shoes")     # ❌ not available
