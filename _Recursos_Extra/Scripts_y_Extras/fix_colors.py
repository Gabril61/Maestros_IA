file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('lineColor="red"', 'lineColor="black"')
text = text.replace('lineColor="green"', 'lineColor="black"')
text = text.replace('lineColor="blue"', 'lineColor="black"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Colors fixed')
