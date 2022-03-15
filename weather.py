temperature = input("Digite o valor da temperatura atual.\n")

if int(temperature) >= 35:
    print("Está quente demais!")

elif int(temperature) <= 10:
    print("Está muito frio!")

else:
    print("A temperatura está agradável!")