# criptografa na chave 5 de cesar:
import string


criptografado = ''
descriptografado = ''
chave_5 = {}
print('Digite a chave')
print('ex: 5')
chave = int(input('>>> '))
cifrado = input('criptografar ou descriptografar(c/d)? ').lower()
palavra = str(input('texto: ')).lower()
if chave == 5:
    # chave 5
    circulo_ex = ['v',  'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', ' ']
    circulo_in = list(string.ascii_lowercase + ' ')  # alfabeto minusculo
    if cifrado == 'c':  # criptografa
        for i in range(len(circulo_in)):
            chave_5.setdefault(circulo_in[i], circulo_ex[i])
        for letras in palavra:
            for k, v in chave_5.items():
                if letras == v:
                    criptografado = criptografado + k
        print(f'O texto criptografado é: {criptografado}')
    elif cifrado == 'd':  # descriptografa
        for i in range(len(circulo_in)):
            chave_5.setdefault(circulo_in[i], circulo_ex[i])
        for letras in palavra:
            for k, v in chave_5.items():
                if letras == k:
                    descriptografado = descriptografado + v
        print(f'O texto descriptografado é: {descriptografado}')
