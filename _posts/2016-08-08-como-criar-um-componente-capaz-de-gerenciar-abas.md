---
layout: post
title: 'Como criar um componente capaz de gerenciar abas'
main-class: 'dev'
date: 2016-08-08 03:07:52 
color: '#637a91'
tags: vue-js components bootstrap
layout: post
author: 4
---

Neste artigo veremos como criar um componente no qual irá renderizar abas, que opdem conter os mais diversos conteúdos. O objetivo final é criar um componente que possui este comportamento:

![](/content/images/2016/07/Animation-1.gif)

Primeiro temos que estabelecer qual framework CSS usaremos. A partir dele podemos criar algumas regras para então poder criar o componente. Neste artigo usaremos o Bootstrap, que possui como base este código html:

```html
<ul class="nav nav-tabs">
  <li class="active"><a data-toggle="tab" href="#home">Home</a></li>
  <li><a data-toggle="tab" href="#menu1">Menu 1</a></li>
  <li><a data-toggle="tab" href="#menu2">Menu 2</a></li>
</ul>

<div class="tab-content">
  <div id="home" class="tab-pane fade in active">
    <h3>HOME</h3>
    <p>Some content.</p>
  </div>
  <div id="menu1" class="tab-pane fade">
    <h3>Menu 1</h3>
    <p>Some content in menu 1.</p>
  </div>
  <div id="menu2" class="tab-pane fade">
    <h3>Menu 2</h3>
    <p>Some content in menu 2.</p>
  </div>
</div>
```

Este código html pode ser testando [neste link](http://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_tabs_dynamic&stacked=h).

Analisando a forma como o Bootstrap cria as abas, perceba que temos inicialmente a tag `<ul>` e `<li>` que representa as abas, e a tag `<div class="tab-content">` que representa o conteúdo de cada aba. O próprio Bootstrap irá se encarregar de alterar o conteúdo de acordo com a aba qye será clicada. 

O nosso objetivo então se "resume" a criar componentes em Vue que simulem a estrutura html acima. 

Primeiro, crie o projeto usando `vue-cli`:

```
vue init browserify-simple mytabs
cd mytabs
npm install
```

Após criar o projeto, vamos adicionar o jQuery+Botostrap da forma mais rápida e simples, pelo CDN, editando o arquivo `index.html`, veja:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="utf-8">
  
    <title>vue-tabs</title>
    
    <!-- bootstrap cdn-->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

  </head>
  <body>
    <app></app>
    
    <!-- bootstrap cdn-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <!-- App build -->
    <script src="dist/build.js"></script>
  </body>
</html>
```

Agora temos que descrever como seria o nosso componente! A princípio, algo como o código a seguir seria viável:

```
<tabs>
  <tab name="t1" title="Tab 1" active=true>
    Hello World
  </tab>
  <tab name="t2" title="Tab 2">
    Hello World 2
  </tab>
  <tab name="t3" title="Tab 3">
    Hello World 3
  </tab>
</tabs>
```

Ou seja, temos um componente chamado `Tabs` e outro chamado `Tab` (No html é sempre em **minúsculo**). O componente `Tab` é mais simpels, pois ele possui o texto de conteúdo e três propriedades. Vamos criá-lo primeiro? Então crie o diretório "components" e o arquivo "Tab.vue":

```
<template>
    <div role="tabpanel" class="tab-pane" :class="{'active': active}" id="{{name}}">
        <slot></slot>
    </div>
</template>
<script>
    export default{
        props: {
            title:{type:String,required: true},
            active:{type:[Boolean,String],default:false},
            name:{type:String,required: true}
        }
    }
</script>
```

Veja que, no template, criamos a `div` que possui o mesmo conteúdo html que da aba do Bootstrap necessita, ou seja, os parâmetros role, class e id devem estar presentes. As propriedades do componente são o título, se a aba está ativa ou não, e o nome da aba, que é necessário para que o Bootstrap possa trocar o conteúdo de cada aba ao ser clicada.

O componente `Tabs` é um pouco mais complexo, pois ele deve simular uma situação mais difícil. Primeiro, ele deve renderizar a lista de `<ul>..<li>..</li>..</ul>` que formam as abas. Depois, eles devem renderizar cada div que é o conteúdo de cada aba. 

Crie o componente `components/Tabs.vue`, com o seguinte código:

```
<template>
    <ul class="nav nav-tabs">
        <li role="presentation" :class="{'active':tab.active}" v-for="tab in tablist" ><a href="#{{tab.name}}" aria-controls="{{tab.name}}" role="tab" data-toggle="tab">{{tab.title}}</a></li>
    </ul>  
    <div class="tab-content">
        <slot></slot>
    </div>
</template>
<script>
    export default{
       data () {
          return {
            tablist: []
          }
      },
      ready(){
        //console.log(this.$children);
        this.$children.forEach(c=>{
            this.tablist.push({
                    "name": c.name,
                    "title": c.title,
                    "active": c.active
                });
        })
      }
  }
</script>
<style>
  .nav-tabs {
    background-color: #eeeeee;
    padding-top:5px;
    padding-left:5px;
    border: 1px solid #ddd;

  }

  .tab-content {
    color : #000000;
    background-color: #ffffff;
    padding : 5px 15px;
    margin-top: -1px;
    border: 1px solid #ddd;
  }
</style>
```

No `<template>` criamos a `<ul>` que irá renderizar quantos `<li>` forem necessários. A quantidade está ligada a um array chamado `tablist`. Este array será criado no método `ready` do componente. Criamos o `ul...li` de acordo com o exemplo do Bootstrap, incluindo o elemento `<a>` que irá apontar para uma aba específica. 

Depois de criar o `<ul>`, criamos `<div>` que conterá o conteúdo de cada aba, e nesse momento usamos o `<slot>` para que os componentes `<tab>` sejam inseridos neste slot.

O maior detalhe deste componente é como deveremos preencher o array `tablist` com as abas a serem criadas. Fazemos isso com o uso da propriedade `this.$children`, nativa do Vue, que retorna um conjunto de elementos que estão presentes no `<slot></slot>` do componente. 

Utilizando `this.$children` podemos saber quantos filhos o componente `Tags` possui, e quais suas propriedades. Dessa forma, podemos montar a lista de `<li>` preenchendo o array `tablist`:

```
 this.$children.forEach(c=>{
            this.tablist.push({
                    "name": c.name,
                    "title": c.title,
                    "active": c.active
                });
        })
```

Na parte final do componente, temos o style, que dá uma graça no mesmo...

Com isso nós conseguimos fazer um componente de abas bem simples, onde é possível adicionar conteúdo em cada aba, de forma organizada, por exemplo:

```
<template>
  <div id="app" class="container">
    <h1> Tabs </h1>

    <tabs>
      <tab name="t1" title="Tab 1" active=true>
        Hello World
      </tab>
      <tab name="t2" title="Tab 2">
        Hello World 2
      </tab>
      <tab name="t3" title="Tab 3">
        Hello World 3
      </tab>
    </tabs>

  </div>
</template>
<script>
  import Tabs from './components/Tabs.vue'
  import Tab from './components/Tab.vue'
  
  export default {
    components: {
      Tabs,Tab      
    }
  }
  
</script>
```

Para adicionar mais elementos, ou elementos mais complexos, dêuma olhada no [exemplo que está no github](https://github.com/danielschmitz/vue-tabs).  




 
