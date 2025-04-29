import os
os.system("cls || clear")

def desconto_inss(valor_salario):
    if valor_salario <= 1320.00:
        inss = valor_salario * 0.075
    elif valor_salario <= 2571.29:
        inss = valor_salario * 0.09
    elif valor_salario <= 3856.94:
        inss = valor_salario * 0.12
    elif valor_salario <= 7507.49:
        inss = valor_salario * 0.14
    else:
        inss = 1051.05

    return inss

def desconto_imposto_de_renda(valor_salario, dependente):
    dependentes = dependente * 189.59
    calculo = valor_salario - dependentes

    if calculo <= 2112.00:
        imposto_de_renda = 0.0
    elif calculo <= 2826.65:
        imposto_de_renda = calculo * 0.075
    elif calculo <= 3544.00:
        imposto_de_renda = calculo * 0.15
    elif calculo <= 4256.00:
        imposto_de_renda = calculo * 0.225
    else:
        imposto_de_renda = calculo * 0.275

    return imposto_de_renda

def desconto_vale_transporte(salario_base, optou_vt):
    return salario_base * 0.06 if optou_vt.lower() == 's' else 0

def desconto_vale_refeicao(valor_vr):
    return valor_vr * 0.20 

def desconto_plano_de_saude(dependentes):
    return dependentes * 150.00

print("=== Acesse seus dados ===")
matricula = int(input("Digite sua matrícula: "))
senha = int(input("Digite sua senha: "))
print("Acesso concedido!\n")

print("=== Solicitando dados ===")
valor_salario = float(input("Digite seu salário: R$ "))
dependentes = int(input("Digite a quantidade de dependentes: "))
transporte = input("Deseja receber vale transporte (S/N)?: ")
refeicao = int(input("Digite o valor do vale-refeição fornecido pela empresa: R$ "))

inss = desconto_inss(valor_salario)
imposto_de_renda = desconto_imposto_de_renda(valor_salario, dependentes)
vale_transporte = desconto_vale_transporte(valor_salario, transporte)
vale_refeicao = desconto_vale_refeicao(refeicao)
plano_de_saude = desconto_plano_de_saude(dependentes)

descontos = inss + imposto_de_renda + vale_transporte + vale_refeicao + plano_de_saude
salario_liquido = valor_salario - descontos

print("\n==== FOLHA DE PAGAMENTO ====")
print(f"Salário base: R$ {valor_salario}\n")
print(f"Desconto INSS: R$ {inss:.2f}")
if imposto_de_renda == 0:
    print("Desconto Imposto de Renda: Isento")
else:
    print(f"Desconto Imposto de Renda: R$ {imposto_de_renda:.2f}")
print(f"Desconto vale-transporte: R$ {vale_transporte:.2f}")
print(f"Desconto vale-refeição: R$ {vale_refeicao:.2f}")
print(f"Desconto Plano de Saúde: R$ {plano_de_saude:.2f}\n")
print(f"Salário líquido: R$ {salario_liquido:.2f}")