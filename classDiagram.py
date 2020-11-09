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


class Admin:

    list_admin = {}

    def __init__(self, gmail):
        self.gmail = gmail
        self.nama = "admin"
        self.isLogin = False
        self.token = ""
        self.list_admin[gmail] = self

    def login(self, gmail):
        login, token = logInWithGmail(gmail)
        if(login):
            self.isLogin = True
            self.token = token
            return token
        else:
            return False

    def logout(self):
        self.isLogin = False
        self.token = None
        return True


class User:
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
            return token
        else:
            return False

    def logout(self):
        self.isLogin = False
        self.token = None
        return True

    def setIdentity(self, nama, umur, gender, alamat, noTelp):
        self._nama = nama
        self._umur = umur
        self._gender = gender
        self._alamat = alamat
        self._noTelp = noTelp

    def getIdentity(self):
        data = {'id': self.idUser, 'nama': self._nama, 'gmail': self._gmail, 'umur': self._umur,
                'gender': self._gender, 'alamat': self._alamat,
                'noTelp': self._noTelp, 'role': self.role}
        return data

    def setRole(self, role):
        self.role = role


class Pasien(User):

    list_pasien = {}

    def __init__(self, gmail):
        super().__init__(self)
        self._gmail = gmail
        self.role = "pasien"
        Pasien.list_pasien[gmail] = self
        Riwayat(gmail)


class Dokter(User):

    list_dokter = {}

    def __init__(self, gmail, noSTR, spesialis):
        super().__init__(gmail)
        self._gmail = gmail
        self.role = "dokter"
        self.noSTR = noSTR
        self.spesialis = spesialis
        self.statusVerifikasi = False
        Dokter.list_dokter[gmail] = self

    def setDokterIdentity(self, noSTR, spesialis):
        self.noSTR = noSTR
        self.spesialis = spesialis

    def getDokterIdentity(self):
        data = {"statusVerifikasi": self.statusVerifikasi,
                'noSTR': self.noSTR, 'spesialis': self.spesialis}
        return data

    def verifikasi(self, statusVerifikasi):
        self.statusVerifikasi = statusVerifikasi

# Class Periksa, class aktivitas utama dalam alur Go-Doc


class Periksa:
    list_periksa = {}

    def __init__(self, idPeriksa, idPasien, idDokter, waktuPeriksa):
        self.idPeriksa = idPeriksa
        self.idPasien = idPasien
        self.idDokter = idDokter
        self._waktuPeriksa = waktuPeriksa
        self._diterima = False
        self._idRekamMedis = ""
        self._idReminderObat = []
        self._namaPenyakit = ""
        Periksa.list_periksa[idPeriksa] = self

    def terima(self, status):
        self._diterima = status
        return self._diterima

    def telahDiperiksa(self, idRekamMedis, idReminderObat, namaPenyakit):
        self._idRekamMedis = idRekamMedis
        self._idReminderObat = idReminderObat
        self._namaPenyakit = namaPenyakit
        return True

    def getPeriksa(self):
        data = {'id': self.idPeriksa, 'idPasien': self.idPasien, 'idDokter': self.idDokter, 'waktuPeriksa': self._waktuPeriksa,
                'diterima': self._diterima, 'idRekamMedis': self._idRekamMedis,
                'idReminderObat': self._idReminderObat, 'namaPenyakit': self._namaPenyakit}
        return data


class Riwayat:
    list_riwayat = {}

    def __init__(self, idPasien):
        self.idPasien = idPasien
        self.idPeriksa = []
        Riwayat.list_riwayat[idPasien] = self

    def updatePeriksa(self, idPeriksa):
        self.idPeriksa.append(idPeriksa)

    def getRiwayat(self):
        data = {'idPasien': self.idPasien, 'idPeriksa': self.idPeriksa}
        return data


class RekamMedis:
    list_rekamMedis = {}

    def __init__(self, idPeriksa, dataPenyakit, keterangan):
        self.idPeriksa = idPeriksa
        self.dataPenyakit = dataPenyakit
        self.keterangan = keterangan
        RekamMedis.list_rekamMedis[idPeriksa] = self

    def getRekamMedis(self):
        data = {'idPeriksa': self.idPeriksa,
                'dataPenyakit': self.dataPenyakit, 'keterangan': self.keterangan}
        return data


class ReminderObat:
    list_reminder = {}

    def __init__(self, idReminder, idPasien, namaObat, jadwalMinumObat):
        self.idReminder = idReminder
        self.idPasien = idPasien
        self.namaObat = namaObat
        self.jadwalMinumObat = jadwalMinumObat
        self.muted = False
        ReminderObat.list_reminder[idReminder] = self

    def getReminderObat(self):
        data = {'idReminder': self.idReminder, 'idPasien': self.idPasien,
                'namaObat': self.namaObat, 'jadwalMinumObat': self.jadwalMinumObat, 'muted': self.muted}
        return data

    def muteReminderObat(self, muted):
        self.muted = muted
        return muted


def loginAdmin():
    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
