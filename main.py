import subprocess
import os

def print_help():
    print("\nComandos disponíveis:")
    print("-" * 60)
    comandos = [
        ("ls", "Lista os arquivos e diretórios no diretório atual."),
        ("pwd", "Mostra o diretório atual."),
        ("mkdir <nome>", "Cria um novo diretório com o nome especificado."),
        ("rm <nome>", "Remove o arquivo ou diretório especificado."),
        ("touch <nome>", "Cria um novo arquivo vazio com o nome especificado."),
        ("cat <nome>", "Exibe o conteúdo do arquivo especificado."),
        ("clear", "Limpa a tela do terminal."),
        ("help", "Mostra esta mensagem de ajuda."),
        ("cd <diretório>", "Muda para o diretório especificado."),
        ("cd..", "Volta ao diretório pai."),
        ("exit", "Sai do mini bash."),
    ]

    for cmd, desc in comandos:
        print(f"{cmd:<15} - {desc}")
    print("-" * 60)

def mini_bash():
    while True:
        try:
            diretorio_atual = os.getcwd()
            comando = input(f"{diretorio_atual} > ").strip()

            if comando == "":
                continue


            if comando.lower() in ["exit", "sair"]:
                break

            if comando == "help":
                print_help()
                continue

 
            if comando.startswith("cd "):
                novo_diretorio = comando[3:].strip()
                try:
                    os.chdir(novo_diretorio)
                except FileNotFoundError:
                    print(f"Diretório inexistente: {novo_diretorio}")
                continue


            if comando == "cd.." or comando == "cd ..":
                try:
                    os.chdir("..")
                except Exception as e:
                    print(f"Erro ao voltar: {e}")
                continue

            args = comando.split()
            processo = subprocess.Popen(args)
            processo.wait()
        except KeyboardInterrupt:
            print("\nUse 'exit' para sair.")
        except FileNotFoundError:
            print(f"Comando não encontrado: {comando.split()[0]}")
        except Exception as e:
            print(f"Erro: {e}")
if __name__ == "__main__":
    mini_bash()