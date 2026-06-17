# ==========================================
# INTERPRETER.PY - Com Tipos em Português
# ==========================================

from parser_lang import VerNode, NumberNode, StringNode, BooleanNode, BinOpNode, ReceberNode, VariableNode, AssignNode

class Interpretador:
    def __init__(self):
        self.tabela_variaveis = {}

    def avaliar(self, node):
        if isinstance(node, NumberNode):
            return node.token.value

        if isinstance(node, BooleanNode):
            return node.token.value

        if isinstance(node, StringNode):
            return str(node.token.value)

        if isinstance(node, VariableNode):
            nome_var = node.token.value
            if nome_var in self.tabela_variaveis:
                return self.tabela_variaveis[nome_var]
            raise Exception(f"Erro de Execução: A variável '{nome_var}' não existe.")

        if isinstance(node, AssignNode):
            nome_var = node.var_node.token.value
            valor = self.avaliar(node.expr_node)
            self.tabela_variaveis[nome_var] = valor
            return valor

        if isinstance(node, BinOpNode):
            esquerda = self.avaliar(node.left)
            direita = self.avaliar(node.right)
            tipo_op = node.op_token.type

            if tipo_op == "PLUS":
                if isinstance(esquerda, str) or isinstance(direita, str):
                    return str(esquerda) + str(direita)
                return esquerda + direita
            elif tipo_op == "MINUS":
                return  esquerda - direita
            elif tipo_op == "MUL":
                return esquerda * direita
            elif tipo_op == "DIV":
                if direita == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero não permitida no Afri.")
                return esquerda / direita

        if isinstance(node, VerNode):
            resultado = self.avaliar(node.argumento)
            print(resultado)
            return resultado

        if isinstance(node, ReceberNode):
            nome_var = node.var_node.token.value
            valor_digitado = input().strip()

            # Mapeamento dinâmico inteligente no input do Afri
            if valor_digitado == "verdade":
                self.tabela_variaveis[nome_var] = True
            elif valor_digitado == "falso":
                self.tabela_variaveis[nome_var] = False
            elif valor_digitado.isdigit():
                self.tabela_variaveis[nome_var] = int(valor_digitado)
            else:
                try:
                    self.tabela_variaveis[nome_var] = float(valor_digitado)
                except ValueError:
                    self.tabela_variaveis[nome_var] = valor_digitado
                    
            return self.tabela_variaveis[nome_var]

        raise Exception(f"Erro de Execução: Tipo de nó desconhecido: {type(node)}")

