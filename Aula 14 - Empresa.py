num_emp = int(input("Digite o numero de empresas: "))
num_mes = int(input("Digite o numero de meses: "))
emp = 1
lucro_total = 0
pat = float(input("Quanto vale a empresa? "))
relaçao_pat_luc = 0

while emp < num_emp:
    mes = 1
    print("Empresa %d: " %emp)
    while mes < num_mes:
        print ("Mes %d: " %mes)
        ganho = float(input("Digite o ganho da empresa no mes: "))
        gasto = float(input("Digite o gasto da empresa no mes: "))
        saldo = ganho - gasto
        if saldo > 0:
            print ("A empresa teve um lucro de %4.2f: " %saldo)
            lucro_total += saldo
        elif saldo < 0:
            print ("A empresa teve um prejuízo de %4.2f:" %saldo)
            lucro_total += saldo
        else:
            print("O saldo foi zero! ")
        mes += 1
    print ("O lucro total foi de %4.2f" %lucro_total)
    relaçao_pat_luc = (pat/lucro_total)*100
    print ("A percentagem em relação ao patrimônio é de %.2f" % relaçao_pat_luc)
    emp += 1
