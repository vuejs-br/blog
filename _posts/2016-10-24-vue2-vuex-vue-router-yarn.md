---
layout: post
title: 'Configuração base usando Vue.js 2, Vuex, Vue-Router e yarn'
main-class: 'dev'
date: 2016-10-24 11:06:33 
color: '#637a91'
tags: vue2 vuejs vue-router vuex yarn
layout: post
author: 9
---

Neste final de semana estava participando do [VanHackathon](https://www.vanhack.com/hackathon), uma competição internacional online sediada em Vancouver, Canada. Como tive alguns probleminhas na hora de organizar a configuração do Vue com os dois plugins mencionados no título deste artigo, resolvi escrever como eu montei o meu projeto e dar um exemplo do mesmo funcionando.

#### Instalação

Primeiramente, usei o `vue-cli` para criar um projeto que usa Vue 2.0 e webpack. Instalei também o **[yarn](https://code.facebook.com/posts/1840075619545360)** para *tomar* o lugar do npm. Para instalar essas ferramentas e criar o projeto faça:

```bash
$ npm i -g vue-cli yarn && mkdir vue2test && cd vue2test && vue init webpack
```

Com o projeto iniciado, instale as dependências e adicione os dois plugins (`vuex` e `vue-router`) executando os comandos abaixo:

```bash
$ yarn install && yarn add vuex vue-router vuex-router-sync
```

O plugin [vuex-router-sync](https://github.com/vuejs/vuex-router-sync) é necessário para assegurar que a minha vuex store estará sempre sincronizada com o vue-router.

#### Organização de diretórios
No meu projeto, eu defini a seguinte estrutura de diretórios:

```
src
├── App.vue
├── assets   #Fonts, Images, Stylus & CSS vendors
|   ├── img
|   └── styles
|       ├── style.styl
|       └── vendors
├── commons   #Vue Directives, Vue Filters and common functions
|   ├── directives
|   ├── filters
|   └── functions
├── shared-components
|   └── DefaultSelect.vue
├── spa
|   ├── Page1
|   ├── Home.vue
├── vuex
|   ├── modules
|   ├── actions.js
|   ├── getters.js
|   ├── mutation-types.js
|   └── store.js
├── main.js
├── router-config.js
```

Ótimo! Agora tenho que configurar três arquivos no meu ambiente: `main.js`, `router-config` e `vuex/store.js`.

O `main.js` é o coração da aplicação. Ele será responsável por conter todas as configurações necessárias.

```javascript
import Vue from 'vue';
import Vuex from 'vuex';
import Router from 'vue-router';
import { sync } from 'vuex-router-sync';

import App from './App';
import VuexStore from './vuex/store';
import { routes } from './router-config';

Vue.use(Vuex);
Vue.use(Router);

const store = new Vuex.Store(VuexStore);

const router = new Router({
  routes,
  mode: 'history',
});

sync(store, router);

const app = new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
```

As minhas rotas serão configuradas a partir do `router-config`, sendo assim, criei-o dessa maneira:

```javascript
import Home from './spa/Home';

export const routes = [
  {
    path: '/',
    component: Home,
    children: [],
  },
];
```

Com isso pronto, posso focar na minha Store. Logo, no arquivo `vuex/store.js` defini a seguinte store:

```javascript
import goal from './modules/goal';

export default {
  modules: {
    goal,
  },
  strict: true,
};
```

Pronto! Com esses três arquivos configurados, fui capaz de desenvolver sem problemas.

#### *Shut up and show me the code!*

O código da minha aplicação pode ser encontrada no meu [Github](https://github.com/pablohpsilva/Goal).
