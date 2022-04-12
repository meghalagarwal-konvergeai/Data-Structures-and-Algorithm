class user:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return "Username='{}', Name='{}', Email='{}'".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

class UserDatabase:
    def __init__(self):
        self.users = []
     
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if(self.users[i].username > user.username):
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if(user.username == username):
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
    
    def list_all(self):
        return self.users

if __name__ =="__main__":
    db = UserDatabase()

    db.insert("Meghal")
    db.insert("Shubham")
    db.insert("Purva")

    us = db.find("Purva")
    print(us)