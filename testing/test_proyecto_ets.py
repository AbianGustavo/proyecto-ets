import pytest
from proyecto_ets import (
    CLIENT_DATABASE,
    EMPLOYEE_DATABASE,
    PRODUCT_DATABASE,
    SALES_DATABASE,
    Person,
    Client,
    Product,
    Product_Detail,
    Sale,
    Sale_Detail,
    Employee,
    Manager,
)

# CONSTRUCTORES


@pytest.fixture
def create_person():
    code = "P001"
    name = "Carlos Guerra"
    phone = "1234567800"
    address = "La Laguna"
    email = "correodeprueba@hotmail.com"
    person = Person(code, name, phone, address, email)
    return person


@pytest.fixture
def create_client():
    code = "C001"
    name = "Abian Gustavo"
    phone = "9876543210"
    address = "La Orotava"
    email = "correodeprueba@hotmail.com"
    client = Client(code, name, phone, address, email)
    return client


@pytest.fixture
def create_product():
    code = "PR001"
    product = Product(code)
    return product


@pytest.fixture
def create_product_detail():
    code = "PR001"
    name = "Call of Duty"
    type = "Videogame"
    price = 40.00
    stock = 20
    description = "FPS GAME"
    product_detail = Product_Detail(code, name, type, price, stock, description)
    return product_detail


@pytest.fixture
def create_sale():
    code = "S001"
    sale = Sale(code)
    return sale


@pytest.fixture
def create_sale_detail():
    code = "S001"
    date = "2023-06-07"
    acquired_products = ["PR001"]
    sale_detail = Sale_Detail(code, date, *acquired_products)
    return sale_detail


@pytest.fixture
def create_employee():
    code = "E001"
    name = "Diego Peraza"
    phone = "1234567890"
    address = "Puerto de la Cruz"
    email = "correodeprueba2@hotmail.com"
    employee = Employee(code, name, phone, address, email)
    return employee


@pytest.fixture
def create_manager():
    code = "M001"
    name = "Jose Lopez"
    phone = "9876543240"
    address = "Santa Cruz de Tenerife"
    email = "correodeprueba4@hotmail.com"
    manager = Manager(code, name, phone, address, email)
    return manager


def test_person_init(create_person):
    person = create_person
    assert person.code == "P001"
    assert person.name == "Carlos Guerra"
    assert person.phone == "1234567800"
    assert person.address == "La Laguna"
    assert person.email == "correodeprueba@hotmail.com"


def test_client_init(create_client):
    client = create_client
    assert client.code == "C001"
    assert client.name == "Abian Gustavo"
    assert client.phone == "9876543210"
    assert client.address == "La Orotava"
    assert client.email == "correodeprueba@hotmail.com"


def test_product_init(create_product):
    product = create_product
    assert product.code == "PR001"


def test_product_detail_init(create_product_detail):
    product_detail = create_product_detail
    assert product_detail.code == "PR001"
    assert product_detail.name == "Call of Duty"
    assert product_detail.type == "Videogame"
    assert product_detail.price == 40.00
    assert product_detail.stock == 20
    assert product_detail.description == "FPS GAME"


def test_sale_init(create_sale):
    sale = create_sale
    assert sale.code == "S001"


def test_sale_detail_init(create_sale_detail):
    sale_detail = create_sale_detail
    assert sale_detail.code == "S001"
    assert sale_detail.date == "2023-06-07"
    assert sale_detail.acquired_products == ("PR001",)


def test_employee_init(create_employee):
    employee = create_employee
    assert employee.code == "E001"
    assert employee.name == "Diego Peraza"
    assert employee.phone == "1234567890"
    assert employee.address == "Puerto de la Cruz"
    assert employee.email == "correodeprueba2@hotmail.com"


def test_manager_init(create_manager):
    manager = create_manager
    assert manager.code == "M001"
    assert manager.name == "Jose Lopez"
    assert manager.phone == "9876543240"
    assert manager.address == "Santa Cruz de Tenerife"
    assert manager.email == "correodeprueba4@hotmail.com"


# MÉTODOS EMPLOYEE - CLIENT


def test_insert_client(create_client):
    client1 = create_client

    Employee.insert_client(client1)

    assert CLIENT_DATABASE.get(client1.code) == {
        "name": "Abian Gustavo",
        "phone": "9876543210",
        "address": "La Orotava",
        "email": "correodeprueba@hotmail.com",
    }


