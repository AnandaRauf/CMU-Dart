#from figma_exporter import FigmaExporter
from dribbble_to_flutter import DribbbleToFlutter
print("------------------------------------------------------------------\n")

nameprogram= "CSM Dart"
version= "1.0.0"
devdate= "04 May 2024"
devby= "Ananda Rauf Maududi"
print(nameprogram)
print(version)
print(devdate)
print(devby)
print("------------------------------------------------------------------\n")


def MenuCMU():
    print("Menu CMU Dart:\n")
    print()
    print("1. Convert Figma to Dart")
    print("2. Convert Dribble to Dart")
    
def FigmaToDart():
    # Masukkan token Figma Anda di sini
    figma_token = "YOUR_FIGMA_TOKEN"
    
    # Buat objek FigmaExporter
    exporter = FigmaExporter(figma_token)
    
    # ID frame atau page Figma yang ingin Anda ekspor
    file_id = "YOUR_FIGMA_FILE_ID"
    frame_id = "YOUR_FIGMA_FRAME_ID"
    
    # Ekspor desain UI dari Figma ke kode Dart
    dart_code = exporter.export_to_flutter(file_id, frame_id)
    
    # Hasil convert kode dart dari Figma
    
    print("Berhasil convert dari Figma ke kode Dart!")
    print(dart_code)

def DribleToDart():
    # Buat objek DribbbleToFlutter
    dribbble_converter = DribbbleToFlutter()
    
    # URL shot Dribbble yang ingin Anda konversi
    
    dribbble_url = "YOUR_DRIBBBLE_URL"
    
    # Ekspor desain UI dari Dribbble ke kode Dart
    dart_code = dribbble_converter.convert_url_to_flutter(dribbble_url)
    
    # Hasil convert kode dart dari Dribbble
    print(dart_code)

MenuCMU()

pilih= int(input("Pilih nomor menu: "))

if pilih== 1:
    FigmaToDart()

elif pilih==2:
    DribleToDart()

else:
    print("Menu tidak tersedia!")
    exit
    
     

