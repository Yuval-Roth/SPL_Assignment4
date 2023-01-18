import sqlite3
import atexit
from dbtools import Dao

class Employee:
    def __init__(self, id: int, name: str, salary: float, branche: int):
        self.id = id
        self.name = name
        self.salary = salary
        self.branche = branche

class Supplier:
    def __init__(self, id: int, name: str, contact_information: str):
        self.id = id
        self.name = name
        self.contact_information = contact_information

class Product:
    def __init__(self, id: int, description: str, price: float, quantity: int):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

class Branche:
    def __init__(self, id: int, location: str, number_of_employees: int):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees

class Activitie:
    def __init__(self, product_id: int, quantity: int, activator_id: int, date: str):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('bgumart.db')
        self._conn.text_factory = bytes
        self.employee_dao = Dao(Employee, self._conn)
        self.supplier_dao = Dao(Supplier, self._conn)
        self.product_dao = Dao(Product, self._conn)
        self.branche_dao = Dao(Branche, self._conn)
        self.activitie_dao = Dao(Activitie, self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE employees (
                id              INT         PRIMARY KEY,
                name            TEXT        NOT NULL,
                salary          REAL        NOT NULL,
                branche    INT REFERENCES branches(id)
            );
    
            CREATE TABLE suppliers (
                id                   INTEGER    PRIMARY KEY,
                name                 TEXT       NOT NULL,
                contact_information  TEXT
            );

            CREATE TABLE products (
                id          INTEGER PRIMARY KEY,
                description TEXT    NOT NULL,
                price       REAL NOT NULL,
                quantity    INTEGER NOT NULL
            );

            CREATE TABLE branches (
                id                  INTEGER     PRIMARY KEY,
                location            TEXT        NOT NULL,
                number_of_employees INTEGER
            );
   
            CREATE TABLE activities (
                product_id      INTEGER REFERENCES products(id),
                quantity        INTEGER NOT NULL,
                activator_id    INTEGER NOT NULL,
                date            TEXT    NOT NULL
            );
        """)

    def add_employee(self, employee: Employee):
        self.employee_dao.insert(employee)

    def add_supplier(self, supplier: Supplier):
        self.supplier_dao.insert(supplier)

    def add_product(self, product: Product):
        self.product_dao.insert(product)
    
    def add_branch(self, branch: Branche):
        self.branche_dao.insert(branch)

    def add_activitie(self, activitie: Activitie):
        self.activitie_dao.insert(activitie)

    def find_all_employees(self):
        return self.employee_dao.find_all()

    def find_all_suppliers(self):
        return self.supplier_dao.find_all()

    def find_all_products(self):
        return self.product_dao.find_all()

    def find_all_branches(self):
        return self.branche_dao.find_all()

    def find_all_activities(self):
        return self.activitie_dao.find_all()

    def find_employee(self, **keyvals):
        return self.employee_dao.find(**keyvals)

    def find_supplier(self, **keyvals):
        return self.supplier_dao.find(**keyvals)

    def find_product(self, **keyvals):
        return self.product_dao.find(**keyvals)

    def find_branch(self, **keyvals):
        return self.branche_dao.find(**keyvals)

    def find_activitie(self, **keyvals):
        return self.activitie_dao.find(**keyvals)

    def delete_employee(self, **keyvals):
        self.employee_dao.delete(**keyvals)

    def delete_supplier(self, **keyvals):
        self.supplier_dao.delete(**keyvals)

    def delete_product(self, **keyvals):
        self.product_dao.delete(**keyvals)

    def update_product(self, product: Product, **keyvals):
        self.product_dao.update(product, **keyvals)
        
    def update_employee(self, employee: Employee, **keyvals):
        self.employee_dao.update(employee, **keyvals)

    def update_branch(self, branche: Branche, **keyvals):
        self.branche_dao.update(branche, **keyvals)

    def update_supplier(self, supplier: Supplier, **keyvals):
        self.supplier_dao.update(supplier, **keyvals)

    def update_activitie(self, activitie: Activitie, **keyvals):
        self.activitie_dao.update(activitie, **keyvals)

 
# singleton
repo = Repository()
atexit.register(repo._close)