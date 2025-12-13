#leia uma cidade com espaços usando strip() e nisso dizendo que tal cidade é "SANTO" usando upper() para deixar o nome em maiúsculo
cidade = str(input("Digite uma cidade: ")).strip()
print(cidade[:5].upper() == 'SANTO')