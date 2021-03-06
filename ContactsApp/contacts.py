class AddressHolder:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    '''Contact class definition'''
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        '''Put an order for the available supplier'''
        print("If this were a real system we would send "
        "'{}' order to '{}'".format(order, self.name))

class Friend(Contact,AddressHolder):
    def __init__(self, name, email, phone, street, city, state, zipcode):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self,  street, city, state, zipcode)
        self.phone = phone
