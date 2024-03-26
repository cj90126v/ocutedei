def Consulta_de_nome():

    nome = input("Digite seu nome" )

    if not nome:
        nome = "você"

    print(f"{nome} caso acerte ganhará um 1")



def A_B():

    A = int(input("digite um valor."))
    B = int(input("digite outro valor."))

    print(f"o primeiro valor é igual{B}. " )
    print(f"o segundo valor é igual{A}. " )

def CLT():

    salario = int(input(f"informe seu salário. "))
    aumento = int(input(f"idade do ANtonio Escobar"))

    reajuste = int(input("informe o aumento."))
    novo_salario = salario + reajuste

    print(f"{reajuste}")

escolha = int(input("Escolher um algo"))


CLT()
Consulta_de_nome()
A_B()