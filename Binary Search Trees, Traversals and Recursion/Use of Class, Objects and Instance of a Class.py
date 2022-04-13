# Defining a class to store the values
class User:
    # Creating a Constructor Function
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    #__repr__ consider the strings as variables
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    #__str__ consider the strings as strings
    def __str__(self):
        return self.__repr__()

# Defining a User Database to Insert, Find, Update and Print the Entire List of the Database
class UserDatabase:
    def __init__(self):
        self.users = []
    
    #Inserts the value in ascending order
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if(self.users[i].username > user.username):
                break
            i += 1
        self.users.insert(i, user)

    #Returns the value if it exists
    def find(self, username):
        for user in self.users:
            if(user.username == username):
                return user

    # Updates the value if it Exists
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
    
    #Prints the entire list of the User Database
    def list_all(self):
        return self.users

# Program Starts here
if __name__ =="__main__":
    db = UserDatabase()

    # Storing the Data
    aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
    biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
    hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
    vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

    users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

    for info in users:
        db.insert(info)

    us = db.find('siddhant')
    print(us)