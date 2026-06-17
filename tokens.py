# ==========================================
# TOKENS.PY - Centralização de Tipos (Afri)
# ==========================================

class TokenType:
    # Tipos de Dados
    INTEIRO = "INTEIRO"
    DECIMAL = "DECIMAL"
    BINARIO = "BINARIO"
    STRING = "STRING"
    
    # Operadores Matemáticos
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    
    # Operadores de Comparação
    COMP_IGUAL = "COMP_IGUAL"
    MENOR = "MENOR"
    MAIOR = "MAIOR"
    
    # Símbolos e Delimitadores
    ASSIGN = "ASSIGN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    
    # Palavras-Chave (Keywords)
    VER = "VER"
    RECEBER = "RECEBER"
    SE = "SE"
    SENAO = "SENAO"
    ENQUANTO = "ENQUANTO"
    MOSTRA = "MOSTRA"
    
    ID = "ID"
    EOF = "EOF"

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

