import re
with open('C:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val', 'r', encoding='utf-8') as file:
    content = file.read()
    matches = re.findall(r'type="([a-zA-Z]+)"', content)
    print("Point types found:", set(matches))
