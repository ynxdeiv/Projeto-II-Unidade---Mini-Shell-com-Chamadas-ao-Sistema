import subprocess
import os


def mini_bash():
    while True:
        try:
            diretorio_atual = os.getcwd()
            comando = input(f"{diretorio_atual} ").strip()
            
            if comando.startswith("cd "):
                novo_diretorio = comando[3:].strip()
                
                try:
                    os.chdir(novo_diretorio)
                except FileNotFoundError:
                    print(f"diretorio inexistente: {novo_diretorio}")
                continue
            
            if comando.startswith("cd.."):
                try:
                    os.chdir("..")
                except FileNotFoundError:
                    print("não foi possível voltar ao diretório anterior.")
                continue
            
            
            if comando == "":
                continue
            
            if comando.lower() in ["exit", "sair"]:
                break
            
            
            args = comando.split()
            processo = subprocess.Popen(args)
            processo.wait()

        except KeyboardInterrupt:
            print("\nUse 'exit' para sair.")
        except FileNotFoundError:
            print(f"Comando não encontrado: {args[0]}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    mini_bash()
