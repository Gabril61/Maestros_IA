import os

def check_file():
    folder = r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Darlis_Sifontes_2026-06-28T233841"
    if os.path.exists(folder):
        print("Folder exists.")
        print(os.listdir(folder))
    else:
        print("Folder does not exist.")

if __name__ == "__main__":
    check_file()
