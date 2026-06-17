​📖 Manual de Introdução ao Motor do Afri
​Bem-vindo ao núcleo de desenvolvimento do Afri! Se estás aqui, significa que queres entender como o motor da nossa linguagem funciona e como podes expandi-lo.
​Este manual explica o ciclo de vida de uma instrução dentro do compilador e como os arquivos interagem entre si.
​🏗️ A Arquitetura do Afri
​O Afri não executa o texto diretamente. Ele transforma o código fonte em três etapas consecutivas
:
Código Fonte (.af) ➡️  [Lexer] ➡️  Lista de Tokens ➡️  [Parser] ➡️  Árvore (AST) ➡️  [Interpretador] ➡️  Execução


1. O Arquivo Central: tokens.py
​É o dicionário da linguagem. Se queres criar uma nova palavra-chave ou operador (ex: ou, e, rotina), o primeiro passo é registar o tipo de Token aqui na classe TokenType.
​2. O Analisador Léxico: lexer.py
​O Lexer lê o arquivo .af caractere por caractere (como um vetor de texto) e agrupa-os em blocos com significado (Tokens).
​Exemplo: O texto se idade > 18 é transformado em:
Token(SE, 'se'), Token(ID, 'idade'), Token(MAIOR, '>'), Token(INTEIRO, 18).
​Onde mexer: Se adicionaste um token em tokens.py, precisas de ir ao método identifier() ou get_next_token() do Lexer para ensinar a linguagem a reconhecer esses novos caracteres.
​3. O Analisador Sintático: parser_lang.py
​O Parser pega na lista de Tokens gerada pelo Lexer e valida se a ordem faz sentido gramatical (Sintaxe). Ele constrói a AST (Abstract Syntax Tree), que é a árvore hierárquica do código.
​Exemplo: Para a estrutura se, ele exige um formato rígido: SE + Expressão de Condição + Bloco entre chavetas {}.
​Onde mexer: Cada estrutura tem o seu próprio "Nó" (dataclass). Se fores criar a lógica do mostra (return), vais precisar de criar um class MostraNode(ASTNode): e atualizar a função statement() para capturar o token correspondente.
​4. O Motor de Execução: interpreter.py
​O Interpretador percorre a árvore (AST) gerada pelo Parser e executa a lógica real em Python. É aqui que a "mágica" acontece: as variáveis ganham valores guardados num dicionário (self.tabela_variaveis) e as operações matemáticas são resolvidas.
​Onde mexer: Para cada nó novo criado no Parser, precisas de adicionar uma verificação if isinstance(node, TeuNovoNode): dentro do método avaliar() para definir o que o Afri deve fazer no terminal ao ler essa instrução.
​🛠️ Guia Prático: Como adicionar um comando novo no Afri?
​Se quiseres propor uma nova funcionalidade para o repositório, segue sempre este roteiro de 4 passos:
​Registar no tokens.py: Cria a constante do Token em maiúsculas.
​Ensinar o lexer.py: Diz ao Lexer qual a palavra exata em português que ativa esse Token.
​Estruturar no parser_lang.py: Cria o Nó da árvore para o comando e define na função statement() o que deve vir antes e depois dele.
​Dar vida no interpreter.py: Escreve o código Python que executa a ação real do comando dentro do método avaliar().
​🚨 Regras de Contribuição
​Mantenha a identidade: O Afri prioriza termos limpos e nativos em português.
​Não suba lixo: Garanta que a pasta __pycache__ e arquivos locais de teste não entram nos teus Commits (use o .gitignore).
​Testes: Antes de enviar um Pull Request, rode o arquivo main.af no Termux para garantir que nenhuma alteração partiu as regras antigas de matemática, loops ou condicionais.
