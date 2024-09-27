print("*************SEJA BEM VINDO(A)!*************")
print("\n")

menu = f"""
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
"""
saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3
saldo_e_extrato = saldo and extrato

while True:
  opcao = input(menu)
  if opcao == "d":
    print("Depósito")
    valor_depositado = float(input("\nInforme o valor a ser depositado: "))
    if valor_depositado > 0:
      saldo += valor_depositado
      extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
    else:
      print("Digite um valor válido.")  

  elif opcao == "s":
    print("Saque")
    valor_sacado = float(input("\nInforme o valor que deseja sacar: "))
    if valor_sacado >0 and valor_sacado <= saldo and valor_sacado <= 500 and numero_saques < LIMITE_SAQUES:
      print(f"Saque de R$ {valor_sacado:.2f} realizado com sucesso.\n")
      saldo -= valor_sacado    
      extrato += f"Saque: R$ {valor_sacado:.2f}\n" 
      numero_saques += 1

    elif valor_sacado > saldo:
      print(f"Não foi possível realizar a operação pois o valor de R$ {valor_sacado:.2f} é superior ao saldo em sua conta")

    elif valor_sacado > 500:
      print(f"O valor informado para saque de {valor_sacado:.2f} é superior ao seu limite diário de R$ 500.00.")

    elif numero_saques >= LIMITE_SAQUES:
      print("Você extrapolou o limite diário para transações de saque")

    else:
      print("Operação falhou. O valor informado é inválido.")
    
  elif opcao == "e":
    print("\n==================Extrato==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================================")

  elif opcao == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
  
print("*************Agradecemos pela preferência!*************")





