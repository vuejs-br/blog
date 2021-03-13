---
layout: post
title: 'Conheça o iView, um toolkit de interface para o Vue.js'
main-class: 'dev'
date: 2018-02-12 17:38:34 
color: '#637a91'
tags: toolkit iview ui interface
author: daniel-schmitz
---

Com o crescimento do *Vue* centenas de bibliotecas surgem a cada dia para dar suporte a ele, dentre eles temos algumas ligadas à interface, como o iView. Neste artigo veremos um pouco sobre ele, e em como usá-lo nos seus projetos. 

Para ter um melhor aproveitamento neste artigo, é necessário o conhecimento introdutório do Vue, dentre eles podemos destacar os seguintes tópicos:

- NPM e em como gerenciar pacotes Node
- O vue-cli e seus templates, juntamente com o webpack
- Os *Single File Componentes* (isso, os arquivos .vue)
- Vue Router

## Instalação

Existem 2 formas básicas de instalar o iview no projeto. A primeira é através do CDN, adicionando diretamente os arquivos JS e CSS no arquivo HTML, da seguinte forma:

<script src="https://gist.github.com/danielschmitz/2c282ce3a492532c8fe777bc710ee068.js"></script>

Um exemplo simples, utilizando CDN e com o locale em pt-BR, pode ser visto a seguir:
<a class="jsbin-embed" href="http://jsbin.com/buwuton/embed">JS Bin on jsbin.com</a><script src="http://static.jsbin.com/js/embed.min.js?4.1.1"></script>

A utilização de CDN é válida para testes, principalmente no JS Bin (ou outro editor online). 

Para os nossos projetos, sempre estaremos utilizando o **vue-cli**, e fazendo a instalação através do NPM. Essa é a forma mais recomendada! O iview possui, inclusive, o **iview-cli** capaz de criar projetos com a sua estrutura, mas seria mais um cli no qual deveríamos ter domínio e, a princípio, não é necessário. 

Vamos começar criando um novo projeto, da seguinte forma:

![](https://i.imgur.com/W7Q6Opa.png)

O que fizemos até agora foi criar um projeto chamado *myproject* usando o template *webpack*, juntamente com *Vue-Router* e sem algumas funcionalidades extras, como o ESLint. Após a criação do projeto, prosseguiremos com a instalação do ivew, da seguinte forma:

![](https://i.imgur.com/ankyCJp.png)

Como você já deve saber, o comando `npm i` irá instalar o pacote e, juntamente com o parâmetro `-S`, irá salvar o pacote no `package.json`.

Continuando, é preciso instalar o iview no arquivo `src/main.js`, que é onde o Vue está instanciado. A princípio, temos o seguinte código:

<script src="https://gist.github.com/danielschmitz/da4e7a42e7ebb64c20ecae5f902a7458.js"></script>

Para adicionar o iview, faremos:

![](https://i.imgur.com/FsUgr3h.png)

O novo código está em destaque. Basicamente, importamos o iView, o seu css e o locale em português. Depois usamos o comando `Vue.use` para adicionar o plugin `iview` ao Vue. Repare que, antes de adicionar o *iview* ao vue, configuramos o seu locale.

> **Para saber mais**
>
> Você pode carregar os componentes do iview sob demanda. Para isso, dê uma olhada neste [artigo](https://www.iviewui.com/docs/guide/start-en#Import_on_demand).
> 
> Você pode usar o *vue-i18n* em conjunto com o ivew, carregando vários *locales* e ativando-o dinamicamente. Para isso, dê uma olhada neste [artigo](https://www.iviewui.com/docs/guide/i18n-en#Use_in_Webpack)

Após realizar a instalação, executamos `npm run dev` para que possamos testar o ivew.

## Testando o ivew 

Neste momento vamos supor que o ivew já foi instalado como um plugin do Vue, no arquivo *src/main.js*, e que o projeto está sendo executado através do comando `npm run dev`. Com o navegador aberto, você deve estar vendo algo como:

![](https://i.imgur.com/djftDLb.png)

Abra o arquivo `src/components/HelloWorld.vue` e altere o código para:

<script src="https://gist.github.com/danielschmitz/271692f4adb34d859df1bedb401c3b2c.js"></script>

Neste novo código, fizemos o seguinte:

- Usamos o componente *i-button* e criamos um botão. Esse botão chama o método *show* no evento *@click*. Este método deverá estar no *methods* do Vue.
- Criamos outro componente chamado *Modal*. A sua visibilidade está condicionada a variável *visible* (no *data* do Vue), através da propriedade *v-model*.
- O método *show* altera a variável *visible* para true, fazendo com que o modal seja visto.

O resultado deste código é visto a seguir:

![](https://i.imgur.com/Vtjs6eX.gif)

## Alterando a app, criando algo útil

Agora que temos o iview funcionando podemos criar algo um pouco mais útil, com cara de aplicação. Quase todas as bibliotecas de interface possuem um componente que gerencia a disposição das informações na tela, e no iView isso não é diferente, através do componente **Layout**.

Este componente divide a tela em blocos, dos quais podemos destacar:

- **Header**: Cabeçalho da aplicação, na parte superior
- **Sider**: A parte do menu flutuante que fica no lado direito ou esquerdo da aplicação
- **Content**: A parte do conteúdo em si ! Se você conhece o Vue Router, sabes que existe o `<router-view></router-view>`, que é o bloco onde o Router renderiza o conteúdo. Então ese bloco é inserido nesta parte.
- **Footer**: Rodapé da aplicação, na parte inferior

A imagem a seguir ilustra melhor a disposição dos blocos.

![](https://i.imgur.com/kVZvk2g.png)

Vamos à prática! Sabemos que o projeto padrão criado pelo vue-cli dispõe do arquivo `src/App.vue` que é onde a aplicação está contida, e que cada tela estaria, basicamente, no diretório `src/componentes`. Neste diretório temos o componente `HelloWorld`, aquele que colocamos o botão modal para teste. 

O que precisamos fazer agora é alterar a aplicação, ou seja, o arquivo `App.vue` e incluir o componente `Layout` para organizar a app. Na [documentação](https://www.iviewui.com/components/layout-en) do componente existem alguns exemplos básicos. Vamos usar um deles e altrar o arquivo `App.vue` para:

<script src="https://gist.github.com/danielschmitz/447ca932120f27fa2427d7bfee361579.js"></script>

Apesar do código extenso, podemos perceber a presença da tag `<Layout>`, juntamente com os componentes `<Header>`, `<Content>`, entre outros. No Header, temos a criação do título da App, que chamamos de "Meu Projeto", e a criação de 2 botões para testarmos o Vue Router. No layout `<Sider>` criamos um Menu, e usamos algumas combinações com o Vue Router para que os links possam ser gerados da forma correta. Ou seja, usamos o `<router-link>` para carregar o conteúdo daquele item de menu no lugar certo. Mas onde fica esse lugar? De acordo com a documentação do Vue Router, é no `<router-view>`, que está estrategicamente adicionado no `<Content>` do Layout.

O router está configurado no `src/router/index.vue`, e nele temos que quando acessarmos a URI `#/` o componente `Hello World` será carregado. 

Desta forma, assim que atualizarmos o App.vue, temos uma tela semelhante a esta:

![](https://i.imgur.com/3EX0IjM.png)

Nesta imagem, removemos o logotipo do vue, mas deixamos como teste a opção da janela Modal. 

Deixo como exercício alterar os itens de menu para algo mais real, inclusive carregando os componentes no Content da aplicação. 

Vamos, no próximo artigo, conhecer um pouco mais dos componentes do iVew. Até lá!





























