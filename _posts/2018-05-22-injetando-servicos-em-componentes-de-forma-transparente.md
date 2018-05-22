---
layout: post
title: 'Injetando serviços em componentes de forma transparente'
date: 2018-05-22 01:00:00 
tags: componentes services api http
author: wilcorrea
---

Este é meu primeiro artigo aqui no blog. É uma honra estar aqui com vocês e o meu objetivo é mostrar como usar serviços nos seus componentes de uma forma madura e organizada.

> Você provavelmente já viu alguns exemplos de aplicações utilizando Vue. Já deve ter percebido que ainda há uma fase de fragmentação quanto ao uso da ferramenta, onde vários grupos tem várias arquiteturas sendo aplicadas e testadas.

Esta situação é um pouco desconfortável para alguns, mas ela espelha um momento cada vez mais comum no desenvolvimento web: POSSIBILIDADES.

É muito provável que se você perguntar a cada arquiteto de cada estrutura visitada ele tenha partido de alguma experiência anterior pela qual passou e tenha organizado sua estrutura porque a que vinha usando o deixou na mão ou não escalou nesta ou naquela situação.
Conosco não é muito diferente. Nosso caso era realmente a preocupação com a flexibilidade e rapidez.
Precisávamos de estruturas que fossem criadas rapidamente e que fossem simples de serem atualizadas, sem ter que abrir centenas de arquivos para aplicar mudanças; esse era nosso desafio.

> Disclaimer: o conteúdo do artigo são apenas sugestões de coisas que usamos no nosso dia-a-dia, fique à vontade para concordar e/ou discordar, aproveitando as experiências da forma que melhor lhe convir.

## Serviços

Nos contextos de arquitetura de software o termo serviço refere-se a uma funcionalidade ou um conjunto de funcionalidades de software com um propósito que pode ser reutilizado em diferentes ocasiões. Geralmente associamos os acessos à recursos HTTP ao nome Service, mas nem sempre usamos uma estrutura dedicada à isso para cada domínio da nossa aplicação, o que, particularmente se tornou um problema.

> Devemos ter cuidado ao usar recursos como `this.$http.get('/api/v1/products')` dentro da nossa aplicação, pois estamos pulverizando uma camada lógica importante por toda a aplicação.

Vou deixar o artigo "[Vue.js: Trabalhando com Serviços](https://blog.codecasts.com.br/vue-js-e-servicos-4d4439320a2)" como referência para construções de serviços, caso queira se aprofundar um pouco mais sobre o tema.

## Mantendo Contratos

Para quem está acostumado com linguagens onde a **Orientação a Objeto** possui suporte à recursos como interfaces, métodos abstratos, enum, entre outros, o javascript se torna um pouco assustador por não entregar esse tipo de composição. Contudo, isso não é exatamente um problema quando você organiza a sua aplicação porque essa chamada falta de rigidez pode ser compensada de outras formas para forçar que alguns caminhos não sejam seguidos. Sugiro dar uma olhada no artigo "[Vue.js ajax patterns](http://vuejs-brasil.com.br/vue-js-ajax-patterns/)" para pegar algumas dicas de composição de serviços.

### Criando Serviços Extensíveis

Para poder seguir com este material apresentaremos uma solução simples para criar um _Service_ que pode ser estendido e usado nos domínios das entidades com as quais estão lidando. A seguir será apresentada uma lista de documentos e a respectiva explicação sobre o que representa cada um deles.

#### **A estrutura**
```
/src
 |
 ├── /domains/
 |   └── /Product
 |        └── /Service
 |             └── Product.js
 |
 ├── /service
 |   ├── helper.js
 |   ├── Api.js
 |   └── Service.js
 |
 └── main.js
```

##### src/main.js

Um pequeno exemplo de uso de como o serviço será usado. Ele importa o _service_ de _Product_ e constrói uma instância para poder executar o método `read` e imprimir a saída;

```javascript
import Product from 'src/domains/Product/Service/Product'

const product = Product.build({})

product.read().then(console.warn)
```

##### src/domains/Product/Service/Product.js

A especialização do serviço _Api_ para ser usado no escopo da entidade _Product_;

```javascript
import Api from 'src/service/Api'

export class Product extends Api {
  /**
   * @param {*} options
   */
  constructor(options) {
    super(options, '/api/v1/market/products')
  }
}
```

##### src/service/Api.js

Serviço para consumo de API’s que entrega 4 métodos básicos para realizar o que é costumeiramente chamado de CRUD;

