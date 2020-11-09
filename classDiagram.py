from datetime import datetime


def logInWithGmail(email):
    token = ""
    if '@gmail' in email:
        return (True, token)
    return (False, None)


def signUpWithGmail(email):
    id, token = ""
    return (True, id, token)


class User:
    def __init__(self, idUser, gmail, nama, umur, gender, alamat, noTelp, role):
        self.idUser = idUser
        self.gmail = gmail
        self.nama = nama
        self.umur = umur
        self.gender = gender
        self.alamat = alamat
        self.noTelp = noTelp
        self.role = role
        self.isLogin = False
        self.token = ""

    def login(self, gmail):
        login, token = logInWithGmail(gmail)
        if(login):
            self.isLogin = True
            self.token = token
            return token
        else:
            return False

    def signup(self, gmail, nama, umur, gender, alamat, noTelp, role):
        login, id, token = signUpWithGmail(gmail)
        if login:
            self.isLogin = True
            self.idUser = id
            self.nama = nama
            self.umur = umur
            self.gender = gender
            self.alamat = alamat
            self.noTelp = noTelp
            self.role = role
            self.token = token
            return token
        else:
            return False

    def logout(self):
        self.isLogin = False
        self.token = None
        return True

    def updateIdentity(self, nama, umur, gender, alamat, noTelp):
        self.nama = nama
        self.umur = umur
        self.gender = gender
        self.alamat = alamat
        self.noTelp = noTelp

    def getIdentity(self):
        return self

    def setRole(self, role):
        self.role = role


class Pasien(User):
    def __init__(self):
        super().__init__()
        self.role = "pasien"


class Dokter(User):
    def __init__(self, noSTR, spesialis, statusVerifikasi):
        super().__init__()
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
        self.idPasien = idPasien
        self.idDokter = idDokter
        self.waktuPeriksa = waktuPeriksa
        self.diterima = bool
        self.idRekamMedis = ""
        self.idReminderObat = []
        self.namaPenyakit = ""

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
