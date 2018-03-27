---
layout: post
title: 'Vue.js para desenvolvedores AngularJS – Parte 2 (Components e states)'
main-class: 'dev'
date: 2016-07-20 11:14:48 
color: '#637a91'
tags: vue-js web-components angular
layout: post
author: 5
---

[Lógica de templates (Parte 1)](http://www.vuejs-brasil.com.br/vue-js-para-desenvolvedores-angularjs-parte-1-logica-de-templates/)  
[Componentes e Estados (Parte 2)]() - Atual  
Comunicação de componentes (Parte 3) - em breve  
Métodos de lifecycle (Parte 4) - em breve  
Demais e não menos importantes (Parte 5) - em breve

## Componentes
Componentes em AngularJS são um tipo especial de *diretiva*, utiliza configurações que se adequa a sua aplicação baseada em componentes de maneira simples. Não encontro comumente esse tipo de aplicação com AngularJS, porem, está vindo como arquitetura padrão na sua versão mais recente AngularJS 2.

O Vue.js é especialmente feito pensando em componentes, então nos fornece uma forma poderosíssima de gerenciá-los. Possibilitando uma estrutura de aplicações modernas e reutilizáveis.

#### Criando um componente
No AngularJS os componentes são registrados através `.component()`, que é um método de um módulo Angular.

```language-javascript
// AngularJS
// Controller principal
angular
  .module('myApp')
  .controller('mainCtrl', function () { ... });

// Registrando
angular.module('myApp').component('greeting', {
  controller: function () {
    ...
  },
  template: '<h1>Bem vindo ao Vue.js Brasil. lol</h1>'
});
```
```language-html
// html
<div ng-controller="mainCtrl as ctrl">
  <greeting></greeting>
</div>
```

**Já o Vue.js disponibiliza diversas formas de registrar componentes.**  
Registrando com o `Vue.extend({})`, o mesmo cria um tipo uma subclasse da instância Vue base e que contém as opções de um componente.
```language-javascript
// Vue.js
// Estendendo
var greeting = Vue.extends({
  template: '<h1>Bem vindo ao Vue.js Brasil</h1>'
  // ... outras opções
})

// Registrando
Vue.component('greeting', greeting)

// Instância base
new Vue({
  el: '#app'
})
```
```language-html
// html
<div id="app">
  <greeting></greeting>
</div>
```
<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/spy443j4/3/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Para facilitar, você pode estender e registrar diretamente nas opções do objeto no `Vue.component({})`. O Vue.js automaticamente chamará o `Vue.extend()`.

```language-javascript
Vue.component('greeting', {
  template: '<h1>Bem vindo ao Vue.js Brasil</h1>'
})
```

<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/t2mhzd16/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Outra forma e a que mais recomendo é utilizar arquivos únicos para cada componente (single file componentes), são arquivos com a extensão `.vue`. Essa forma nos ajuda a segmentar os componentes e estruturar a aplicação para uma maior organização e manutenibilidade. 

> Nesse caso usamos o Webpack ([vue-loader](https://github.com/vuejs/vue-loader)) ou o Browserify ([Vueify](https://github.com/vuejs/vueify)) para construir os componentes.


![](/content/images/2016/07/componentes-vue.png)


## Estado inicial de componentes
Em ambos é simples a maneira de iniciar com dados para que possamos utilizar no componente.

```language-javascript
angular.module('myApp').component('greeting', {
  controller: function () {
    this.blog = 'Vue.js Brasil'
  },
  template: '<h1>Bem vindo ao {{ $ctrl.blog }}</h1>'
})
```
*Declarar no controller utilizando o `this` e não se esquecer de utilizar o `$ctrl` antes de cada propriedade (variável) no template.*

O [Vue.js](https://vuejs.org/) também é simples de se iniciar com dados e ele disponibiliza uma opção chamada `data`, para que possamos declarar propriedades iniciais de nosso componente, dando o poder da reatividade do Vue.js.

```language-javascript
Vue.component('greeting', {
  data: function () {
    return {
      blog: 'Vue.js Brasil'
    }
  },
  template: '<h1>Bem vindo ao {{ blog }}</h1>'
})
```

<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/esfo26kk/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

> O Vue recomenda declarar todas as propriedades reativas inicias na `data` option.

- Fazendo isso você evita de forçar o observador ficar reavaliando um dado que não foi iniciado, mas foi declarado posteriormente.

- Inicializando as propriedades na `data` option, você obtém maior desempenho na manipulação da mesma e com a propriedade já observada pelo Vue.

Esse serve somente de exemplo, não é uma boa prática:
<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/at9po88L/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Com esse ponto de partida, percebe-se que é muito simples começar a desenvolver componentes com Vue.js, na próxima parte falaremos sobre como passar dados para os componentes e o binding entre eles.

Valeu e até mais!





