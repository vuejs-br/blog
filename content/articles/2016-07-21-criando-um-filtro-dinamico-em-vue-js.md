---
layout: post
title: 'Criando um filtro dinâmico em Vue.js'
main-class: 'dev'
date: 2016-07-21 14:13:32 
color: '#637a91'
tags: vue-js filters filtros
author: pablohpsilva
---

Trabalho para uma startup e, por mais que o escopo do projeto esteja bem definido, a aplicação como um todo está passível de sofrer alterações não previstas. Semana passada deparei-me com um problema sobre como filtrar itens em um laço Vue (v-for). Usar o v-for é algo bem simples, o problema em si é que eu tenho uma única visão para renderizar três listas semelhantes, porém, cada uma contém suas particularidades.

> "Se eu tenho três *sources* diferentes para renderizar, como eu farei os filtros para cada uma delas? Eu não posso usar a [notação padrão de filtro do Vue](http://vuejs.org/guide/custom-filter.html#ad) para resolver o meu problema, visto que o filtro de uma lista pode até não existir para outra. O que eu faço?!"


#### Filtros dinâmicos! 

A ideia, basicamente, é criar um objeto que seria responsável por armazenar filtros e, com a mudança de escopo (trocar uma lista por outra na aplicação), o filtro deste novo escopo seria ativado e filtraria a lista alvo, graças ao [two-way binding do Vue](https://vuejs.org/guide/#Two-way-Binding). Interessante, certo? Logo pensei nesta estrutura:

```json
{
	id: String, //identificador
	args: Array, //um vetor com argumentos do filtro
	func: Function //uma função, ou seja, o próprio filtro
}
```
Perceba que tenho fácil acesso a qualquer informação que ela contenha (como adicionar, remover ou alterar um filtro). 

> "Huuum... Como eu aplicaria essa estrutura dentro do Vue?"

Filtros em Vue nada mais são que funções, sendo assim, eu posso usar [Higher-Order functions](https://www.youtube.com/watch?v=BMUiFMZr7vk)! O meu próximo passo foi criar um [Custom Filter](http://vuejs.org/guide/custom-filter.html#ad) que teria um valor (a lista que quero filtrar) e um vetor de objetos (que são a estrutura declarada anteriormente). Logo, o meu *Custom Filter* deve ser inteligente o suficiente para pegar cada objeto desse vetor, usar a função contida nele (e aplicar os seus argumentos) e retornar uma lista filtrada. Sendo assim, construí este filtro Vue:

```javascript
Vue.filter('formatResult', function(value, functionArray){
    if (functionArray) {
        let rList = value,
            aux = [];
        for (let i = 0, total = functionArray.length; i < total; i++) {
            aux = [rList].concat((functionArray[i]).args);
            rList = (functionArray[i]).func.apply(null, aux);
        }
        return rList;
    }
    return value;
});
```
O filtro acima faz exatamente o que eu havia dito. Dado uma lista, ele aplicará todos os filtros (se houver) do *functionArray* e retornará uma nova lista filtrada.

O poder desse *Custom Filter* com a estrutura declarada anteriormente é que eu não mais preciso declarar cada um dos filtros que eu tenho no v-for:
```html
<li v-for="item in list | filterA | filterB | filterC | ... > {{item}} </li>

```

Agora eu posso escrever desta forma:
```html
<li v-for="item in list | formatResult filters> {{item}} </li>
```

Perceba acima que *formatResult* é o nosso *Custom Filter* e que *filters* é um Array com objetos da estrutura declarada no começo desta postagem. Aqui pode ser visto um exemplo completo deste filtro dinâmico:

<iframe width="100%" height="550" src="//jsfiddle.net/yMv7y/1646/embedded/js,html,css,result/dark/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Perceba como o método *addFilterFunction* funciona e como ele faz uso da estrutura que criei. Depois, perceba como o *Custom Filter* criado consome este filtro e como ele retorna a lista filtrada. Bem interessante, certo?

Gostaria de salientar que, em produção, o meu código é um pouco diferente, visto que, como havia dito no início deste artigo, eu tenho várias listas e cada lista tem o seu próprio conjunto de filtros.

Originalmente fiz [esta publicação no medium](https://medium.com/tldr-tech/vuejs-applying-filters-on-the-fly-aabde13fcad0#.73930351o) sobre o mesmo tópico em inglês.

Se você gostou e tem ideias legais, vamos conversar! Deixe um comentário com sugestões de melhorias.
