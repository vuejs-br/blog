---
layout: post
title: 'Conheça o Vuetify com este tutorial'
date: 2018-04-02 09:00:00 
tags: componentes vuetify css 
author: daniel-schmitz
---

O Vuetify é um framework responsivo em Vue, baseado no Material Design. Já possui uma boa gama de componentes e uma documentação sólida. Neste artigo iremos conhecê-lo através de um tutorial completo, criando uma pequena aplicação para ler dados de uma conta no GitHub.

## Comunidade

Já temos um grupo próprio do Vuetify em português no [Telegram](https://t.me/vuetifybr). Além deste grupo, temos toda uma [comunidade br](https://github.com/vuejs-br/comunidades) do Vue no qual você pode participar! 

## Criando a aplicação

Precisamos basicamente do Node, versão 8 ou superior, e de um editor de textos como o Visual Studio Code. Com tudo isso pronto, podemos criar o projeto Vuetify escolhendo os mais diversos templates existentes:

<p align="center">
<img src="https://i.imgur.com/ApVRDTu.png">
</p>

Vamos usar o template **Webpack**, criando o projeto através do seguinte comando:

```bash
npx vue-cli init vuetifyjs/webpack vuetifyproject
```

Responda as perguntas e aguarde todas as dependências serem instaladas. Após isso, acesse o diretório do projeto e execute `code .` para abrir o Visual Studio Code, e `npm run build` para executar o projeto no modo desenvolvedor. O navegador será aberto com o design do projeto semelhante a este:

<p align="center">
<img src="https://i.imgur.com/GAJJzxz.png">
</p>

No caso acima, estou usando a extensão para o Google Chrome chamada [Vue DevTools](https://github.com/vuejs/vue-devtools) que exibe diversas informações sobre a instância Vue do projeto. A esquerda podemos ver o Vuetify em ação, já com um menu flutuante, uma barra de títulos, um menu flutuante na parte direita, e um rodapé.

## Estrutura de diretórios

Sempre que eu estou estudando um novo framework, gosto de analisar bem a estrutura de diretórios que ele trabalha. Com isso terei a base necessária para expandir o meu sistema criando os componentes no lugar certo, além de conhecer suas limitações. Conhecer bem o framework antes de utilizá-lo em um projeto real é fundamental para o sucesso do seu projeto.

<p align="center">
<img src="https://i.imgur.com/KOcJvtx.png">
</p>