```javascript
import Service from 'src/service/Service'
import { promise } from 'src/service/helper'

/**
 * @type {Api}
 */
export default class Api extends Service {
  /**
   * @param {Object} options
   * @param {string} resource
   */
  constructor (options, resource) {
    super(options)
    this.resource = resource
  }

  /**
   * @param {Object} record
   */
  create (record) {
    return promise({status: 'CREATE'})
  }

  /**
   * @param {string} id
   */
  read (id) {
    return promise([{status: 'READ'}])
  }

  /**
   * @param {Object} record
   */
  update (record) {
    return promise({status: 'UPDATE'})
  }

  /**
   * @param {Object} record
   */
  destroy (record) {
    return promise({status: 'DESTROY'})
  }
}
```

##### src/service/Service.js

Contrato básico para a _factory_ de instâncias do _Service_;

```javascript
/**
 * @type {Service}
 */
export default class Service {
  /**
   * @param {*} options
   */
  constructor (options) {
    this.options = options
  }

  /**
   * @param {*} options
   */
  static build (options) {
    return new this(options)
  }
}
```

##### src/service/helper.js

Apenas uma função `fake` para simular o delay da troca de contexto de da manipulação dos dados.

```javascript
/**
 * @type {Function}
 */
export const promise = response => {
  return new Promise(function (resolve) {
    window.setTimeout(() => resolve(response), 1000)
  })
}
```

A saída exibida nesse caso é algo parecida com a imagem abaixo.

<p align="center">
<img src="https://i.imgur.com/yu7cDKn.png">
</p>


Com o que fora apresentado até aqui não é difícil perceber que podemos usar essa estrutura para representar diversas estratégias de API’s porque não está fechado o que o nosso serviço consome. Essa deve ser a visão do componente acerca do service: conhecer o contrato e não a implementação.

> Embora o Javascript não tenha estruturas formais para contratos, é possível criar padrões para que a codificação componha esses contratos de forma orgânica.

Se quiser se aprofundar em abordagens de gestão de _services_ pode dar uma olhada no artigo [How not to suffer with APIs](https://itnext.io/how-not-to-suffer-with-apis-8aa75f890fe6) (dica que recebi do [Vinicius Reis](https://medium.com/@luizvinicius73)) onde é explorado em níveis bem profundos o uso do serviço como um modelo da entidade totalmente isolado da apresentação do componente.

### Lidando com Componentes
Bom, se o serviço agora é uma estrutura totalmente segmentada do meu componente, como posso fazer uso desse recurso dentro do componente? A resposta dessa pergunta também é uma pergunta: quão flexível será seu componente e quão dinâmica será sua estrutura?

#### Importando serviços para o meu componente
Essa estratégia é bem simples e consiste basicamente em usar os módulos Javascript para usar o _service_ dentro do escopo do seu componente.

```vue
<template>
  <table>
    <tr>
      <th>Name</th>
      <th>Price</th>
    </tr>
    <tr v-for="(row, key) in rows" :key="key">
      <td>{{ row['name'] }}</td>
      <td>{{ row['price'] | money }}</td>
    </tr>
  </table>
</template>

<script>
import { money } from 'src/support/formatter'
import Product from 'src/domains/Product/Service/Product'

const service = Product.build({})

export default {
  name: 'ProductTable',
  data: () => ({
    rows: []
  }),
  filters: {
    money: money
  },
  mounted () {
    service.read().then(rows => {
      this.rows = rows
    })
  }
}
</script>
```

Se precisar de uma estratégia mais eficiente de distribuir o service, pode usar um plugin para manipular o estado dele dentro do componente.

Seguindo essa abordagem teríamos o **ProductTable.vue**:
```vue
<template>
  ...
</template>

<script>
import { money } from 'src/support/formatter'
import Product from 'src/domain/product/service'

export default {
  name: 'ProductTable',
  service: Product.build({}),
  data: () => ({
    rows: []
  }),
  filters: {
    money: money
  },
  mounted () {
    this.$service.read().then(rows => {
      this.rows = rows
    })
  }
}
</script>
```

E teríamos uma modificação no protótipo do **_Vue_** através do **src/service/Plugin.js**:
```javascript
export default Vue => {
  Object.defineProperty(Vue.prototype, '$service', {
    get () {
      if (this.$options.service) {
        return this.$options.service
      }
      if (this.$props.service) {
        return this.$props.service
      }
      throw new Error('The component doesn`t have a service')
    }
  });
}
```

Com esta segunda abordagem, mesmo que algum desenvolvedor sem querer faça:
```javascript
this.$service = null
```
A resposta do **_Vue_** será contundente

<p align="center">
<img src="https://i.imgur.com/Zrz3W7H.png">
</p>

Com a implementação do _plugin_ feita dessa forma o _service_ é passado para o componente e então ele “descobre” se este é um item das opções do construtor da instância do **_Vue_** ou se é uma _prop_ do componente, entregando um elemento, que como vimos acima, é imutável; o que nos leva a próxima abordagem, passar os serviços via _props_.

#### Utilizando serviços como props
No ecossistema do **_Vue_** (na verdade é um conceito um pouco mais abrangente que isso) uma _prop_ é um estado que é passado para um componente.
Se não estiver recordando muito bem como funcionam essas propriedades dos componentes recomendo fazer uma [visita à documentação](https://vuejs.org/v2/guide/components-props.html) antes de continuar.

Com a leitura em dia será fácil compreender que usando _props_ tenho a capacidade de passar parâmetros para meus componentes sem ter que deliberadamente deixar esse parâmetro “hard-coded” dentro dele.

Para receber uma _prop_ dentro de um componente é preciso declarar essa necessidade. O resultado é semelhante ao exemplo a seguir:
```vue
<template>
  ...
