import json
import os

ARQUIVO = "livros.json"

def carregar_livros():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_livros(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)

def cadastrar_livro():
    livros = carregar_livros()

    titulo = input("Título do livro: ").strip()
    autor = input("Autor do livro: ").strip()

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            print("❌ Livro já cadastrado.")
            return

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    }

    livros.append(novo_livro)
    salvar_livros(livros)
    print("✅ Livro cadastrado com sucesso!")

def listar_livros():
    livros = carregar_livros()

    if not livros:
        print("📚 Nenhum livro cadastrado.")
        return
    
    print("\n=== Lista de Livros ===")
    for i, livro in enumerate(livros, start=1):
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({status})")

def emprestar_livro():
    livros = carregar_livros()
    listar_livros()

    if not livros:
        return

    try:
        escolha = int(input("Número do livro para emprestar: "))
        livro = livros[escolha - 1]

        if not livro["disponivel"]:
            print("❌ Livro já está emprestado.")
            return

        livro["disponivel"] = False
        salvar_livros(livros)
        print("✅ Livro emprestado com sucesso!")

    except (ValueError, IndexError):
        print("❌ Opção inválida.")

def devolver_livro():
    livros = carregar_livros()
    listar_livros()

    if not livros:
        return

    try:
        escolha = int(input("Número do livro para devolver: "))
        livro = livros[escolha - 1]

        if livro["disponivel"]:
            print("❌ Livro já está disponível.")
            return

        livro["disponivel"] = True
        salvar_livros(livros)
        print("✅ Livro devolvido com sucesso!")

    except (ValueError, IndexError):
        print("❌ Opção inválida.")

def menu():
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            emprestar_livro()
        elif opcao == "4":
            devolver_livro()
        elif opcao == "5":
            print("Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()