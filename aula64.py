"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf_digitado = input('Digite um cpf: ')

cpf_tratado = ''
cpf_sem_pontuacao = []

# retira "." e "-"
if cpf_digitado:
    for numero in cpf_digitado:
        if numero == '.' or numero == '-':
            continue
        cpf_sem_pontuacao.append(numero)


# cria lista de multiplicadores
multiplicadores = []
for i in range(10, 1, -1):
    multiplicadores.append(i)


# retira os digitos
cpf_sem_pontuacao_original = cpf_sem_pontuacao.copy()

cpf_sem_pontuacao.pop()
cpf_sem_pontuacao.pop()


# faz multiplicacao
total_multiplicacao = 0

for chave, numero in enumerate(cpf_sem_pontuacao):
    numero_int = int(numero)
    total_multiplicacao += (numero_int * multiplicadores[chave])


# validação primeiro digito
total_multiplicacao *= 10
resto_da_divisao = total_multiplicacao % 11


if resto_da_divisao == 10:
    primeiro_digito = 1
elif resto_da_divisao > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto_da_divisao

cpf_sem_pontuacao.append(str(primeiro_digito))
