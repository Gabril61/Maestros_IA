import re

file_path = "Blazer_Dama_Maestro.val"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<line firstPoint="89503" id="89511" lineColor="blue" secondPoint="89504"/>'
idx_start = content.find(start_marker)

if idx_start != -1:
    idx_end = content.find('</nodes>', idx_start)
    if idx_end != -1:
        # We want to keep the \n        </nodes> part
        # Let's find the last newline before </nodes>
        idx_end_real = content.rfind('\n', idx_start, idx_end)
        if idx_end_real == -1:
            idx_end_real = idx_end
            
        new_content = content[:idx_start] + content[idx_end_real:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Orphaned points removed.")
else:
    print("Orphaned points not found.")
