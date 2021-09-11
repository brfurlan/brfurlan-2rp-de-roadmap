#!/bin/bash
# DESCRIÇÃO: executar.sh. Dentro deste arquivo, se executam as funções lista_arquivos e insere_texto do arquivo funcoes.sh
# SINOPSE: meuscript [OPÇÕES]
# AUTOR: Bruno Ramalho Furlan
# EXEMPLO DE USO: ./executar.sh /home/usuario/Downloads/pasta/  mensagem


#Chamando arquivo funcoes.sh
source funcoes.sh

#fazendo loop para inserir texto no final de cada elemento do vetor
cnt=${#lista[@]}
for ((i=0;i<cnt-1;i++)); do
	insere_texto
	echo ${lista[i]}
done




