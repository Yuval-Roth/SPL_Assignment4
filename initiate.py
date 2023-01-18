from persistence import *

import sys
import os

def add_branch(splittedline : list[str]):
    id = int(splittedline[0])
    location = splittedline[1]
    number_of_employees = int(splittedline[2])
    branch = Branche(id, location, number_of_employees)
    repo.add_branch(branch)

def add_supplier(splittedline : list[str]):
    id = int(splittedline[0])
    name = splittedline[1]
    contact_info = splittedline[2]
    supplier = Supplier(id, name, contact_info)
    repo.add_supplier(supplier)

def add_product(splittedline : list[str]):
    id = int(splittedline[0])
    description = splittedline[1]
    price = float(splittedline[2])
    quantity = int(splittedline[3])
    product = Product(id, description, price, quantity)
    repo.add_product(product)

def add_employee(splittedline : list[str]):
    id = int(splittedline[0])
    name = splittedline[1]
    salary = float(splittedline[2])
    branch = int(splittedline[3])
    employee = Employee(id, name, salary, branch)
    repo.add_employee(employee)

adders = {  "B": add_branch,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)