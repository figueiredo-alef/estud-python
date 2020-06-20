# Gerenciador de pagamentos

print('=' * 5, 'EX_044', '=' * 5)

print('{:=^40}'.format('LOJA FIGUEIREDO')) # KKKKKKKK MDS

total = float(input('Valor total da compra: R$'))

print('''Forma de pagamento:
[ 1 ] Pagamento à vista (espécie)
[ 2 ] Pagamento à vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] A partir de 3x no cartão''')

opcao = int(input('Informe a FORMA DE PAGAMENTO:'))

if opcao == 1:
    pagamento = total - (total * 10) / 100

elif opcao == 2:
    pagamento = total - (total * 5) / 100

elif opcao == 3:
    pagamento = total
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))

elif opcao == 4:
    numeroparcelas = int(input('Informe o número de parcelas:'))
    pagamento = total + (total * 10) / 100
    parcela = pagamento / numeroparcelas
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(numeroparcelas, parcela))

else:
    print('Opção inválida!')

print('A compra de R${:.2f} passa a custar R${:.2f} devido o método de pagamento.'.format(total, pagamento))
