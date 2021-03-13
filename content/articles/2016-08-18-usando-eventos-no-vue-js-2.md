---
layout: post
title: 'Usando eventos no Vue.js 2.0'
main-class: 'dev'
date: 2016-08-18 12:08:22 
color: '#637a91'
tags: vue-js-2 events bus
author: vedovelli
---

Sabemos que a recomendação é utilizar Vuex para a sanidade do projeto e da equipe de desenvolvimento, porém, os métodos **$broadcast()** e **$dispatch()**, recém depreciados na nova versão ainda tem um papel fundamental comunicação entre componentes, mesmo que se esteja utilizando Vuex.

Como então manter esta possibilidade?

A solução é muito simples e ainda mais poderosa do que a que foi depreciada. 

Vamos à receita do bolo:

Em qualquer local da sua aplicação, crie um arquivo chamado `bus.js`. Exemplo: num projeto criado com *vue-cli* você pode criar em `/src/utils/events/bus.js`. Segue o conteúdo do arquivo:

```javascript
import Vue from 'vue'
const bus = new Vue()
export default bus
```

Então basta importar esta constante em qualquer componente que precise disparar um evento:

```javascript
import bus from './utils/events/bus' // << adequar o path à sua estrutura
export default {
    methods: {
        buttonClickHandler () {
            bus.$emit('botao-foi-clicado', 13)
        }
    }
}
```

E em qualquer componente que possa ter interesse neste evento:

```javascript
import bus from './utils/events/bus' // << adequar o path à sua estrutura
export default {
    mounted () { // << mounted subititui o hook ready()
        bus.$on('botao-foi-clicado', (id) => console.log(id))
    }
}
```

Qual a grande vantagem desta abordagem?! Como se tem um local centralizado para disparar e escutar eventos, a comunicação entre componentes "irmãos" (*siblings*, que estão lado a lado na hierarquia de componentes) é facilitada, se comparado com a versão 1 do Vue.js. Naquela versão era necessário 1. capturar um $dispatch() 2.  executar um callback 3. ler as informações do evento e 4. fazer um $broadcast().

Até o próximo artigo!

Ved


