msg = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(msg))
print('Só tem espaços? {}'.format(msg.isspace()))
print('É um número? {}'.format(msg.isnumeric()))
print('É alfabético? {}'.format(msg.isalpha()))
print('É alfanumérico? {}'.format(msg.isalnum()))
print('Está em maiúscula? {}'.format(msg.isupper()))
print('Está em minúscula? {}'.format(msg.islower()))
print('Está capitalizada? {}'.format(msg.istitle()))
print('É um digito? {}'.format(msg.isdigit()))
print('É um identificador? {}'.format(msg.isidentifier()))
print('É imprimivel? {}'.format(msg.isprintable()))