def test_delete_client(create_client):
    client1 = create_client

    Employee.delete_client(client1.code)

    assert CLIENT_DATABASE.get(client1.code) is None


def test_modify_client(create_client):
    client1 = create_client

    Employee.insert_client(client1)

    Employee.modify_client(
        client1.code,
        "Diego Peraza",
        "987654321",
        "Puerto de la Cruz",
        "correodeprueba2@hotmail.com",
    )

    assert CLIENT_DATABASE.get(client1.code) == {
        "name": "Diego Peraza",
        "phone": "987654321",
        "address": "Puerto de la Cruz",
        "email": "correodeprueba2@hotmail.com",
    }


def test_show_client(create_client):
    client1 = create_client

    Employee.insert_client(client1)
    result = Employee.show_client(client1)

    assert result == {
        "name": "Abian Gustavo",
        "phone": "9876543210",
        "address": "La Orotava",
        "email": "correodeprueba@hotmail.com",
    }


# MÉTODOS EMPLOYEE - PRODUCT


def test_insert_product(create_product_detail):
    product1 = create_product_detail

    Employee.insert_product(product1)

    assert PRODUCT_DATABASE.get(product1.code) == {
        "name": "Call of Duty",
        "type": "Videogame",
        "price": 40.00,
        "stock": 20,
        "description": "FPS GAME",
    }


def test_delete_product(create_product_detail):
    product1 = create_product_detail

    Employee.delete_product(product1.code)

    assert PRODUCT_DATABASE.get(product1.code) is None


def test_modify_product(create_product_detail):
    product1 = create_product_detail

    Employee.insert_product(product1)

    Employee.modify_product(
        product1.code, "Minecraft", "Videogame", 20.00, 10, "Videojuego Minecraft"
    )

    assert PRODUCT_DATABASE.get(product1.code) == {
        "name": "Minecraft",
        "type": "Videogame",
        "price": 20.00,
        "stock": 10,
        "description": "Videojuego Minecraft",
    }


def test_show_product(create_product_detail):
    product1 = create_product_detail

    Employee.insert_product(product1)
    result = Employee.show_product(product1)

    assert result == {
        "name": "Call of Duty",
        "type": "Videogame",
        "price": 40.00,
        "stock": 20,
        "description": "FPS GAME",
    }


# MÉTODOS EMPLOYEE - SALE


def test_have_sale(create_sale_detail):
    sale1 = create_sale_detail

    Employee.have_sale(sale1)

    assert SALES_DATABASE.get(sale1.code) == {
        "date": "2023-06-07",
        "acquired_products": ("PR001",),
    }


def test_show_sale(create_sale_detail):
    sale1 = create_sale_detail
    Employee.have_sale(sale1)
    result = Employee.show_sale(sale1)
    assert result == {"date": "2023-06-07", "acquired_products": ("PR001",)}


# MÉTODOS MANAGER - EMPLOYEE


def test_insert_employee(create_employee):
    employee1 = create_employee

    Manager.insert_employee(employee1)

    assert EMPLOYEE_DATABASE.get(employee1.code) == {
        "name": "Diego Peraza",
        "phone": "1234567890",
        "address": "Puerto de la Cruz",
        "email": "correodeprueba2@hotmail.com",
    }


def test_delete_employee(create_employee):
    employee1 = create_employee

    Manager.delete_employee(employee1.code)

    assert EMPLOYEE_DATABASE.get(employee1.code) is None


def test_modify_employee(create_employee):
    employee1 = create_employee

    Manager.insert_employee(employee1)

    Manager.modify_employee(
        employee1.code,
        "Juan Perez",
        "987654320",
        "Los Realejos",
        "correodeprueba3@hotmail.com",
    )

    assert EMPLOYEE_DATABASE.get(employee1.code) == {
        "name": "Juan Perez",
        "phone": "987654320",
        "address": "Los Realejos",
        "email": "correodeprueba3@hotmail.com",
    }


def test_show_employee(create_employee):
    employee1 = create_employee

    Manager.insert_employee(employee1)
    result = Manager.show_employee(employee1)

    assert result == {
        "name": "Diego Peraza",
        "phone": "1234567890",
        "address": "Puerto de la Cruz",
        "email": "correodeprueba2@hotmail.com",
    }
