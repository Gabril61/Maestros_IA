import os
import re

dama = open(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val', encoding='utf-8').read()
dama_calc = dama[:dama.find('</calculation>')]

match = re.search(r'<[^>]*\bid="166"\b[^>]*>', dama_calc)
if match:
    print("In Dama:", match.group(0))
else:
    print("Not found in Dama")
