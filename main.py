print("ABPJ1 - CÁLCULO FINANCEIRO\n")

# Entradas receitas
salario = float(input("Informe seu Sálario:"))
receita_outros = float(input("Informe o valor de outras receitas:"))

# Entradas Despesas
valor_aluguel = float(input("Informe o valor do aluguel:"))
valor_alimentacao = float(input("Informe o valor gasto com alimentação:"))
valor_agua = float(input("Informe o valor do consumo de água:"))
valor_energia = float(input("Informe o valor do consumo de energia:"))
valor_lazer = float(input("Informe o valor gasto com lazer:"))
valor_cartao = float(input("Informe o valor gasto com cartão de crédito:"))
valor_outras_desp = float(input("Informe o valor das despesas adicionais:"))

#Somatoria despesas
somatoria_desp = (valor_aluguel + valor_alimentacao + valor_agua + valor_energia + valor_lazer + valor_cartao +valor_outras_desp)

#Somatorio receitas
somatoria_receitas = (salario + receita_outros)

#Calculo saldo atual
saldo_atual = (somatoria_receitas - somatoria_desp)

# Faz a comparação do saldo e imprime condição do saldo atual sem a meta
print("Situação do saldo atual sem o valor da meta!\n")
if saldo_atual < 0.00:
    print(f"Saldo Negativo R$ {saldo_atual:.2f}, você está no vermelho!")
elif saldo_atual == 0.00:
    print(f"Saldo zero, no limite")
else:
    print(f"Saldo Positivo R$ {saldo_atual:.2f}, você está no Azul")

#Apresenta Totais
print(f"Valor total receitas: R$ {somatoria_receitas:.2f}")
print(f"Valor total despesas: R$ {somatoria_desp:.2f}\n")

#Condição para calcular a meta s ou n
cond_meta = str(input("Deseja calcular a meta(s para SIM ou n para NAO):"))

if cond_meta == "s":

    #Entradas meta
    valor_meta = float(input("\nInforme o valor da meta que deseja alcançar:"))
    valor_mensal_meta = float(input("Informe o valor mensal que quer guardar:"))

    #Calculo meta 
    qtd_meses_meta = int(valor_meta // valor_mensal_meta)

    #Adiciona o valor da meta as despesas
    somatoria_desp = (somatoria_desp + valor_mensal_meta)
    saldo_atual = (somatoria_receitas - somatoria_desp)

    # Faz a comparação do saldo e Imprime condição do saldo atual com a meta
    print("\nSituação do saldo atual com o valor da meta mensal!\n")

    if saldo_atual < 0.00:
        print(f"Saldo Negativo de R$ {saldo_atual:.2f}, você está no vermelho!")
    elif saldo_atual == 0.00:
        print(f"Saldo zero, no limite")
    else:
        print(f"Saldo Positivo de R$ {saldo_atual:.2f}, você está no Azul")

    # Apreseta Meses  para atingimento para meta
    print(f"\nA sua meta de R$ {valor_meta:.2f} será atingida em {qtd_meses_meta} meses.")

    #Apresenta Totais com meta
    print(f"Valor total receitas: R$ {somatoria_receitas:.2f}")
    print(f"Valor total despesas com a meta: R$ {somatoria_desp:.2f}\n")
else:
    print("Cálculo realizado com sucesso. Programa finalizado!")

