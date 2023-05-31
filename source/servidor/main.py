CLIENT_DATABASE = {}
EMPLOYEE_DATABASE = {}
PRODUCT_DATABASE = {}
SALES_DATABASE = {}

class Person:
    def __init__(self, code: str, name: str, phone: str, address: str, email: str):
        self.code = code
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email


class Client(Person):
    def __init__(self, code: str, name: str, phone: str, address: str, email: str):
        super().__init__(code, name, phone, address, email)


class Product:
    def __init__(self, code: str):
        self.code = code

class Product_Detail(Product):
   def __init__(self, code: str, name: str, type: str, price: float, stock: int, description: str):
        super().__init__(code)
        self.name = name
        self.type = type
        self.price = price
        self.stock = stock
        self.description = description

class Sale:
    def __init__(self, code: str):
        self.code = code

class Sale_Detail(Sale):
        def __init__(self, code: str, date: str, *acquired_products):
            super().__init__(code)
            self.date = date
            self.acquired_products = acquired_products


class Employee(Client):
    def __init__(self, code: str, name: str, phone: str, address: str, email: str):
        super().__init__(code, name, phone, address, email)

    @staticmethod
    def insert_client(client):
        CLIENT_DATABASE[client.code] = dict(
            name = client.name,
            phone = client.phone,
            address = client.address,
            email = client.email,
        )
    
    @staticmethod
    def delete_client(code):
        if code in CLIENT_DATABASE:
            del CLIENT_DATABASE[code]
    
    @staticmethod
    def modify_client(code: str, new_name: str, new_phone: str, new_address: str, new_email: str):
        if code in CLIENT_DATABASE:
            CLIENT_DATABASE[code] = dict(
                name = new_name,
                phone = new_phone,
                address = new_address,
                email = new_email,
            )

    @staticmethod
    def show_client(client):
        return CLIENT_DATABASE.get(client.code, 'Does not exist')

    @staticmethod
    def insert_product(product):
        PRODUCT_DATABASE[product.code] = dict(
            name = product.name,
            type = product.type,
            price = product.price,
            stock = product.stock,
            description = product.description
        )
    
    @staticmethod
    def delete_product(code):
        if code in PRODUCT_DATABASE:
            del PRODUCT_DATABASE[code]
    
    @staticmethod
    def modify_product(code: str, new_name: str, new_type: str, new_price: str, new_stock: str, new_description: str):
        if code in PRODUCT_DATABASE:
            PRODUCT_DATABASE[code] = dict(
                name = new_name,
                type = new_type,
                price = new_price,
                stock = new_stock,
                description = new_description
            )

    @staticmethod
    def show_product(product):
        return PRODUCT_DATABASE.get(product.code, 'Does not exist')

    @staticmethod
    def have_sale(sale):
        SALES_DATABASE[sale.code] = dict(
            date = sale.date,
            acquired_products = sale.acquired_products,
        )

    @staticmethod
    def show_sale(sale):
        return SALES_DATABASE.get(sale.code, 'Does not exist')

class Manager(Employee):
    def __init__(self, code: str, name: str, phone: str, address: str, email: str):
        super().__init__(code, name, phone, address, email)

    @staticmethod
    def insert_employee(employee):
        EMPLOYEE_DATABASE[employee.code] = dict(
            name = employee.name,
            phone = employee.phone,
            address = employee.address,
            email = employee.email,
        )

    def delete_employee(code):
        if code in EMPLOYEE_DATABASE:
            del EMPLOYEE_DATABASE[code]
    
    @staticmethod
    def modify_employee(code, new_name, new_phone, new_address, new_email):
        if code in EMPLOYEE_DATABASE:
            EMPLOYEE_DATABASE[code] = dict(
                name = new_name,
                phone = new_phone,
                address = new_address,
                email = new_email,
            )

    @staticmethod
    def show_employee(employee):
        return EMPLOYEE_DATABASE.get(employee.code, 'Does not exist')
