---
layout: post
title: 'Testando sua aplicação Vue.js'
main-class: 'dev'
date: 2016-07-18 13:12:25 
color: '#637a91'
tags: vue-js testes tdd bdd
layout: post
author: jjsquad
---

Testes de software já são uma realidade no nosso dia-a-dia de desenvolvedor, mas ainda existe uma parte que acham besteira fazer levantando umas justificativas como perda de tempo, curva de aprendizado(já que o estilo de programar muda).
Mas ele...

![I'm a devil necessary](http://i.imgur.com/s50RqBn.gif)

### Dependências e Configurações

Ao invés de fazer o famoso exemplo de quando se esta explicando testes, a incrível soma de dois números o.O, vamos começar testando uma aplicação pequena, um projetinho que tenho no meu [github](https://github.com/Halfeld/v-notes) com Vue.

Para fazer os testes vou utilizar o [karma](https://karma-runner.github.io/1.0/index.html) como Test Runner, o [jasmine](http://jasmine.github.io/) como Framework de testes e o [PhantonJS](http://phantomjs.org/) como Browser.

Primeiro vamos instalar as dependências e iniciar o nosso arquivo `karma.conf.js`

```sh
npm install karma karma-webpack karma-jasmine jasmine-core karma-phantomjs-launcher phantomjs --save-dev
```

```javascript
// Fizemos a requisição da configuração do webpack e deletamos a entrada do arquivo 
var webpackConfig = require('./webpack.config.js');
delete webpackConfig.entry

// karma.conf.js
module.exports = function (config) {
  config.set({
    browsers: ['PhantomJS'],

    frameworks: ['jasmine'],

    files: [
      'test/index.spec.js'
    ],

    // Vamos enviar os testes para o bundle
    preprocessors: {
      'test/index.spec.js': ['webpack']
    },
    
    // Usando a configuração do Webpack
    webpack: webpackConfig,
    
    // Evitar paredes de informações 
    webpackMiddleware: {
      noInfo: true
    },

    autoWatch: true,

    singleRun: true
  })
}
```

você pode tanto copiar essa configuração ou dar um `karma init`, só não esquece de instalar ele globalmente ;)

### Testes

Vamos fazer um teste para o método de `start` dentro do meu arquivo `App.vue`, como esse projeto mexe com localStorage, quero me certificar que ele vai armazenar o objeto base.

Dentro do arquivo `index.spec.js` na pasta `test` colocaremos o seguinte: 

```javascript
var App = require('./../src/App.vue');

describe('Local Storage', function () {

  beforeAll(function() {
    App.methods.start();
  });

  afterAll(function() {
    localStorage.clean();
  });

  it('Should create object base on localStorage', function() {
    expect(localStorage.getItem('vNotes')).toBeDefined();
  });
});
```

Simplesmente, chamamos o método dentro do arquivo `App` e em um `it` verificamos se foi criado certo.

E agora, como nesse projeto é usando o [Vuex](https://github.com/vuejs/vuex), vamos testar as `mutations`. Caso você não tem ideia de como usar o Vuex e não tem a mínima noção do que é, dá um confere [nesse](http://www.vuejs-brasil.com.br/vuex/) post deste mesmo Blog.

Para fazer isso, é exatamente a mesma coisa, olha só:

```javascript

var Vue = require('vue');
var App = require('./../src/App.vue');
var Mutations = require('./../src/vuex/mutations').default;

describe('Local Storage', function () {

  beforeAll(function() {
    App.methods.start();
  });

  afterAll(function() {
    localStorage.clean();
  });

  it('Should create object base on localStorage', function() {
    expect(localStorage.getItem('vNotes')).toBeDefined();
  });

  it('Should set note on store', function() {
    var store = {
      note: ''
    };
    Mutations.SET_NOTE(store, 'testing');
    expect(store.note).toEqual('testing');
  });

  it('Should set search engine on store', function() {
    var store = {
      search: ''
    };
    Mutations.SET_ENGINE_SEARCH(store, 'testing');
    expect(store.search).toEqual('testing');
  });

  it('Should add note on localStorage', function() {
    var store = {
      note: {
        name: 'hello',
        text: 'world',
        date: ''
      }
    };
    Mutations.ADD_NOTE(store, '123123');
    expect(JSON.parse(localStorage.getItem('vNotes')).notes[0]).toBeDefined();
  });

  it('Should not add note on localStorage if already exists', function() {
    var store = {
      note: {
        name: 'hello',
        text: 'world',
        date: '123123'
      }
    };
    Mutations.ADD_NOTE(store, '123123');
    expect(JSON.parse(localStorage.getItem('vNotes')).notes[0]).toBeDefined();
  });
});
```

outra coisa que podemos testar e que nesse exemplo não vi necessidade, é os valores em componentes.
Como nesse exemplo na documentação:

```javascript
var Vue = require('vue');
var ComponentA = require('../../src/components/a.vue');

Vue.config.silent = true;

describe('a.vue', function () {

  it('should have correct message', function () {
    expect(ComponentA.data().msg).toBe('Hello from Component A!')
  })

  it('should render correct message', function () {
    var vm = new Vue({
      template: '<div><test></test></div>',
      components: {
        'test': ComponentA
      }
    }).$mount()
    expect(vm.$el.querySelector('h2.red').textContent).toBe('Hello from Component A!')
  })
})
```

Aqui eu só adicionei a linha `Vue.config.silent = true` para não amostrar no console os _warnings_ do Vue caso venha a aparecer.

Perceba no primeiro teste que eu acessei o método data para verificar se o atributo correspondia a algum valor, é praticamente o jeito que eu estava fazendo com as `mutations`, e no segundo teste eu instânciei o Vue para colocar o `ComponentA` e iniciei ele com o `$mount()` já que não colocamos o atributo `el` na instância.

O modo como eu acesso as propriedades é entrando em `vm.$el` para ele me retornar o template e usar o `querySelector` para pegar o que eu quero, simples assim :D

Bem é isso aí pessoal, como vocês viram testar uma aplicação Vue é super simples!
