def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interprete(imc):
    if imc < 18.5:
        print("IMC: ", imc, "- Peso insuficiente")
    elif imc < 25:
        print("IMC: ", imc, "- Peso normal")
    elif imc < 30:
        print("IMC: ", imc, "- Peso Sobrepeso")
    else:
        print("IMC: ", imc, "- Peso Obeso")

def main():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))

    imc = calcular_imc(peso, altura)
    interprete(imc)

if __name__ == "__main__":
    main()