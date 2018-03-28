---
layout: post
title: 'Como publicar artigos no nosso blog'
date: 2018-03-28 11:45:46 
tags: blog markdown publicar
author: daniel-schmitz
---

Nessa semana nós migramos o Blog para Jekyll, que integrado ao Github permitirá que qualquer pessoa possa publicar artigos. O processo de publicação é baseado no que chamamos de PR, que é o Pull Request do Git. Vamos, nesse artigo, mostrar o passo a passo de como fazer isso.

## Pré requisitos

Tudo que o que você precisa para escrever um artigo para o Blog é possui um conta no [GitHub](https://github.com). É perfeitamente possível usar somente o site github para escrever o artigo. 

Existem outra formas como, por exemplo, realizar o clone do nosso blog no seu sistema operacional, executar o jekyll em linha de comando para ver o site, realizar o Pull Request via linha de comando. Mas optamos, nesse momento, em usar somente o GitHub.

## Fork

Apos criar a sua conta é necessário fazer o que chamamos de *fork*, que é uma cópia de todo o blog para a sua conta. Para fazer isso, acesse [https://github.com/vuejs-br/blog](https://github.com/vuejs-br/blog) e clique no botão `fork`, conforme a imagem a seguir:

<p align="center">
<img src="https://i.imgur.com/5eXjh5q.png">
</p>

Após realizar o fork, todo o blog estará vinculado a sua conta, como se fosse um projeto seu.

## Website

É interessante configurar o seu fork para que ele possa ser visto também como um site web, assim você poderá ver como o seu artigo está formatado dentro no site. Para realizar esta configuração, acesse o item `Settings` do projeto:

<p align="center">
<img src="https://i.imgur.com/dHZdc9q.png">
</p>

E navegue até o item *Github Pages*. Em *source*, escolha `master branch` e clique no botão `save`. A página será carregada e você verá uma informação sobre o endereço do seu blog "espelho". No meu caso, apareceu isso:
Após a criação dessa entrada, você deverá se lembrar da chave, nesse caso hipotético, o `fulano-silva`.

<p align="center">
<img src="https://i.imgur.com/oZwzM3w.png" border="1">
</p>

Para você, surgirá uma url diferente, mas que quando acessada, irá exibir o blog Vuejs Brasil na sua conta.

## Verifique se você já é autor

É a primeira vez que você publica no site? Já pulicou? Essas informações estão configuradas no arquivo `_config.yml`. Acesse-o e encontre o item `authors`. Verifique se o seu nome está nas entradas e caso não encontre, crie uma seguindo as regras de formatação, e preenchendo todos os campos, se possível. 

> Toda a edição do arquivo pode ser feita no próprio GitHub. Basta clicar no arquivo e clicar em edit. Edite-o e clique em Save

Lembre que, para inserir uma nova entrada, a sua "chave" deve ser diferente das outras. Usamos a chave no formato:

- Seu nome e sobrenome 
- Tudo em minúsculos
- Sem espaços
- Sem acentos
- Use hífen para espaços

Supondo que seu nome seja "Fulano Silva", uma entrada válida seria:

```yml
fulano-silva:
    name: Fulano Silva
    email: fulanosilva@gmail.com
    gravatar: HASH DO GRAVATAR
    description: Eu sou o fulano silva
    web: http://fulanosilva.com
    location: Fulanópilis
    facebook: fulanosilva
    twitter: fulanosilva
```


## Configurando a sua imagem com gravatar

Para configurar o seu avatar (imagem), é necessário configurar a entrada do gravatar, que pode ser criada no site [gravatar.com](http://www.gravatar.com). Perceba que existe um *hash* para cada usuário. No site do gravatar, após criar a sua conta e fornecer uma imagem, você poderá obter este hash e adicioná-lo aqui.

## Criando o artigo

Para criar o artigo, é necessário adicionar um arquivo markdown no diretório `_posts`. Este arquivo deverá possuir um nome com o formato válido, com as seguintes regras:

1. Data de publicação do arquivo no formato: YYYY-MM-DD
2. Título do artigo (ou algo bem similar), seguindo as seguintes regras:
    - Tudo em minúsculo
    - Espaços são substituídos por hífen
    - Não acentuar  

3. A extensão do arquivo deve ser `.md`

Um exemplo válido seria:

```
2018-03-28-como-integrar-o-vue-com-php.md
```

> Você pode usar o próprio GitHub para criar o arquivo. Basta clicar na pasta `_posts` e clicar no link `Insert New File`. 

Após criar o arquivo, devemos configurá-lo adicionando algumas informações no início do arquivo. Você pode usar o seguinte modelo:


```yaml
---
layout: post
title: 'O título do artigo'
date: a data nesse formato: 2018-03-19 11:45:46 
tags: tags separadas por espaço
author: a chave que referencia sua configuração de autor
---
```

O campo layout é fixo, e deve ter o valor `post`. Os outros campos podem ser alterados de acordo com o seu artigo. O ideal é criar um bom título para que o SEO seja bem aplicado. As tags também são importantes, mas o título é o fator principal se o seu artigo irá aparecer na primeira página do google ou não.

Um bom título deve conter pelo menos as palavras chave que compõe o artigo.

O campo `author` é a chave que irá ligar o seu artigo ao autor do arquivo `_config.yml`. Lembra do Fulano Silva? Neste caso teríamos: `author: fulano-silva`

Por exemplo, a configuração deste artigo é:

```yaml
---
layout: post
title: 'Como publicar artigos no nosso blog'
date: 2018-03-19 11:45:46 
tags: blog markdown publicar
author: daniel-schmitz
---
```

## Escrevendo o artigo

Após  configuração inicial você pode iniciar a escrita, que deve seguir os padrões de um documento markdown. Esta linguagem é extremamente simples de usar e você não necessitará se preocupar com formatação. Use apenas Markdown e seu artigo ficará bem formatado visualmente. 

Para aprender um pouco mais sobre MarkDown, acesse este link.

Rapidamente, podemos resumir a sua marcação da seguinte forma:

```markdown

Títulos:

# Título
## Sub Título
### Sub Sub Título

Links:

[texto do link](url do link)
[link interno](#link-interno)

Imagens:

![](url da imagem)

ps: Recomendamos o imgur.com para hospedar suas imagens

Listas:

- Item 1
- Item 2
- Item 3

Listas Numeradas:

1. Item 1
2. Item 2
3. Item 3

Pra código no meio do texto, use aspas invertidas. Por exemplo:

A variável `$foo` irá fazer armazenar o nome...

Para colar um código inteiro, você pode usar a seguinte marcação: 



```

## Publicando o seu artigo

Após escrever o artigo, você poderá enviá-lo para o nosso Blog oficial, através de uma ação chamada Pull Request. Esta ação significa que o que você comitou para o seu github será aplicado na conta original do nosso Blog, que é onde o *fork* foi feito originalmente.

O Github mostra a informação do seu progresso em relação ao fork na página do projeto, incluindo o link para que você fazer o Pull Request:

<p align="center">
<img src="https://i.imgur.com/aIJPpkD.png">
</p>

Ao clicar no link `Pull Request`, surge uma página mostrando suas alterações e um botão verde `Create Pull Request`. Ao clicar nele, o GitHub irá analisar se o Pull Request está Ok para se integrar ao repositório original. Caso esteja, basta adicionar um comentário e clicar em `Create Pull Request`.

<p align="center">
<img src="https://i.imgur.com/7eHUKoJ.png">
</p>

Após realizar o PR, basta aguardar a aprovação de um dos nossos moderadores.


