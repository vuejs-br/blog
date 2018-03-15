---
layout: post
title: 'CRUD básico com Vue.js e json-server #6'
main-class: 'dev'
date: 2016-08-03 12:05:29 
description: derscricao
color: '#637a91'
tags: vue-js
layout: post
introduction: introducao
---

Para finalizar o básico do CRUD, já temos a leitura com paginação, e a inclusão e edição de dados. Falta remover as cervejarias. 

Quando clicamos no link para remover a cervejaria, que fica ao lado do ícone de edição, é necessário perguntar ao usuário se ele realmente deseja fazer isso. Ao invés de usarmos a função `confirm` nativa do Javascript, vamos inovar um pouco e aprender a instalar um plugin externo. Vamos usar o sweet alert, um dos melhores para este fim.

Primeiro, execute o comando:

```bash
 npm install sweetalert -S
```

Depois do *sweetalert* estar instalado, precisamos adicionar as suas bibliotecas no arquivo `index.html`, veja:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>crud-vuejs</title>
    <link rel="stylesheet" href="node_modules/bulma/css/bulma.css">

    <!-- sweetalert inicio -->
    <link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">
    <script src="node_modules/sweetalert/dist/sweetalert.min.js"></script>
    <!-- sweetalert fim -->

    <link rel="stylesheet" type="text/css" href="node_modules/sweetalert/dist/sweetalert.css">
  </head>
  <body>
    <app></app>
    <script src="dist/build.js"></script>
  </body>
</html>
```

Com o *SweetAlert* pronto, podemos usá-lo de acordo com a sua [documentação](http://t4t5.github.io/sweetalert/). No link para remover a cervejaria, chamamos o método `removeBrewery`:

```html
...
<a href="#" @click.prevent="removeBrewery(brewery)">
  <i class="fa fa-trash"></i>
</a>
...
```

O método então usa o Sweet Alert, da seguinte forma:

```
methods:{
 ...
 removeBrewery(brewery){
   let self = this;
   swal({  title: "Você tem certeza?",
           text: `Deseja apagar "${brewery.name}"`,   
           type: "warning",   
           showCancelButton: true,   
           confirmButtonColor: "#DD6B55",   
           cancelButtonText: "Cancelar",
           confirmButtonText: "Sim, pode apagar!",
           showLoaderOnConfirm: true,   
           closeOnConfirm: false }, function(){   
                  //swal("Deleted!", "Your imaginary file has been deleted.", "success"); 
        });
       },
 ...
}
```

O código acima produz o seguinte resultado, quando o usuário clica no link:

![](https://i.imgur.com/zbRPnr2.png)

Agora precisamos implementar a funcionalidade para apagar a cervejaria. Para isso usamos o método `self.$http.delete` do Vue Resource, lembrando que a variável `self` é necessária para mantermos o escopo do vue em relação ao escopo do sweet alert. O código final é apresentado a seguir:

```
removeBrewery(brewery){
        let self = this;
        swal({  title: "Você tem certeza?",
                 text: `Deseja apagar "${brewery.name}"`,   
                 type: "warning",   
                 showCancelButton: true,   
                 confirmButtonColor: "#DD6B55",   
                 cancelButtonText: "Cancelar",
                 confirmButtonText: "Sim, pode apagar!", 
                 showLoaderOnConfirm: true,  
                 closeOnConfirm: false }, function(){   
                  
                  self.$http.delete(`/breweries/${brewery.id}`).then(
                    result=>{
                      swal("Cervejaria removida!")
                      self.loadBreweries()
                    })
        });
       },
```

Um detalhe interessante é que o parâmetro `showLoaderOnConfirm` irá exibir um pequeno loader no botão vermelho, logo após o usuário clicá-lo. Esse loader irá aguardar o retorno do callback no qual apresentamos uma nova mensagem.

Se você desejar ver o que mudou exatamente no projet, [acesse este link para ver o diff](https://github.com/danielschmitz/crud-vuejs/commit/0a55b0f5d1a24f5de3bdd229ac26ca55c256156d).

Com este artigo nós terminamos o "CRUD Básico" exibindo todos os passos para criar, alterar, exibir e remover dados utilizando o Vue e o Json Server. Ainda existem outros pontos a serem abordados, como o botão GPS para exibir um google maps, o botão + para exibir as cervejas de uma cervejaria, que é uma típica tela 1xN. Vamos sim continuar esse processo, aguardem! 



