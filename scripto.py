#!/usr/bin/python
# -*- coding: utf-8 -*-

texto=open("dicionario2.txt","r").read()
texto=texto.split('\n')
nova_lista = ''

i=0
while i<len(texto):
	
	if ("á" in texto[i]):
		nova_lista+=texto[i]+'\n'
	
	i+=1

arq_out = open("dicionario3.txt","w")
arq_out.write(nova_lista)

#close(texto)
close(arq_out)

#print(texto[1])