---
layout: post
title: 'Utilizando Vuex na forma modular'
main-class: 'dev'
date: 2016-07-22 12:26:29 
color: '#637a91'
tags: vuex mudular modulos
layout: post
author: 8
---

##Coisas "fora" do Vuex
*Bom.. vou deixar em meu primeiro artigo aqui no blog do **Vuejs-Brasil**, uma solução que aprendi sobre acessar externamente a store do **Vuex** e o porquê bati tanto cabeça para algo 'relativamente simples' =P.*

Geralmente nossos componentes recebem os estados e ações do **Vuex** via propriedade *vuex* no componente: 
```javascript
//MeuComponente.vue
export default {
    vuex: {
        getters: {
            //aqui ficam as propriedades
        },
        actions: {
            // aqui as ações
        }
    }
```

Essa é a estrutura básica de como se obter as propriedades armazenadas na **store** e suas **mutations** *(actions)*. 

Mas… e quando quisermos “abstrair” uma funcionalidade global?

Por exemplo:

No meu caso eu gostaria muito de ter um serviço de autenticação independente de componente, ou seja, que ele ficasse contido dentro de um arquivo e que consultasse a **store** diretamente sem a necessidade de encapsular ele dentro de um componente como no código acima.

Se tu procurares aí na internet a fora verás muitos exemplos como do código acima, e na própria documentação do **Vuex** está assim. Outro trecho de código comum que tu achas por aí para inicializar a **store** é algo deste tipo:
```javascript
// store.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({...})
``` 

E lá na instância do Vue ou do componente App (no caso de usar o **vue-cli**) o seguinte código:

```javascript
// main.js
import Vue from 'vue'
import store from 'store'

new Vue({
    store, //<- injeta a store dentro da instância do Vue
    ...
})
```

Procurei, procurei até que resolvi arriscar.. e confesso não ser um programador **javascript** avançado, ou até mesmo intermediário, mas a coisa é que muitos anos no **C#** *(C-Sharp)* ainda pesam sobre minhas decisões no **JS**!

Bom… eu já tinha a **store** no meu compomente `App.vue` e ela ficava disponível para toda aplicação, OK, mas lembra o meu serviço de autenticação *(**authService**)* ?

Então foi aí que resolvi arriscar e importar o `store` pra dentro de um arquivo chamado **index.js** dentro de uma pasta com o nome de **authService** e voilà!!!! Agora bastava eu importar **authService** que eu tinha acesso ao conteúdo da `store`. Mas espera! Não foi por causa da pasta e tão menos os nomes, fiz isso justamente para organizar o código *(pretendo escrever sobre isso em outra oportunidade)*.

Agora posso ter o serviço da seguinte forma:

```javascript
// main.js
import Vue from 'vue'
import store from 'store'

new Vue({
    store,
    ...
})
```
```javascript
//index.js em /vuex/auth

const SET_TOKEN = 'SET_TOKEN'
const state = {
        token: ''
    }
const mutations = {
      [SET_TOKEN] (state, token) {
         state.token = token
    }

export default { state, mutations }
```

```javascript
// store.js
import Vue from 'vue'
import Vuex from 'vuex'

//importo o state e mutations
import auth from './vuex/auth'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        auth
    }
})
```
E por fim... o **authService**:
```javascript
// index.js em /services/authService
import store from '../../vuex/store'

//mudando o valor do token diretamente na store!
const setToken = function(token) {
    store.dispatch('SET_TOKEN', token)
}
//recuperando o valor de token da store!
const getToken = function() {
    return store.state.auth.token
}
```
Quando eu precisar usar o serviço de autenticação para gravar o token a partir de algum componente eu faço da seguinte forma:
```html
//MeuComponente.vue
<script>
    import authService from '/services/authService'
    export default {
        methods: {
            UmMetodoQualquer () {
                // ... faz algo e recebo o token //
                let token = 'a23dd343...sde343231'
                // gravo o token
                authService.setToken(token)
                // ... 
                // o mesmo pode ser feito para recuperar o token
                token = authService.getToken()
            }
        }
</script>
```

O resultado ficou ótimo!

**Moral da história!**

Eu tava era preocupado com o `new Vuex.Store` gerar uma **“nova instância”** e perder os dados que já haviam nela!!!! hahahahahahahaha

Obrigado por ler! ;)

---------

### Vamos entender o que aconteceu.

Oi, eu sou [Vinicius](http://www.vuejs-brasil.com.br/author/vinicius/).
Em resumo javascript é uma linguagem de script interpretada em *runtime*, e entre outras características o js possui **escopo léxico**, que nos permite criar *clousures*.

Em javascript tudo (tirando *undefined*) são objetos, javascript (sozinho) não possui suporte a módulos ou *imports*, isso significa que você não pode "incluir" um arquivo js durante a execução do seu script.  
Porém, há especificações para criar módulos javascript. Os mais conhecidos são [AMD](https://github.com/amdjs/amdjs-api) e [CommonJS](http://www.commonjs.org/). Eles são parecidos e podem funcionar em conjunto.
Há ferramentas como [requirejs](http://requirejs.org/) que ajudam a usar módulos, e ferramentas como o [browserify](http://browserify.org/) ou [webpack](https://webpack.github.io/) que deixam isso mais simples ainda. 


Assumimos que **um arquivo javascript é *'módulo javascript'***, e um módulo expõe valores. Um módulo é basicamente um objeto servindo como *namespace* para valores, que podem ser outros objetos.

Os módulos js fazem uso da técnica de *clousure* do javascript para criar valores privados e públicos, além disso os módulos são (por muitas vezes) [IIFE (immediately-invoked function expression)](http://imasters.com.br/front-end/javascript/sobre-funcoes-imediatas-javascript-iife/) sendo o "retorno" dessas funções um "singleton".

**E é nesse ponto que entendemos o que aconteceu.**
```javascript
export default new Vuex.Store({...})
``` 

Estamos **expondo uma instância** do Vuex.Store. Qualquer um que importar este arquivo  terá acesso a essa instância, e ela **sempre** será a mesma (*singleton*). Em javascript os objetos são passados como referência, então todos os locais que usam esse *módulo* estão usando a mesma referência. 

Esse comportamento é extremamente útil e se você não gosta dele há maneira simples de contornar.

Essa é uma explicação rasa. Inicialmente javascript pode parecer algo muito complexo, porém estudando os conceitos por trás dos comportamentos tudo se torna muito simples.  
