import os
import shutil
import sys
import time

def listar_diretorios():
    print("\nDiretórios disponíveis:")
    for drive in "CDEFGHIJKLMNOPQRSTUVWXYZ":
        if os.path.exists(f"{drive}:\\"):
            print(f" - {drive}:\\")

def selecionar_origem():
    origem = input("\nDigite o caminho do diretório ou disco a ser copiado (ex: C:\\MeusArquivos): ").strip()
    if not os.path.exists(origem):
        print("Origem inválida. Tente novamente.")
        return None
    return origem

def selecionar_destino():
    destino = input("\nDigite o caminho do diretório de destino (ex: D:\\Backup): ").strip()
    if not os.path.exists(destino):
        try:
            os.makedirs(destino)
            print(f"Destino {destino} criado!")
        except Exception as e:
            print(f"Erro ao criar destino: {e}")
            return None
    return destino

def fazer_backup(origem, destino):
    try:
        print("\nIniciando backup...")
        nome_backup = f"backup_{time.strftime('%Y%m%d_%H%M%S')}"
        caminho_backup = os.path.join(destino, nome_backup)
        shutil.copytree(origem, caminho_backup)
        print(f"Backup concluído com sucesso em {caminho_backup}!")
    except Exception as e:
        print(f"Erro durante o backup: {e}")

def menu():
    while True:
        print("\n===== Menu de Backup =====")
        print("1. Listar discos disponíveis")
        print("2. Fazer backup")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_diretorios()
        elif opcao == "2":
            listar_diretorios()
            origem = selecionar_origem()
            if origem:
                destino = selecionar_destino()
                if destino:
                    fazer_backup(origem, destino)
        elif opcao == "3":
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
