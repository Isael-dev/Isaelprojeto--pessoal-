## Criar uma função
def imprimir(texto=""):
    print(texto)
def media(n1=2, n2=5, n3=8):
    media = (n1+n2+n3)/3
    print(media)
imprimir()
media(3,5,8)

def CalcularIMC(peso, altura):
    imc = peso / (altura + altura)
    imprimir