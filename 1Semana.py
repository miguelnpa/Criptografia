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
