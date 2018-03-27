---
layout: post
title: 'Como funciona a reatividade no Vue.js'
main-class: 'dev'
date: 2016-08-22 01:30:00 
color: '#637a91'
tags: vue-js observer-pattern reatividade
layout: post
author: 6
---



Esse tema é um tanto avançado, demanda um pouco pouco de _design pattern_ em Javascript e saber como funciona a sua cadeia de protótipos, porém vou tentar ser o mais didático o possível para que vocês entendam sem maiores problemas.

Prevejo que, se surgir grandes dúvidas aqui seu problema provavelmente é com Javascript e não com Vue, então partiu estudar :D

Entender como Vue funciona é indispensável para por exemplo saber resolver certas armadilhas como a [situação](http://www.vuejs-brasil.com.br/imprevistos-com-libs-de-terceiros-c3-js/) do [Vinicius](http://www.vuejs-brasil.com.br/author/vinicius/) com a Lib D3, que por sua vez, tinha conhecimento do funcionamento e resolveu o problema tranquilamente.

### Reactive System

Esse sistema funciona da seguinte forma, quando você passa um objeto para o atributo `data` da instância do Vue, ele percorre as propriedades transformando-as em `getters/setters` usando o [Object.defineProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty).

Cada diretiva ou data binding no template, corresponderá a um **watcher object** que irá guardar as propriedades durante a avaliação de dependências(o que pegar no `getter` para amostrar na view). Quando o `setter` for chamado, o **watcher object** vai reavaliar as dependências que causará o update na view.

Aqui para você entender melhor tem uma imagem da própria documentação

![Reactive System](/content/images/2016/08/vue.png)


### Observer Pattern

Para fazer o loop funcionar sem problemas, o Vue usa o **Observer Pattern** que basicamente consiste em você ter um Objeto(conhecido como **Subject**) manter uma lista de Objetos(conhecido como **Observers**) dependendo dele, podendo tanto remover Observers ou adicionar novos, sempre que o Suject precisa notificar uma coisa importante que esteja acontecendo, é transmitido a notificação para os Observers.

![](/content/images/2016/08/vue-5.png)

Olhando no código fonte para entender mais, temos Observer criando o `__ob__` com a `function` `def`, que é onde fica praticamente toda reatividade.

```javascript
export function Observer (value) {
  this.value = value
  this.dep = new Dep()
  def(value, '__ob__', this)
  if (isArray(value)) {
    var augment = hasProto
      ? protoAugment
      : copyAugment
    augment(value, arrayMethods, arrayKeys)
    this.observeArray(value)
  } else {
    this.walk(value)
  }
}
```

Na `function` `def` temos a implementação de `Object.defineProperty`
```javascript
export function def (obj, key, val, enumerable) {
  Object.defineProperty(obj, key, {
    value: val,
    enumerable: !!enumerable,
    writable: true,
    configurable: true
  })
}
```

Aquele `this.dep = new Dep()` nada mais é do que o Subject, então sabendo que você manja dos paranauês do design pattern vamos olhar um de seus métodos, o `notify`

```javascript
Dep.prototype.notify = function () {
  // stablize the subscriber list first
  var subs = toArray(this.subs)
  for (var i = 0, l = subs.length; i < l; i++) {
    subs[i].update()
  }
}
```

como você pode ver, sempre que ele notar um `setter` sendo chamado, ele irá chamar o `notify` para percorer a lista de Observers chamando também a `function` `update` para atualizar a view.

### Definindo reativo

Existe uma `function` no código fonte que é chamada de `defineReactive`, nela é onde acontece a criação dos `getters/setters`.

```javascript
export function defineReactive (obj, key, val) {
  var dep = new Dep()

  var property = Object.getOwnPropertyDescriptor(obj, key)
  if (property && property.configurable === false) {
    return
  }

  // cater for pre-defined getter/setters
  var getter = property && property.get
  var setter = property && property.set

  var childOb = observe(val)
  Object.defineProperty(obj, key, {
    enumerable: true,
    configurable: true,
    get: function reactiveGetter () {
      var value = getter ? getter.call(obj) : val
      if (Dep.target) {
        dep.depend()
        if (childOb) {
          childOb.dep.depend()
        }
        if (isArray(value)) {
          for (var e, i = 0, l = value.length; i < l; i++) {
            e = value[i]
            e && e.__ob__ && e.__ob__.dep.depend()
          }
        }
      }
      return value
    },
    set: function reactiveSetter (newVal) {
      var value = getter ? getter.call(obj) : val
      if (newVal === value) {
        return
      }
      if (setter) {
        setter.call(obj, newVal)
      } else {
        val = newVal
      }
      childOb = observe(newVal)
      dep.notify()
    }
  })
}
```

O `dep.depend()` é apenas ele definindo os Obeservers, olhe o código:

```javascript
Dep.prototype.depend = function () {
  Dep.target.addDep(this)
}
```

e alí no finalzinho do `setter` você vê ele chamando o `notify` para atualizar a view.

### Olhando em ação

Para você ver isso, basta criar alguma coisa em `data` e no `ready` colocar um `console.log`, assim:

```javascript
new Vue({
  el: '#app',
  data: {
    people: {
      name: 'Igor',
      age: 18,
      location: {
        lat: 19419812341,
        lng: 19203819483
      }
    }
  },
  ready () {
    console.log(this.people)
  }
})
```

e ele vai amostrar isso:

![](/content/images/2016/08/vue-6.png)

aí você consegue ver tanto o `__ob__` com a propriedade `dep` nele com seus métodos de Suject no prototipo quanto os `getters/setters`, e além dos **watcher object**.


### Considerações

Levantando algumas observações...

#### Inicializando sua `data`

Devido a limitação do ES5, o Vue não consegue deletar e nem adicionar propriedades, o processo de conversão para `getters/setter` acontece na inicialização, por isso a propriedade deve estar presente em data mesmo que seja apenas uma String vazia, assim ele consegue tornar Reativo.

Porém há um jeito de adicionar propriedades, esse jeito é o `$set`, com ele você pode adicionar propriedades depois da inicialização, sua syntax é `$set(path, value)`, é claro que é melhor definir a propriedade logo no inicio, tanto pra servir como Schema quanto para ter a reatividade logo de cara, porém você vai usar o `$set` para quando quiser tornar algo vindo de uma chamada Ajax Reativo por exemplo.

#### Computed Properties

As computed properties não tem apenas `getters`. Elas mantem sua própria lista de dependências, isto porquê elas tem cache, isso mesmo! Este valor em cache só é trocado quando existem mudanças, por tanto, enquanto as depedências não mudam, o valor retornado vai ser o do cache ao inves do `getter`

> Mas para que eu preciso de cache aí?

Imagine que você tem uma computed property  **A** maior... mais expressiva..., que por sua vez dependênde de um Array grande. E então você tem uma computed property **B** que dependênde de **A**. Isso poderia chamar o `getter` de **A** mais vezes que o necessário.

Por causa desse cache o `getter` acaba não sendo sempre chamado.

Vamos olhar esse comportamento em ação com um _timestamp_:

```javascript
var vm = new Vue({
  el: '#app',
  data: {
    msg: ' Igor!'
  },
  computed: {
    example: {
      cache: false,
      get: function () {
        return Date.now() + this.msg
      }
    }
  }
})

console.log(vm.example)
```

com o cache para `false` você terá um _timestamp_ diferente do amostrado no `console`. O `get` ali consegue demostrar legal o funcionamento do cache, já que cada chamada a função ele é chamado.

Então é isso ae pessoal, como eu falei, se o que você viu aqui foi algo de outro mundo, o seu problema provavelmente é Javascript e não o Vue ;)
Não adianta procurar aprender um framework, uma biblioteca sem saber a linguagem por tras(apensar que tem gente até hoje que usa jQuery pensando que é linguagem :P).
