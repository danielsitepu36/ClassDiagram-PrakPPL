nama_dokter = ["Sitepu", "Khrisna", "Wardana"]

def logInWithGmail(email):
    if '@gmail' in email:
        return (True, token)
    return (False, None)

def signUpWithGmail(email):
    return (True, token)

class User:
    def __init__(self, gmail, name, age, gender, address, phone):
        self.gmail = gmail
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone
        if name in nama_dokter:
            self.role = "dokter"
        elif name in list_admin:
            self.role = "admin"
        else:
            self.role = "user"
        self.isLogin = False
        self.id = None

    def login(self, gmail):
        login, ID = logInWithGmail(gmail)
        if(login):
            self.isLogin = True
            self.id = ID
            return True
        else:
            return False

    def signup(self, gmail):
        login, ID = signUpWithGmail(gmail)
        if login:
            self.isLogin = True
            self.id = ID

    def logout(self):
        self.isLogin = False
        self.id = None
        return True

    def updateIdentity(self, name, age, gender, address, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone

class Pasien(User):
    def __init__(self):
        super().__init__()
        self.role = "pasien"


