# ==========================================
# LEXER.PY - Com Nomes em Português
# ==========================================

class TokenType:
    INTEIRO = "INTEIRO"      # Antigo INT
    DECIMAL = "DECIMAL"      # Antigo FLOAT
    BINARIO = "BINARIO"      # Novo BOOLEAN
    STRING = "STRING"
    ASSIGN = "ASSIGN"        # Símbolo '='
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    VER = "VER"
    RECEBER = "RECEBER"
    ID = "ID"
    EOF = "EOF"

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        """Captura Inteiros ou Decimais"""
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            
        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            return Token(TokenType.DECIMAL, float(result))
            
        return Token(TokenType.INTEIRO, int(result))

    def string(self):
        result = ""
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        if self.current_char == '"':
            self.advance()
            return Token(TokenType.STRING, result)
        else:
            raise SyntaxError("Erro Léxico: String não fechada com aspas.")

    def identifier(self):
        result = ""
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
            
        if result == "ver":
            return Token(TokenType.VER, result)
        if result == "receber":
            return Token(TokenType.RECEBER, result)
            
        # Reconhecimento dos literais binários do Afri
        if result in ("verdade", "falso"):
            return Token(TokenType.BINARIO, True if result == "verdade" else False)
            
        return Token(TokenType.ID, result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.number()
            if self.current_char == '"':
                return self.string()
            if self.current_char.isalpha():
                return self.identifier()
                
            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, '=')
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV, '/')
                
            raise SyntaxError(f"Caractere inválido: '{self.current_char}'")
        return Token(TokenType.EOF, None)

