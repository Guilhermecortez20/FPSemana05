# Criar uma conta bancária
conta = ContaBancaria("João Silva", 1000.0, 500.0)

# Depositar um valor
conta.depositar(200)  # Saída: 1
conta.depositar(-50)  # Saída: 0

# Levantar um valor
conta.levantar(300)  # Saída: 1
conta.levantar(1500) # Saída: 0

# Exibir o saldo atual
conta.exibir_saldo()  # Saída: 900.00

# Exibir as informações da conta
conta.exibir_info()  # Saída: "João Silva 900.00 500.00"
