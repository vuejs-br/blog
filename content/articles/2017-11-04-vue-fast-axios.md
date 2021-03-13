---
layout: post
title: 'Contatando APIs de maneira fácil com o vue fast axios'
main-class: 'dev'
date: 2017-11-04 18:52:34 
color: '#637a91'
tags: vue2 axios
layout: post
author: leonardovilarinho
---

Olá pessoal, nesse artigo estarei mostrando um plugin bem simples que desenvolvi, o mesmo foi criado com intuito de facilitar o envio e validação de requisições no Vue.js.

O `vue-fast-axios` nada mais é que um *wrapper* para a biblioteca *axios*, permitindo que você use o *axios* sem muitas configurações adicionais e dores de cabeça.

Antes de iniciar, é preciso instalar no seu projeto o `babel-polyfill`, ele permite que trabalhemos com métodos assíncronos usando as palavras reservadas `async/await`:

```shell
npm install babel-polyfill --save
```

Para habilita-lo no *webpack*, devemos informar esse plugin no campo de `entry` do arquivo *webpack.config.js*:

```json
entry: ['babel-polyfill', './src/main.js'],
```

Agora sim, executamos `npm install vue-fast-axios --save` e importamos o plugin para usar no Vue.js:

```javascript
import VueFastAxios from 'vue-fast-axios'
Vue.use(VueFastAxios)
``` 

A partir disso, o plugin registra um método de instância chamado `$serviceFactory`, como o próprio nome dita, ele é uma fábrica de serviços, devemos passar como parâmetro para ele a classe esqueleto do serviço e o componente Vue onde ele irá trabalhar.

Mas antes de criar um serviço temos que criar o esqueleto do mesmo, esse esqueleto irá setar as configurações a serem seguidas. Vamos criar o arquivo `src/esqueletos/PessoasEsqueleto.js`:

```javascript
'use strict'

// Exportando a classe do esqueleto
export default class PessoasEsqueleto {
  
  // definição da raiz da nossa API
  base() {
    return 'https://vuefastaxios.firebaseio.com/'
  }
  
  // define e retorna um objeto com as rotas da API que temos para esse objeto
  routes() {
    return {
      raiz: { // raiz é o nome da rota
        methods: 'get,post', // métodos aceitos na rota
        path: 'peoples.json' // caminho da rota
      },
      pessoas: {
        methods: 'put,delete',
        path: 'peoples'
      }
    }
  }
  
  // métodos são assíncronos e servem como atalho para as rotas,
  // devem ser usados quando você tem uma resposta importante da
  // API, como uma lista de pessoas
  methods() {
    return {
      lista: { // lista é o nome do método
        method: 'get', // método HTTP a usar na requisição
        route: 'raiz' // rota a ser usada na requisição
      }
    }
  }
  
  // No método validation podemos criar validações para
  // os atributos do objeto pessoa, que possui nome e chave
  validation() {
    return {
      name: { // name é o atributo a ser validado
        // o método validator retorna um boolean com o 
        // resultado da validação
        validator: function (v) {
          return v.length > 2
        },
        // mensagem de erro, quando validação é false
        message: 'Nome está errado'
      },
      
      // podemos colocar direto o validador, assim a mensagem 
      // de erro será a padrão desse esqueleto
      key: function (v) {
        return v > 0
      }
    }
  }
  
  // método que define a mensagem de erro padrão desse esqueleto, sempre
  // que uma validação sem mensagem falhar essa mensagem será retornada
  defaultVMessage() {
    return 'Erro ao manipular pessoas'
  }
}
```

Note que no esqueleto definimos apenas o que nosso backend possui, vinculando esses recursos a métodos ou objetos, além disso, temos a validação dos dados enviados a ele.

*PS:* estou usando o Firebase como rest api, logo os links usados são:

- GET | POST -> https://vuefastaxios.firebaseio.com/peoples.json
- PUT | DELETE-> https://vuefastaxios.firebaseio.com/peoples/{key}.json

Agora no componente `App`, vamos de fato criar o serviço, inicialmente vamos apenas mostrar os dados:

