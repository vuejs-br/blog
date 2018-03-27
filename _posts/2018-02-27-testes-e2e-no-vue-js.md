---
layout: post
title: 'Automação de testes e2e no Vue.js'
main-class: 'dev'
date: 2018-02-27 17:03:42 
color: '#637a91'
tags: vue2 javascript e2e testes
layout: post
author: daniel
---

Hoje em dia muito se fala em fazer testes automatizados para seus sistemas, e isso é um fato concreto, se seu sistema não é testado computacionalmente a tendência de surgir *bugs* na produção é gigante.

Um dos maiores problemas ao pesquisar sobre tal área é a imensa quantidade de tipos de testes, o que deixa qualquer novato perdido. Com intuito de simplificar um pouco a abordagem da área, em 2009 Mike Cohn criou a [representação de uma pirâmide](https://www.mountaingoatsoftware.com/blog/the-forgotten-layer-of-the-test-automation-pyramid) que relaciona o custo e tempo dos principais tipos de testes:

![Pirâmide de testes - representação de Martin Fowler](https://martinfowler.com/bliki/images/testPyramid/test-pyramid.png)

Como é possível ver, quanto mais próximo do usuário é o teste, mais caro e lento ele será. Mas dado que o conceito foi criado em 2009, é possível ver mudanças nesse cenário?

Sim! Atualmente essa relação caiu bastante, pois com o surgimento de novas ferramentas para testes e2e a complexidade em sua construção teve uma queda livre. E isso acabou chamando a atenção de grandes empresas de consultoria, que possuem áreas destinadas ao teste de interface.

Recentemente tive a oportunidade de trabalhar na área e pesquisar mais sobre tais ferramentas, uma que me agradou bastante foi o [TestCafé](devexpress.github.io/testcafe). Que consiste em um framework feito em Node.js e que conta com sintaxe agradável, identificação de seletores de alguns frameworks front-end (vue, aurelia, angular e react) e [plataforma online paga](https://testcafe.devexpress.com) que lhe permite executar seus testes remotamente, com gravação e outros recursos. 

Agora que já temos uma introdução sobre o assunto, podemos começar a colocar a mão na massa! Nesse caso vamos criar uma aplicação simples, com um componente que captura uma mensagem do cliente e envia a outro componente.

Então, depois de executar `vue init webpack-simple testcafe-vue`, precisamos criar o componente `Sender.vue` para capturar a mensagem do cliente e enviar a partir de um evento:

```html
<template>
  <section>
    <label for="message">You:</label>
    <input v-model="message" @keydown.enter="$emit('submit', message)" id="message" autofocus/>
  </section>
</template>

<script>
export default {
  name: 'sender',
  data: () => ({
    message: null
  })
}
</script>
```

Precisamos fazer a outra ponta, o componente `Receiver.vue` vai apenas pegar uma mensagem por propriedade e mostra-la na tela formatando-a:

```html
<template>
  <small v-text="content" />
</template>

<script>
export default {
  name: 'receiver',
  props: ['message'],
  computed: {
    content() {
      return `Has received: ${this.message}`
    }
  }
}
</script>
```

> Note que os nomes dos componentes ignoraram o guia de estilo do Vue.js, eles não estão no padrão CamelCase, há um motivo para isso. Existe pequeno problema no plugin do Vue para a ferramenta de testes que vamos usar, o qual já mandei *pull request* corrigindo, mas ainda não foi visto.

Por fim, no `App.vue` vamos fazer uma ponte entre os dois componentes, declarando-os e ouvindo o evento disparado pelo `sender` para pegar o resultado e transmitir ao `receiver` via propriedade:

```html
<template>
  <div id="app">
    <sender @submit="signup" />
    <receiver :message="clientMessage" />
  </div>
</template>

<script>
import Receiver from './components/Receiver.vue'
import Sender from './components/Sender.vue'

export default {
  name: 'app',
  components: { Receiver, Sender },
  data: () => ({
    clientMessage: null
  }),
  methods: {
    signup(message) {
      this.clientMessage = message
    }
  }
}
</script>
```

Agora sim! Temos uma aplicação base funcionando, ao escrever uma mensagem e pressionar Enter, ela é mostrada no outro componente, simples não? Para iniciar os testes, vamos instalar o TestCafé e o plugin do Vue para ele, com o comando:

```
npm i -D testcafe testcafe-vue-selectors
```

Para terminarmos de configurar o ambiente de testes, temos que editar um pouco o arquivo `package.json`. Precisamos criar o comando `test` para rodar o testes e o comando `test-server` para iniciar um servidor de testes, e nesse caso, vou criar uma variável `baseURL` declarando o domínio da aplicação para usa-lo nos testes. O resultado deverá parecer com isso:

```json
{
  "name": "testcafe-vue",
  ...
  "baseURL": "http://localhost:8080",
  "scripts": {
    ...
    "test-server": "webpack-dev-server",
    "test": "testcafe chrome tests --app 'npm run test-server' --app-init-delay 10000"
  },
  ...
}
```

Note que o comando `test` executa o comando `testcafe ` usando navegador `chrome` para rodar os testes do diretório `tests` (que vamos criar a seguir). Além disso, usamos algumas flags, como a `app` para definir um comando para iniciar o sistema e o `app-init-delay` para esperar a resposta do comando de inicialização por no máximo 10 segundos.

> Você pode alterar o navegador a executar os testes, colocando `all` para executar em todos navegadores instalados, ou então definir outro, para isso execute o comando `testcafe -b` para ver a lista de navegadores disponíveis.

Chegou a hora! Vamos criar nossos testes, para isso, na raiz do projeto crie o diretório `tests` e dentro dele o arquivo `transmitter.test.js`. Nele teremos dois testes, o primeiro enviando a mensagem sem qualquer valor e o segundo escrevendo um texto qualquer e enviando para verificar o retorno:

```javascript
import VueSelector from 'testcafe-vue-selectors'
import scenario from '../package.json'

fixture`trasmitter-message`.page`${scenario.baseURL}`

const receiver = VueSelector('receiver')
const sender = VueSelector('sender')

test('Message without content', async t => {
  await t
    .pressKey('enter')
    .expect(receiver.innerText).contains('null')
})

test('Message with content', async t => {
  const message = 'hello, how are you?'

  await t
    .typeText(sender.find('#message'), message)
    .pressKey('enter')
    .expect(receiver.innerText).contains(message)
})
```

No ínicio temos uma sintaxe um pouco distinta, a `fixture` define um recurso do sistema, normalmente uso um padrão para definir esse nome, pois podemos rodar um comando do TestCafé para executar determinadas `fixture`. Logo após isso, temos que definir a página do recurso, no caso peguei a que declarei no `package.json` (não sei se isso é recomendável, mas é prático!).

Após isso, declaramos os elementos ou componentes que vamos usar no teste, usamos o plugin `testcafe-vue-selectors` para procurar os elementos do DOM baseado nos nomes dos componentes Vue. Esse código ainda pode melhorar, mas ficará para um artigo do futuro...

Em seguida temos de fato os testes, compostos por um nome e uma função assíncrona (pois ele deve esperar os elementos aparecerem no navegador), nessa função temos a variável `t` com todas as ações possíveis. Onde:

- No primeiro teste apenas pressionamos Enter e vemos se o elemento do componente `receiver` recebeu o valor nulo.
- No segundo teste digitamos uma mensagem no input do componente `sender`, pressionamos Enter e verificamos o valor final do `receiver`.

Agora podemos executar o comando `npm run test` para executar esses dois testes, a partir disso você verá o navegador ser aberto e o teste ser executado (você pode não ver essa parte por ser muito rápido). No final, teremos a mensagem falando que os testes dessa `fixture` passaram:

![Testes passando](/content/images/2018/02/DeepinScreenshot_select-area_20180227135252.png)

Finalmente os testes passaram, e com isso o fim desse artigo também! Espero que esse artigo tenha aberto um pouco  conceito desse tipo de testes, que são poucos explorados mas com grandes vantagens.

Caso tenha alguma dúvida, sugestão ou critíca deixe nos comentários. Também aceito novos assuntos para poder estar abordando ;)
