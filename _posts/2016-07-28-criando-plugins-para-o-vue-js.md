---
layout: post
title: 'Criando plugins para o Vue.js'
main-class: 'dev'
date: 2016-07-28 14:00:29 
color: '#637a91'
tags: vue-js plugins
layout: post
author: jjsquad
---

Quando usamos o Vue usamos também alguns plugins para complementar o mesmo tal como, [vue-router](https://github.com/vuejs/vue-router) , [vuex](https://github.com/vuejs/vuex), [vue-validator](https://github.com/vuejs/vue-validator), etc... já que ele traz somente o necessário.

É incrivelmente fácil criar plugins pro Vue, e esses plugins podem ser de diversos tipos, como adicionar propriedades, métodos, assets(diretivas, filtros...) globais, um método de instacia para anexar no protótipo do Vue ou até uma biblioteca que provê uma API própria :D

Para criar o plugin, o mesmo deve expor um método `install` que por sua vez recebe dois argumentos, o primeiro é o construtor do Vue e o segundo são as opções:

```javascript
MyPlugin.install = function (Vue, options) {
  // 1. Adicionando um método global
  Vue.myGlobalMethod = ...
  // 2. Adicionando uma diretiva
  Vue.directive('my-directive', {})
  // 3. Adicionando um método ao protótipo
  Vue.prototype.$myMethod = ...
}
```

Agora você só precisa dizer para Vue usar seu plugin:

```javascript
Vue.use(MyPlugin)
```

podendo passar opções:

```javascript
Vue.use(MyPlugin, { someOption: true })
```

e pronto! Agora você já sabe como fazer seus próprios plugins pro Vue.
