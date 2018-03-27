---
layout: post
title: 'O que é cada propriedade num Vue Object'
main-class: 'dev'
date: 2016-07-10 18:08:19 
color: '#637a91'
tags: vue-js
layout: post
author: 1
---

Quando criamos métodos no Vue Object nós o fazemos dentro de um [objeto literal](http://blog.caelum.com.br/criacao-de-objetos-em-javascript/) `{}`, que é uma forma de iniciar um objeto usando apenas as chaves.

Este objeto de **configuração** possui propriedades pré-definidas pelo Vue.js, dentro das quais o desenvolvedor distribuirá seu próprio código. Esta forma de distribuição do código é uma das belezas do Vue, pois ajuda na organização geral dos seus scripts.

E é sobre estas propriedades que este artigo falará. Comecemos com o seguinte *snippet* de código:

```javascript
new Vue({
    el: 'body'
})
```

***el*** é uma propriedade do objeto passado como único parâmetro para o construtor de Vue. Ela é essencial para **ligar** o HTML ao Vue Object e é uma propriedade obrigatória.

> Daqui por diante utilizarei nos exemplos o objeto como se estivesse criando *single file components* com extensão ***.vue**. Isso significa que a criação do Vue Object já foi feita em algum outro lugar de sua aplicação. Para mais informações sobre esta forma de se criar componentes, sugiro o link oficial do **Vue-loader**. [http://vue-loader.vuejs.org/en/index.html](http://vue-loader.vuejs.org/en/index.html)

Seguindo adiante temos as duas propriedades mais utilizadas, porém não obrigatórias:

```javascript
export default {
    data () {},
    methods: {},
}
```

A propriedade **data** conterá um objeto com os dados do componente e que estarão disponíveis para serem mostrados no HTML. Indo um pouco além, o HTML configurado na propriedade **el** também terá acesso a estes mesmos dados, podendo modifica-los.

Já a propriedade **methods** conterá um objeto com todos os métodos também disponíveis ao HTML mas não limitados a ele. Digo isso pois qualquer método contido neste objeto pode também executar os demais métodos do componente, bastando para isso utilizar o `this` (neste caso o this se refere ao próprio componente).

Vamos em frente...

```javascript
export default {
    ready () {},
    events: {},
    props: [],
    computed: {},
    vuex: {},
    components: {},
    watch {},
    data () {},
    methods: {},
}
```

>**Importante -** a ordem das proprieades **não** é importante.

Acredito que o *snippet* acima mostre todas as principais propriedades que se costuma utilizar com o Vue Object. Repare que **ready** e **data** não se parecem com propriedades, mas saiba que elas são sim.

Acontece que `ready () {}` é um atalho ES2015 para `ready: function () {}`. O mesmo se aplica a `data () {}` que quando utilizada dentro de componentes é uma factory e não um objeto. Mais detalhes em [http://vuejs.org/guide/components.html#Component-Option-Caveats](http://vuejs.org/guide/components.html#Component-Option-Caveats).

Explicando:

* **ready () {}** é um método que será executado quando componente estiver totalmente configurado e pronto para uso. É um dos hooks do *fluxo de vida dos componentes*: [http://vuejs.org/api/#Options-Lifecycle-Hooks](http://vuejs.org/api/#Options-Lifecycle-Hooks).

* **events: {}** contém os *listeners* para todos os eventos nos quais o componente tiver interesse. Caso um evento seja nomeado com dash (ex. `user-created`) então utilize o nome da propriedade encapsulado em apóstrofes.
```javascript
events: {
   'user-created' (obj) {
        // faça algo com o valor de obj
   }
}
```
* **props: []** são as propriedades que o componente pode receber de seu pai. Assim se o componente for `<meu-componente :list="users"><meu-componente>` então teremos `props: ['list']`. Em sua forma de uso mais simples, `props` recebe um *array* de *strings*, porém, caso ao menos uma das propriedades necessite ter um valor padrão ou precise ser validada, então `props` será um objeto. Mais detalhe neste link [http://vuejs.org/guide/components.html#Prop-Validation](http://vuejs.org/guide/components.html#Prop-Validation).

* **computed: {}** são as *computed properties* que retornam um novo valor após avaliar um ou mais valores já existentes. Melhor dar logo um exemplo:

```javascript
export default {
    data () {
        first: 'Fabio',
        last: 'Vedovelli',
    },
    computed: {
        full () {
            return this.first '+ +' this.last
        }
    }
}
```
... e agora nosso componente possui 3 dados relacionados a um usuário: **primeiro nome**, **segundo nome** e **nome completo** sendo este último a **computed property**. Este é o exemplo clássico porém seu uso é muito mais abrangente. O fato delas serem factories (métodos que retornam um valor) faz com que qualquer verificação possa ser feita numa *computed property*.

É importante lembrar que devido à natureza reativa do Vue.js, cada vez que *first* ou *last* for modificada *full* será executado, resultado em novo valor retornado. Caso a propriedade *full* tenha sido utilizada num controle de formulário, por exemplo, o novo valor será exibido.

* **vuex: {}** é onde podemos acessar os valores do *state* centralizado da aplicação, caso esta faça uso do Vuex. Nesta propriedade também se adiciona as **actions** que são responsáveis por modificar o state.

* **components: {}** é a propriedade responsável por registrar componentes a serem utilizados no template do componente atual. Um resumo: os componentes são compostos por Javascript (comportamento) e HTML (estrutura) e neste último é possível usar mais do que HTML puro: é possível fazer uso de outros componentes Vue, desde que registrados previamente na propriedade *components*.

* **watch: {}** permite observar valores contidos na propriedade *data* e/ou passados como *props*. Todas as vezes que o valor mudar então o método contido em *watch* será executado, lhe permitindo executar alguma ação. Apesar da tentação de utilizar watchers por todo lado, o ideal é utilizar uma *computed property* que, graças à natureza reativa do Vue.js, são também executadas quando um ou mais valores mudam.

Espero que tenha gostado,

Um forte abraço,

[Vedovelli](http://vedcasts.com.br)
