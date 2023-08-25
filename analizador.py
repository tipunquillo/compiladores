# ahorita solo probando como la estructura y lo de que agarre las clases (usamos el ejercicio anterior para guiarnos solo en esta parte, toca cambiarlo a como lo queremos despues
import re

class analizadorLexico:
    def analizar(self, entrada):
        tokens_temp = []
        caracteres_invalidos = []

        regexp = {
            "NUMERO_DECIMAL": r"\d+\.\d+",
            "NUMERO_ENTERO": r"\d+",
            "SIGNO": r"[+\-*/()^.]"
        }

        mapeo = {
            "NUMERO_DECIMAL": "NUMERO_DECIMAL",
            "NUMERO_ENTERO": "NUMERO_ENTERO",
            "SIGNO": {
                "+": "SIGNO_MAS",
                "-": "SIGNO_RESTA",
                "*": "SIGNO_MULTIPLICACION",
                "/": "SIGNO_DIVISION",
                "^": "SIGNO_EXPONENTE",
                "(": "PARENTESIS_IZQ",
                ")": "PARENTESIS_DER",
                ".": "SIGNO_PUNTO"
            }
        }

        for match in re.findall(r"\d+\.\d+|\d+|[+\-*/()^.]|[^ \t\n]", entrada):
            for token_name, regex in regexp.items():
                if re.match(regex, match):
                    etiqueta = mapeo.get(token_name)
                    if isinstance(etiqueta, dict):
                        etiqueta = etiqueta.get(match)
                    tokens_temp.append((etiqueta, match))
                    break
            else:
                caracteres_invalidos.append(match)

        return tokens_temp, caracteres_invalidos
