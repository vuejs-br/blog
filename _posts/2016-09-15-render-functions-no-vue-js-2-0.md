---
layout: post
title: 'Render Functions no Vue.js 2.0'
main-class: 'dev'
date: 2016-09-15 13:23:27 
color: '#637a91'
tags: render-functions render functions vue-js vue-js2 vue vue2
layout: post
author: 6
---

Uma das coisas que vocês mais vão notar em questão de API no Vue 2 são as Render Functions, com a implementação do VirtualDOM meio que foi necessário essa abordagem de renderização.

## O que é o VirtualDOM?

Imagine que você vai renderizar sua interface feita em Vue com headers, inputs, buttons…, antes dessa interface ir para o DOM do browser ela passa por um DOM virtual que é um objeto javascript.
Assim sempre que houver mudança, o Virtual DOM vai rendenrizar para a representação virtual e fazer a comparação com a representação antiga(caso não esteja sendo renderizado pela primeira), vendo somente o mínimo que precisa ser mudado, e depois fazer a troca de só o que mudou no DOM do browser.

Então o VirtualDOM acaba sendo muito rápido porquê o DOM do browser é muito lento e a [hashtable](https://en.wikipedia.org/wiki/Hash_table) em javascript é uma das melhores.


## O que são as Render Functions?

Como o próprio nome diz, as funções de renderização  são as funções que vão renderizar algo para View.
Basicamente você recebe um parâmetro que é uma função, que a mesma deve ser retornada e executada com o componente principal como parâmetro.
 
Olhando o código que tudo fica mais fácil de entender:

```javascript
import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: '#app',
  render: h => h(App)
})
```

esse `h` que colocamos no parâmetro, na mais é do que um shorthand para `$createElement`, então não há problemas em renomear-lo(há uma exceção com o JSX, mas veremos mais a frente)

Além disso, no Vue 2 temos três formas diferentes de renderização, elas são:

+ Pela tag template
+ Por Hyperscript
+ Por JSX

Pela tag template, é como usamos antes, tendo o seu **Single File Component** que são aqueles arquivos com extensão `.vue`. Simplesmente deixando o código do `main.js` daquele jeito que amostrei acima e continuando escrevendo em seus arquivos `.vue`.

Por Hyperscript, que é uma forma que eu não acho que vai ser adotada por muitos, por sua dificuldade de manter o código, mas existe gente que vai curtir :P
Funciona da seguinte forma:

```javascript
import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: '#app',
  render (createElement) {
    return createElement('h1', {}, 'Hello World')
  }
})
```

> Note que mudei o nome do parâmetro para ficar mais didático, mas caso vá usar dessa forma, recomendo que faça isso também para melhorar a legibilidade ;)

a syntax do Hyperscrypt é a seguinte:

**createElement(`TAG_HTML`, `OPTIONS`, `ARRAY_DE_CHILDRENS_DO_HTML`)**

apesar do terceiro parâmetro ser os childrens do HTML, caso você não os tenha, é só passar a String que irá dentro do elemento, como foi o caso do exemplo acima.

então dando um exemplo mais complexo:

```javascript
import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: '#app',
  render (createElement) {
    return createElement('div', {
      attrs: {
        id: 'Igor'
      }
    }, [
      createElement('h1', 'I\'m a Title'),
      createElement('p', 'Fuck you title, nobody cares!'),
    ])
  }
})
```

assim como há uma exceção quanto ao terceiro parâmetro, há também em relação ao segundo que é o de opções, a exceção é que se você não precisa passar opções, simplesmente passe a String ou os childrens do HTML.

olhando as opções possíveis:

```javascript
{
  // Same API as `v-bind:class`
  'class': {
    foo: true,
    bar: false
  },
  // Same API as `v-bind:style`
  style: {
    color: 'red',
    fontSize: '14px'
  },
  // Normal HTML attributes
  attrs: {
    id: 'foo'
  },
  // Component props
  props: {
    myProp: 'bar'
  },
  // DOM properties
  domProps: {
    innerHTML: 'baz'
  },
  // Event handlers are nested under "on", though
  // modifiers such as in v-on:keyup.enter are not
  // supported. You'll have to manually check the
  // keyCode in the handler instead.
  on: {
    click: this.clickHandler
  },
  // For components only. Allows you to listen to
  // native events, rather than events emitted from
  // the component using vm.$emit.
  nativeOn: {
    click: this.nativeClickHandler
  },
  // Other special top-level properties
  key: 'myKey',
  ref: 'myRef'
}
```

Como você viu o exemplo acima, é idealmente isso, passa a tag HTML, as opções e os childrens.

Nesses exemplos estou usando só o arquivo `main.js`, mas se eu tivesse colocado no Single File Component, era só eu apagar a tag Template e retornar o template pela função render, assim:

```javascript
<script>
export default {
  data () {
    return {
      msg: 'Hello Vue 2.0!'
    }
  },
  render (createElement) {
    return createElement('div', {
      attrs: {
        id: 'Igor'
      }
    }, [
      createElement('h1', 'I\'m a Title'),
      createElement('p', 'Fuck you title, nobody cares !'),
    ])
  }
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}
</style>
```

e no meu `main.js`, deixar como o primeiro exemplo, assim:

```javascript
import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: '#app',
  render: h => h(App)
})
```

e o ultimo modo de renderizar algo, é por JSX, que é aquele paranauê de colocar HTML dentro do javascript

![No god please no!](/content/images/2016/09/giphy-1.gif)

então... tem uma galera aí que vai curtir :D

para usar o JSX você precisa instalar o plugin para o babel, o [babel-plugin-transform-vue-jsx
](https://github.com/vuejs/babel-plugin-transform-vue-jsx), assim:

```
npm install\
  babel-plugin-syntax-jsx\
  babel-plugin-transform-vue-jsx\
  babel-helper-vue-jsx-merge-props\
  --save-dev
```

e adicionar ele no seu `.babelrc`, assim:

```javascript
{
  "presets": ["es2015"],
  "plugins": ["transform-vue-jsx"]
}
```

agora você já pode ir escrevendo o seu JSX, mas com uma ou duas exceções.

amostrando código:

```javascript
import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: '#app',
  methods: {
    hello () {
      alert('Hello!')
    }
  },
  render (h) {
    return (
      <div>
        <h1 on-click={this.hello}>Hello from JSX</h1>
      </div>
    )
  }
})
```

> Dei de novo o exemplo no `main.js`, mas o uso como no modo Hyperscript é igualitário em todos os 3 modos.

As exceções em relação ao JSX do Vue, são:

+ O `h` não pode ser renomeado, ele precisa estar no escopo

+ Não é usado `onClick` como no React, mas ao invés disso `on-click`. Existia uma adapter que foi feito com a intenção de usarmos o JSX igual a como usamos no React, mas o repositório deixou de existir, então vamos seguir usando esse já que é praticamente uma exceção :D

Pessoal eu sei que é bastante coisa para digerir, mas como eu disse, isso foi a maior mudança em questão de API.

Esse é um assunto um tanto chato de escrever, era se bom que fossem vídeos...

Olha que coincidência, eu estou fazendo uma [serie(mini curso)](https://www.youtube.com/playlist?list=PLFtCenSt_W2Fxgh1fjjwXK20qg2MdC2wp) de Vue 2 e é de grátis :D

![que loko](/content/images/2016/09/giphy-2.gif)

Isso é tudo pessoal!

