#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print (files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()
passphrase = "secretkey"
upassword = input("Digite a senha para descriptografar os arquivos: ")
if upassword == passphrase:
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		content_decrypt = Fernet(secretkey).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(content_decrypt)
		print("Seus dados foram recuperados!")
		print("Agora você pode acessar normalmente os seus dados.")
else:
	print("Entre com a senha correta!")

