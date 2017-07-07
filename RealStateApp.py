class Property:
    def __init__(self, square_feet='', num_bedrooms='', num_bathrooms='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
    
    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}". format(self.num_bedrooms))
        print("bathrooms: {}". format(self.num_bathrooms))
        print()
    
    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "),
                    beds = input("Enter number of bedrooms: "),
                    baths = input("Enter number of bathrooms: "))
    prompt_init = staticmethod(prompt_init)

class Apartment(Property):
    valid_laundries = ("coin","ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")
    
    def __init__(self, balcony = '', laundry ='', **kwargs):
        super().__init__(**kwargs)
        self.laundry = laundry
        self.balcony = balcony
    
    def display(self):
        super().display()
        print("DEPARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have?", Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have balcony?", Apartment.valid_balconies)            
        parent_init.update({"laundry":laundry, "balcony":balcony})
        return parent_init
    
    prompt_init = staticmethod(prompt_init)

def get_valid_input(input_string, valid_options):
    input_string += "({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    
    return response