class Contact:
    '''Contact class definition'''
    all_contacts = []
    def __init__(self, name = '', email = '', *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street = '', city = '', state = '', code = '', *args, **kwargs):
        super(AddressHolder, self).__init__(*args, **kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self,phone = '', *args, **kwargs):
        super(Friend, self).__init__(phone, *args, **kwargs)
        self.phone = phone