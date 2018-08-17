from submarino import Submarino

comando = input('Exemplo de comando: RMMLMMDL\nEntre com a sequencia de comandos: ')
sub = Submarino()

print('Posição final:\n')
print(sub.movimentar(comando))