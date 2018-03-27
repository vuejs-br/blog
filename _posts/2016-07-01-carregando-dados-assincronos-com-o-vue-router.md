---
layout: post
title: 'Carregando dados assíncronos com o Vue-router'
main-class: 'dev'
date: 2016-07-01 11:41:01 
color: '#637a91'
tags: vue-router vue-js
layout: post
author: 5
---

Que o **Vue-router** é poderoso, isso nós já sabemos, correto? 
> **Não, você não conhece ainda o Vue-router?**   
Então dá uma olhada [nesse artigo](http://www.vuejs-brasil.com.br/vue-router/) publicado por *Vedovelli* sobre o Vue-router de maneira prática e bem explicada, para você poder já por em prática aplicações mais complexas com Vue.js.  

Uma dúvida de quando se utiliza o Router em seus componentes, é sobre o carregamento assíncrono de dados, ou seja, quando utilizamos de dados externos para montar o componente que está sendo invocado.

Assim que o Vue-router está instalado em sua aplicação Vue, desta maneira:
```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)	// Instalação
...
```

Ficará disponível em todos os componentes o objeto route, com ele podemos chamar os denominados **Transition Hooks** (Ganchos de transição, traduzindo ao pé da letra), que são métodos chamados de acordo com o estado de carregamento do componente na rota utilizada.

Você pode ver todos os hooks disponíveis através desse link: [Transition hooks](http://router.vuejs.org/en/pipeline/hooks.html).

```
...
module.exports = {
    // outras opções
    route: {
       // Aqui chamamos os hooks
    }
}
```

Com isso, temos em mente que devemos executar tarefas assíncronas dentro dos ganchos, fazendo com que a transição só continue até que seja resolvida uma *Promise* ou quando chamarmos um método para ir ao próximo passo.

O gancho recomendado é o **data hook**, com ele é possível carregar e definir dados no componente atual. Ele é chamado após que o **activate hook** for resolvido e também quando a rota for alterada, mesmo o componente atual sendo reutilizado.

Veja o exemplo abaixo e sua explicação, utilizaremos a função `setTimeout` para simular uma mudança assíncrona:

```
<template>
  <div class="hello">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
module.exports = {
    data () {
      return {
          message: 'Loading'
      }
    },
    route: {
       data (transition) {
          setTimeout(() => {
            transition.next({
              message: 'Hello world'
            })
          }, 3000)
       }   
    }
}
</script>
```

**transition**: É um argumento (Object) que estará disponível em todos os hooks, com ele podemos redirecionar, abortar, prosseguir, dentre outros.   
Veja nesse link os métodos possíveis de utilizar no objeto transition [Transition Object](http://router.vuejs.org/en/pipeline/hooks.html#transition-object)

**transition.next**: Avança para o próximo passo da transição. Esse método faz possível atualizar o objeto data do componente mantendo a reatividade, passando um objeto e efetuando a alteração.

*OBS: O data hook que está no objeto route é um mixin, fazendo automaticamente a mesclagem com o método data do componente.*

Quando a rota for acessada, o valor inicial de `message: 'Loading'`, como mostra abaixo:
![](/content/images/2016/06/async-com-vue-router.png)

Após 3 segundos, devido ao `setTimeout` a transição irá prosseguir e o valor de `message` sofrerá a mudança e passará a ter o valor de `message: 'Hello world'`
![](/content/images/2016/06/async-com-vue-router-2.png)

Existe também a maneira para só renderizar o componente por completo quando os dados estiverem disponíveis, para isso basta adicionar a propriedade `waitForData` e defini-la como `true`.

```
//...
module.exports = {
    data () {
      return {
          message: 'Loading'
      }
    },
    route: {
       data (transition) {
          setTimeout(() => {
            transition.next({
              message: 'Hello world'
            })
          }, 3000)
       },
       waitForData: true   
    }
}
```

 
### Carregando através de Promise
Retornar uma *Promise* é opcional, mas é possível aproveitá-la em todos os transition hooks. Com a particularidade de utilizar o `resolve` e o `reject` da *Promise* para respectivamente `prosseguir` ou `abortar` com o carregamento do componente e seus dados.

Cada gancho que utilizar *Promise* só será resolvido quando a mesma for resolvida, se com sucesso, prossegui automaticamente, porem se houver falha, será necessário chamar o método `transition.abort()` *para retornar a rota anterior*, ou por exemplo `transition.redirect('/404')` *enviando o usuário para uma página (rota) de erro*.

Veja esse exemplo tirada da documentação:
```
...
route: {
     canActivate () {
        return authenticationService.isLoggedIn()
     },
     activate (transition) {
         let vm = this
         let params = transition.to.params
         return messageService
           .fetch(`url/to/api/message/${params.messageId}`)
           .then((message) => {
              vm.message = message
         })
     }
}
```

Dessa forma, em algum momento utilizando o Vue-router você irá deparar-se com algumas situações, mas esse add-on é potente e muito bem desenvolvido, tendo diversas soluções para a maioria dos problemas que encontraremos.

Espero ter ajudado você antecipadamente ou ate mesmo com o seu atual problema, qualquer dúvida ou contribuição, somando ainda mais conhecimento a essa postagem, deixa seu comentário.


