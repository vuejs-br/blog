---
layout: post
title: 'Vue.js para desenvolvedores AngularJS – Parte 1 (Lógica de templates)'
main-class: 'dev'
date: 2016-07-12 11:53:23 
color: '#637a91'
tags: 
layout: post
author: 5
---

*Separei esse post inicialmente em 5 partes, para não ficarem muito extensos e poder utilizar de bastantes exemplos no decorrer da postagem, espero que curtam.*

[Lógica de templates (Parte 1)](http://www.vuejs-brasil.com.br/vue-js-para-desenvolvedores-angularjs-parte-1-logica-de-templates/) - Atual   
[Componentes e Estados (Parte 2)](http://www.vuejs-brasil.com.br/vue-js-para-desenvolvedores-angularjs-parte-2-components-e-states/)  
Comunicação de componentes (Parte 3) - em breve  
Métodos de lifecycle (Parte 4) - em breve  
Demais e não menos importantes (Parte 5) - em breve 

## Breve introdução
Começo esse artigo explicando que meu intuito não é fazer você deixar de utilizar o AngularJS e começar a utilizar Vue.js.
Mas bem que deverias :D

Brincadeiras à parte, abordarei um compilado de familiaridades entre essas tecnologias e que servirá como um ponto de partida para você desenvolvedor AngularJS fazer uma migração ou até mesmo começar a desenvolver com Vue.js. E o melhor, com uma curva de aprendizagem super rápida.

O Vue.js é um lib focada em ViewModel e apropriada para o desenvolvimento de interfaces web modernas e interativas. Altamente flexível, pois com ele podemos combinar várias outras libs que gostamos de utilizar, proporcionando um maior poder no desenvolvimento.

E não podemos esquecer que o Vue.js foi também inspirado no AngularJS, porem com melhorias perceptíveis quanto a agilidade no desenvolvimento, melhorias do Two-way bindind com uma checagem mais limpa que a do AngularJS e um melhor desempenho, principalmente por não ter a sobrecarga que pode vim em Frameworks maiores como o AngularJS.

> Saiba mais neste artigo esclarecedor do Vinicius: [Por que Vue.js é uma boa opção](http://www.vuejs-brasil.com.br/por-que-vuejs-e-uma-boa-opcao/)

Para as similaridades vamos nos basear na versão (v1.0.24) do Vue.js e na (v1.5.5) do AngularJS.

> Para complemento deste, leia também o artigo que o Vedovelli detalhou [cada propriedade de um Vue Object](http://www.vuejs-brasil.com.br/o-que-e-cada-propriedade-num-vue-object/)

## Lógica de templates
#### Interpolação de texto
A interpolação de texto ocorre em ambos utilizando  **Mustaches** que são conhecidos também como *Double Curly Braces* ou simplesmente *Chaves duplas*
```language-html
<!-- AngularJS / Vue.js -->
<h1>{{ msg }}</h1>
```
Dentro dos *mustaches* podemos utilizar quaisquer expressões javascript, neste caso foi usada uma variável. 
*Tanto o AngularJS quanto o Vue.js saberá interpretar essas expressões.*

<iframe width="100%" height="300" src="//jsfiddle.net/q4pv6c22/2/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

#### Bind de texto por diretiva
Também podemos utilizar diretivas para substituir o textContent (TextNode) pelo valor da expressão informada na diretiva.
```language-html
<!-- AngularJS -->
<h1 ng-bind="msg"></h1>
```
```language-html
<!-- Vue.js -->
<h1 v-text="msg"></h1>
```

Por que isso é legal? Por oferecer um desempenho melhor e também por evitar o **FOUC (Flash of Uncompiled Content)**, se nunca ouviu falar, você pode não está ligando o nome ao problema, mas você já percebeu quando acessamos uma página e devido ao código ainda não ter sido analisado completamente, vemos os *Mustaches = {{ expression }}* para depois o valor devidamente compilado da expressão após a compilação completada.

<iframe width="100%" height="300" src="//jsfiddle.net/fmmo88t2/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

#### Saída de HTML puro
Tenha a maior consciência do que terá na saída do seu HTML, pode ser muito perigoso, pois facilita alguns ataques. Use primordialmente para dados confiáveis.
```language-html
<!-- AngularJS -->
<div ng-bind-html="html"></div>
```
```language-html
<!-- Vue.js -->
<div>{{{ html }}}</div>

<!-- igual a -->
<div v-html="html"></div>
```
<iframe width="100%" height="300" src="//jsfiddle.net/9qr3z78t/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

#### Ligar dados em saída HTML
Ambos não tratam a ligação de dados na saída do HTML puro, porem é possível utilizar:
- **$compile** no AngularJS  
- **partial** no Vue.js

Veja esse exemplo básico usando partial no Vue.js
<iframe width="100%" height="300" src="//jsfiddle.net/9bu5rp9d/2/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

#### Filtros
Os filtros são utilizados na transformação de dados que serão exibidos para o usuário, em ambos é utilizado como separador o símbolo **pipe |**.

> Para saber mais sobre os [Filtros com Vue.js](http://www.vuejs-brasil.com.br/usando-e-criando-filtros-com-vue-js/), veja neste artigo incrível feito pelo Daniel Schmitz, autor do livro [**Vue.js na prática**](https://leanpub.com/livro-vue).

```language-html
<!-- AngularJS / Vue.js -->

<!-- Filtro simples -->
<h1>{{ msg | uppercase }}</h1>

<!-- Múltiplos filtros -->
<h1>{{ msg | lowercase | reverse }}</h1>
```
O filtro *reverse* não é padrão no Vue.js, mas veja nesse exemplo como é fácil criar um filtro.
<iframe width="100%" height="300" src="//jsfiddle.net/2xaqc5xu/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>


#### Filtros com argumentos
Diferente do exemplo anterior, quando se trata de filtros com argumentos existem algumas particularidades na sintaxe.
```language-html
<!-- AngularJS -->
<span class="price">{{ price | currency : 'R$' : 2 }}</span>
```
```language-html
<!-- Vue.js -->
<span class="price">{{ price | currency 'R$' 2 }}</span>
```
**OBS:** Note que o Vue.js não precisa de **dois pontos ":"** separando os argumentos, basta somente adicionar **um espaço** que o Vue.js já os identifica.
<iframe width="100%" height="300" src="//jsfiddle.net/pv2bzh3e/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

#### Bind em atributos
Podemos utilizar a interpolação *(mustaches)* dentro de atributos HTML.
```language-html
<!-- AngularJS / Vue.js -->
<button type="button" class="btn btn-{{ status }}">
    CADASTRAR
</button>
```
**OBS:** No Vue.js não são permitidos interpolações nas diretivas e atributos especiais, mas você sempre será avisado no console quando utilizar em um local inapropriado.
<iframe width="100%" height="300" src="//jsfiddle.net/bLvag7ph/2/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Existe também uma diretiva denominada **v-bind**, basicamente com ela é possível fazer a ligação de vários atributos em uma expressão.
```language-html
<!-- AngularJS -->
<a ng-href="{{ url }}" title="#">Clique aqui</a>
<button ng-disabled="checked">Ok</button>
```
```language-html
<!-- Vue.js -->
<a v-bind:href="url">Clique aqui</a>
<button v-bind:disabled="checked">Ok</button>
```
<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/crq2t8gn/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

**DICA:** O legal do Vue.js também é disponibilizar formas mais curtas de utilizar algumas diretivas, no exemplo do **v-bind**, podemos **substituí-lo por dois pontos " : "**
<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/ro15ar5u/1/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

#### Remover e recriar DOM
Tanto o AngularJS, quanto o Vue.js disponibiliza uma diretiva para remover ou recriar o DOM com base numa condição.
```language-html
<!-- AngularJS -->
<div ng-if="isVisible"></div>
```
```language-html
<!-- Vue.js -->
<div v-if="isVisible"></div>
```

**OBS:** O Vue.js disponibiliza também a diretiva **v-else** para indicar um *bloco else*, e esse bloco deve vir imediatamente após o *v-if*, para o seu perfeito funcionamento.

<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/rm0wan8r/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Quando a condição para o *v-if* se tornar verdade (true), o Vue.js compila e logo após ele armazena em cache, para disponibilizar de maneira mais ágil, porem evite utilizá-lo se a condição venha a mudar frequentemente em tempo de execução.

**OBS:** Se a utilização for para condições que se alterne com mais frequência, utilize a diretiva de visibilidade **v-show**, que trabalha da mesma forma que o **ng-show** do AngularJS.

#### Renderizando listas
Trabalhar com listas de itens ficou fácil com o **ng-repeat** do AngularJS e com o Vue.js não seria diferente, a diretiva nesse caso que utilizamos é **v-for**.

```language-html
<!-- AngularJS -->
<ul>
  <li ng-repeat="person in people">
	{{ person.name }}
  </li>
</ul>
```
```language-html
<!-- Vue.js -->
<ul>
  <li v-for="person in people">
	{{ person.name }}
  </li>
</ul>
```

Aqui vemos que a posição do *alias (person)* e a *matriz (people)* não mudam.

Exemplo de uma simples listagem, utilizando o filtro padrão orderBy:
<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/qq394fon/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

#### Event handler
Da mesma maneira que para bind no Vue.js existe o v-bind que resolve um montão de diretivas presentes no AngularJS, para eventos também utilizamos somente uma diretiva chamada **v-on**, onde também é possível substituí-lo pelo símbolo **arroba @** como uma sintaxe curta (Shorthand) para ouvir eventos DOM.

```language-html
<!-- AngularJS -->
<div>
  <button type="button" ng-click="increment()"> + 1 </button>
</div>

```
```language-html
<!-- Vue.js -->
<div>
  <button type="button" v-on:click="increment"> + 1 </button>
  <!-- Shorthand -->
  <button type="button" @click="decrement"> - 1 </button>
</div>
```

**OBS:** Note que com o Vue.js você não precisa invocar a função passando os parênteses "**()**", se a mesma não tiver que passar algum parâmetro.

Exemplo simples de um contador:
<iframe width="100%" height="300" src="//jsfiddle.net/ktquez/9f1ufojn/1/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Com o **v-on** é possível também passar alguns modificadores, que são bastante usados e agiliza bastante o desenvolvimento

Um exemplo comum é quando submetemos um formulário e queremos utilizar AJAX para enviar a request para o servidor, utilizamos o prevent para cancelar o evento, sem parar a propagação.

```language-html
<!-- Vue.js -->
<form @submit.prevent></form>
```
Equivalente ao `event.preventDefault()`.

Existem vários outros, confira esses exemplos tirados da documentação:
```language-html
<!-- Vue.js -->
<!-- Stop propagation --> 
<button @click.stop="doThis"></button>
<!-- Prevent default -->
<button @click.prevent="doThis"></button>
<!-- Somente se o evento for disparado pelo próprio elemento -->
<div @click.self="doThat"></div>  
<!-- Key Modifiers (13 = enter) -->
<input @keyup.13="submit"></div>
```

Essa é só uma primeira parte de 5 ou mais posts mostrando o poder do Vue.js e ajudar a ter um ponto de partida ou inspiração para devs que estão começando ou que já tem alguma experiência com o Framework AngularJS, experimente a vontade o Vue.js e veja o quão bem ele se encaixa no seu projeto atual ou até mesmo em um próximo.

Caso tenha algo que você usa no AngularJS e gostaria de saber como fazer com o Vue.js, deixa nos comentários, que responderei e também posso abordar nas próximas partes.







