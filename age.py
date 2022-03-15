age = int(input("How old are you?\n"))
    # Coleta somente a primeira parte do número
calc = age // 10 
    # Coleta somente a segunda parte do número
years = age % 10
    # Concatena as strings e os textos.
print("You are " + str(calc) + " decades and " + str(years) + " years old.")