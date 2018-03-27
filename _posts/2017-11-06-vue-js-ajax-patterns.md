---
layout: post
title: 'Vue.js ajax patterns'
main-class: 'dev'
date: 2017-11-06 13:20:56 
color: '#637a91'
tags: vue vue2 ajax vuex components design-patterns
layout: post
author: 6
---

Você vira para um desenvolvedor front-end e pergunta:

> Qual o jeito de fazer ajax em aplicações Vue.js

Se você iniciou com front-end há pouco tempo, e pelo fato de usar Vue.js ser muito simples, provavelmente sua resposta foi:

> Ahh mermão taca uns axios por ali e aqui e tá tudo suave... (fazendo uns [hang loose](https://www.google.com.br/search?q=hang+loose&oq=hang+loose&aqs=chrome..69i57.217j0j7&sourceid=chrome&ie=UTF-8) com as mãos xD)

Bem... não é assim que funciona, a aplicação vai funcionar, mas se você esta mexendo em uma app que precisa ser robusta e escalar facilmente, é bom pararmos e entender qual a melhor forma de fazer isso.

Por o Vue não prover uma maneira exata de como fazer ajax, existem varios patterns de como implementar isso, eu vou mostrar 5 maneiras nesse artigo, cada uma com seus prós e contras e podendo ser usado um com o outro.

Elas são:

1. Root instance
2. Components
3. Vuex actions
4. Route navigation guards
5. União de design patterns (ou quase isso xD)

> Para ler esse artigo, recomendo fortemente você ler esse outro [artigo](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) do Dan Abramov sobre **Presentational and Container Components** :D

## Root instance

Com esta arquitetura, você vai colocar todos os seus requests ajax na root instance, e guardar todo o state lá também. Caso qualquer subcomponente precisar de dados, vai ser passado via props. Caso qualquer subcomponente precisar atualizar os dados, um evento vai ser lançado da root instance para isso acontecer.

**Exemplo:**

```javascript
new Vue({
  data: {
    message: ''
  },
  methods: {
    refreshMessage (resource) {
      this.$http.get('/message').then(({ data }) {
        this.message = data.message
      })
    }
  }
})
 
Vue.component('sub-component', {
  template: '<div>{{ message }}</div>',
  props: ['message']
  methods: {
    refreshMessage() {
      this.$emit('refreshMessage')
    }
  }
})
```

**Prós**

+ Mantem toda a lógica do ajax e os dados em um lugar.
+ Mantem seus componentes "dumb" e então você consegue focar no presentation.

**Contras**

+ Muitos eventos e props serão necessários caso sua app cresça.


## Components

Com esta arquitetura, os componentes são responsáveis por lidar com seus próprios requests ajax e state indenpendentemente. Na prática, você terá que criar vários "containers" components que lidam com dados para seus próprio state local e passar para os "presentational" components.

> Agora reforço que se você não leu o [artigo](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) do Dan Abramov que falei no início do post você deve tá perdido xD

A gente vê bastante isso em aplicações React, mas no caso do Vue, podemos fazer essa implementação de forma mais fácil colocando a lógica do ajax em um mixin.

**Exemplo:**


```javascript
const mixin = {
  methods: {
    callAJAX (resource) {
      ...
    }
  }
};
 
Vue.component('container-comp', {
  // No meaningful template, I just manage data for my children
  template: '<div><presentation-comp :mydata="mydata"></presentation-comp></div>', 
  mixins: [myMixin],
  data() {
    return { ... }
  } 
});
 
Vue.component('presentation-comp', {
  template: <div>I just show stuff like {{ mydata }}</div>,
  props: ['mydata']
});
```

**Prós**

+ Mantem o componente desacoplado e reusável.
+ Pega os dados quando e onde for preciso.

**Contras**

+ Difícil a comunicação com outros componentes ou grupo de componentes.

+ Os componentes podem acabar com muitas responsabilidades e funcionalidades duplicadas.


## Vuex actions

Com esta arquitetura, você lida com state e a lógica dos requests ajax na sua Vuex store. Componentes podem pedir mais dados só no "dispatching" uma action.

Se você implementar esse pattern, é uma boa ideia retornar uma promise da sua action e então fazer alguma coisa após a resolução do ajax como por exemplo, esconder um spinner, reabilitar uma buttão, etc...

**Exemplo:**

```javascript
const store = new Vuex.Store({
  state: {
    message: ''
  },
  mutations: {
    updateMessage (state, payload) {
      state.message = payload
    }
  },
  actions: {
    refreshMessage (context) {
      return new Promise((resolve) => {
        this.$http.get('...')
         .then(({ data }) => {
          context.commit('updateMessage', data.message)
          resolve()
        })
      })
    }
  }
})
 
Vue.component('my-component', {
  template: '<div>{{ message }}</div>',
  methods: {
    refreshMessage () {
      // Please use mapActions from vuex
      this.$store.dispatch('refeshMessage')
        .then(() => {
        // do stuff
        })
    }
  },
  computed: {
    message: { return this.$store.state.message }
  }
})
```

Se você estiver usando Vuex, essa a forma de fazer. Se você não estive usando, esta pode ser o motivo por você querer usar.

![catiorro dançando](https://media.giphy.com/media/PSKAppO2LH56w/giphy.gif)


**Prós**

+ Mantem toda a lógica do ajax e os dados em um lugar.
+ Mantem seus componentes "dumb" e então você consegue focar no presentation.
+ Sem precisar de props ou eventos.

**Contras**

+ Adiciona um overhead no Vuex.

> [Screencast](https://www.youtube.com/watch?v=Fn6pB3sYhn4) do vedovelli falando sobre isso :D

## Route navigation guards

Com esta arquitetura, sua app é dividida em páginas e todos os dados necessários para uma página e seus subcomponentes, são obtidos quando a rota é alterada.

A grande vantagem dessa abordagem é que ela realmente simplifica sua UI. Se os componentes forem indenpendentes obtendo seus próprios dados, a página voltará a ser imprevisivel à medida que os dados do componente foram preenchidos em uma ordem arbitrária.

Uma excelente maneira de implementar isso é criar endpoints em seu servidor para cada página como por exemplo, `/about`, `/contact`, etc..., que correspondem aos nomes das rotas em sua app.

**Exemplo:**

```javascript
import axios from 'axios';
 
router.beforeRouteEnter((to, from, next) => {
  axios.get(`/api${to.path}`).then(({ data }) => {
    next(vm => Object.assign(vm.$data, data))
  });
})
```

**Pros**

+ Torna a UI mais previsível.

**Contras**

+ Fica mais lento no geral já que a página não pode renderizar até ter todos os dados.
+ Não ajuda se você não estiver usando rotas =\

## União de design patterns

Eu que fiz esse pattern e no caso do Vue eu uso ele em conjunto com o Vuex actions pattern e no geral tem me atendido muito bem :D

Antes de tudo vamos olhar a organização de pastas

```
➜  vuejs-ajax-patterns tree -L 3 src/services
src/services
├── AbstractInterface.js
├── index.js
├── MainRequesterComposite.js
└── strategies
    ├── User
    │   ├── actions
    |   |   ├── list.js
    │   └── index.js
    └── index.js

3 directories, 5 files
```

Essa é a services layer para se comunicar seja com a sua API ou com seu WebSocket,
ela usa dois design patterns chamados [Composite](https://en.wikipedia.org/wiki/Composite_pattern) e [Strategy](https://en.wikipedia.org/wiki/Strategy_pattern).

Todo novo request vai ser intermediado e estar no `MainRequester`, quando você precisar implementar um novo request, você vai criar uma nova pasta com o mesmo nome da classe dentro da página de `strategies`.

Quando uma nova strategy for criada, ela vai extender de `AbstractInterface` que vai provê métodos que vão ser necessários para fazer os requests.

Vamos dar uma olhada nos arquivos:

_MainRequesterComposite.js_
```javascript
class MainRequesterComposite {
  add (Requester) {
    this[Requester.NAME] = Requester.handler
  }
}

export default MainRequesterComposite
```

_AbstractInterface.js_
```javascript

import axios from 'axios'
import autoBind from 'react-autobind'

import { store } from '~/store'

class AbstractInterface {

  /**
   * Initialize all clients and bind all methods from strategies
   */
  constructor () {
    this.initializeAllClientRequesters()
    autoBind(this)
  }

  /**
   * Create all clients
   * @return {undefined}
   */
  initializeAllClientRequesters () {
    // Put $httpClient available to all strategies
    this.$httpClient = this._createHttpClient()
    this.$webSocketClient = this._createWebSocketClient()
  }

  /**
  * Create axios instance to
  * use on all of strategies
  * @return {Object} axios instance
  */
  _createHttpClient () {
    const axiosOptions = {
      baseURL: process.env.API_BASE,
      headers: {}
    }

    const token = store.getters['auth/token']

    if (token) {
      axiosOptions.headers['Authorization'] = `JWT ${token}`
    }

    return axios.create(axiosOptions)
  }
   
  _createWebSocketClient () {
    // WS Implementation...
  }
 

  /**
   * Handle error to each request made
   * @param  {Object} error contains the type of error and its payload that says which error happened
   * @return {undefined}
   */
  handlerErrors (error) {
    switch (error.type) {
      case 'API':
        console.log('[API ERROR]', error.payload) // eslint-disable-line
        return
      case 'WS':
        return
      default:
        console.log('Please pass a error type') // eslint-disable-line
    }
  }

  /**
   * Force strategies to have handler
   * function such as request method
   * @return {Object} Error if not implemented
   */
  handler () {
    // Simulates an interface
    throw new Error('Not implemented yet')
  }
}

export default AbstractInterface
```

_User/index.js_
```javascript
import AbstractInterface from '../../AbstractInterface'
import {
  list,
  LIST_METHOD_NAME
} from './actions/list'

class User extends AbstractInterface {

  get NAME () {
    return 'User'
  }

  constructor () {
    super()
  }

  handler (userActionType, payload = {}) {
    switch (userActionType) {
      case LIST_METHOD_NAME:
        return list(this, payload.params)
      default:
        return new Error('Please pass a action type to', this.NAME())
    }
  }

}

export default new User()
```

_user/actions/list.js_
```javascript
export const LIST_METHOD_NAME = 'list'

/**
 * List all users with pagination
 * @param  {[type]} self      AbstractInterface context to use helper methods
 * @param  {Object} [params]  Options to do pagination
 * @return {Promise}
 */
export const list = (self, params = {}) => {

  return new Promise((resolve, reject) => {

    self.$httpClient.get('users/', params)
      .then(({ data }) => data)
      .then(resolve)
      .catch((userListError) => {
        self.handlerErrors({
          type: 'API',
          payload: userListError
        })
        reject(userListError)
      })
  })
}
```

_src/index.js_
```javascript

import MainRequesterComposite from './MainRequesterComposite'
import Strategies from './strategies'

const MainRequester = new MainRequesterComposite()

/**
 * Register all strategies
 */
Strategies.map((strategy) => MainRequester.add(strategy))

export { MainRequester }
```

Assim quando vou usar no meu Vuex fica assim:

```javascript
const store = new Vuex.Store({
  actions: {
    getUsers (context) {
      return new Promise((resolve) => {
        this.$MainRequester.User('list')
          .then((response) => {
            context.commit('setUser', response)
            resolve()
          })
      })
    }
  }
})
```

que no caso do Vue, eu coloco o `MainRequester` no `prototype` e fica mais facil ainda de usar :D

**Prós**

+ Mantem toda a lógica do ajax e os dados em um lugar.
+ Mantem seus componentes "dumb" e então você consegue focar no presentation.
+ Sem precisar de props ou eventos.
+ Total desacoplamento, não só dos componentes mas de toda aplicação.

**Contras**

+ Aumento na complexidade quando for fazer um simples ajax.


## Referências

+ https://vuejsdevelopers.quora.com/4-AJAX-Patterns-For-Vue-js-Apps

+ https://www.andrewhfarmer.com/react-ajax-best-practices/

Bem, é isso pessoal, espero ter esclarecido a cabeça do pessoal aí. Se eu esqueci de falar alguma coisa só falar nos comentários ;)

> Pessoal, tendo uns erros de português aí, me fala que escrevi isso ae rapidex xD
