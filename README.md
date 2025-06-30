

## 🐚 Mini Bash – Projeto II Unidade

Este é um mini interpretador de comandos (shell) feito em Python. Ele simula um terminal básico, permitindo rodar comandos como `ls`, `cd`, `rm`, `touch`, etc., tanto no **Windows (PowerShell)** quanto no **Git Bash**.

---

## ✅ Como compilar e rodar

**Pré-requisitos:**

* Python 3 instalado no sistema
* Terminal compatível (PowerShell, Git Bash, ou terminal Linux)

**Para rodar:**

```bash
python mini_bash.py
```

---

## 🛠️ Chamadas ao sistema utilizadas

* `os.getcwd()` → retorna o diretório atual
* `os.chdir()` → muda de diretório
* `os.write()` e `os.read()` → leitura e escrita no terminal
* `subprocess.run()` e `subprocess.Popen()` → executa comandos do sistema

Essas chamadas permitem interação direta com o sistema operacional.

---

## 💡 Exemplos de comandos testados

| Comando           | Descrição                    | Saída esperada (exemplo)                |
| ----------------- | ---------------------------- | --------------------------------------- |
| `ls`              | Lista arquivos/pastas        | `arquivo.txt pasta/`                    |
| `pwd`             | Mostra onde estou            | `C:\Users\Usuario\Documentos`           |
| `cd pasta`        | Entra em uma pasta           | Muda o prompt para aquela pasta         |
| `cd..` ou `cd ..` | Volta uma pasta              | Volta para o diretório anterior         |
| `rm arquivo.txt`  | Apaga um arquivo             | Apaga o arquivo sem mensagens (Windows) |
| `touch novo.txt`  | Cria um arquivo vazio        | Cria `novo.txt`                         |
| `cat arquivo.txt` | Mostra o conteúdo do arquivo | Exibe texto do arquivo no terminal      |
| `clear`           | Limpa a tela                 | Tela limpa                              |
| `help`            | Mostra ajuda com os comandos | Lista com descrições                    |
| `exit`            | Encerra o mini bash          | Sai do programa                         |

---

## ⚠️ Limitações conhecidas

* O suporte a comandos é **limitado aos que estão definidos** no código.
* Alguns comandos funcionam de forma diferente em **Windows e Linux**.
* O comando `rm` não apaga pastas no Windows.
* O comando `touch` pode falhar se o nome do arquivo estiver errado.
* Não há verificação de segurança ao executar comandos externos.
* `subprocess.run()` e `Popen()` estão sendo usados juntos — o ideal seria usar apenas um.

---

## 🧑‍💻 Autor

Projeto feito para a disciplina de Sistemas Operacionais – 2ª Unidade.

---

Se quiser, posso salvar esse conteúdo como um arquivo `README.md` para você. Deseja isso?
