---
layout: post
title: 'Criando uma TODO LIST com Vuejs e Google Firebase'
main-class: 'dev'
date: 2018-03-08 00:00:00 
description: derscricao
color: '#637a91'
tags: 
layout: post
introduction: introducao
---

Neste novo artigo vamos abordar algo que todos nós fazemos: **TAREFAS!** 
E nada melhor que ficar em dia com elas. 

Mas para isto precisamos listá-las de maneira que saibamos que tarefas temos a fazer. Dito isso, vamos por a mão na massa e desenvolver uma aplicação de *TODO LIST*, ou em bom português: *LISTA DE TAREFAS*.

Meu objetivo aqui, é além de apresentar (*novamente!*) o Vue, também apresentar o uso do [Google Firebase](firebase.google.com). 

>**"O Firebase é uma plataforma móvel que ajuda a desenvolver aplicativos de alta qualidade."**

Chega de enrolação e vamos **escovar bits**!

>##Passo#1

* Criar um projeto Firebase no [Google Firebase Console](https://console.firebase.google.com) (GFC)
 * **É necessária uma conta Google!**
* Copiar o *snnipet* de configuração com os dados de acesso ao projeto recém criado

> #####Criando o Projeto Firebase

Acessando o link do GFC, você encontra a seguinte tela:
![GFC](http://i67.tinypic.com/2wdn85l.png)

Clique em **CRIAR NOVO PROJETO**

![GFC](http://i64.tinypic.com/55pdg1.png)

Preencha com o nome da nossa aplicação (**todolist**) e selecione Brasil na lista, e clique em CRIAR PROJETO.
Pronto! Agora já temos onde salvar nossas tarefas!

>#####Copiando o *snippet* de configuração

Ao voltar para o GFC, você verá seu Projeto Firebase, clique nele para acessar a tela de **OVERVIEW** e poder copiar o *snippet*. A tela de **OVERVIEW** tem estas opções:
![](http://i66.tinypic.com/vxit7p.png)

Vamos clicar no botão roxo e "Adicionar o Firebase ao seu app da Web".

Feito isso temos o *snippet*!
![](http://i68.tinypic.com/2uzcmea.png)

Observem o código do *snippet* e notem que ele já vem pronto pra ser adicionado ao seu index.html, usando a tag **`<script>`**.

Nele contém algumas informações que o Firebase precisa para fazer o acesso aos dados contidos no banco. Vamos passar rapidamente para cada uma das propriedades:

* **apiKey**: uma chave única para cada projeto Firebase
* **authDomain**: URL para fazer a autenticação de usuário ao banco (não utilizaremos aqui)
* **databaseURL**: como o próprio nome sugere, este é o caminho (URL) para o banco de dados
* **storageBucket**: indica qual storage ficarão os arquivos carregados para o banco (não utilizaremos também)

Por fim, a linha `firebase.initializeApp(config);` inicia o firebase com as configuraçoes passadas pelo *snippet*.

Isto encerra nossa parte de criar o banco de dados **Firebase**.

>##Passo#2

* Criar o SPA (single page application)
* Importar o Vuejs
* Importar o Bootstrap
* Escrever o script para iniciar o Vue
* Escrever o HTML da aplicação

>#####Criando o SPA

Nosso aplicativo de página única (da sigla SPA em inglês) será apenas um arquivo HTML. 
Abaixo o "esqueleto" padrão com o markup inicial e com nosso *snippet* adicionado.

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Lista de Tarefas</title>
</head>
<body>

<script src="https://www.gstatic.com/firebasejs/3.2.0/firebase.js"></script>
<script>
  // Initialize Firebase
  var config = {
    apiKey: "%API_KEY%",
    authDomain: "%AUTH_DOMAIN%",
    databaseURL: "%DATABASE_URL%",
    storageBucket: "",
  };
  firebase.initializeApp(config);
</script>
</body>
</html>
```

>#####Importando o Vue e o Bootstrap

Até agora nossa SPA não absolutamente nada! Vamos importar o Vue e o Bootstrap alterando a tag **`<head>`**. Ambos os sites fornecem um link CDN para incorporar no HTML. 

**Vue**:
`https://cdnjs.cloudflare.com/ajax/libs/vue/1.0.26/vue.min.js`

**Bootstrap**:
`https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css`

Vamos modificar nosso **head**:
```html
<head>
  <meta charset="UTF-8">
  <title>Lista de Tarefas</title>
  <!-- ACRESCENTE AS LINHAS ABAIXO -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vue/1.0.26/vue.min.js">
</head>
```

>#####Inciando o Vue

Agora vamos estruturar o **Vue**!
Vamos modificar nossa tag **script**:

```html
<script>
  // Initialize Firebase
  var config = {
    apiKey: "%API_KEY%",
    authDomain: "%AUTH_DOMAIN%",
    databaseURL: "%DATABASE_URL%",
    storageBucket: "",
  };
  firebase.initializeApp(config);
  //***
  //ADICIONE ESTAS LINHAS
  new Vue({
    el: "#app",

    data: {
      todos: [],
      todo: {
        title: '',
        completed: false
      }
    }
  })
```

Vamos entender o bloco que adicionamos para inicializar o **Vue**:

* `new Vue`: inicia uma instância do Vuejs e como parâmetro, passamos um objeto javascript de configuração entre `{}`
* `el:"#App"`: aqui indicamos qual elemento HTML será observado pelo Vue e tudo que estiver dentro deste elemento poderá ser observado e manipulado também.
* `data: { ... }`: a propriedade **data** nós passamos um objeto de configuração (OC) onde cada propriedade é uma "variável" que é observada pelo Vue. Para esclarecer melhor, `todos: []` é um **array**, enquanto `todo: { title: '', completed: false }` é um objeto com duas propriedades: **title** (título da tarefa) e **completed** (se a tarefa está ou não completa).

Como visto acima, nós "dizemos" ao **Vue** qual elemento observar, no caso um elemento com o `id="app"`, então vamos adicionar este elemento e o markup restante contendo a tabela e o campo para adicionar tarefas!

>#####Criando o markup HTML da Aplicação

Vamos incluir nosso markup logo abaixo da tag **`<body>`**:

```html
<body>
  <!-- APP CONTROLADA PELO VUE -->
  <div id="App">
    <!-- Tudo que estiver aqui dentro será tambem observado e controlado pelo Vue -->
    <div class="container well-lg">
      <h3>Lista de Tarefas</h3>
      <hr>
      <!-- CAMPO PARA ADICIONAR A TAREFA -->
      <div class="col-md-6 col-md-offset-6">
        <div class="form-group">
          <div class="input-group">
            <input type="text" class="form-control" v-model="todo.title" />
            <div class="input-group-btn">
              <button @click="addTodo" class="btn btn-primary">Adicionar Tarefa</button>
            </div>
          </div>
        </div>
      </div>
      <hr>
      <!-- TABELA -->
      <div class="col-md-12">
        <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Tarefa</th>
            <th width="1%">Completa?</th>
            <th width="1%"></th>
          </tr>
        </thead>
      </table>
      </div>
    </div>
    <!-- SCRIPT -->
```

Vamos dar uma olhada no markup acima, nós criamos um container usando a classe bootstrap `container` junto com outra classe para dar uma certa margem interna ao container, `well-lg`. O intuíto deste artigo não é abordar HTML e/ou Bootstrap, o nosso foco aqui é **Vue** e **Firebase**, então eu espero que pelo menos o markup HTML esteja fazendo sentido para você! *(risos)* :)
Continuando, criamos uma tabela com apenas o cabeçário, e bordas.

**Mas!** Se observar melhor o markup, vai ver dois *"caras estranhos"* ali no meio. O primeiro está dentro do elemento **`<input>`** e o outro dentro do elemento **`<button>`**. 

>#####O que faz cada um?

* `v-model`: esta é uma diretiva do Vue que faz a ligação entre uma propriedade Vue e o elemento HTML (*isso é chamado de* ***two-way data binding***). Portanto o `v-model="todo.title"` vai *fazer a ponte* entre o valor que será digitado no campo de texto e a propriedade `title` do objeto `todo`. O inverso também acontece. Toda vez que o valor de `title` sofrer uma alteração no Vue, essa alteração será refletida no campo de texto.

* `@click`: esta é outra diretiva do Vue, chamada `v-on`, mas aqui representada por seu atalho `@`. Essa diretiva diz ao Vue para ficar de olho num determinado evento, no nosso caso o `click` do botão, e executar um método ou expressao, toda vez que este evento for disparado (ou ocorrer).
