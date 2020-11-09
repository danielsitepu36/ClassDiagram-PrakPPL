from datetime import datetime
import random
import string


def randomizer():
    val = (''.join([random.choice(string.hexdigits) for i in range(16)]))
    return val


def logInWithGmail(gmail):
    gmail = gmail
    token = randomizer()
    return (True, token)


def signUpWithGmail(gmail):
    gmail = gmail
    token = ''.join(random.choice(string.hexdigits) for i in range(16))
    ID = ''.join(random.choice(string.hexdigits) for i in range(16))
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
            User.list_user[gmail] = {'id': ID, 'nama': nama, 'gmail': gmail, 'umur': umur,
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
        return User.list_user[self._gmail]

    def setRole(self, role):
        self.role = role


class Pasien(User):
    def __init__(self, gmail):
        super().__init__(self)
        self._gmail = gmail
        self.role = "pasien"


class Dokter(User):
    def __init__(self, gmail, noSTR, spesialis, statusVerifikasi):
        super().__init__(gmail)
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
    list_periksa = {}

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
    list_riwayat = {}

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


def login(role):
    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
Silahkan Login/Signup terlebih dahulu
1. SignUp
2. LogIn
0. Kembali""")
    choice = input("Masukkan pilihan: ")
    while choice != '0':
        if choice == '1':
            # signup("pasien")
            gmail = input("Masukkan email: ")
            nama = input("Masukkan nama: ")
            umur = input("Masukkan umur: ")
            alamat = input("Masukkan alamat: ")
            gender = input("Masukkan gender: ")
            noTelp = input("Masukkan noTelp: ")
            if role == 'pasien':
                pasien = Pasien(gmail)
                pasien.signup(gmail, nama, umur, gender, alamat, noTelp, role)
                menuPasien(pasien)
            elif role == 'dokter':
                noSTR = input("Masukkan noSTR: ")
                spesialis = input("Masukkan nomor spesialis: ")
                statusVerifikasi = input("Masukkan nomor statusVerifikasi: ")
                dokter = Dokter(gmail, noSTR, spesialis, statusVerifikasi)
                dokter.signup(gmail, nama, umur, gender, alamat, noTelp, role)
                menuDokter(dokter)
        elif choice == '2':
            # login("dokter")
            gmail = input("Masukkan email: ")
            if role == 'pasien':
                pasien = Pasien.list_user[gmail]
                pasien.login(gmail)
                menuPasien(gmail)
            elif role == 'dokter':
                dokter = Dokter.list_user[gmail]
                dokter.login(gmail)
                menuDokter(gmail)
    return


def menuPasien(gmail):
    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
Menu Pasien:
1. Periksa
2. Riwayat
3. Reminder Obat
4. Edit Profil
0. LogOut""")
    choice = input("Masukkan pilihan: ")
    while choice != '0':
        if choice == '1':
            periksaPasien(gmail)
            pass
        elif choice == '2':
            riwayat(gmail)
        elif choice == '3':
            reminder(gmail)
        elif choice == '4':
            profil(gmail)
    main()


def periksaPasien(gmail):
    print("Anda memilih periksa.\nAjukan daftar periksa")
    print("Daftar dokter: ")
    idPeriksa = randomizer()
    idPasien = gmail
    dokter = input("Masukkan nomor dokter: ")
    waktu = input(
        "Pilih tanggal & waktu untuk konsultasi (mis. 10 Nov 2020, 10:00): ")
    periksa = Periksa(idPeriksa, idPasien, dokter, waktu)

    print("Daftar periksa berhasil!")
    print(f"Nama Pasien: {User.list_user[gmail]['nama']}")
    print(f"Dokter:")


def riwayat(gmail):
    print("Anda memilih riwayat.")


def reminder(gmail):
    print("Anda memilih periksa.")


def profil(gmail):
    print("Anda memilih profil.\nEdit data diri anda")
    pasien = Pasien.list_user[gmail]
    print(pasien.getIdentity)
    nama = input("Masukkan nama: ")
    umur = input("Masukkan umur: ")
    alamat = input("Masukkan alamat: ")
    gender = input("Masukkan gender: ")
    noTelp = input("Masukkan noTelp: ")
    pasien.updateIdentity(nama, umur, gender, alamat, noTelp)
    print("Profil terupdate")


def menuDokter(user):
    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
Menu Dokter:
1. Periksa
2. Riwayat
3. Edit Profil
0. LogOut""")
    choice = input("Masukkan pilihan: ")
    while choice != '0':
        if choice == '1':
            login("pasien")
        elif choice == '2':
            login("dokter")
        elif choice == '3':
            login("dokter")
        elif choice == '0':
            main()
    main()


def periksa():
    nama = input("Masukkan nama dokter: ")
    umur = input("Masukkan waktu: ")


def main():
    # dokter = Dokter(gmail, noSTR, spesialis, statusVerifikasi)
    # dokter.signup(gmail, nama, umur, gender, alamat, noTelp, role)
    newDoc = Dokter("doc1", '345.123', 'umum', True)
    # newDoc.signup("doc1", )

    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
1. Pasien
2. Dokter
3. Admin
0. Keluar""")
    choice = input("Masukkan pilihan: ")
    while choice != '0':
        if choice == '1':
            login("pasien")
        elif choice == '2':
            login("dokter")
        elif choice == '3':
            login("admin")
    exit()


if __name__ == "__main__":
    main()
