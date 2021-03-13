---
layout: post
title: 'Code splitting com Vue.js e Webpack'
main-class: 'dev'
date: 2017-09-07 14:17:16 
color: '#637a91'
tags: vue-js vue-js2 vue code-splitting import webpack
author: halfeld
---

Se pararmos para ver como fazemos aplicações hoje me dia acabamos notando que separamos o nosso código front-end (me refiro ao javascript nesse caso) em varios arquivos o que facilita a manutenção, e com ajuda de ferramentas como [Webpack](https://webpack.github.io/) e [Browserify](http://browserify.org/) e até mesmo o [gulp-concat](https://www.npmjs.com/package/gulp-concat), fazemos a união desses arquivos para ficar todos em um só, porque entendemos que varios _requests_ para buscar vários arquivos era ruim e deixava lento o carregamento da página.

Mas a chegada do [HTTP 2](https://en.wikipedia.org/wiki/HTTP/2) com funcionalidades como [Server push](http://blog.caelum.com.br/http2-server-push-na-pratica/) perdemos a necessidade de fazer coisas como a união do código js em um arquivo `main` só e outras coisas que eram levadas em conta antes com o HTTP 1.1.

Com a união de varios arquivos em um só, ainda mais com a complexidade e a quantidades de libs js que usamos temos o problema:

![foto do networking do chrome mostrando o tamanho do arquivo js](/content/images/2017/09/main-qimg-925bb293d17759f5be2a515db66eb4ae.jpg)

O problema agora é que o usuário vai baixar o arquivo js para **todas** as páginas da SPA de uma vez, mesmo sem ter acessado a página antes.

==_Code splitting_ é a ideia de quebrar esse arquivo main em varios arquivos permitindo o usuário baixar somente o que ele precisa==

Por exemplo se olharmos para essa app assim, podemos ver o que não era preciso carregar logo de primeira.

![mostrando partes da página que não precisavam ser carregadas logo de primeira](/content/images/2017/09/main-qimg-f8582b538693fdc8a418c4a08c84f870.jpg)

A grande questão é, e se atrasarmos o carregamento dessas partes até depois do render inicial? o usuário conseguiria uma interação muito mais rápida.

## Async components

A chave para fazer code splitting no Vue são os async components. Estes caras são os componentes que por sua definição são carregados assincronamente.

Vamos declarar um componente usando o `component` API (`Vue.component(name, definition)`). Ao invés de termos um objeto como segundo argumento, os async components tem uma função. Esta função tem duas notáveis features:

1. É meio que um wrapper de uma Promise, tal que tem o argumento `resolve`.
2. É uma _factory function_, tal que retorna um objeto, só que neste caso a definição do componente.

``` js
Vue.component('async-component', (resolve) => {
  resolve({
    template: '<div>Async Component</div>',
    props: [ 'myprop' ]
  });
});
```

Esses async components são apenas o primeiro step para o code splitting porquê agora temos que implementar o mecanismo para haver a troca de código da nossa app.


## Dynamic module loading

Nós também precisamos de uma ajuda do ~~brother~~ webpack. Vamos separar nosso componente em um modulo ES6:

_AsyncComponent.js_
```js
export default {
  template: '<div>Async Component</div>',
  props: [ 'myprop' ]
}
```

Como a gente poderia carregar isso assincronamente? ficariamos tentados a fazer isso:

```js
import AsyncComponent from './AsyncComponent.js'`;
Vue.component('async-component', AsyncComponent);
```

Porém isso é estático e é resolvido em tempo de execução. O que precisamos é uma maneira de carregar isso durante a app rodando se quisermos ter os benefícios do code splitting.

## import()

Atualmente não é possível carregar dinamicamente o arquivo de modulo com javascript, Existe, entretanto, uma função que consegue fazer isso para nós, ainda em [proposal](https://github.com/tc39/proposal-dynamic-import) para o ECMAScript chamada `import()`.

O Webpack já tem uma implementação para o `import()` que lida com o code splitting, colocando o modulo de request separado quando o bundle é criado (um _chunk_ na verdade, mas pense como um arquivo separado por hora).

`import()` recebe como argumento o nome do arquivo e retorna uma Promise. Aqui esta como carregamos o modulo acima:

_main.js_
```js
import(/* webpackChunkName: "async-component" */ './AsyncComponent.js')
  .then((AsyncComponent) => {
    console.log(AsyncComponent.default.template);
    // Output: <div>Async Component</div>
  });
```

> Caso você esteja usando o Babel, você vai precisar adicionar o plugin `syntax-dynamic-import` para ele conseguir parsear a sintaxe.

Agora quando você der build no projeto irá receber a notícia que um modulo apareceu como arquivo próprio:

![agora existem dois arquivos sendo carregados](https://qph.ec.quoracdn.net/main-qimg-44d748e3f9118ae3be2ddfe1d19a13a1.webp)


## Dynamic component loading

Tendo em mente que o `import()` retorna uma Promise, podemos unir isso com a feature async component do Vue. O Webpack vai fazer o bundle do async component separadamente e injetar via AJAX quando o componente for necessário.


_main.js_
```javascript
import Vue from 'vue';
 
Vue.component('async-component', (resolve) => {
  import('./AsyncComponent.js')
    .then((AsyncComponent) => {
      resolve(AsyncComponent.default);
    });
});
 
new Vue({ 
  el: '#app' 
});
```

_index.html_
```html
<div id="app">
  <p>This part is included in the page load</p>
  <async-component></async-component>
</div>
<script src="bundle.main.js"></script>
```

Quando o `main.js` rodar, irá acontecer um request automaticamente para o componente, isso porquê a implementação do `import()` para o Webpack vai carregar o module via AJAX!

Caso o AJAX chamado retorna sucesso e o modulo retornado, a Promise se resolve e o componente pode ser renderizado, então o Vue vai renderizar a página de novo:

```html
<div id="app">
  <p>This part is included in the page load</p>
  <div>Async Component</div>
</div>
```

Aqui esta um diagrama que pode ajudar você a entender:

![resultado final no html](/content/images/2017/09/main-qimg-dfd2c3bb4b891173d3c92573cd37e004.png)

## Single file components

Beleza, mas como eu uso o code splitting com os Single file components?
É incrível como fica ainda mais simples!

_AsyncComponent.vue_
```html
<template>
  <div>Async Component</div>
</template>

<script>
  export default {
    props: [ 'myprop' ]
  }
</script>
```

E a sintaxe fica ainda mais idiota...

```javascript
new Vue({ 
  el: '#app',
  components: {
    AsyncComponent: () => import('./AsyncComponent.vue')
  }
});
```

## Conclusão

Beem.... legal, sabemos o que é code splitting, sabemos como fazer no Vue com Webpack usando de duas formas, tanto com o `Vue.component` quando com os Single File Component, mas como eu faço uma arquitetura de uma aplicação pensando nisso?

Acho que a forma mas óbvia de pensar é separando por página, por exemplo, ter bundlers separados para uma página home e para uma página about.

Mas existem outras formas, como fazer o code splitting de qualquer componente que não é necessariamente mostrado na hora como por exemplo, tabs, modals, dropdown, menus, etc...

Então é isso pessoal, e vamos discutir o assunto nos comentários!

## Referências

+ https://vuejsdevelopers.quora.com/Code-Splitting-With-Vue-js-And-Webpack
+ https://webpack.github.io/docs/code-splitting.html
+ https://webpack.js.org/guides/code-splitting/
+ https://router.vuejs.org/en/advanced/lazy-loading.html
