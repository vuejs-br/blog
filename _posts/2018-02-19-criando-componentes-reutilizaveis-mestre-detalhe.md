---
layout: post
title: 'Criando componentes reutilizáveis (mestre/detalhe)'
main-class: 'dev'
date: 2018-02-19 16:19:42 
description: derscricao
color: '#637a91'
tags: vue
 - componentes
 - props
 - event
 - composicao
 - slots
layout: post
introduction: introducao
---

Quando trabalhamos com componentes, seja em qualquer framework (com vue fica mais divertido!), estamos utilizando um dos requisitos mais básicos da programação que é dividir um problema em diversos problemas menores. Neste caso, dividimos uma interface em pedaços, e a montamos como se fosse um lego. O uso de componentes é vital para um perfeito entendimento de um sistema, pois seria humanamente impossível criar todo um sistema em apenas um arquivo. 

> Recomendo a leitura do artigo [Pensando em web componentes](http://www.vuejs-brasil.com.br/aplicacoes-com-vuejs-pensando-em-componentes/) para você compreender melhor a filosofia do conceito

Dentre as diversas utilizadas da criação de componentes, temos a reutilização do mesmo em diversas partes do sistema, podendo inclusive agrupar componentes em uma hierarquia mestre/detalhe, como no esboço a seguir.

![Exemplo de composição](https://user-images.githubusercontent.com/1509692/36111809-898257f8-100e-11e8-9d03-afba649bbae9.png)

O que temos nesta imagem é a distinção entre dois tipos de componentes. O primeiro, que chamamos de "formulário pai" - em cinza - contém alguns elementos como o título do formulário e os botões *Save* e *Clear*. Dentro deste formulário, temos o "formulário filho" - em branco - que contém os campos do mesmo. Se imaginarmos um sistema relativamente complexo, teremos dezenas de formulários que possuem um design muito similar, com algum elementos da tela sendo os mesmos. A partir desta necessidade, podemos criar um componente padrão, que conteria as seguintes particularidades:

- Uma barra de título
- Uma caixa de informação contendo um texto qualquer (por exemplo, um help)
- O lugar onde os controles de formulário seriam incluídos (chamamos de slot)
- Um botão save
- Um botão clear

Quando este componente estiver pronto, ele poderá ser usado para desenhar diversas telas que contém formulários, sendo que você necessitará apenas incluir os campos do formulário, sem se preocupar com demais funcionalidades. 

## Objetivo deste artigo

Criar um componente capaz de agrupar algumas funções similares dos formulários, como uma barra de títulos, o botão salvar, etc. O esboço a seguir ilustra como o componente será:

![image](https://user-images.githubusercontent.com/1509692/36112419-be216dc6-1010-11e8-8011-9c7b2d41a9d7.png)

## Preparando o projeto

Pode-se aplicar todos os conceitos que serão aprendidos aqui em um projeto existente. Mas neste exemplo de projetos iremos criar algo do zero, através do `vue-cli`. Primeiro, certifique-se de possuir o Node na versão 8 ou superior, e também o `npx`, para que não seja necessário instalar o `vue-cli` no seu sistema. Criaremos o projeto com o seguinte comando:

```
npx vue-cli init webpack myproject
```

Use as opções padrão do template, pois elas são importantes para um projeto de média escala. Apesar de estarmos apenas demonstrando uma funcionalidade, é interessante já conhecer tudo que o template webpack tem a oferecer (como ESLInt, Nightwatch etc).

Após a criação do projeto, abra ele no seu editor de textos predileto. Eu recomendo o Visual Studio Code. Nossa primeira tarefa é executar o comando `npm run dev` e verificar se o navegador abre com o projeto em execução, como na imagem a seguir:

![image](https://user-images.githubusercontent.com/1509692/36112858-1baa2b8a-1012-11e8-9b1a-20df1ef3bc2a.png)

## Instalando um CSS Framework

Você pode instalar qualquer tipo de CSS Framework (Bulma, Material, Boostrap) ou UI Toolkit (iView, Vuetify). Neste artigo usaremos Bulma, mais precisamente o **Buefy**, um port do Bulma para o Vue. Para instalá-lo, digite:

```
npm i -S buefy
```

Após a instalação, ele estará disponível no *node_modules*. Preciamos apenas configurá-lo no Vue, alterando o arquivo `src/main.js` para:

<script src="https://gist.github.com/danielschmitz/360eb90fc78755fc853ee4dfad0ef67d.js"></script>

Adicionamos 3 linhas ao arquivo. Primeiro, o `import Buefy from 'buefy'` para importar o Buefy que está no diretório `node_modules`. Logo abaixo incluímos o CSS do Buefy (necessário em qualquer framework css), e finalmente usamos `Vue.use(Buefy)` para importar o Buefy no Vue.

## Alterando um pouco a estrutura do projeto

Quando usamos o template do webpack, temos a seguinte estrutura de projeto:

![](https://user-images.githubusercontent.com/1509692/36113490-201ce2d2-1014-11e8-8d5a-c3bc4e243c24.png)

O arquivo principal do projeto é o `main.js`, o mesmo que incluímos o Buefy. O arquivo `App.vue` é o componente principal da aplicação, que possui o seguinte código:

<script src="https://gist.github.com/danielschmitz/4c0b5fe5828db3e78aff3ee071741d1f.js"></script>

A mudança que iremos realizar aqui é:

- Remover o logotipo
- Remover o `<style>` 
- Trocar `<div>` para `<section>`

No final, teremos:

<script src="https://gist.github.com/danielschmitz/42b9d1f2ba849de61be4978643cc9b2e.js"></script>

O arquivo `App.vue` possui agora apenas o `router-view`, que é onde o Vue Router irá carregar os componentes de acordo com a rota estabelecida. Trocamos também o `<div>` por `<section>` para se adequar ao padrão do Buefy.

Neste artigo iremos utilizar a rota padrão do `HelloWorld.vue`, que pode ser observada no arquivo `src/routes/index.js`. 

Para finalizar, abra o arquivo `HelloWorld.vue` e altere para:

<script src="https://gist.github.com/danielschmitz/07c6238bdd7601e7bad9cac4d1dda6fa.js"></script>

Removemos o código html que exibia algumas informações sobre o Vue, trocamos o `<div>` por `<section>` e removemos o `<style>`. No final, temos a app com a seguinte interface:

![image](https://user-images.githubusercontent.com/1509692/36114073-10ba3b6c-1016-11e8-9efa-a6c97cd3ca85.png)

## Criando o componente FormBox

O componente *FormBox* já possui o seguinte esboço:

![image](https://user-images.githubusercontent.com/1509692/36112419-be216dc6-1010-11e8-8011-9c7b2d41a9d7.png)

Para criar o componente, crie o arquivo `FormBox.vue` em `src/components`, inicialmente com o seguinte código:

<script src="https://gist.github.com/danielschmitz/642713efaa1dacab28b40800115aab82.js"></script>

Vamos agora alterar o `HelloWorld.vue` incluindo o componente recém criado `FormBox.vue`. Veja:

<script src="https://gist.github.com/danielschmitz/0f75bd91b18eb4c864ca47b768493cc8.js"></script>

Para incluir um componente em outro componente, é necessário realizar 3 procedimentos:

1. Realizar o import do componente na seção `<script>`
2. Adicionar o componente na propriedade `components` da instância Vue
3. Adicionar o componente na seção `<template>` usando [kebab case](https://br.vuejs.org/v2/guide/components.html#camelCase-vs-kebab-case). Ou seja, `FormBox` se torna `<form-box>`

O resultado até o momento é algo semelhante a figura a seguir:

![image](https://user-images.githubusercontent.com/1509692/36152377-04b50f94-10b2-11e8-9056-d9cd3379fe12.png)

Acima, temos o texto do componente `FormBox`, e podemos também ver o Vue DevTools, uma extensão para o Google Chrome (tem para firefox também). No DevTools, pode-se ver a hierarquia de componentes. 

## Configurando o componente FormBox

Agora que já criamos o componente `FormBox` e já o incluímos no `HelloWorld.vue`, podemos codificá-lo de forma que fique semelhante ao que propomos.

Primeiro, criamos o código reaproveitando o exemplo encontrado no [Buefy](https://buefy.github.io/#/documentation/message), veja:

<script src="https://gist.github.com/danielschmitz/61f95551bb0e42053b46637714dfff52.js"></script>

Então temos que, a princípio, realizar a comunicação entre o componente pai e o componente filho. Por exemplo, o título do *FormBox* não pode ser fixo, quem o determina é o componente *HelloWorld*. Configuramos isso através de uma funcionalidade do Vue chamada **props**.

## Configurando o título do FormBox

Para incluir uma propriedade no componente filho, usamos a propriedade `props` na instância do Vue, da seguinte forma:

<script src="https://gist.github.com/danielschmitz/34bf2604b442839f2860dcadb57f3665.js"></script>

Alteramos o código em duas partes. Primeiro, adicionamos `:title='title'` no componente `bMessage` do Buefy. Você já deve saber que o uso do : antes da propriedade é um atalho para `v-bind`. A outra alteração é na instância, incluindo a propriedade `title` através do `props`. Se estiver com dúvidas sobre o `props`, leia a [documentação](https://br.vuejs.org/v2/guide/components.html#Passando-Dados-com-Propriedades).

Voltando ao componente `Hello World`, podemos alterá-lo para:

```html
 <form-box title="Hello Form Box"></form-box>
```

Perceba que agora passamos a propriedade `title` do pai para o filho, realizando a comunicação (pausa para aplausos)

Até agora temos o seguinte resultado (veja no Vue DevTools a propriedade *title*):

![image](https://user-images.githubusercontent.com/1509692/36154863-e1d610ec-10b9-11e8-8d1e-24ec4e1fdae7.png)

## Configurando o campo de mensagem do FormBox

Assim como fizemos no `title`, vamos configurar a propriedade `message` que irá aparecer logo abaixo do título.

Primeiro, a criamos no `FormBox.vue`:

<script src="https://gist.github.com/danielschmitz/43e8364fae8147f0ec858f7d29c470e1.js"></script>

Além de adicionar a propriedade no `props`, a referenciamos da seguinte forma:

```html
<b-tag type="is-warning" v-show="message">{{message}}</b-tag>
```

Usamos o componente bTag do Buefy, junto com uma checagem se a propriedade foi definida através do `v-show`. 

Voltando ao componente `HelloWorld.vue`, podemos adicionar a propriedade `message` da seguinte forma:

```html
<form-box title="Hello Form Box" message="A help message"></form-box>
```

Com isso, teremos o seguinte resultado:

![image](https://user-images.githubusercontent.com/1509692/36180401-698e91d8-1107-11e8-8382-509280b2d6fa.png)

## Adicionando os botões Save e Clear

Em nossa especificação, o componente FormBox possui dois botões: *Save* e *Clear*. Estes botões estarão no componente, mas quem deve cuidar da lógica no *click* de cada botão é o componente pai que está usando o FormBox. Assim, podemos ter vários FormBox na aplicação, mas o que acontece quando se clica no botão será responsabilidade do componente pai.

O Vue trbalha com eventos de forma bastante simples, através dos métodos `$emit` (disparar evento) e `on` (receber evento).

Primeiro, vamos adicionar o botão `Save` e o botão `Clear` ao FormBox:

<script src="https://gist.github.com/danielschmitz/e3b2de42888a4b3ce485c0f354c33609.js"></script>

Neste código, temos o uso do `@click` no botão `Save` (poderia ser `v-on:click`) e no próprio parâmetro da propriedade repassamos o `$emit`. Já no botão `Clear`, apenas para diferenciar (use de acordo com o que achar melhor), chamamos o método `onClearClick` que está definido na propriedade `methods` da instância Vue do componente. Neste método, usamos `this.$emit('clear')`.

Perceba que a responsabilidade do que vai acontecer no clique do botão é do pai, não do componente. Então, para finalizar, vamos voltar ao `HelloWorld.vue` e adicionar tais funcionalidades.

<script src="https://gist.github.com/danielschmitz/9099ee35f696d0e9b0d74d194cf8231a.js"></script>

Aqui temos a forma como capturar os eventos e chamar seus respectivos métodos. Perceba que temos `v-on:save="onSave"` e `@clear="onClear"`, sendo que o segundo é o atalho do primeiro (@ é atalho para v-on). Os respectivos métodos apenas disparam um `alert` indicando o botão que foi clicado, veja:
 
![image](https://user-images.githubusercontent.com/1509692/36181217-1190c31c-110b-11e8-86cd-cc8e4e8163cd.png)

## Compondo o componente mestre/detalhe

Todo o nosso componente FormBox foi elaborado para ser reutilizável. Ou seja, se o objetivo é criar apenas uma casca do nosso formulário, deverá haver uma área onde será possível adicionar campos de caixa de texto, de seleção, etc (lembre-se do mockup lááá em cima).

O Vue trabalha com o conceito de *slots*, onde é possível embutir um conteúdo de um componente em outro. 

Para compreender melhor, vamos alterar o componente FormBox.vue para:

<script src="https://gist.github.com/danielschmitz/f0b7677532f5f20eeacf5c6bcf80df13.js"></script>

O que fizemos foi adicionar `<slot></slot>` após o `<b-tag>` e antes do `<hr/>`. Com isso, estamos dizendo que, tudo que estiver entre `<form-box>` e `</form-box>` deverá ser embutido no *slot*. 

Voltando ao `HelloWorld.vue`, podemos configurar o `<form-box>` da seguinte forma:

<script src="https://gist.github.com/danielschmitz/2ee1ffcf8a53a50b754c7527e1536623.js"></script>

Aqui realizamos algumas modificações:

1. Incluímos dois campos dentro da tag `<form-box>`
2. Adicionamos as variáveis `name` e `email` na propriedade `data` da instância do componente Vue. Estas propriedades estão ligadas às duas caixas de texto através do `v-model`
3. Alteramos o método `onSave` incluindo a informação dos campos digitados.

As testar a aplcação, temos a seguinte tela:

![image](https://user-images.githubusercontent.com/1509692/36181750-54b6b4b0-110d-11e8-98f6-4ccbcd4df249.png)

Agora uma outra pausa para os aplausos!! Criamos com o Vue um componente que pode ser reutilizado em diversas partes da sua aplicação, sendo que somente o "miolo" será controlado pelo componente pai.

Se você tiver alguma dúvida, fique a vontade em perguntar nos comentários abaixo.

Este projeto está no github: https://github.com/danielschmitz/vue-componente-composicao

Você pode acessar o demo do projeto aqui: http://danielschmitz.com.br/vue-componente-composicao/#/



 







 


