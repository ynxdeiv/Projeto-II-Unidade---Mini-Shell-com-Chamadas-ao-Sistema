import subprocess
import os
import platform

def help():
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

windows = platform.system() == "Windows"

def mini_bash():
    while True:
        try:
            diretorio_atual = os.getcwd()

            os.write(1, f"{diretorio_atual} > ".encode())
            comando = os.read(0, 1024).decode().strip()

            if comando == "":
                continue

            if comando.lower() in ["exit", "sair"]:
                break

            if comando == "help":
                help()
                continue
 
            if comando.startswith("cd "):
                novo_diretorio = comando[3:].strip()
                try:
                    os.chdir(novo_diretorio)
                except FileNotFoundError:
                    os.write(1, f"Diretorio inexistente: {novo_diretorio}\n".encode())
                continue


            if comando == "cd.." or comando == "cd ..":
                try:
                    os.chdir("..")
                except Exception as e:
                    os.write(1, f"Erro ao voltar: {e}\n".encode())
                continue

            if windows:
                if comando == "ls":
                    comando = "dir"
                elif comando == "clear":
                    comando = "cls"
                elif comando.startswith("rm"):
                    nome = comando[3:]
                    comando = f"del {nome}"
                elif comando.startswith("touch"):
                    nome = comando[6:]
                    comando = f"type null>{nome}"

            subprocess.run(comando, shell=True)
                

            args = comando.split()
            processo = subprocess.Popen(args, shell=True)
            processo.wait()

        except KeyboardInterrupt:
            os.write(1, "\nUse 'exit' para sair.\n".encode())

        except FileNotFoundError:
            os.write(1, f"Comando nao encontrado: {comando.split()[0]}\n".encode())

        except Exception as e:
            os.write(1, f"Erro: {e}\n".encode())
            
if __name__ == "__main__":
    mini_bash()