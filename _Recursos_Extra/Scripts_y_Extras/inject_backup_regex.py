import sys
import re

path = 'C:/Users/Ricx18/Desktop/Panel_TextilFit.hta'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Use regex to find the end of the first button and inject the new button
pattern = r'(<button class="btn-maestros" onclick="abrirEscritorio\(\'Maestros_IA\'\)">[^<]+</button>)'
replacement = r'\1\n                <button class="btn-primary" style="background: linear-gradient(45deg, #11998e, #38ef7d);" onclick="ejecutarRespaldo()"> ☁️ Respaldar Maestros en la Nube</button>'

new_content = re.sub(pattern, replacement, content)

if content == new_content:
    print("Failed to match the button HTML!")
else:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Button injected via regex.")