Admin silahkan Login terlebih dahulu
1. LogIn
0. Kembali""")
    choice = input("Masukkan pilihan: ")
    while choice != '0':
        if choice == '1':
            gmail = input("Masukkan email: ")
            Admin.list_admin[gmail].login(gmail)

            while True:
                for i in Dokter.list_dokter.keys():
                    data1 = Dokter.list_dokter[i].getIdentity()
                    data2 = Dokter.list_dokter[i].getDokterIdentity()
                    if data2['statusVerifikasi'] == False:
                        print(data1, data2)

                idDokter = input(
                    "Masukkan gmail dokter yang mau diverifikasi (0 untuk keluar): ")
                if idDokter == '0':
                    break
                Dokter.list_dokter[idDokter].verifikasi(True)
            break
    main()


def login(role):
    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
Silahkan Login/Sign Up terlebih dahulu
1. Sign Up
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
                menuPasien(gmail)
            elif role == 'dokter':
                noSTR = input("Masukkan noSTR: ")
                spesialis = input("Masukkan nomor spesialis: ")
                dokter = Dokter(gmail, noSTR, spesialis)
                dokter.signup(gmail, nama, umur, gender, alamat, noTelp, role)
                menuDokter(gmail)
        elif choice == '2':
            # login("dokter")
            gmail = input("Masukkan email: ")
            if role == 'pasien':
                pasien = Pasien.list_pasien[gmail]
                pasien.login(gmail)
                menuPasien(gmail)
            elif role == 'dokter':
                dokter = Dokter.list_dokter[gmail]

                dokter.login(gmail)
                menuDokter(gmail)
    main()


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
            menuPasien(gmail)
        elif choice == '2':
            riwayatPasien(gmail)
            menuPasien(gmail)
        elif choice == '3':
            reminderPasien(gmail)
            menuPasien(gmail)
        elif choice == '4':
            profilPasien(gmail)
            menuPasien(gmail)
    main()


def periksaPasien(gmail):
    print("Anda memilih periksa.\nAjukan daftar periksa")
    print("Daftar dokter: ")
    j = 1
    for i in Dokter.list_dokter.values():
        if i.getDokterIdentity()['statusVerifikasi'] == True:
            print(j, ")", i.getIdentity(), end=" ")
            print(i.getDokterIdentity())
            j += 1
    idPeriksa = randomizer()
    idPasien = gmail
    idDokter = input("Masukkan gmail dokter: ")
    waktu = input(
        "Pilih tanggal & waktu untuk konsultasi (misal. 10 Nov 2020, 10:00): ")
    periksa = Periksa(idPeriksa, idPasien, idDokter, waktu)
    Riwayat.list_riwayat[idPasien].updatePeriksa(idPeriksa)
    reminder = ReminderObat(randomizer(), [], [], True)
    ReminderObat.list_reminder[idPasien] = reminder
    print("Daftar periksa berhasil!")
    print(periksa.getPeriksa())
    return


def riwayatPasien(gmail):
    print("\nAnda memilih riwayat.\nBerikut riwayat periksa anda:")
    print(Riwayat.list_riwayat[gmail].getRiwayat())
    while True:
        idPeriksa = input(
            "\nMasukkan id periksa untuk detail (0 untuk kembali)\n")
        if(idPeriksa == '0'):
            break
        print(Periksa.list_periksa[idPeriksa].getPeriksa())
    return


def reminderPasien(gmail):
    print("Anda memilih reminder obat.")
    found = False
    for i in ReminderObat.list_reminder.keys():
        data = ReminderObat.list_reminder[i].getReminderObat()
        if data['idPasien'] == gmail:
            found = True
            print(data)
    if not found:
        print("Tidak ada data reminder ditemukan")
    else:
        while True:
            idReminder = input("Masukkan idReminder yang ingin di mute (0 untuk keluar): ")
            if idReminder == '0':
                break
            ReminderObat.list_reminder[idReminder].muteReminderObat(True)
    return


def profilPasien(gmail):
    print("Anda memilih profil.\nEdit data diri anda")
    pasien = Pasien.list_pasien[gmail]
    print(pasien.getIdentity())
    choice = input("Anda ingin mengubah data (y/n) = ")
    if choice == "y" or choice == "Y":
        nama = input("Masukkan nama: ")
        umur = input("Masukkan umur: ")
        alamat = input("Masukkan alamat: ")
        gender = input("Masukkan gender: ")
        noTelp = input("Masukkan noTelp: ")
        pasien.setIdentity(nama, umur, gender, alamat, noTelp)
        print("Profil terupdate")
    else:
        print("Profil tidak diupdate")
    return


def menuDokter(gmail):
    status = Dokter.list_dokter[gmail].getDokterIdentity()["statusVerifikasi"]
    if not status:
        print("!!! Go-Doc Alert !!!")
        print("Status Anda sebagai dokter belum terverifikasi oleh admin. Silakan tunggu atau hubungi admin")
        main()
    print("""
