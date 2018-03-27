---
layout: post
title: 'O caso de uso mais simples com Vue.js'
main-class: 'dev'
date: 2016-07-06 12:04:53 
color: '#637a91'
tags: vue-js
layout: post
author: vedovelli
---

Vue.js é muito bom para se trabalhar com dados. Ele provê meios para acessar, modificar e validar os dados. Indo além ele atua como cola entre os elementos HTML e os dados, removendo do desenvolvedor a irritante tarefa de pegar referências aos elementos DOM apenas para mostra-los/esconde-los ou ler seus valores.

Este exemplo super simples lhe mostrará como habilitar/desabilitar o botão submit quando todos os campos do formulário estiverem preenchidos. Trata-se de um único arquivo HTML com o Vue.js inserido usando uma tag `<script>`.

O documento:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/vue/1.0.25/vue.min.js"></script>
    <script>
        new Vue({
            el: 'body'
        })
    </script>
</body>
</html>
```

Nada de especial está acontecendo no momento: perto da tag `</body>` está um include javascript e a criação do Vue Object. Como único parâmetro passado ao método construtor `Vue()` temos um objeto literal contendo algumas informações de configuração. No exemplo acima a propriedade `el` liga o Vue Objeto ao `<body>`. Tudo que estiver contido em body estará também disponível para o Vue.js.

Para prosseguir, precisamos do form:

```html
...
<body>
    <form action="#">
        <div>
            <label for="name">Name</label>
            <input type="text" id="name" name="name">
        </div>
        <div>
            <label for="email">E-mail</label>
            <input type="email" id="email" name="email">
        </div>
        <div><button type="submit">Submit</button></div>
    </form>
</body>
...
```

Qual o nosso objetivo? **Manter o botão submit desabilitado até que ambos os campos do formulário estejam preenchidos**. Agora pare e pense: *"- Como você atingiria este objetivo com JS puro ou jQuery?"* Provavelmente você pegaria uma referência a ambos os campos e leria seus valores, correto? Bem, com Vue.js isso é um pouco diferente!

Primeiro voltemos ao Vue Object para criar um novo objeto com os dados que estamos interessados...

```javascript
...
    new Vue({
        el: 'body',
        data: {
          name: '',
          email: ''
        }
    })
...
```

... e então ligar estes dados ao nosso form:

```html
...
  <input type="text" id="name" name="name" v-model="name">
  <input type="email" id="email" name="email" v-model="email">
...
```

Preste atenção ao novo atributo `v-model` agora presente em ambos os campos. Eles contém uma referência direta às propriedades contidas no nosso objeto **data** que vive dentro do Vue Object.

Esta propriedade (v-model) é uma **diretiva** e sua finalidade é ligar ao HTML os dados carregado em memória e acessíveis via Javascript. Ao fazer isso, tudo o que for digitado nos campos mudará a informação disponível para o Javascript. O oposto também é verdadeiro e se a informação for modificado no Javascript, digamos, pelo retorno de uma chamada AJAX, o novo valor será automaticamente mostrado no campo do formulário.

Este útil comportamento é chamado  de **two-way data binding**.

Estamos chegando lá!

Agora é chegada a hora de trabalhar no botão, afinal, ele é o nosso personagem principal neste exemplo. Para incluir o comportamento desejado vamos usar uma outra diretive: `v-bind`. Sua função é adicionar de forma condicional atributos aos elementos HTML, baseada no estado dos dados contidos em memória. Neste caso em particular faremos uso da propriedade nativa `disabled`:

```html
...
<div>
    <button type="submit"
        v-bind:disabled="(name != '' && email != '')">
        Submit
    </button>
</div>
...
```

Ao usar a configuração acima o Vue Object é instruído a fazer o seguinte: adicionar o atributo `disable` ao `<button>` quanto **name** e **email** não forem vazios. Graças ao *two-way data binding* isso é feito em tempo real e de forma automatica. **Este é o poder do Vue**.

Mas isso é meio que sujo, não é mesmo? E se for necessário validar a estrutura do e-mail antes de considerar o form como válido para envio? Bem, há uma forma melhor de implementar esta validação: **computed property**.

```javascript
...
    new Vue({
        el: 'body',
        data: {
          name: '',
          email: ''
        },
        computed: {
          isValid: function () {
            return this.name != '' && this.email != ''
          }
        }
    })
...
```

```html
...
<div><button type="submit" v-bind:disabled="!isValid">Submit</button></div>
...
```

Mais uma vez, graças à natureza reativa do Vue.js todas as vezes que uma das propriedades mencionadas no método `isValid()` forem modificadas, o método será executado, retornando *true* ou *false*. E uma vez que o método é um método como outro qualquer você pode fazer qualquer tipo de verificar dentro dele!

Abaixo você encontra o código completo. Se quiser ver em ação, há um Fiddle disponível aqui: [https://jsfiddle.net/vedovelli/focs85v3/](https://jsfiddle.net/vedovelli/focs85v3/)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <form action="#">
        <div>
            <label for="name">Name</label>
            <input type="text" id="name" name="name" v-model="name">
        </div>
        <div>
            <label for="email">E-mail</label>
            <input type="email" id="email" name="email" v-model="email">
        </div>
        <div><button type="submit" v-bind:disabled="!isValid">Submit</button></div>
    </form>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/vue/1.0.25/vue.min.js"></script>
    <script>
    new Vue({
        el: 'body',
        data: {
          name: '',
          email: ''
        },
        computed: {
          isValid: function () {
            return this.name != '' && this.email != ''
          }
        }
    })
    </script>
</body>
</html>
```

Segue exemplo:

<iframe width="100%" height="450" src="//jsfiddle.net/vedovelli/5ea439zz/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>
