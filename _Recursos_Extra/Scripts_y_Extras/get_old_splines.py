import subprocess
import re

out = subprocess.check_output(['git', 'show', 'b4af099:Blazer_Dama_Maestro.val']).decode('utf-8')
splines = re.findall(r'<spline [^>]+id="(?:12020|12021|12022)"[^>]+/>', out)
print("\n".join(splines))
