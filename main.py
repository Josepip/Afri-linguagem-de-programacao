# ==========================================
# MAIN.PY - Interface CLI para a Linguagem Afri
# ==========================================

import sys
import os
from lexer import Lexer
from parser_lang import Parser
from interpreter import Interpretador

def executar_codigo(codigo_fonte, interpretador):
    """Executa um bloco de código Afri usando o mesmo interpretador (mantém a memória)"""
    if not codigo_fonte.strip():
        return
    try:
        lexer = Lexer(codigo_fonte)
        parser = Parser(lexer)
        arvore_ast = parser.parse()
        interpretador.avaliar(arvore_ast)
    except Exception as e:
        print(f"❌ Erro: {e}")

def abrir_modo_interativo():
    """Abre o terminal interativo (REPL) do Afri"""
    interpretador = Interpretador()
    print("=========================================")
    print("    Afri Interpretador - Modo Interativo ")
    print("    Digita o teu código ou 'sair' para fechar.")
    print("=========================================")
    
    while True:
        try:
            # Mostra um prompt personalizado no Termux
            linha = input("afri > ")
            if linha.strip().lower() == "sair":
                print("Kanimambo! (Obrigado!) Até à próxima.")
                break
            executar_codigo(linha, interpretador)
        except (KeyboardInterrupt, EOFError):
            print("\nSaindo...")
            break

def ler_e_executar_ficheiro(caminho_ficheiro):
    """Lê um ficheiro externo .af e executa todo o conteúdo"""
    if not os.path.exists(caminho_ficheiro):
        print(f"❌ Erro: O ficheiro '{caminho_ficheiro}' não foi encontrado.")
        return

    # Validação da extensão que escolheste
    if not caminho_ficheiro.endswith('.af'):
        print("⚠️  Aviso: O Afri recomenda ficheiros com a extensão '.af'")

    with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
        codigo_fonte = f.read()

    interpretador = Interpretador()
    executar_codigo(codigo_fonte, interpretador)

if __name__ == "__main__":
    # Se o utilizador passar um argumento (ex: python main.py script.af)
    if len(sys.argv) > 1:
        ler_e_executar_ficheiro(sys.argv[1])
    else:
        # Se correr apenas 'python main.py', abre o modo interativo
        abrir_modo_interativo()

