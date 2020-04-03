---
layout: post
title: 'Pensando em estados com Vuejs'
date: 2018-04-05 19:00:00 
tags: estados
author: emanuelgdesouza
---

Olá meu caro leitor, hoje estou trazendo mais um texto do nosso colega de longa data: Vuejs. Este é o meu primeiro texto [neste querido blog](http://vuejs-brasil.com.br/). O objetivo deste texto é trazer à elucidação alguns conceitos que alguns desenvolvedores iniciantes tem acerca de como trabalhar com Vuejs. Portanto, espero que este texto seja de muito proveito a você.

## Conhecendo a aplicação

Estudando para a matéria de Libras na faculdade em que curso Análise de Sistemas, me deparei com a [API do IBGE](https://servicodados.ibge.gov.br/api/docs). Pensando em como fazer algo bacana com ela, me deparei com outro serviço, o [Via CEP](https://viacep.com.br) que é usado para pesquisa de informações a partir do CEP. Daí surgiu uma vontade de brincar um pouquinho com esses serviços e de quebra, tratar de alguns assuntos com Vuejs. Com isso surge a aplicação: [Public Data App](https://emanuelgdev.com.br/public-data-app), que, até o momento, possui duas funcionalidades:

* Pesquisa de informações a partir do CEP
* Pesquisa do CEP a partir do [logradouro](https://www.significados.com.br/logradouro/).

Estas duas funções já serão mais do que suficientes para o que irei tratar aqui: estados com Vuejs.

## Estados com Vuejs? O que é isso?

Para quem não sabe, Vuejs é um framework que te possibilita a todo momento desenvolver orientado a estados. Antes da dar continuidade, te aconselho a ler este [texto do Vinicius sobre estados com Vuejs](https://blog.codecasts.com.br/estados-com-vue-js-data-computed-props-e-store-d8c6da4627ca).

Mas o que é um estado? Segundo o Dicionário Aurélio:

> Modo atual de ser (de pessoa ou coisa); Modo geral; conjunto de circunstâncias em que se está e se permanece.

Fonte: https://dicionariodoaurelio.com/estado

Um estado é a condição atual de alguma coisa. Dentro do contexto do Vuejs, podemos enxergar dois estados, dois escopos:

* **Local**: data, computed e props
* **Global**: store - [Vuex](https://vuex.vuejs.org/)

O que irei abordar a partir daqui, são os conceitos acima, com exemplos da aplicação que comentei anteriormente.

## Estado Local

Pense em um estado local como o estado dentro de um escopo de um componente Vuejs. Entende-se como componente uma instância do Vue.js. Se você estiver trabalhando com *[Single File Components](https://medium.com/emanuelg-blog/descomplicando-os-single-file-components-do-vue-js-2df16724baab)*, cada arquivo **.vue** será um componente. Para uma explicação mais detalhada, [consulte a documentação do Vuejs](https://vuejs.org/v2/guide/components.html).

### Data

*Data* é uma propriedade do componente que vai trabalhar com o estado inicial da sua aplicação. Os atributos em *data* poderão ser modificados e assistidos. Para um exemplo de uso, dé uma olhada no código abaixo:

```js
export default {
  name: 'PageIndex',
  data: () => ({
    cep: '',
    result: {}
  })
}
```

Fonte: https://github.com/emanuelgsouza/public-data-app/blob/v.1.0.0/src/pages/cep/consult.vue

Os atributos em data, podem ser arrays, objetos, strings e números, serão compartilhados no escopo do componente. É nele que você poderá usar de um *[two-way data-binding](https://medium.com/criciumadev/two-way-data-binding-fd5d71712d28)* para, por exemplo, capturar uma entrada do usuário num *input*. Repare no link colocado acima.

Para uma olhada mais detalhada, [confira a documentação](https://vuejs.org/v2/guide/instance.html#Data-and-Methods).

Para uma demostração do exemplo acima, olhe este método do meu componente:

```js
methods: {
  getApiInformations () {
    const cep = this.cep
    this.$q.loading.show()

    if (!this.isCepValid) {
      return
    }

    cepApi
      .get(`/${cep}/json`)
      .then(result => {
        this.$q.loading.hide()
        this.result = result.data || {}
      })
  }
}
```

Este método será invocado quando o usuário clicar em "Pesquisar". Eu faço uma requisição para api do Via CEP passando como url o CEP que a pessoa digitou no input. Quando eu recebo o retorno dos dados, eu manipulo um atributo em *data* (result), colocando nele o resultado da requisição.

Mas e se o usuário tentar clicar em pesquisar sem ter digitado um CEP válido? Conheça as *computeds*

### Computed

```js
computed: {
  isCepValid () {
    return size(this.cep) === 8
  }
}
```

Para mais detalhes, [confira a documentação](https://vuejs.org/v2/guide/computed.html).

Computeds, como o próprio nome sugere, são propriedades computadas. O que é computar? Vamos ao dicionário:

> Contar; Fazer o cômputo de;

Fonte: https://dicionariodoaurelio.com/computar

E cômputo, o que significa?

> Cálculo, contagem

Fonte: https://dicionariodoaurelio.com/computo

Dentro do contexto do Vuejs, computeds são dados gerados a partir de outros dados. No exemplo, se você reparar, eu retorno um booleano dizendo se o CEP é válido ou não. A validação que faço é simples: para mim, um CEP válido possui 8 posições. A computed acima será usada para me dizer quando eu posso deixar o usuário clicar no botão, e mesmo ao clicar, validar se está tudo ok antes de fazer a requisição.

## Estado Global

É inegável, que quando você está trabalhando com sistemas de médio a grande porte, haverá estado global. Quer um exemplo? Se você está trabalhando com usuários na sua aplicação, com autenticação essas coisas, você terá um objeto compartilhado por todos com os dados do usuário autenticado. Pensando nisso, o *[Core Team](https://vuejs.org/v2/guide/team.html)* do Vuejs desenvolveu uma ferramenta muito conhecida pela comunidade: o [Vuex](https://vuex.vuejs.org/).

Mas, para que serve o Vuex? Aonde usá-lo? Se você leu o texto do Vinicius, verá que ele já responde a essa pergunta e ainda explica cada coisa da instância do Vuex, não deixe de conferir para não esquecer alguma coisa.

### State

A segunda funcionalidade da minha aplicação é uma busca de dados para encontrar o CEP. Quais são os dados? UF, Cidade e o logradouro. Dos três, o único que o usuário livremente escreve é o logradouro. Mas e os outros? Por comodidade, coloquei dois selects, um para o UF e o outro para as cidades. No meu *state* coloquei a listagem de estados do Brasil e o estado selecionado pelo usuário, como abaixo:

```js
export default {
  states: [],
  stateSelected: null
}
```

Mas repare, a listagem de estados está vazia. De onde vem os dados? Conheça um recurso bacana do Vuex, os [plugins](https://vuex.vuejs.org/en/plugins.html).

### Plugin

Um plugin do Vuex é uma função, que recebe a instância do Vuex e manipula ela assim que essa instância é carregada, ou seja, um plugin do Vuex será executado toda vez que sua aplicação é carregada.

Vejamos o exemplo:

```js
const applicationPlugin = store => {
  return store.dispatch('getStates')
}

export default [ applicationPlugin ]
```

Fonte: https://github.com/emanuelgsouza/public-data-app/blob/v.1.0.0/src/store/plugins.js

Para um exemplo mais completo, dê uma olhada [aqui](https://github.com/debate3d/debate3d-site/blob/master/src/domains/user/vuex-module/plugin.js).

Mas o que seria esse `store.dispatch`? Conheça as *[actions](https://vuex.vuejs.org/en/actions.html)*

### Actions

Actions são funções assíncronas que podem manipular seu state. No nosso exemplo, é na action que eu busco a listagem de todos os estados e carrego no meu state.

```js
import { path } from 'ramda'
import * as types from './mutation-types'
import { ibgeApi } from '../support/http'

export const getStates = ({ commit }) => {
  return ibgeApi
    .get('/v1/localidades/estados')
    .then(path(['data']))
    .then(result => {
      commit(types.SET_STATES, result)
    })
}
```

Se voçê reparar, eu carrego esses dados no meu state através de uma *[mutation](https://vuex.vuejs.org/en/mutations.html)*

### Mutations

Mutations são funções síncronas que trabalham diretamente com o state. No meu exemplo, é na mutation que eu insiro a listagem de estados e também é lá que eu, a partir de um UF, carrego os dados de uma estado selecionado pelo usuário.

```js
import { find } from 'lodash'
import * as types from './mutation-types'

export default {
  [types.SET_STATES] (state, states) {
    state.states = states || []
  },
  [types.SELECTED_STATE] (state, uf) {
    const states = state.states || []
    const _state = find(states, _state => _state.sigla === uf)
    state.stateSelected = _state || {}
  }
}
```

Com isso, eu tenho compartilhado com toda a aplicação, a listagem de estados, que é carregada quando a aplicação é carregada. E tenho já uma lógica separada para, a partir de um UF, selecionar um estado dentre a listagm. Para ver o código completo de como eu uso no componente, dá uma [olhada aqui](https://github.com/emanuelgsouza/public-data-app/blob/v.1.0.0/src/pages/cep/search.vue).

---

É isso pessoal, espero que tenham gostado do texto e que ele possa servir de norte para a compreensão, a partir de um exemplo mais real, do conceito de estados com Vuejs.

* Código fonte do projeto: https://github.com/emanuelgsouza/public-data-app/tree/v.1.0.0
* Aplicação rodando: https://emanuelgdev.com.br/public-data-app/#/

Para quem ainda não sabe, o Vuejs tem um *Cookbook* oficial! Confira [aqui](https://vuejs.org/v2/cookbook/)

---
Sou Emanuel, desenvolvedor na Decision6, amo tecnologias web, open source e acredito no lema: “to go fast, go alone; to go far, go togheter”. Mais informações sobre mim se encontram no meu site, emanuelgdev.com.br.
