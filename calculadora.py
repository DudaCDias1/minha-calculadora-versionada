#CALCULADORA
def somar (a, b):
    somar = a+b
    return somar
def subtrair (a, b):
    subtrair = a - b
    return subtrair
def multiplicar (a, b):
    multiplicar = a * b
    return multiplicar
def dividir (a, b):
    try:
        divisao = a / b
        return divisao
    # Tratamento de erro
    except ZeroDivisionError:
        return "Nenhum número pode ser dividido por 0"

# Loop para funcionar enquanto o usuário quiser
print ("Calculadora versionada")
while True:
    # Menu
    try:
        opcao = int(input("""
---- Menu de Opções ----
1. Somar
2. Subtrair
3. Multiplicar
4. Dividir
5. Sair
------------------------      
Digite sua escolha: """))
        if opcao > 0 and opcao < 6:
            # Opção de Saida
            if opcao == 5:
                print ("Bye.")
                exit()
            # Variaveis utilizadas
            num1 = float (input ("Insira um número: "))
            num2 = float (input ("Insira um número: "))
                
            # Escolha do Menu
            if opcao == 1:
                equacao = "soma"
                resultado = somar(num1, num2)
            elif opcao == 2:
                equacao = "subtraição"
                resultado = subtrair(num1, num2)
            elif opcao == 3:
                equacao = "multiplicação"
                resultado = multiplicar(num1, num2)
            else:
                equacao = "divisão"
                resultado = dividir(num1, num2)

            print (f"\nO resultado da {equacao}: {resultado:.2f}")
    
    # Tratamento de Erros    
        else:
            print ("\nOpção invalida. \nPor favor insira um número equivalente a opção desejada.\n")
        
    except ValueError:
        print ("\nInsira apenas números. Tente novamente\n")