~~~=====Selamat Datang di Go-Doc=====~~~
Menu Dokter:
1. Daftar Periksa
2. Riwayat Pasien
3. Edit Profil
0. LogOut""")
    choice = input("Masukkan pilihan: ")
    while choice != '0':
        if choice == '1':
            periksaDokter(gmail)
            menuDokter(gmail)
        elif choice == '2':
            riwayatDokter(gmail)
            menuDokter(gmail)
        elif choice == '3':
            profilDokter(gmail)
            menuDokter(gmail)
    main()


def riwayatDokter(gmail):
    print("Anda memilih riwayat.")
    idPasien = input("Masukkan ID Pasien: ")
    print(Riwayat.list_riwayat[idPasien].getRiwayat())
    return


def periksaDokter(gmail):
    print("Anda memilih daftar periksa.\nDaftar periksa pasien anda:")
    found = False
    for i in Periksa.list_periksa.keys():
        data = Periksa.list_periksa[i].getPeriksa()
        if data['idDokter'] == gmail:
            found = True
            print(data)
    if not found:
        print("Tidak ada data ditemukan")
        menuDokter(gmail)
    while True:
        idPeriksa = input("Masukkan pilihan idPeriksa (0 untuk keluar): ")
        if (idPeriksa == '0'):
            break
        periksa = Periksa.list_periksa[idPeriksa]

        while True:
            print("Pilih menu:\n1. Lihat isi periksa\n2. Ubah status periksa\
                \n3. Lengkapi data periksa\n4. Lihat Rekam Medis\n0. Kembali")
            choice = input("Masukkan pilihan: ")
            if choice == '0':
                break
            if choice == '1':
                print(periksa.getPeriksa())
            elif choice == '2':
                status = input("Status periksa (1. Diterima/2. Ditolak): ")
                if status == '1':
                    # Periksa.list_periksa[idPeriksa].terima(True)
                    periksa.terima(True)
                else:
                    # Periksa.list_periksa[idPeriksa].terima(False)
                    periksa.terima(False)
                print("Status terinput")
            elif choice == '3':
                print("Masukkan keterangan tambahan untuk rekam medis.")
                namaPenyakit = input("Masukkan nama penyakit: ")
                dataPenyakit = input("Masukkan data penyakit: ")
                keterangan = input("Masukkan keterangan periksa: ")
                RekamMedis(idPeriksa, dataPenyakit, keterangan)

                count = int(input("Jumlah obat: "))
                arrayIdReminder = []
                for i in range(count):
                    idReminder = randomizer()
                    arrayIdReminder.append(idReminder)
                    idPasien = Periksa.list_periksa[idPeriksa].idPasien
                    namaObat = input("Masukkan nama obat: ")
                    jadwalMinumObat = input("Masukkan jadwal minum obat: ")
                    ReminderObat(idReminder, idPasien,
                                 namaObat, jadwalMinumObat)

                Periksa.list_periksa[idPeriksa].telahDiperiksa(
                    idPeriksa, arrayIdReminder, namaPenyakit)
                # telahDiperiksa(self, idRekamMedis, idReminderObat, namaPenyakit)

            elif choice == '4':
                print(RekamMedis.list_rekamMedis[idPeriksa].getRekamMedis())
    menuDokter(gmail)


def profilDokter(gmail):
    print("Anda memilih profil.\nEdit data diri anda")
    dokter = Dokter.list_dokter[gmail]
    print(dokter.getIdentity())
    choice = input("Anda ingin mengubah data (y/n) = ")
    if choice == "y" or choice == "Y":
        nama = input("Masukkan nama: ")
        umur = input("Masukkan umur: ")
        alamat = input("Masukkan alamat: ")
        gender = input("Masukkan gender: ")
        noTelp = input("Masukkan noTelp: ")
        dokter.setIdentity(nama, umur, gender, alamat, noTelp)
        print("Profil terupdate")
    else:
        print("Data tidak diupdate")
    print(dokter.getDokterIdentity())
    choice = input("Anda ingin mengubah data (y/n) = ")
    if choice == "y" or choice == "Y":
        noSTR = input("Masukkan noSTR: ")
        spesialisasi = input("Masukkan spesialisasi: ")
        dokter.setDokterIdentity(noSTR, spesialisasi)
        print("Profil terupdate")
    else:
        print("Data tidak diupdate")
    return


def main():
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
            loginAdmin()
    exit()


if __name__ == "__main__":
    Admin('admin')
    doc1 = Dokter("doc1", '345.123', 'umum')
    doc1.signup("doc1", "dr Rian", "30", "L", "Bali", "123456", "dokter")
    doc1.verifikasi(True)
    doc2 = Dokter("doc2", '236.329', 'jantung')
    doc2.signup("doc2", "dr Wardani", "36", "P", "Jakarta", "514234", "dokter")
    Dokter("doc3", '745.156', 'mata').signup(
        "doc3", "dr Adhit", "26", "L", "Medan", "132532", "dokter")
    Pasien("pas1").signup("pas1", "Daniel", "27",
                          "L", "Yogyakarta", "543245", "pasien")
    Pasien("pas2").signup("pas2", "Dina", "23",
                          "P", "Surabaya", "342865", "pasien")
    Pasien("pas3").signup("pas3", "Alex", "45",
                          "L", "Bandung", "132897", "pasien")
    main()
