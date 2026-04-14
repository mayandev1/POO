def pode_formar_triangulo(l1, l2, l3):
    return (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1)

def tipo_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilátero"
    elif l1 != l2 and l1 != l3 and l2 != l3:
        return "Escaleno"
    else:
        return "Isósceles"

def isTriAngRect(l1, l2, l3):
    lados = sorted([l1, l2, l3])  
    a, b, c = lados  

    return c**2 == a**2 + b**2

l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))

if pode_formar_triangulo(l1, l2, l3):
    print("É possível formar um triângulo!")

    print("Tipo:", tipo_triangulo(l1, l2, l3))

    if isTriAngRect(l1, l2, l3):
        print("É um triângulo retângulo!")
    else:
        print("Não é um triângulo retângulo.")
else:
    print("Não é possível formar um triângulo.")