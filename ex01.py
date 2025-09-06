#
# autor: Michel
# data: 06/09/2025

while True:
  
  # entrada de dados
  idade = int(input("Informe sua idade: "))

  # processamento
  if (idade >= 18):
    print("você é maior de idade!")
  else:
    print("você é menor de idade!")
    print("fechando o aplicativo!")
    break