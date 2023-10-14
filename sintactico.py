import ply.lex as lex
import ply.yacc as yacc

class analizarSintactico:
    @staticmethod
    def analizar_sintactico(entrada_cadena):
        # Definición de tokens
        tokens = (
            'IF',
            'LPAREN',
            'RPAREN',
            'LBRACE',
            'RBRACE',
            'NUMERIC',
            'GT',
            'LT',
            'GE',
            'LE',
            'EQ',
            'NEQ',
            'PRINT',
            'SEMICOLON',
            'STRING'
        )

        # Expresiones regulares para tokens
        t_IF = r'if'
        t_LPAREN = r'\('
        t_RPAREN = r'\)'
        t_LBRACE = r'\{'
        t_RBRACE = r'\}'
        t_NUMERIC = r'\d+'
        t_GT = r'>'
        t_LT = r'<'
        t_GE = r'>='
        t_LE = r'<='
        t_EQ = r'=='
        t_NEQ = r'!='
        t_PRINT = r'print'
        t_SEMICOLON = r';'
        t_STRING = r'"[^"]*"'

        # Ignorar espacios en blanco y tabulaciones
        t_ignore = ' \t'

        # Manejo de errores
        def t_error(t):
            raise SyntaxError(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")

        # Construcción del analizador léxico
        lexer = lex.lex()

        # Definición de la gramática
        def p_if_statement(p):
            'statement : IF LPAREN condition RPAREN LBRACE body RBRACE'
            p[0] = "Sentencia if válida"

        def p_condition_numeric(p):
            '''condition :  expression GT expression
                         | expression LT expression
                         | expression GE expression
                         | expression LE expression
                         | expression EQ expression
                         | expression NEQ expression'''

        def p_expression(p):
            '''expression : NUMERIC
                          | expression GT expression
                          | expression LT expression
                          | expression GE expression
                          | expression LE expression
                          | expression EQ expression
                          | expression NEQ expression'''

        def p_body(p):
            '''body : PRINT LPAREN STRING RPAREN SEMICOLON
                    | PRINT LPAREN NUMERIC RPAREN SEMICOLON
                    | LBRACE error RBRACE'''
            p[0] = "Cuerpo válido"

        def p_error(p):
            raise SyntaxError(f"Error de sintaxis en la línea {p.lineno}: {entrada_cadena.splitlines()[p.lineno-1]}")

        # Construcción del analizador sintáctico
        parser = yacc.yacc()

        try:
            resultado = parser.parse(entrada_cadena)
            return [resultado] if resultado else ["Sentencia if válida"]
        except SyntaxError as e:
            return [str(e)]  # Devolver una lista con el mensaje de error