</template>

<script>
...

export default {
  name: 'ProductTable',
  props: {
    service: {
      required: true
    }
  },
  ...,
  mounted () {
    this.$service.read().then(rows => {
      this.rows = rows
    })
  }
}
</script>
```

O que implicaria em um caso de uso semelhante à:
```html
<ProductTable v-bind:service="service"/>
```

Embora essa abordagem não seja ruim, ela possui alguns pontos que devem ser observados. Entre as situações que não me deixam confortável temos a questão de usar um estado do componente (uma propriedade no data) para abrigar o serviço que será mapeado à _prop_, e a necessidade imperativa de ter que criar um arquivo `.vue` para cada rota implementada.

#### Usando o Router para injetar dependência

Durante a construção de app’s mais robustos geralmente usamos um _router_. O **Vue Router** é uma ferramenta que faz parte do ecossistema do **_Vue_** e nos permite criar rotas para nossos componentes. Ele tem suporte a informar as _props_ que serão usadas para montar o componente e isto está descrito [neste trecho da documentação](https://router.vuejs.org/en/essentials/passing-props.html).

No caso do nosso exemplo, vamos explorar o [Function Mode](https://router.vuejs.org/en/essentials/passing-props.html#function-mode) onde as _props_ serão geradas por uma função que recebe a rota carregada como parâmetro. Com o _service_ sendo uma _prop_ poderemos passá-lo por parâmetro através da rota onde seu componente será montado.

Como podemos ver no exemplo abaixo, será possível combinar as duas abordagens no seu projeto. Poderemos usar um mesmo componente recebendo o __service__ por _props_ ou através de _$options_, _template_, _render_ ou _route_ porque o acesso ao _**$service**_ será transparente para o componente.

```javascript
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from 'src/components/HelloWorld'
import Service from 'src/domains/Product/Service/Product'
import Component from 'src/domains/Product/Components/ProductTable'

Vue.use(Router)

export default new Router({
  routes: [
    ...,
    {
      path: '/dashboard/products',
      component: Component,
      props: route => ({
        service: Service.build({})
      })
    }
  ]
})
```

## Conclusão
O _**Vue**_ é muito flexível e deixa à cargo da sua capacidade de manipulação do Javascript a criação do ecossistema em que o componente está inserido. Tenha sempre cuidado para escolher abordagens que te permitam escalar a sua aplicação de forma mais objetiva possível pesquisando e estudando o máximo que puder antes de começar a escrever seus códigos.
Ademais, você pode começar a fazer uso dessas metodologias para fazer seus _requests_ sem que seu componente perceba que algo mudou.

> Isolar o comportamento dos serviços é uma boa pedida em tempos onde estão surgindo opções interessantes para manipulação de dados, como o [GraphQL](https://graphql.org).

Fique à vontade para enviar suas dúvidas, sugestões e/ou elogios. Para falar mais sobre _**VueJS**_ fique ligado na comunidade e em todo o seu ecossistema : )

[VueJS Comunidades](https://github.com/vuejs-br/comunidades/blob/master/README.md)

Ah, já ia esquecendo, segue o link do repositório [https://github.com/wilcorrea/transparent-services](https://github.com/wilcorrea/transparent-services), fica a dica para seguir os commits que será possível ver a evolução da mesma forma que a estrutura foi evoluindo nos artigos.