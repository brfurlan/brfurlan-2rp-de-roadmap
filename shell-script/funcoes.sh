#!/bin/bash
# DESCRIÇÃO: funcoes.sh. Dentro deste arquivo, estão as funções lista_arquivos e insere_texto
# SINOPSE: meuscript [OPÇÕES]
# AUTOR: Bruno Ramalho Furlan
# XXX: usando o comando "find /home/bruno/Downloads/ -type f  > lista.list" era gerado o caminho inteiro dos arquivos, \
# mas na função só se mostrava o caminho para os arquivos depois do diretório 


# Iniciando função lista_arquivos
# Usei essa linha de comando abaixo para inserir o diretório em cada elemento do vetor
inicio=$1
# Mudando para diretorio home
cd ~
# Mudando para diretorio
cd $inicio
function lista_arquivos(){
	lista=()
	diretorio=$1
	while IFS=  read -r -d $'\0'; do
	   lista+=("$REPLY")
	done < <(find $diretorio -type f -print0)

	#Arrumando elementos do vetor para mostrarem o caminho completo
	cnt=${#lista[@]}
	for ((i=0;i<cnt;i++)); do
		lista[i]="${inicio}${lista[$i]:2}" 
	done

}

#Chamando função
lista_arquivos $diretorio


# Iniciando função insere_texto
# Usei essa linha de comando abaixo para inserir o diretório em cada elemento do vetor
str=$2
# Função insere_texto 
insere_texto(){
	lista[i]="${lista[$i]}${str}"
}

#Chamando função
insere_texto 


	


