---
layout: post
title: 'Vue-router'
main-class: 'dev'
date: 2016-06-30 11:36:50 
color: '#637a91'
tags: vue-js vue-router single-page-application
layout: post
author: vitor-arjol
---

A característica mais marcante de uma ***Single Page Application*** é a velocidade. Os elementos de interface já estão presentes e quando sua estrutura de servidor é bem montada (web service para prover os dados), a sensação que o usuário tem ao usar a aplicação é a de que a ela está instalada no próprio computador, tão rápida que é a resposta.

Um componente essencial de uma SPA é o **Router** que é responsável por mostrar/esconder um ou mais elementos dependendo da URL que se acessa no browser. Esta é sua única responsabilidade, o que não significa que seja uma ferramenta simples!

Este artigo tem por objetivo mostrar como configurar o **Vue-router**: um add-on para o Vue.js, desenvolvido pela própria equipe de desenvolvimento do Vue e que se integra de forma nativa à sua aplicação.

Como aplicação exemplo será criado um novo projeto utilizando o Vue-cli, ferramenta de linha de comando que permite criar um esqueleto de projeto Vue. Caso nunca tenha visto sugiro ler o [excelente artigo](http://www.vuejs-brasil.com.br/crie-rapidamente-um-projeto-vue-com-vue-cli-e-browserify/) publicado por **Daniel Schmitz** neste mesmo blog.

#### Criação do Projeto

Assumindo que você já tenha todas as ferramentas instaladas (node.js, npm e vue-cli) basta estar numa pasta do sistema e executar `vue init webpack-simple nome-do-projeto`.

![](/content/images/2016/06/Screen-Shot-2016-06-30-at-7-53-40-AM.png)

Após responder às 4 perguntas sobre o projeto, basta acessar a pasta com `cd nome-do-projeto` *(substituindo nome-do-projeto pelo nome que você tenha escolhido, claro)* e executar `npm install`. Ao final da instalação, é preciso instalar o Vue-router, pois este não é instalado por padrão na criação do projeto com o Vue-cli: `npm install --save-dev vue-router`.

> Todos os arquivos ficarão armazenados na pasta **/node_modules** e estarão a disposição dos seus arquivos do projeto para import

Ao abrir no seu editor predileto o arquivo ```/src/main.js``` você verá a estrutura básica de um Vue object:

```javascript
import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: 'body',
  components: { App }
})
```

Preste atenção em **App** pois este será nosso componente pai de todos os demais componentes que venham a fazer parte de nossa aplicação.

#### Configuração do Vue-router

Antes de iniciarmos a configuração, precisamos de pelo menos 2 componentes para haver alguma navegação. Assim, basta criar na pasta ```/src``` **ComponenteA.vue** e **ComponenteB.vue**. Em cada um deles basta adicionar um trecho HTML que os diferencie:

```html
<template>
    <h1>Componente A</h1>
</template>
```

```html
<template>
    <h1>Componente B</h1>
</template>
```

Agora, voltando ao ```/src/main.js``` iniciaremos a configuração do Vue-router:

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router' // << aqui
import App from './App.vue'

Vue.use(VueRouter) // << e aqui

new Vue({
  el: 'body',
  components: { App }
})
```

Neste ponto apenas importamos o Vue-router diretamente da pasta **node_modules** e notificamos o Vue de sua presença.

Agora, importaremos ambos os componentes que farão parte da aplicação...

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import ComponenteA from './ComponenteA.vue'
import ComponenteB from './ComponenteB.vue'

Vue.use(VueRouter)

new Vue({
  el: 'body',
  components: { App }
})
```

... e então partimos para a configuração do router:

```javascript
...
Vue.use(VueRouter)

const router = new VueRouter()

router.map({
    '/componente-a': {
        component: ComponentA
    },
    '/componente-b': {
        component: ComponentB
    },
})

new Vue({
...
```

Dentro do objeto passado para o método **map()** mapeamos as URLs aos componentes a serem mostrados. Agora, precisamos adaptar nosso App.vue para que receba o componente indicado pela URL em seu corpo e o exiba:

**Remova tudo o que o Vue-cli tiver colocado em App.vue** e adicione o HTML abaixo:

```html
<template>
    <div>
        <router-view></router-view>
    </div>
</template>
```

A tag especial ```<router-view>``` trazida pelo Vue-router será o local onde os componentes mapeados serão adicionados. Nada impede que você adicione outros elementos HTML ao App.vue. Por exemplo: uma barra de navegação na sua aplicação pode ser adicionada ali!

O último passo é substituir a criação do Vue object pelo router.start(). Esta parte costuma confundir os iniciantes, pois a criação do Vue object passa a ser feita de forma implícita pelo Vue-router:

```javascript
...

router.map({
    '/componente-a': {
        component: ComponentA
    },
    '/componente-b': {
        component: ComponentB
    },
})

router.start(App, '#container')
...
```

Perceba que o método start() associa o componente principal da aplicação (o que contém a tag ```<router-view>```) a um elemento do DOM. Onde está este elemento? Ainda não existe mas será agora criado em **/index.html**:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>route</title>
  </head>
  <body>
    <div id="container">
        <router-view></router-view>
    </div>
    <script src="dist/build.js"></script>
  </body>
</html>
```

Perceba o div de id container. Dentro dele também há um ```<router-view>``` e esta é a manha para que se possa usar um componente .vue como inicializador do Vue-router. Na documentação oficial se pede para que se crie um componente Vue genérico com esta finalidade. Mas isso não é necessário e você pode continuar usando a estrutura que está acostumado.

Veja abaixo o arquivo main.js completo:

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import ComponenteA from './ComponenteA.vue'
import ComponenteB from './ComponenteB.vue'

Vue.use(VueRouter)

const router = new VueRouter()

router.map({
    '/componente-a': {
        component: ComponentA
    },
    '/componente-b': {
        component: ComponentB
    },
})

router.start(App, '#container')
```

Para finalizar basta voltar ao terminal e executar `npm run dev` e então, no seu browser predileto, acessar ```http://localhost:8080/#!/componente-a``` e ```http://localhost:8080/#!/componente-b```.

Este é apenas um setup inicial básico e para uma aplicação real esta configuração será armazenada numa pasta dedicada a ela. Isso por que a quantidade de rotas pode crescer de forma indefinida, dependendo de quantos componentes e quantas funcionalidades sua aplicação tiver.

Por fim, o link para a documentação oficial do Vue-router: [http://router.vuejs.org/en/index.html](http://router.vuejs.org/en/index.html).
