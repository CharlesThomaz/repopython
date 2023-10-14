# Obtenha os comprimentos dos três lados do triângulo
lado1 = float(input("Comprimento do primeiro lado: "))
lado2 = float(input("Comprimento do segundo lado: "))
lado3 = float(input("Comprimento do terceiro lado: "))

# Verifique se é possível formar um triângulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("É possível formar um triângulo com esses lados.")
else:
    print("Não é possível formar um triângulo com esses lados.")
