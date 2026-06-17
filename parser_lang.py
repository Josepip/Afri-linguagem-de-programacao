# ==========================================
# PARSER_LANG.PY - Com Nomes em Português
# ==========================================

from dataclasses import dataclass

class ASTNode:
    pass

@dataclass
class NumberNode(ASTNode):
    token: any
    def __repr__(self): return f"{self.token.value}"

@dataclass
class StringNode(ASTNode):
    token: any
    def __repr__(self): return f'"{self.token.value}"'

@dataclass
class BooleanNode(ASTNode):
    token: any
    def __repr__(self): return f"{self.token.value}"

@dataclass
class VariableNode(ASTNode):
    token: any
    def __repr__(self): return f"{self.token.value}"

@dataclass
class BinOpNode(ASTNode):
    left: ASTNode
    op_token: any
    right: ASTNode
    def __repr__(self): return f"({self.left} {self.op_token.value} {self.right})"

@dataclass
class AssignNode(ASTNode):
    var_node: VariableNode
    expr_node: ASTNode
    def __repr__(self): return f"{self.var_node} = {self.expr_node}"

@dataclass
class VerNode(ASTNode):
    argumento: ASTNode
    def __repr__(self): return f"ver {self.argumento}"

@dataclass
class ReceberNode(ASTNode):
    var_node: VariableNode
    def __repr__(self): return f"receber {self.var_node}"

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise SyntaxError(f"Token inesperado: {self.current_token}. Esperado: {token_type}")

    def factor(self):
        token = self.current_token
        from lexer import TokenType

        if token.type in (TokenType.INTEIRO, TokenType.DECIMAL):
            self.eat(token.type)
            return NumberNode(token)
        elif token.type == TokenType.BINARIO:
            self.eat(TokenType.BINARIO)
            return BooleanNode(token)
        elif token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return StringNode(token)
        elif token.type == TokenType.ID:
            self.eat(TokenType.ID)
            return VariableNode(token)

        raise SyntaxError(f"Sintaxe inválida no factor: {token}")

    def term(self):
        from lexer import TokenType
        node = self.factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            op_token = self.current_token
            self.eat(self.current_token.type)
            node = BinOpNode(left=node, op_token=op_token, right=self.factor())
        return node

    def expr(self):
        from lexer import TokenType
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op_token = self.current_token
            self.eat(self.current_token.type)
            node = BinOpNode(left=node, op_token=op_token, right=self.term())
        return node

    def statement(self):
        from lexer import TokenType

        if self.current_token.type == TokenType.VER:
            self.eat(TokenType.VER)
            return VerNode(argumento=self.expr())

        if self.current_token.type == TokenType.RECEBER:
            self.eat(TokenType.RECEBER)
            if self.current_token.type == TokenType.ID:
                var_node = VariableNode(self.current_token)
                self.eat(TokenType.ID)
                return ReceberNode(var_node=var_node)
            else:
                raise SyntaxError("Esperado nome de variável após 'receber'.")

        if self.current_token.type == TokenType.ID:
            var_node = VariableNode(self.current_token)
            self.eat(TokenType.ID)
            if self.current_token.type == TokenType.ASSIGN:
                self.eat(TokenType.ASSIGN)
                expr_node = self.expr()
                return AssignNode(var_node=var_node, expr_node=expr_node)
            else:
                raise SyntaxError("Instrução inválida baseada em identificador.")

        return self.expr()

    def parse(self):
        return self.statement()