```html
<template>
  <div id="app">
    <!-- Barra de status, exibe carregando ou a mensagem retornada -->
    <strong v-if="carregando">Carregando...</strong>
    <strong v-else>{{ mensagem }}</strong>

    <!-- Lista de pessoas -->
    <ul>
      <li v-for="(pessoa, chave) in pessoas" :key="chave">
        {{ pessoa.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import PessoasEsqueleto from './esqueletos/PessoasEsqueleto'

export default {
  name: 'app',
  data: () => ({
    servico: null,
    mensagem: '',
    pessoas: [],
    carregando: false,
  }),
  // cria o serviço passando o esqueleto e o componente atual, após isso
  // chama o método para carregar a lista
  mounted() {
    this.servico = this.$serviceFactory(new PessoasEsqueleto, this)
    this.carregar()
  },
  methods: {
    // método assíncrono que carrega a lista, além de manipular 
    // a variável de estado 'carregando', lista de pessoas
    // aguarda o retorno da requisição no método 'lista'
    // do esqueleto definido
    async carregar() {
      this.carregando = true
      this.pessoas = await this.servico.call('lista')
      this.carregando = false
    },
    validationError(mensagem) {
      this.mensagem = mensagem
      this.carregando = false
    }
  }
}
</script>
```

*PS:* Estou usando o mesmo banco que o plugin, então pode ser que a lista de pessoas venha vazia no exemplo.

Note que declarei o método `validationError` mas nem usei ele em lugar algum, o plugin obriga que declaremos esse método, pois ele será chamado sempre que houver um erro de validação naquele serviço.

Agora vamos criar novas pessoas na lista, para isso, crie um formulário antes da lista de pessoas:

```html
<section v-if="!carregando">
  <input v-model="novaPessoa" placeholder="Adicionar nova pessoa..." />
  <button @click="criarPessoa">Criar</button>
</section>
```

No `data` inicie a variável `novaPessoa` com uma string em branco, e então declare os métodos `criarPessoa`, `serviceSuccess` e `serviceError`:

```javascript
criarPessoa() {
  this.carregando = true
  // chama com o método POST (pos()) a rota 'raiz' passando o nome
  this.servico.pos().execute('raiz', { name: this.novaPessoa })
},
serviceSuccess(data) {
  this.mensagem = 'Lista foi atualizada!'
  this.carregando = false
  this.carregar()
},
serviceError(error) {
  this.mensagem = 'Erro desconhecido'
  this.carregando = false
},
```

Note que tivemos que criar dois métodos, o plugin nos obriga a cria-los para manipular o retorno de todas requisições com retornos não importantes do serviço. Em caso de erro na requisição o método `serviceError` será chamado, em caso de sucesso será chamado o `serviceSuccess`.

Note também que ao tentarmos cadastrar uma pessoa com o nome menor ou igual a 2 caracteres será retornada a mensagem de erro daquele validador (no exemplo online esqueci de colocar isso, desculpem-me :$).

Para ter um crud completo está faltando as opções de edição e remoção, mas para o post não ficar longo, não irei mostrar o passo a passo, e sim apenas como ficaria a linha do método `apagar` e `editar` que contata o serviço criado.

Para apagar uma pessoa, usaremos o método `execute`, pois não estamos importando com o conteúdo do retorno, mas apenas se houve erro ou não. Uma novidade aqui é o método `append`, que irá concatenar a string passada para ele no final do link da requisição. Por exemplo: *meusite.com/caminho-da-rota/chave.json*

```javascript
this.servico.append(`/${chave}.json`).del().execute('pessoas')
```

Fazemos exatamente o mesmo para editar uma pessoa, apenas alterando o método para PUT e enviando um parâmetro:

```javascript
 this.servico.append(`/${chave}.json`).put().execute('pessoas', {name: this.novoNome})
```


No final teremos um CRUD bem parecido [com esse](https://leonardovilarinho.github.io/vue-fast-axios). Você pode relatar problemas ou dar sugestões tanto nos comentários ou nas issues do [repositório](https://github.com/leonardovilarinho/vue-fast-axios). (veja outros recursos do plugin no readme do repostório também :D)

Caso você possua dúvidas em qualquer neste ou em outro assunto relacionado ao Vue.js, sugira novas postagens nos comentários que atenderei na medida do possível.

