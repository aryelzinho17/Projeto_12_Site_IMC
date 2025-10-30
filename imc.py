try:
    peso =  float(input('digite o seu peso: '))
    altura = float(input('digite a sua altura: '))

    imc = (peso / (altura ** 2))

    print(f"seu IMC e: {imc:.2f}")

    if imc < 18.5:
        print("voce esta abaixo do peso.")
    elif imc >= 25:
        print("peso normal.")
    elif imc >= 30:
        print("sobrepeso.")
    else:
        print("obesidade.")

except:
    print("voce digitou um valor invalido.use apenas nusmeos")