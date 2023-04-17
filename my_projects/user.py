class User:
    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def describe_user(self):
        name = self.first_name.title() + " " + self.last_name.title()
        print('\n' + name + " " + self.age + " years old!")
        print("lives In: " + self.address.title() + ".")

    def greet_user(self):
        name = self.first_name.title() + " " + self.last_name.title()
        print("So very nice to meet you, " + name + "!")


kevin = User('Kevin', 'Kraft', '45', "Renton Washington")
kevin.describe_user()
kevin.greet_user()

marjan = User('Marjan', 'Didra', '40', "Renton Washington")
marjan.describe_user()
marjan.greet_user()

