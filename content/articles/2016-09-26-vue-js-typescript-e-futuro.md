---
layout: post
title: 'Vue.js, Typescript e futuro'
main-class: 'dev'
date: 2016-09-26 12:53:06 
color: '#637a91'
tags: vue-js typescript
author: daniel-schmitz
---

Tanto Vue quanto Typescript são ótimos em seus propósitos. O Vue como framework mvvm e o Typescript como uma "camada" tipada ao ES6. Para quem não conhece o typescript, pode-se pensar em javascript no padrão ES6 e com tipos, ou seja, podemos adicionar um tipo "string" a uma variável chamada "name". Tem gente que curte, tem gente que não curte.

É de se esperar que ambas as tecnologias vão se [encontrar](https://github.com/vuejs/vue/issues/478) um dia, até mesmo o *Evan You* mostrou-se aberto ao uso do TS (claro que não mandatório). Até o momento, a biblioteca que mais se destacou foi a [vue-typescript](https://github.com/itsFrank/vue-typescript), na qual já possui algumas funcionalidades disponíveis.

**Mas e o código? Como que fica??**

Na imagem a seguir temos um exemplo de como seria a união entre vue e ts:

![](/content/images/2016/07/screenshot.png)

O primeiro detalhe é o:

```
import { VueComponent, Prop, Watch } from 'vue-typescript'
```

Isso irá importar alguns *decorators* que podem ser usados no código. O primeiro deles é o `@VueComponent`, que possui inicialmente duas propriedades: template e style. Perceba que, neste momento, é realizado um require no código que irá incorporar a build do webpack. 

Ao invés de termo um objeto vue, no estilo new Vue({...}), temos uma classe, e esta classe é filha da classe Vue. Veja que saímos do modo "Vue" de ser para cair em algo mais parecido com c#, java ou até mesmo php. (Mais uma vez, tem gente que gosta e tem gente que não gosta).

Como criamos uma classe, podemos criar variáveis dentro dela que poderão ser categorizadas pelos *decorators*. Por exemplo, ao invés de termos:

```
new Vue({
 props:['todo']
})
```

Temos:

```
class TodoListComponent extends Vue{
 @Prop 
 todos:TodoListComponent[]
}
```

Ao invés de usarmos a propriedade *data*:

```
new Vue({
 data:{
   msg:"Hello World"
 }
})
```

podemos ter uma simples variável na classe:

```
class TodoListComponent extends Vue{
 msg:string = "Hello World"
}
```

**Futuro**

Falando um pouco do futuro, o vue-typescript é um projeto criado fora do escopo do Evan, talvez ele goste da ideia e incorpore aos seus projetos principais no seu repositório, assim como é o vue-resource. Até lá, podemos apenas observar o desenrolar da história e aguardar! 

Deixo aqui apenas como esse "romance" entre vue e Ts pode ser útil, veja a classe a seguir e confira com o ficaria a criação de um menu:

<script src="https://gist.github.com/danielschmitz/2f5cea465679404bce2647ede1d598c8.js"></script>


