print('ola')

notas = [10, 9, 8, 7]


def media(array):
  total = 0
  media = 0
  for nota in array:
    total = total + nota
  media = total / 4

  if(media < 5): 
    print('Reprovado')
  else:
    print('Aprovado')

print(media(notas))


cont = 0

while(cont <= 10):
    cont += 1
    print(cont)