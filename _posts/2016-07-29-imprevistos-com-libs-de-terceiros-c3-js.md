---
layout: post
title: 'Imprevistos com libs de terceiros - C3.js'
main-class: 'dev'
date: 2016-07-29 13:59:56 
color: '#637a91'
tags: libs c3js d3js third-party
layout: post
author: 7
---

Em todos os projetos sempre acabamos usando várias bibliotecas para vários fins.  
Nesse artigo quero falar de uma experiencia interessante que eu tive ao usar C3.js em conjunto com os componentes do VueJS.

## C3.js
C3.js é uma biblioteca javascript para criar gráficos usando outra biblioteca a D3.js muito usada para trabalhar com SVG. Ela é bem simples, tem seus problemas, mas no geral funciona bem.  
Abaixo você tem um código de exemplo simples.

<iframe width="100%" height="400" src="//jsfiddle.net/Lodd585j/2/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

## Objetivo: Criar um componente de gráfico

No meu trabalho eu tenho que criar muitos gráficos, nada mais óbvio do que abstrair isso em um componente.  
Comecei a criar algo simples (incompleto) porém funcional.

```javascript
export default {
  data() {
    return {
      instance: undefined,
    };
  },
  ready() {
    this.instance = c3.generate(this.getArgs());
  },
 // omited
}
```

Inicialmente e aparentemente *funcionou*, porém ao começar a manipular `this.instance` comecei a obter vários erros.

A primeira atitude que tomei, naturalmente, foi buscar o erro na internet, tentando associar ele ao uso do VueJS. Achei alguma coisa de 2014 sobre um erro um pouco diferente do meu e com uma solução que não existia mais no VueJS.

Então a segunda coisa que fiz foi debugar o problema.

### Localizando o problema

O erro em questão era: `TypeError: d.main.select is not a function`, ele  significa que a propriedade `main` não possui um metodo chamado `select`

Usando o **Chrome DevTools** eu coloquei um *breakpoint* na linha que disparava o erro.  
Com o *devtools* eu consegui ver o valor de `d.main` a cada interação com essa função/objeto.  
Descobri que ele era um `Array`. Achei estranho de inicio, nesse momento analiso o `__proto__` do array, e vi que não era um array "puro", ele possuía uma herança de protótipos que veio do D3.

Na interação seguinte (onde eu estava carregando os dados do gráfico) esse protótipo havia "sumido", dando lugar a um `__proto__` de array, disparando assim o erro no console.

Olhando mais atentamente vi que o array em questão possuía a propriedade `__ob__` (isso não estava lá antes... 😨).

### Entendendo a problemática

Achou isso estranho?  
Só se você não sabe como VueJS faz seu **two-way data binding**, ele usa uma implementação de **Observer**.

Quando você cria um instância/componente VueJS ele pega seu objeto data e deixa ele "reativo" usando o seu *Observer*, com isso ele *"muta"* o objeto original, e ele faz isso **recursivamente**.  
Como efeito colateral, objetos com protótipos modificados podem apresentar esse problema. Vale mencionar que *arrays* são objetos, e podem possuir métodos e propriedades.

Sendo assim, não é uma opção viável deixar um objeto (instância) de tamanha complexabilidade dentro do `$data` da instância do VueJS. Além é claro do gasto de memória e processamento desnecessários, já que o objeto passou a ser "reativo" sem que eu precise disso.

### Solucionando a problemática 

Sabendo agora qual é o problema, me concentrei na solução. Eu não posso ter essa instância "dentro" do componente.  
Inicialmente tenho a ideia de colocar ele fora do objeto que representa o componente.

```javascript
let instance;

export default {
  // omited
  ready() {
    instance = c3.generate(this.getArgs());
  },
 // omited
}
```

Porém essa ideia é descartada **imediatamente**, afinal vou usar esse componente em vários locais, em diversas situações o terei em mais de um local ao mesmo tempo. Sendo assim `instance` seria compartilhado entre todas as instâncias do meu componente, o que obviamente não é o que eu quero.

A solução que eu implementei é bem simples.

```javascript
const charts = {};

export default {
  data() {
    return {
      instance: Symbol('instance'),
    };
  },
  ready() {
    charts[this.instance] = c3.generate(this.getArgs());
  },
 // omited
}
```

Agora eu possuo um objeto que é sim **compartilhado** em todas as instâncias do componente, porém cada instância do componente tem acesso apenas a sua instância de c3.  
Esse comportamento é obtido graças ao [**Symbol**](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Symbol).

Cada vez que você cria um objeto *Symbol* ele é único, mesmo que possua a mesma descrição.  
Eu aproveito que um novo objeto `$data` é criado cada vez que eu uso o componente, assim eu sempre terei um symbol novo. Depois eu uso esse symbol para identificar uma chave no meu objeto compartilhado `charts`, garantindo que apenas aquele componente tem acesso a sua instância do c3.

Não é uma técnica a prova de falhas, mas resolveu o problema perfeitamente.

----------------

#### That’s all, folks!
