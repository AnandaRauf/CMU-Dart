import requests
from bs4 import BeautifulSoup

print("------------------------------------------------------------------\n")

nameprogram = "CSM Dart"
version = "1.0.0"
devdate = "04 May 2024"
devby = "Ananda Rauf Maududi"
print(nameprogram)
print(version)
print(devdate)
print(devby)
print("------------------------------------------------------------------\n")


def MenuCMU():
    print("Menu CMU Dart:\n")
    print()
    print("1. Convert Figma to Dart")
    print("2. Convert Dribbble to Dart")


def FigmaToDart():
    # Masukkan token dan file id Figma Anda di sini
    file_id = 'YOUR_FIGMA_FILE_ID'
    access_token = 'YOUR_FIGMA_ACCESS_TOKEN'

    # Endpoint untuk mengambil informasi tentang desain UI dari Figma
    url = f"https://api.figma.com/v1/files/{file_id}"

    # Mengirimkan request ke API Figma
    response = requests.get(url, headers={'X-Figma-Token': access_token})

    # Mengambil data desain UI dari response
    ui_data = response.json()
    print("Berhasil convert dari Figma ke kode Dart!")
    print(ui_data)


def DribleToDart():
    # URL halaman Dribbble yang berisi desain UI
    url = 'https://dribbble.com/shots/12345678'

    # Mengirimkan request ke halaman Dribbble
    response = requests.get(url)

    # Mengambil HTML halaman
    html = response.text

    # Membuat objek BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Mengambil informasi desain dari halaman menggunakan BeautifulSoup
    # Anda perlu menyesuaikan ini sesuai dengan struktur HTML dari halaman Dribbble
    # Misalnya, untuk mengambil judul desain:
    title = soup.find('h1', class_='shot-title').text
    print("Berhasil convert dari Dribble ke kode Dart!", title)


MenuCMU()

pilih = int(input("Pilih nomor menu: "))

if pilih == 1:
    FigmaToDart()

elif pilih == 2:
    DribleToDart()

else:
    print("Menu tidak tersedia!")
    exit()
