---
layout: post
title: 'Comunicação com web services'
main-class: 'dev'
date: 2016-07-07 22:29:00 
color: '#637a91'
tags: vue-js vue-resource
layout: post
author: vedovelli
---

Sabemos que uma interface, por melhor que seja, não é nada útil se os dados por ela gerenciados não forem salvos num banco de dados. Infelizmente utilizar os recursos do browser para salva-los é inviável, pois os dados estariam disponíveis apenas para o próprio usuário. A verdade é que desenvolvemos sistemas para compartilhar informações com outras pessoas e para isso precisamos de um local centralizado para armazenar e acessar estas informações.

A natureza de uma aplicação de browser é que toda a interação com os dados é feita em memória e no computador do usuário. Desde o *input*, passando pela validação, modificação e indo até a publicação das informações, tudo é feito pelo Javascript que é interpretado pela *engine* existente no navegador. Para salvar é preciso enviar a um servidor.

O Vue.js é mestre em levar a informação de um lado a outro porém não é sua responsabilidade persistir a informação e torna-la disponível para outros clientes. Assim, depende de um *web service* para desempenhar este papel. Atualmente o tipo mais comum de *web service* é o [**REST**](https://pt.wikipedia.org/wiki/REST) e os dados são trafegados codificados com [**JSON**](https://pt.wikipedia.org/wiki/JSON).

Muitos *frameworks* Javascript já trazem por padrão uma biblioteca para se comunicar com um *web service*, comunicação que é feita utilizando [**AJAX**](https://pt.wikipedia.org/wiki/AJAX_(programa%C3%A7%C3%A3o)) mas este não é o caso do Vue.js: seu *core* contém apenas o necessário para implementar o padrão [**MVVM**](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel) e então é necessário incluir uma biblioteca que proverá recursos para a comunicação.

Felizmente o próprio time de desenvolvimento disponibiliza uma excelente opção para chamadas AJAX: trata-se do Vue-resource, que pode ser facilmente instalado com o comando `npm i --save vue-resource`. Sua configuração também é bem simples, bastando importa-lo e informar ao Vue Object que ele utilizará a biblioteca. Vejamos como fica ao utilizar o Vue com um *module bundler*...

```javascript
import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

new Vue({
    el: 'body'
})
```

>**Dica**: caso você inclua tanto o Vue quanto o Vue-resource via tag `<script>` então não será necessária a utilização de `Vue.use(VueResource)` uma vez que a biblioteca reconhece o Vue no objeto **window** e se auto-instala.

Após estes passos simples de configuração você ganha a propriedade `$http` em todos os seus componentes, podendo então utiliza-la para suas chamadas. Os métodos retornam [Promises](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Promise) e então métodos `then()` e `catch()` podem ser encadeados para finalizar o processamento da requisição.

```javascript
export default {
    ready () {
        this.$http.get('http://webservice-url').then(res => {
            // faça algo com o retorno do web service
        })
    }
}
```

>O Vue-resource é a biblioteca de comunicação mais utilizada com o Vue.js

*"- Mas eu preciso utilizar esta biblioteca? Gosto tanto de jQuery!"* ^.^

A resposta é simples: **o Vue.js não te obriga a nada**. Sim você pode usar jQuery ou até mesmo outra, como [superagent](https://github.com/visionmedia/superagent). 

No caso de jQuery basta fazer o include numa tag `<script>` e então o objeto jQuery estará disponível como propriedade do objeto **window**.

```javascript
export default {
    ready () {
        window.jQuery.get('http://webservice-url', res => {
            // faça algo com o retorno do web service
        })
    }
}
```

ou simplesmente...

```javascript
export default {
    ready () {
        $.get('http://webservice-url', res => {
            // faça algo com o retorno do web service
        })
    }
}
```

Caso você opte por incluir jQuery utilizando **npm** e seu *module bundler* predileto então você provavelmente já sabe como tornar jQuery disponível para seus scripts. O mesmo vale para outra biblioteca, como a citada **superagent**.

Para finalizar segue um exemplo funcional utilizando Vue-resource:

<iframe width="100%" height="450" src="//jsfiddle.net/danielschmitz/kz8de1kp/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

E assim a vida segue, com o Vue.js tornando nossa vida muito mais fácil de ser vivida.

Obrigado por ter lido,

[Vedovelli](http://vedcasts.com.br)
