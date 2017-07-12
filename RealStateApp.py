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

class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    def __init__(self, num_stories = '', garage = '', fenced = '', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: ".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced_yard":fenced, "garage": garage, "num_stories":num_stories})
        return parent_init
    prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self, price = '', taxes = '', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
    
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
    
    def prompt_init():
        return dict(
            price = input("What is the sealling price? "),
            taxes = input("What are the estimated taxes? "))
    
    prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self, furnished = '', utilities='', rent = '', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent
    
    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
    
    def prompt_init():
        return dict(
            rent = input("What is the montly rent? "),
            utilities = input("What are the estimated utilities? "), 
            furnished = get_valid_input("Is the property furnished? ", ("yes", "no")))
    
    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class Agent:
    def __init__(self):
        self.property_list = []
    
    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase
    }

    def add_property(self):
        property_type = get_valid_input("what type of property? ", ("house", "apartment",)).lower()
        payment_type = get_valid_input("Whta payment type? ", ("purchase", "rental")).lower

        PropertyClass = self.type_map[(property_type, payment_map)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args)]