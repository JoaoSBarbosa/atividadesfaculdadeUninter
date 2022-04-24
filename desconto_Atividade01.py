# 1. Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
# 2. Entre com a quantidade desse produto;
# 3. O programa deve retornar o valor total sem desconto;
# 4. O programa deve retornar o valor total após o desconto;
# 5. Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
# 6. Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 10 und.
# (para mostrar que o desconto foi aplicado)

print()

# Identificação pessoal
print('-' * 15, ' Bem-vindo a loja do João da Silva Barbosa', '-' * 15, ' \n')

# Entrada de dados
valor = float(input(' Digite o valor do produto: R$ \n '))

# If- para capturar valores abaixo de R$ 1,00
if valor > 0:
    qtd = int(input(' Digite a quantidade do produto: \n '))
    # If- para capturar qtd abaixo de R$ 1,00 antes de processar
    if qtd > 0:

        # processamento
        if qtd > 9:
            if (qtd >= 10 and qtd < 100):
                valorT = qtd * valor
                des = 0.05 * valor
                valorFinal = (valor - des) * qtd
                perc = ' (desconto de 5%)'

            elif (qtd > 99 and qtd < 1000):
                valorT = qtd * valor
                des = 0.1 * valor
                valorFinal = (valor - des) * qtd
                perc = ' (desconto de 10%)'

            elif (qtd >= 1000):
                valorT = qtd * valor
                des = 0.15 * valor
                valorFinal = (valor - des) * qtd
                perc = ' (desconto de 15%)'
            # Saída para o usuário
            print(' \n O valor sem desconto foi: R$ R$ {:.2F} \n O valor final com desconto foi: R$ {:.2F} {}'.format(
                valorT,
                valorFinal, perc))

        # Saída para compras sem desconto
        else:
            valorT = qtd * valor
            print(' Quantidade comprada: {} \n Valor total R$ {}'.format(qtd, valorT))

    # Saída para valores errados inseridos
    else:
        print('\n Quantidade inválida')
else:
    print(' \n Valor inválida')
