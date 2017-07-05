class Contact:
    '''Contact class definition'''
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        '''Put an order for the available supplier'''
        print("If this were a real system we would send "
        "'{}' order to '{}'".format(order, self.name))