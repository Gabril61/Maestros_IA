import sys

path = 'C:/Users/Ricx18/Desktop/Panel_TextilFit.hta'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Inject HTML button
target_html = '<button class="btn-maestros" onclick="abrirEscritorio(\'Maestros_IA\')"> Abrir Maestros_IA (Diseo)</button>'
new_button = '<button class="btn-primary" style="background: linear-gradient(45deg, #11998e, #38ef7d);" onclick="ejecutarRespaldo()"> Respaldar Maestros en la Nube</button>'
if new_button not in content:
    content = content.replace(target_html, target_html + '\n                ' + new_button)

# Inject JS function
js_target = 'function abrirEscritorio(carpeta) {'
js_func = '''function ejecutarRespaldo() {
            var shell = new ActiveXObject("WScript.Shell");
            var desktop = shell.SpecialFolders("Desktop");
            var batPath = desktop + "\\\\Maestros_IA\\\\Respaldar_Nube.bat";
            shell.Run('cmd.exe /c "' + batPath + '"', 1, false);
        }

        '''
if 'function ejecutarRespaldo()' not in content:
    content = content.replace(js_target, js_func + js_target)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Panel_TextilFit.hta updated successfully.")
