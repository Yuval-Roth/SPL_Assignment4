from persistence import *
import sys

def main(args : list[str]):
    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline = line.strip().split(", ")
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]
            
            product = repo.find_product(id=product_id)[0]
            if product is None:
                continue
            elif quantity < 0:
                if product.quantity < abs(quantity):
                    continue
                else:
                    product.quantity -= abs(quantity)
            elif quantity > 0:
                product.quantity += quantity
            else:
                continue
            repo.update_product(product, id=product_id)
            activitie = Activitie(product_id, quantity, activator_id, date)
            repo.add_activitie(activitie)
                
if __name__ == '__main__':
    main(sys.argv)
