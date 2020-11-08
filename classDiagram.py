from datetime import datetime

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

# Class Periksa, class aktivitas utama dalam alur Go-Doc
class Periksa:
    def __init__(self, idPasien, idDokter, idRekamMedis, idReminderObat, namaPenyakit):
        self._idPasien = idPasien
        self._idDokter = idDokter
        self._idRekamMedis = idRekamMedis
        self._idReminderObat = idReminderObat
        self._diterima = False

    def setPeriksa(idPeriksa, idPasien, idDokter, tanggalPeriksa):
        tanggalPeriksa = dateNow()

    def terima(idPeriksa):
        self.diterima = True
        self.idPeriksa = idPeriksa

class ReminderObat:
     def __init__(self, idReminder, namaObat, jadwalMinumObat, muted):
         self._idReminder = idReminder
         self._namaObat = namaObat
         self._jadwalMinumObat = jadwalMinumObat
         self._muted = muted

     def setReminderObat(idReminder, namaObat, jadwalMinumObat):
         jadwalMinumObat = dateNow()
         muted = False

     def getReminderObat(idReminder):


     def muteReminderObat(idReminder, muted):
         muted = True
