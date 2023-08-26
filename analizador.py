import re

class tokenizador:
    def __init__(self, tipo, valor, num_linea):
        self.tipo = tipo
        self.valor = valor
        self.num_linea = num_linea

class analizadorLexico:
    def analizar(self, contenido):
        tokens_temp = []
        caracteres_invalidos = []
        num_linea = 1

        regexp = {
            "PALABRA_RESERVADA": r"(abstract|continue|for|new|switch|boolean|default|goto|null|synchronized|"
                                r"break|do|if|package|this|byte|double|implements|private|threadsafe|"
                                r"byvalue|else|import|protected|throw|throws|case|extends|instanceof|public|transient|"
                                r"catch|false|int|return|true|char|final|interface|short|try|"
                                r"class|finally|long|static|void|const|float|native|super|while|"
                                r"cast|future|generic|inner|operator|outer|rest|var)\b",
            "IDENTIFICADOR": r"[a-zA-Z_$][a-zA-Z0-9_$]*",
            "NUMERO_DECIMAL": r"\d+\.\d+",
            "NUMERO_ENTERO": r"\d+",
            "OPERADOR": r"[+\-*/=!&|^<>]",
            "DELIMITADOR": r"[\[\](){},.;]",
        }

        for linea in contenido.split('\n'):
            # Buscar comentarios de documentación
            doc_matches = re.findall(r"/\*\*.*?\*/", linea)
            for match in doc_matches:
                tokens_temp.append(tokenizador("COMENTARIO_DOCUMENTACION", match, num_linea))
                linea = linea.replace(match, "")  # Eliminar el comentario ya procesado

            # Procesar el resto de la línea
            for match in re.findall(r"//.*|/\*.*?\*/|"
                            r"[a-zA-Z_$][a-zA-Z0-9_$]*|\d+\.\d+|\d+|[+\-*/=!&|^<>[\](){},.;]", linea):
                if match.startswith("//"):
                    tokens_temp.append(tokenizador("COMENTARIO_UNA_LINEA", match, num_linea))
                elif match.startswith("/*"):
                    tokens_temp.append(tokenizador("COMENTARIO_VARIAS_LINEAS", match, num_linea))
                else:
                    for token_name, regex in regexp.items():
                        if re.match(regex, match):
                            tokens_temp.append(tokenizador(token_name, match, num_linea))
                            break
                    else:
                        caracteres_invalidos.append((match, num_linea))
            num_linea += 1  # Incremento fuera del bucle interno

        return tokens_temp, caracteres_invalidos
