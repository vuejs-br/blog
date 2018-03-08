---
layout: post
title: 'Desmistificando o Vue Router 2'
main-class: 'dev'
date: 2018-03-08 00:00:00 
description: derscricao
color: '#637a91'
tags: vue-router-2
 - vue-js
 - vue-js2
layout: post
introduction: introducao
---

O Vue Router conseguiu ficar ainda mais poderoso e simples de usar nessa nova versão. Vamos nesse artigo olhar as mudanças que houveram e as novas funcionalidades implementadas.


## Começando...

Realmente esta muito simples, olhando o código para ver uma implementação básica:

HTML: 

```html
<div id="app">
  <h1>Hello App!</h1>
  <p>
    <!-- Use componente `router-link` para navegação. -->
    <!-- Especifique para onde o link vai na props `to`. -->
    <!-- `<router-link>` irá renderizar um `a` por padrão. -->
    <router-link to="/foo">Go to Foo</router-link>
    <router-link to="/bar">Go to Bar</router-link>
  </p>
  
  <!-- Vai ser renderizado aqui -->
  <router-view></router-view>
</div>
```

Javascript:

```javascript
// Caso você esteja usando com o vue-cli não precisa registrar no Vue.
Vue.use(VueRouter)

// Define os componentes.
// É claro que pode ser importando de outros arquivos sendo `.vue`
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }

// Define algumas rotas
// Cada rota deve mapear um componente mesmo que seja via Vue.extend() ou só um componente de opções.
const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar }
]

// Cria uma instancia router.
const router = new VueRouter({
  routes // shorthand para routes: routes
})

// Cria e monta a instancia.
const app = new Vue({
  router
}).$mount('#app')
```

## Dynamic Route Matching

*_Alguém sabe como eu traduziria esse titulo xD_

###### Edit
_Poderia ser:_ "Apresentando as rotas dinâmicas", dado que matching seria 'correspondência', que é sinônimo do verbo apresentar. PS: não sei se era pra dar a sugestão editando o post mesmo.

