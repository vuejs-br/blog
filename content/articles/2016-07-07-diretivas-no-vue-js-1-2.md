---
layout: post
title: 'Diretivas no Vue.js #1'
main-class: 'dev'
date: 2016-07-07 04:22:15 
color: '#637a91'
tags: vue-js diretivas
author: halfeld
---

Além do conjunto padrão de diretivas embarcadas, o Vue também permite registrar diretivas personalizadas que fornecem um mecanismo para alterações de dados mapeamendo o comportamento no DOM.

### O que é uma Diretiva?

Diretivas basicamente são extensões da linguagem HTML que permitem a implementação de comportamentos.

Ou seja, elas facilitam o trabalho fazendo com que você faça coisas que seria preciso escrever muito javascript por exemplo.

> Mas no Vue nós não já temos componentes?

bem... se você veio do angular, deve estar com essa dúvida(ou não :P), já que temos diretivas de UI também. 
No Vue temos componentes que definem _widgets_ e tem um comportamento associado a eles, e diretivas que modificam comportamento que podem ou não ser _widgets_. Essa definição é um pouco abstrata mas é uma forma de pensar.

### Criando uma diretiva

É possível criar uma diretiva usando `Vue.directive(id, definition)`, passando o identificador e o objeto de definição, mas antes de partimos para o código temos que entender uma coisa.

#### Hook Functions

O objeto de definição pode prover algumas _hook functions_(todas são opcionais):

+ bind - chamada uma vez quando a diretiva é ligado ao elemento.
+ update - chamada imediatamente após o `bind` com o valor inicial e sempre que há alterações de valor só que agora trazendo o novo valor e o antigo como argumento.
+ unbind - chamada uma vez quando a diretiva é desacoplada do elemento.

exemplo da documentação:

```javascript
Vue.directive('my-directive', {
  bind: function () {},
  update: function (newValue, oldValue) {},
  unbind: function () {}
});
```

uma vez registrada, você pode usar em seus _templates_ prefixando com `v-`

```html
<div v-my-directive="someValue"></div>
```

**quando você precisar somente do `update`, você pode passar somente uma função ao invés do objeto de definição**

dessa forma: 

```javascript
Vue.directive('my-directive', function(value) {})
```

### Propriedades de instancia

O objeto da diretiva disponibiliza uma serie de propriedades, são elas:

+ el - o elemento que a diretiva foi colocada.
+ vm - a instancia do Vue responsável pela diretiva.
+ expression - a expressão passada, excluindo filtros e argumentos.
+ arg - o argumento passado, se presente.
+ name - o nome da diretiva.
+ modifiers - um objeto com os modificadores, se o modificador estiver presente ele aparece no objeto como `true`
+ descriptor - um objeto contendo o resultado de análise de toda a diretiva.
+ params - um objeto contendo parâmetros vindos de atributos. 

um exemplo da própria documentação usando algumas dessa propriedades:

```html
<div id="demo" v-demo:hello.a.b="msg"></div>
```


```javascript
Vue.directive('demo', {
  bind: function () {
    console.log('demo bound!')
  },
  update: function (value) {
    this.el.innerHTML =
      'name - '       + this.name + '<br>' +
      'expression - ' + this.expression + '<br>' +
      'argument - '   + this.arg + '<br>' +
      'modifiers - '  + JSON.stringify(this.modifiers) + '<br>' +
      'value - '      + value
  }
})
var demo = new Vue({
  el: '#demo',
  data: {
    msg: 'hello!'
  }
})
```

o resultado desse código será

```
name - demo
expression - msg
argument - hello
modifiers - {"b":true,"a":true}
value - hello!
```

### Parâmetros

O compilador do Vue vai extrair os atributos do elemento que você colocar dentro do array `params`, segue o exemplo:

```html
<div v-example a="hi"></div>
```

```javascript
Vue.directive('example', {
  params: ['a'],
  bind: function () {
    console.log(this.params.a) // -> "hi"
  }
})
```

### Element Directives

Se você veio do angular é o equivalente ao `restrict : "A"`, que nada mais é do que a diretiva como elemento.

ao invés de usar assim: 

```html
<div v-my-directive></div>
```

usar assim:

```html
<my-directive></my-directive>
```

Element Directives não aceitam argumentos ou expressões, mas você pode ler os atributos para determinar o comportamento.

A grande diferença dessa diretivas é que uma vez encontradas pelo Vue, ele vai ignorar o elemento, fazendo com que a só a diretiva manipule ela e seus filhos.


### Literal Modifier

Quando a diretiva é usando com Literal Modifier, o atributo que for passado vai ser interpretado como uma string simples e vai ser passado diretamente para o método `update` que também vai ser chamado só uma vez, afinal o atributo não vai ser reativo.

```html
<div v-demo.literal="foo bar baz">
```

```javascript
Vue.directive('demo', function (value) {
  console.log(value) // "foo bar baz"
})
```

### Object Literals

Se sua diretiva precisa de muitos valores, é possível passar um objeto javascript.

```html
<div v-demo="{ color: 'white', text: 'hello!' }"></div>
```

```javascript
Vue.directive('demo', function (value) {
  console.log(value.color) // "white"
  console.log(value.text) // "hello!"
})
```

bem, isso é tudo pessoal, resolvi parar por aqui para não ficar cansativo, mas no próximo post vou abordar uma abordagem mais avançada, ainda tem bastante coisa de diretivas pra aprender!

