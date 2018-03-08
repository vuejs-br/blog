---
layout: post
title: 'Maneiras de montar uma instância de componente'
main-class: 'dev'
date: 2016-08-05 17:36:08 
description: derscricao
color: '#637a91'
tags: components
 -angular
layout: post
introduction: introducao
---

VueJS é uma biblioteca para se criar [web-components](http://www.vuejs-brasil.com.br/aplicacoes-com-vuejs-pensando-em-componentes/). Muitos *desavisados* que começam a ler sobre VueJS imaginam ele como um *angularjs só que mais simples*, por sorte basta alguns momentos com ele que você percebe que a pegada é outra. A principal diferença é a maneira de se criar aplicações com componentes, que possui pouca ou nenhuma semelhança com a _maneira angularjs_ de se criar aplicações.

Na versão 1 do angular, você tinha "duas peças" o *controller* e a *view (template)*, com vuejs você tem **apenas** componente. Em outros posts eu já falei como é a *filosofia* de se trabalhar com *web-components*, e como eles funcionam no [VueJS](http://vuejs.org/guide/application.html#Single-File-Components). Nesse post darei um foco mais técnico em como esses componentes funcionam.

> Vale lembrar que *web-components* é uma [especificação](https://www.w3.org/standards/techs/components) e que mesmo assim ferramentas como VueJS e ReactJS não a implementam ***exatamente*** como está na especificação. 

----

## Root component

Direto ao ponto: querendo ou não **tudo** em VueJS gira em torno dos componentes.

```javascript
import Vue from 'vue';

new Vue({
  el: 'body',
  data: {...},
  methods: {...},
  computhed: {..},
});
```

Este é um exemplo corriqueiro, faz parte de todos os *hello world* do VueJS. Em uma ponta você tem o *código javascript* atuando como controller e na outra você tem a propriedade `el` fazendo a *ligação* com o elemento DOM que atuará como *template*.  
Por isso é natural se confundir, e imaginar VueJS como uma *versão simplificada* do angular.

Porém, se eu te disser que você acabou de criar um componente?
  
Isso mesmo, esse código nada mais é do que seu **root component** (componente raiz). Ele existe por que o VueJS precisa de um "start", um elemento onde ele possa se "montar".

E por falar em montar.

```javascript
import Vue from 'vue';

const root = new Vue({
  data: {...},
  methods: {...},
  computhed: {..},
});

// Faz qualquer coisa elaborada antes de iniciar o componente root

// root.$mount(document.getElementById('app'));
root.$mount('#app');
```

Com o exemplo anterior agora eu tenho uma outra maneira de iniciar meu componente *root*. VueJS se adapta muito bem a vários tipos de cenários, as possibilidades são inúmeras, tudo que você precisa é um *pedaço* de DOM.

### Criando objetos VueJS

Como você já percebeu, um objeto VueJS é um componente, então como se não fosse suficiente, há mais uma maneira de se criar um componente root.

```javascript
import Vue from 'vue';

const RootComponent = Vue.extend({
  methods: {...},
});

const root = new RootComponent({
  // el: 'body',
  data: {...},
});

root.$mount('body');
```

Se isso é produtivo ou se você um dia vai precisar fazer algo assim, é completamente discutível, a questão é a flexibilidade proporcionada pelo VueJS é simplesmente incrível. Incrível não pela possibilidade em si, mas pela **facilidade**. 

## Manipulando seu componente root

Como eu disse, são **muitas** as possibilidades, o importante é você conhecer o que a instância do componente expõe para você, e inevitavelmente você vai achar um uso.

```javascript
import Vue from 'vue';

const root = Vue({
  data: {
    umaPropMuitoLoca: '1969',
  },
  methods: {...},
  computhed: {..},
});

root.$mount('#app');

// ouvindo eventos do componente
root.$on('evento:disparado:pelo:componente:root', (data) => { .. });

// algo FORA do controle do componente ocorre
root.$emit('evento:que:veio:de:fora', arg1, arg2);

// algo de FORA exige que o componente seja "desmontado"
root.$destroy(true);

//acessando dados do componente
$root.umaPropMuitoLoca = '2016';
```

Esse tipo de coisa pode ser feito não apenas com componentes root, é possível fazer com componentes filho também, porém isso é assunto para outro artigo.

## VueJS dentro do AngularJS

Entre essas possibilidades esta a de usar VueJS **dentro do angular**, isso mesmo que você leu. Graças a essa flexibilidade eu estou criando um módulo novo no sistema que trabalho, totalmente com VueJS + Vuex. Não é algo que eu recomendo para quem esta começando, mas ainda é uma possibilidade para muitos.

No meu caso eu pretendo migrar todas as outras partes do projeto para VueJS, porém o mundo não é uma utopia, e preciso continuar a evolução do sistema, então nossa decisão foi de fazer esse trecho com o VueJS, e esta sendo muito bom. O fluxo de desenvolvimento não é perfeito, porém isso é insignificante se considerar a qualidade e facilidade que é trabalhar com VueJS.

### O processo

Criei um projeto com [*vue-cli*](https://github.com/vuejs/vue-cli) dentro da minha estrutura de pasta do projeto com angular. Após alguns ajustes eu já estava criando um *bundle* com o VueJS dentro da minha pasta final, onde os arquivos do angular ficam.

> O projeto que criei com *vue-cli* esta sendo completamente ignorado pelo projeto angular, ele possui seu próprio *node_modules* e *package.json*, ele também ignora tudo relacionado ao projeto angular.

Em meu `src/main.js` eu tenho algo parecido com:

```javascript
// OMITIDO
function MeuVueFactory() {
  return new Vue({
    store,
    vuex: {
      actions: { resetData },
    },
    components: { MeuComponenteVuejs }
    ready() { ... },
    beforeDestroy() {
      this.resetData();
    },
  });
}

// expondo globalmente para possibilitar o uso dentro do Angular
window.MeuVueFactory;
```

Como o componente precisa de um elemento DOM para ser montado, eu usei diretivas do angular para fazer este trabalho.

```javascript
var DiretivaQueIniciaOVuejs = function() {
  function link(scope, element, attrs) {
    var root = window.MeuVueFactory();
    root.$mount(element[0]);
    scope.$on("$destroy", function() {
      root.$destroy(true);
    });
  }

  return {
    restrict: 'E',
    link: link,
    template: '<span><meu-componente-vuejs></meu-componente-vuejs></span>',
  };
};
```

Esse tipo de integração não é algo que eu recomendo, mas cada projeto é um projeto único, então eu optei por fazer isso.

-------

### That’s all, folks!
