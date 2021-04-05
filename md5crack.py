import hashlib

print('''

██████╗  ██████╗  ██████╗██╗  ██╗ ██████╗ ██████╗  ██╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔═████╗██╔══██╗███║
██║  ██║██║   ██║██║     █████╔╝ ██║██╔██║██║  ██║╚██║
██║  ██║██║   ██║██║     ██╔═██╗ ████╔╝██║██║  ██║ ██║
██████╔╝╚██████╔╝╚██████╗██║  ██╗╚██████╔╝██████╔╝ ██║
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═╝
  
	''')

lista=input("wordlist: ")##WORDLIST
hash2crack=input("hash: ")##HASH

linhasDeLista=open(lista, "r").readlines()

for i in range(0, len(linhasDeLista)):
	hash2comp=hashlib.md5(linhasDeLista[i].replace("\n","").encode()).hexdigest()
	if hash2crack == hash2comp:
		print("Senha Encontrada: " +linhasDeLista[i].replace("\n",""))
		exit()
print("Senha Não Encontrada")
