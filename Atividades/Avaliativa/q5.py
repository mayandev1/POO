def placa_antiga_valida(placa):
    # AAA-1234
    if len(placa) != 8:
        return False

    if placa[3] != '-':
        return False

    letras = placa[:3]
    numeros = placa[4:]

    return letras.isalpha() and letras.isupper() and numeros.isdigit()

def placa_mercosul_valida(placa):
    # AAA1A23
    if len(placa) != 7:
        return False

    parte1 = placa[:3]   
    parte2 = placa[3]    
    parte3 = placa[4]    
    parte4 = placa[5:]   

    return (
        parte1.isalpha() and parte1.isupper() and
        parte2.isdigit() and
        parte3.isalpha() and parte3.isupper() and
        parte4.isdigit()
    )

def validar_placa(placa):
    if placa_antiga_valida(placa):
        return "Placa válida | Modelo Antigo"
    elif placa_mercosul_valida(placa):
        return "Placa válida | Mercosul"
    else:
        return "Placa inválida"

placa = input("Digite a placa: ")

print(validar_placa(placa))