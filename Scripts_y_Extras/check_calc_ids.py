import re

ids = ['247', '1025', '2014', '2012', '2008', '232', '280', '1024', '201', '1022', '262', '1028', '230', '281', '2000', '30010', '231', '240', '1005', '1029', '1023', '1006', '2001', '214']

def check_file(path):
    content = open(path, encoding='utf-8').read()
    calc = content[:content.find('</calculation>')]
    missing = [i for i in ids if not re.search(r'\bid="' + i + r'"', calc)]
    print(f"{path}: missing {missing}")

check_file(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val')
check_file(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
