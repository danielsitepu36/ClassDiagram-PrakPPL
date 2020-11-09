from datetime import datetime
import random
import string


def logInWithGmail(email):
    token = ''.join(random.choice(string.hexdigits) for i in range(16))
    if '@gmail' in email:
        return (True, token)
    return (False, None)


def signUpWithGmail(email):
    token = ''.join(random.choice(string.hexdigits) for i in range(16))
    ID  = token
    return (True, ID, token)


class User:
    list_user = {}
    def __init__(self, gmail):
        self.idUser = ''
        self._gmail = gmail
        self._nama = ''
        self._umur = ''
        self._gender = ''
        self._alamat = ''
        self._noTelp = ''
        self._role = 'user'
        self._token = ''
        self.isLogin = False

    def login(self, gmail):
        login, token = logInWithGmail(gmail)
        if(login):
            self.isLogin = True
            self.token = token
            return token
        else:
            return False

    def signup(self, gmail, nama, umur, gender, alamat, noTelp, role):
        login, ID, token = signUpWithGmail(gmail)
        if login:
            self.isLogin = True
            self.idUser = ID
            self._nama = nama
            self._umur = umur
            self._gender = gender
            self._alamat = alamat
            self._noTelp = noTelp
            self._role = role
            self._token = token
            User.list_user[ID] = {'nama': nama, 'gmai': gmail, 'umur': umur,
                             'gender': gender, 'alamat': alamat,
                             'noTelp': noTelp, 'role': 'user'}
            return token
        else:
            return False

    def logout(self):
        self.isLogin = False
        self.token = None
        return True

    def updateIdentity(self, nama, umur, gender, alamat, noTelp):
        self._nama = nama
        self._umur = umur
        self._gender = gender
        self._alamat = alamat
        self._noTelp = noTelp

    def getIdentity(self):
        return User.list_user[self.token]

    def setRole(self, role):
        self.role = role


class Pasien(User):
    def __init__(self,gmail):
        super().__init__(self)
        self._gmail = gmail
        self.role = "pasien"


class Dokter(User):
    def __init__(self, gmail, noSTR, spesialis, statusVerifikasi):
        super().__init__()
        self._gmail = gmail
        self.role = "dokter"
        self.noSTR = noSTR
        self.spesialis = spesialis
        self.statusVerifikasi = statusVerifikasi

    def setSpesialis(self, spesialis):
        self.spesialis = spesialis

    def getSpesialis(self):
        return self.spesialis

    def verifikasi(self, statusVerifikasi):
        self.statusVerifikasi = statusVerifikasi
        return statusVerifikasi


class Admin:
    def __init__(self, idAdmin, gmail, nama):
        self.idAdmin = idAdmin
        self.gmail = gmail
        self.nama = nama
        self.isLogin = False
        self.token = ""

# Class Periksa, class aktivitas utama dalam alur Go-Doc
class Periksa:
    def __init__(self, idPeriksa, idPasien, idDokter, waktuPeriksa):
        self.idPeriksa = idPeriksa
        self._idPasien = idPasien
        self._idDokter = idDokter
        self._waktuPeriksa = waktuPeriksa
        self._diterima = False
        self._idRekamMedis = ""
        self._idReminderObat = []
        self._namaPenyakit = ""

    def setPeriksa(self, idPeriksa, idPasien, idDokter, waktuPeriksa):
        self.idPeriksa = idPeriksa
        self.idPasien = idPasien
        self.idDokter = idDokter
        self.waktuPeriksa = waktuPeriksa

    def terima(self, status):
        self.diterima = status
        return self.diterima

    def telahDiperiksa(self, idRekamMedis, idReminderObat, namaPenyakit):
        self.idRekamMedis = idRekamMedis
        self.idReminderObat = idReminderObat
        self.namaPenyakit = namaPenyakit
        return True

    def getPeriksa(self):
        return self


class Riwayat:
    def __init__(self, idPasien, idPeriksa):
        self.idPasien = idPasien
        self.idPeriksa = idPeriksa

    def setRiwayat(self, idPasien, idPeriksa):
        self.idPasien = idPasien
        self.idPeriksa = idPeriksa

    def updatePeriksa(self, idPeriksa):
        self.idPeriksa = idPeriksa

    def getRiwayat(self):
        return self


class RekamMedis:
    def __init__(self, idPeriksa, dataPenyakit, keterangan):
        self.idPeriksa = idPeriksa
        self.dataPenyakit = dataPenyakit
        self.keterangan = keterangan


class ReminderObat:
    def __init__(self, idReminder, namaObat, jadwalMinumObat, muted):
        self.idReminder = idReminder
        self.namaObat = namaObat
        self.jadwalMinumObat = jadwalMinumObat
        self.muted = muted

    def setReminderObat(self, idReminder, namaObat, jadwalMinumObat):
        self.idReminder = idReminder
        self.namaObat = namaObat
        self.jadwalMinumObat = jadwalMinumObat
        self.muted = False

    def getReminderObat(self):
        return self

    def muteReminderObat(self, muted):
        self.muted = muted
        return muted

def App():
    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
1. Login
2. Sign Up
3. Keluar
    """)
    choice = input()
    while choice != '3':
        if choice == '1':
            gmail = input("Masukkan email: ")
            user = User(gmail)
            user.login(gmail)
