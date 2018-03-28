---
layout: post
title: 'Como publicar artigos no nosso blog'
main-class: 'dev'
date: 2018-03-19 11:45:46 
tags: blog vuejsbrasil
layout: post
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

<p align="center">
<img src="https://i.imgur.com/oZwzM3w.png" border="1">
</p>

Para você, surgirá uma url diferente, mas que quando acessada, irá exibir o blog Vuejs Brasil na sua conta.

## Verificar se você já é autor


