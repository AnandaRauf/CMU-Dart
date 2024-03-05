import requests
from bs4 import BeautifulSoup
import json

def generate_flutter_code_from_figma(figma_token, file_id, frame_id):
    url = f'https://api.figma.com/v1/files/{file_id}/nodes?ids={frame_id}'
    headers = {'X-Figma-Token': figma_token}
    response = requests.get(url, headers=headers)
    data = response.json()

    flutter_code = ''
    for node_id, node_data in data['nodes'].items():
        if node_data['type'] == 'TEXT':
            flutter_code += f'Text("{node_data["characters"]}", style: TextStyle(fontSize: {node_data["fontSize"]})),\n'

    with open('figma_to_flutter.dart', 'w') as file:
        file.write(flutter_code)

def generate_flutter_code_from_dribbble(dribbble_url):
    response = requests.get(dribbble_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    flutter_code = ''
    for text_element in soup.find_all(class_='shot-description-text'):
        flutter_code += f'Text("{text_element.text.strip()}", style: TextStyle(fontSize: 16)),\n'

    with open('dribbble_to_flutter.dart', 'w') as file:
        file.write(flutter_code)

def main():
    print("------------------------------------------------------------------\n")
    nameprogram = "CMU Dart"
    version = "1.0.0"
    devdate = "04 May 2024"
    devby = "Ananda Rauf Maududi"
    print(nameprogram)
    print(version)
    print(devdate)
    print(devby)
    print("------------------------------------------------------------------\n")

    print("Menu CMU Dart:\n")
    print("1. Convert Figma to Dart")
    print("2. Convert Dribbble to Dart")

    pilih = int(input("Pilih nomor menu: "))

    if pilih == 1:
        figma_token = 'YOUR_FIGMA_TOKEN'
        file_id = 'YOUR_FIGMA_FILE_ID'
        frame_id = 'YOUR_FIGMA_FRAME_ID'
        generate_flutter_code_from_figma(figma_token, file_id, frame_id)
        print("File Figma telah berhasil dikonversi ke kode Flutter (figma_to_flutter.dart)")

    elif pilih == 2:
        dribbble_url = 'https://dribbble.com/shots/15939921-Login-Page-UI-Design'
        generate_flutter_code_from_dribbble(dribbble_url)
        print("File Dribbble telah berhasil dikonversi ke kode Flutter (dribbble_to_flutter.dart)")

    else:
        print("Menu tidak tersedia!")
        exit()

if __name__ == "__main__":
    main()
