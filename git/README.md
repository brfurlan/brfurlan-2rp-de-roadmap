# Anotações sobre  o git- Bruno Ramalho Furlan
#

## Configurações Básicas

Para se criar um repositório local

1. Cria-se a pasta;
2. Usam-se os comandos:

```sh
git config --global user.name <seu nome>
git config --global user.email <seu e-mail>
git init 
```
## Comandos básicos

Para ver se há alguma mudança no reposítório

```sh
git status
```


Para adicionar arquivos prontos para versionar

1. Todos os arquivos:
```sh
git add --all
git add .
```

2. Um arquivo específico:
```sh
git add <nome do arquivo>
```
Realizando commits
**Sem o commit a mudança não é salva**

1. Comum:
```sh
git commit -m "<mensagem>"
```
2. Adicionar tudo e fazer o commit:
```sh
git commit -a -m "<mensagem>"
```

Ver as diferenças de versões (commits)

```sh
git diff
```

Ver versões

```sh
git log
```

Removendo  tag do servidor

```sh
git push --delete origin <nome da tag>
```

ver lista de commits antigos

```sh
git --oneline
```

Ir para versão anterior

```sh
git checkout <chave da versão>
```

Reverter ações

```sh
git reset --hard
```

Para ignorar arquivo no reopositório ao se fazer commit deve-se criar uma arquivo .gitignore utilizando o ccomando ren no Windows e mv no Linux


## Criando um repositório remoto

1. Criei um repositório https://github.com/brfurlan
2. Clico em em repositeries>New
3. Nomeio e preencho as informações
4. Copio os comandos para a clonagem no repósitório local:

```sh
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin <endereço do repositório>
git push -u origin main
```

Para criar um repositório no servidor para uma pasta local   

```sh
git remote add origin <endereço do repositório>
git branch -M main
git push -u origin main
```
Existem outros servidores como o BitBucket que ele utiliza autenticações em 2 fatores e chaves SSH.

Funcionalidades do github:

- Fork- Copia um repositório externo parao o seu repositório;
- Star- Acompanha mudanças em um repositório externo;
- Watch- ver mudanças de um repositório;
- issues- Relatar ocorrrências ou erros;
- Labels- Define informações e mostra os status das issues;
- Milestones- marco determinaddo para resolver a issue;
- Branch- Versões utilizadas para desenvolver funcionalidades isoladas da versão principal (*master/main*);
- Pull requests- quando se envia a sua versão ao servidor (*branch*) para a avaliação;
- Merge-Juntar duas branches.

Mandar mudanças do repositório local para o servidor

```sh
git push
```

Atualizar  mudanças do repositório do servidor para o repositório local

```sh
git pull
```

### Branches

**No servidor basta clicar em criar uma branch e nomeá-la.**

Criando uma branch local

```sh
git branch <nome da branch>
```

Ver lista de branches

```sh
git branch
```
**Em verde aparece a branch em que você está**

Indo para uma branch localmente

```sh
git checkout <nome da branch>
```

Criando uma branch e indo para ela localmente

```sh
git checkout -b <nome da branch>
```

Removendo  branch localmente

```sh
git branch -d  <nome da branch>
git branch -D  <nome da branch>
```
**O último código serve para forçar a exclusão**

Subir branch local para o servidor 

```sh
git push -u origin <nome da branch>
```
Remover branch do servidor 

```sh
git push --delete origin <nome da branch>
```

Mudar nome de branch local 

1. Estando na branch que vai mudar de nome
```sh
git branch -m  <nome novo da branch>
```

2. Estando em outra branch
```sh
git branch -m  <nome antigo da da branch><nome novo da branch>
```

**Não é possivel renomear a branch no servidor, e preciso mudar o nome da branch localmente que se quer renomear e apagar a branch do servidor, e depois voltar ao nome original localmente e fazer o push novamente da branch**

Atualizar branch do repositório

```sh
git pull  <endereço repositório><nome da branch>
```

### Merge

**Sempre deve-se fazer o pull do repositório antes do merge**

1. Entra-se na branch que vai receber a merge com a outra branch;
2. Digita-se o comando:
```sh
git merge <nome da branch que se quer mergear>
```
**Caso haja algum conflito com algum arquivo abra ele no Visual Studio Code e escolha a alteração que se que que prevaleça. Em seguida, realize o mesmo comando anterior**

**Existem softwares domo o Kdiff3 que realizam o merge de forma gráfica.**

### Tags

**As tags mostram a versão em que se quer ddestacardo projeto**


Criando tag localmente

```sh
git tag -a  <nome da tag> -m "<mensagem>"
```

Fazendo push da tag para o servidor

```sh
git push origin  <nome da tag> 
```

Entrando na tag

```sh
git checkout  <nome da tag> 
```

**Evitar** fazer commit em tag, se for fazer aparecerá um código do commit, para não perdê-lo use

```sh
git checkout  -b <nome da tag> <código do commit da mensagem>
```

Removendo  tag localmente

```sh
git tag -d  <nome da tag>
git tag -D  <nome da tag>
```

**O último código serve para forçar a exclusão**

Removendo  tag do servidor

```sh
git push --delete origin <nome da tag>
```

Fazer tag em commits antigos

```sh
git log --oneline
git log -a <nome da tag> <código da versão copiado da lista de versões que se quer fazer a tag>
```

### Stash

**O stash é quando se quer salvvar mudanças na branch sem fazer o commit**

Fazendo stash

```sh
git stash save -m "<mensagem>"
```

Listando stashes

```sh
git stash list
```

**Os stashes vão aparecer do mais rrecente para o mais antigo**

Aplicando stash

1. Último stash (mas mantem o stash na lista)
```sh
git stash apply
```

2. Último stash (mas apaga os stash da lista)
```sh
git stash pop
```

Ir para um stash antigo

```sh
git stash drop @<numero de satashes para pular>
```

## Outras funcionalidades

Desfazer commit

```sh
git reset --hard HEAD-<quantidade de commits para desfazer>
```
**Não dá para desfazer commits no servidor**

Adicionar mudanças em um commit

```sh
git add .
git commit --amend -m "<mensagem>"
```

Se não for utilizado o comando **-m** na última linha de código, aparecerá uma janela para a mensagem. Escreva a mensagem e aperte a tecla *"Esc"* e escreva **:wq**  e aperte a tecla *"Enter"*

### Fetch
A soma dos comandos fetch e merge é igual ao comando pull. O comando *git fetch* Usado para trazer atualizações ao repositório local. Mas já existem nos servidores ffuncionalidades para editar permissõess de branch. 

### Rebase

O comando *git rebase* tem as mesmas funcionalidades que o *git merge*, mas ele faz com que os commits das branches  se tornem uma linha.

### Alias

Usado para fazer uma "abreviação" de comandos

Fazer alias

```sh
git config --global alias.<nome do alias> <comando que se quer fazer um alias> 
```

Desfazer alias

```sh
git config --global unset alias.<nome do alias>  
```

### Listar endereços

Comando para listar endereços de repositórios

Listando endereços

```sh
git -V
```

### Grep

Comando para achar branches que começam com determinados caracteres

Fazer grep

```sh
git branch | grep  <caracteres iniciais>          
```

## Informações finais

Para ver as branches de forma gráfica pode-se usar os softwares Sourcetree e Git Kraken. Os programas Visual Studio Code e Android Studio também tem funcionalidades que auxiliam na utilização do git.
