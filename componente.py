class Componente:
    def __init__(self, lexema, token):
        self.__corazon = {'token': token, 'lexema': lexema}
        self.__id = None
        self.tipos_de_datos = {'int', 'float', 'char', 'string', 'bool', 'void', 'None', 'Null', 'enum'}
        self.palabras_reservadas = {
            'in', 'append', 'print', 'return', 'class', 'public', 'private', 'protected',
            'const', 'try', 'except', 'def', 'finally', 'import', '#include', 'from', 'as',
            'is', 'global', 'nonlocal', 'case', 'break', 'continue', 'default', 'template',
            'catch', 'new', 'del', 'with', 'lambda', 'super', '__init__', 'self', 'len'}
        self.operadores_logicos = {'&&', '||', 'or', 'and', 'not', '!', 'True', 'False'}
        self.estructuras_de_control = {'while', 'for', 'do while', 'switch'}
        self.condicionales = {'if', 'else', 'elif'}
        self.operadores_relacionales = {'==', '<', '>', '<=', '>=', '!='}
        self.signos = {'.', ',', ';'}
        self.set_id()
        self.set_token()

    def __str__(self):
        return ("Lexema: " + str(self.__corazon['lexema']) + ", token: " + str(self.__corazon['token']) + " # " +
                str(self.__id))

    def get_lexema(self):
        return self.__corazon['lexema']

    def get_token(self):
        return self.__corazon['token']

    def get_id(self):
        return self.__id

    def set_token(self):
        # Asignacion de token -------------------------------------------------
        if self.__corazon['lexema'] in self.condicionales:
            self.__corazon['token'] = "Condicional"
        elif self.__corazon['lexema'] in self.palabras_reservadas:
            self.__corazon['token'] = "Palabra reservada"
        elif self.__corazon['lexema'] in self.tipos_de_datos:
            self.__corazon['token'] = "Tipo de dato"
        elif self.__corazon['lexema'] in self.estructuras_de_control:
            self.__corazon['token'] = "Estructura de control"
        elif self.__corazon['lexema'] in self.operadores_logicos:
            self.__corazon['token'] = "Operador logico"
        elif self.__corazon['lexema'] in self.signos:
            self.__corazon['token'] = "signo de puntuacion"
        elif self.__corazon['lexema'] in self.operadores_relacionales:
            self.__corazon['token'] = "Operador relacional"

    def set_id(self):
        token_lexema_a_numero = {
            'tipo de dato': 0,
            'id': 1,
            ';': 2,
            ',': 3,
            '(': 4,
            ')': 5,
            '{': 6,
            '}': 7,
            '=': 8,
            'if': 9,
            'while': 10,
            'return': 11,
            'else': 12,
            'constante': 13,
            'opSuma': 14,
            'opLogico': 15,
            'opMultiplicacion': 16,
            'opRelacional': 17,
            '$': 18
        }
        # Asignacion de ID ----------------------------------------------------
        if self.__corazon['lexema'] in token_lexema_a_numero:
            self.__id = token_lexema_a_numero.get(self.__corazon['lexema'], -1)
        elif self.__corazon['token'] in token_lexema_a_numero:
            self.__id = token_lexema_a_numero.get(self.__corazon['token'], -1)
        # print(self)
