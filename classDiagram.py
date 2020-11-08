

class User:
    def __init__(self, gmail, name, age, gender, address, role):
        self.gmail = gmail
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.role = role
        self.isLogin = False

    def login(self, gmail):
        if(logInWithGmail(gmail)):
            self.isLogin = True
            return True
        else:
            return False
    
    def logout(self):
        self.isLogin = False
        return True