from persistence import *
from dbtools import *

def main():
    
    print('Activities')
    activities = repo.find_all_activities()
    for activity in activities:
        print(f'({activity.product_id}, {activity.quantity}, {activity.activator_id}, \'{activity.date.decode()}\')')
    
    print('Branches')
    branches = repo.find_all_branches()
    for branch in branches:
        print(f'({branch.id}, \'{branch.location.decode()}\', {branch.number_of_employees})')
    
    print('Employees')
    employees = repo.find_all_employees()
    for employee in employees:
        print(f'({employee.id}, \'{employee.name.decode()}\', {employee.salary}, {employee.branche})')
    
    print('Products')
    products = repo.find_all_products()
    for product in products:
        print(f'({product.id}, \'{product.description.decode()}\', {product.price}, {product.quantity})')
    
    print('Suppliers')
    suppliers = repo.find_all_suppliers()
    for supplier in suppliers:
        print(f'({supplier.id}, \'{supplier.name.decode()}\', \'{supplier.contact_information.decode()}\')')
    
    print();
    
    print('Employees report')
    c = repo._conn.cursor()
    c.execute('''
        SELECT e.name, e.salary, b.location, SUM(ABS(a.quantity) * p.price)
        FROM employees e
        JOIN branches b ON e.branche = b.id
        LEFT JOIN activities a ON a.activator_id = e.id AND a.quantity < 0
        LEFT JOIN products p ON a.product_id = p.id
        GROUP BY e.id
        ORDER BY e.name   
    ''')

    for row in c.fetchall():
        output = ''
        output += row[0].decode()+' '
        output += str(row[1])+' '
        output += row[2].decode()+' '
        output += (str(row[3]) if row[3] != None else '0')
        print(output)

    print();

    print('Activities report')
    c = repo._conn.cursor()
    c.execute('''
        SELECT a.date, p.description, a.quantity, e.name, s.name
        FROM activities a
        JOIN products p ON a.product_id = p.id
        LEFT JOIN employees e ON a.activator_id = e.id
        LEFT JOIN suppliers s ON a.activator_id = s.id
        ORDER BY a.date
    ''')
    for row in c.fetchall():
        output = '('
        output += '\''+row[0].decode()+'\', '
        output += '\''+row[1].decode()+'\', '
        output += str(row[2])+', '
        output += ('\''+row[3].decode()+'\', ' if row[3] != None else 'None, ')
        output += ('\''+row[4].decode()+'\'' if row[4] != None else 'None')
        output += ')'
        print(output)
        
if __name__ == '__main__':
    main()