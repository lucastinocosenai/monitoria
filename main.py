# Declaração de função (def)

# 1: def - definir função
# 2: nome da função (verbo)
# 3: () parâmetros
# 4: (parametro1, parametro2) é o que eu quero passar
# todas as vezes que eu chamar a função


def somaDoisValores(numero1, numero2):
    soma = numero1 + numero2
    
    print(soma)

# Chamada da função

x = 1 + 5
y = 2 + 7
z = 2.5

somaDoisValores(1, 2)
somaDoisValores(5, 7)
somaDoisValores(x, y)

# Declaração de função

def printaNomeCompleto(nome, sobrenome):
    nomeCompleto = nome + " " + sobrenome
    print(nomeCompleto)

# Chamada da função

qualquer = "Qualquer"
coisa = "Coisa"

printaNomeCompleto("Lucas", "Tinoco")
printaNomeCompleto(qualquer, coisa)