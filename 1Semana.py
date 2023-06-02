# def charRange(c1,c2):
#     lista = []
#     for c in range(ord(c1),ord(c2)+1):
#         lista = lista + [chr(c)]
#     return lista

# alfabeto = charRange("a","z")

# Escreva uma função em Python que recebe um texto e retira do mesmo todos os caracteres que não são letras, inclusive espaços.

# def limparTexto(alfabeto,texto):
#     textoSemEspeciais = ''
#     for i in texto:
#         if i.lower() in alfabeto:
#             textoSemEspeciais += i
#     return textoSemEspeciais

# texto = 'Marcelo Gama - Rua 1233, %$#dfe'

# lista = limparTexto(alfabeto,texto)
# print(lista)

# class CryptoDeslocamento:
#     def __init__(self):
#         self._valor = None
    
#     @property
#     def valor(self):
#         self._valor = self.charRange()
#         return self._valor

#     def charRange(self):
#         lista = []
#         for c in range(ord("a"),ord("z")+1):
#             lista = lista + [chr(c)]
#         return lista
    
#     def limparTexto(self,texto):
#         textoSemEspeciais = ''
#         for i in texto:
#             if i.lower() in self.valor:
#                 textoSemEspeciais += i
#         return textoSemEspeciais
    
class CryptoDeslocamento:
    def __init__(self):
        self.alfabeto = self.charRange()

    def charRange(self):
        lista = []
        for c in range(ord("a"),ord("z")+1):
            lista = lista + [chr(c)]
        return lista
    
    def limparTexto(self,texto):
        textoSemEspeciais = ''
        for i in texto:
            if i.lower() in self.alfabeto:
                textoSemEspeciais += i
        return textoSemEspeciais
    
crypto = CryptoDeslocamento()

print(crypto.limparTexto('Marcelo Gama - Rua 1233, %$#dfe'))
