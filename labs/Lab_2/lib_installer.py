import subprocess

libraries = [
    'pandas',
    'seaborn',
    'matplotlib',
    'scikit-learn'
]

def install_libraries():
    for library in libraries:
        try:
            subprocess.check_call(['pip', 'install', library])
            print(f"{library} успешно установлена!")
        except subprocess.CalledProcessError:
            print(f"Ошибка при установке {library}")

if __name__ == "__main__":
    install_libraries()