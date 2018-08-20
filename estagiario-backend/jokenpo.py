# Teste estagio-backend Buscapé
# Juiz de Jo-ken-pô

armas = ('pedra', 'papel', 'tesoura')

print('Armas: Pedra, Papel ou Tesoura')
p1 = input('Jogador 1, escolha sua arma: ')
p2 = input('Jogador 2, escolha sua arma: ')

if p1 == 'Pedra':
	if p2 == 'Pedra':
		print('Empate!')
	elif p2 == 'Papel':
		print('Jogador 2 venceu!')
	elif p2 == 'Tesoura':
		print('Jogador 1 venceu!')
	else:
		print('Jogador 2 escolheu opção inválida. Tente novamente')

elif p1 == 'Papel':
	if p2 == 'Papel':
		print('Empate')
	elif p2 == 'Pedra':
		print('Jogador 1 venceu!')
	elif p2 == 'Tesoura':
		print('Jogador 2 venceu!')
	else:
		print('Jogador 2 escolheu opção inválida. Tente novamente')

elif p1 == 'Tesoura':
	if p2 == 'Papel':
		print('Jogador 1 venceu!')
	elif p2 == 'Pedra':
		print('Jogador 2 venceu!')
	elif p2 == 'Tesoura':
		print('Empate!')
	else:
		print('Jogador 2 escolheu opção inválida. Tente novamente')
else:
	print('Opção inválida, tente novamente.')


