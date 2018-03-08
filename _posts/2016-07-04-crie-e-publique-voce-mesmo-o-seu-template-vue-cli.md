---
layout: post
title: 'Crie e publique você mesmo o seu template vue-cli'
main-class: 'dev'
date: 2016-07-04 15:57:17 
description: derscricao
color: '#637a91'
tags: vue-js
 - ferramentas
layout: post
introduction: introducao
---

Vimos no [artigo anterior](http://www.vuejs-brasil.com.br/crie-rapidamente-um-projeto-vue-com-vue-cli-e-browserify/) o **vue-cli**, uma ferramenta de linha de comando instalada pelo npm (npm i -g vue-cli) e que é usada para criar projetos prontos com uma estrutura mínima possível (chamados de skeletion ou boilerplate).

Neste artigo é abordado como você pode criar o seu próprio template. Para criar o template, é necessário criar uma estrutura de arquivos no qual o **vue-cli** consiga compreender. 

Para facilitar este processo, vamos dividir a criação do template em 4 etapas distintas:

- Etapa de criação 
- Etapa de adaptação
- Etapa de testes e uso
- Etapa de publicação

## 1 - Etapa de criação

Nesta fase estamos decidindo o que o template terá em termos de instalação e uso. Criaremos como exemplo um template que possui uma infra estrutura completa para o vue, com os seguintes plugins:

- Vue e Vueify (componentes .vue)
- Vuex
- Vue Router
- Vue Resource
- Bootstrap CSS (Bulma)

O nome do nosso template será `vue-browserify-complete`. O nome `browserify` é adicionado ao template para facilitar o uso dos desenvolvedores, pois geralmente existe uma escolha entre `browserify` e `webpack`.

Em um primeiro momento, podemos iniciar o nosso template se baseando em outro. Essa é a forma mais simples de começar. Escolhemos então o `browserify-simple` e criamos o projeto, da seguinte forma:

```
$ vue init browserify-simple vue-browserify-complete-template
```

Logo na criação, é pedido o nome do projeto. Neste ponto, ao invés de colcoar o nome do project, coloque `projectname`, conforme a imagem a seguir:

![](/content/images/2016/07/2016-07-01-15_09_33-npm-1.png)

Faça o mesmo para `description` e `author`, informando `projectdescription` e `projectauthor`. Em "Private", escolha "n". O seu projeto será configurado conforme a figura a seguir:

![](/content/images/2016/07/2016-07-01-15_16_04-npm.png)

> **Anote aí**
>
> Estes nomes serão usados no futuro: projectname, projectdescription e projectauthor.

Após a criação do diretório `vue-browserify-complete-template`, use o npm install para carregar as bibliotecas básicas, pois precisamos testar o projeto antes de publicá-lo:

```
cd vue-browserify-complete-template
npm install
```

Após a instalação padrão, vamos adicionar os pacotes extras que iremos incluir no template:

```
npm i -S vuex vue-router vue-resource bootstrap
```

Após instalar todas estas bibliotecas, precisamos fazer o nosso template funcionar, vamos conferir como está o nosso projeto. Abra-o no seu editor de textos preferido e dê uma olhada na estrutura do projeto:

![](/content/images/2016/07/2016-07-01-15_22_46-vue-browserify-complete-template---Visual-Studio-Code-2.png)

Temos aqui um simples projeto, já com as bibliotecas instaladas no node_modules e configuradas no arquiv `package.json`. Veja que, o `package.json` é o arquivo que configura todo o seu projeto. Então ele deve ser tratado com muito cuidado! Vamos dar uma olhada nele, que a princípio possui o seguinte código inicial:

```json
{
  "name": "projectname",
  "description": "projectdescription",
  "author": "projectauthor",
  "scripts": {
    "watchify": "watchify -vd -p browserify-hmr -e src/main.js -o dist/build.js",
    "serve": "http-server -c 1 -a localhost",
    "dev": "npm-run-all --parallel watchify serve",
    "build": "cross-env NODE_ENV=production browserify src/main.js | uglifyjs -c warnings=false -m > dist/build.js"
  },
  "dependencies": {
    "bootstrap": "^3.3.6",
    "vue": "^1.0.0",
    "vue-resource": "^0.9.3",
    "vue-router": "^0.7.13",
    "vuex": "^1.0.0-rc"
  },
continua...
```

Os nomes que usamos lá no início, como "projectname" está agora presente aqui no `package.json`. Este é o primeiro detalhe que você tem que saber sobre a criação do template: você pode criar variáveis que serão questionadas no início da criação do template, e que serão usadas na construção do mesmo. Uma delas é o nome do projeto. 

Vamos supor que no nosso template queremos informar a versão do projeto, iniciando do "0.0.1". Então precisamos, primeiro, adicionar essa informação no `package.json`: 

```json
{
  "name": "projectname",
  "version" : "0.0.1",
  "description": "projectdescription",
  "author": "projectauthor",
continua...
```

> **Anote aí**
>
> O package.json configura o template e precisamos ter máxima atenção nele

Agora chegou o momento de criarmos as funcionalidades que estarão disponíveis no template. 

### Router

O router pode ser configurado da seguinte forma:

- Editar o arquivo main.js
- Incluir o arquivo router.js
- Incluir o arquivo routerconfig.js
- Incluir o arquivo content/MainContent.vue

No arquivo main.js, alteramos para:

```
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import RouterConfig from './routerconfig'

Vue.use(VueRouter)
const router = new VueRouter()
router.map(RouterConfig)
router.start(App, 'App')
```

Incluímos aqui o `VueRouter` do node_modules e o `RouterConfig` que é o arquivo `routerconfig.js`. Veja que alteramos o `main.js` para usar o Vue Router, e que configuramos o router para carregar as informações do arquivo `routerconfig.js`. Este novo arquivo possui o seguinte código:


```
import MainContent from './content/MainContent.vue'

const RouterConfig = {
    '/': {
        component: MainContent
    }
}

export default RouterConfig;
```

O  routerconfig.js terá toda a configuração de rotas do template. Ainda vamos criar alguns templates depois, mas por enquanto temos apenas o `MainContent`, que será criado a seguir:

```
<template>Main Content</template>
<script>
    export default{
        
    }    
</script>
```

Para finalizar a configuração básica do router, voltamos ao componente `App.vue` para adicionar o `router-view`, que é o local onde o router irá processar as rotas. Alteramos o `App.vue` para:

```
<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <div>
        <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Hello Vue!'
    }
  }
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}
</style>
``` 

Perceba que adicionamos uma nova div com o `<router-view></router-view>`. Até o momento, o projeto possui os seguintes arquivos

![](/content/images/2016/07/2016-07-01-15_55_05-vue-browserify-complete-template---Visual-Studio-Code.png)

**Vamos testar!!**

Precisamos testar o projeto e ver se não existem erros até o momento. Então execute `npm run dev` no terminal e verifique no navegador se o resultado é este aqui:

![](/content/images/2016/07/2016-07-01-16_00_16-projectname.png)

Perceba que o router está funcionando perfeitamente. Na barra de endereços temos o /#!/ e temos o "Main Content abaixo do "Hello Vue!".

## Vue Resource

O Vue Resouce é configurado para que possamos ler um objeto JSON do servidor. Primeiro, devemos criar este objeto, que poderemos chamar de "foo.json", veja:

```
{ 
  "msg": "a foo message"
}
```

Este arquivo deve ser criado na raiz do projeto, conforme a figura a seguir:

![](/content/images/2016/07/2016-07-01-16_08_24-foo-json---vue-browserify-complete-template---Visual-Studio-Code.png)

Para usarmos o Vue Resource, altere o arquivo `main.js`, adicionando o plugin:

```
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import RouterConfig from './routerconfig'
import VueResource from 'vue-resource'

Vue.use(VueRouter)
Vue.use(VueResource)
const router = new VueRouter()
router.map(RouterConfig)
router.start(App, 'App')
```

Veja que importamos o resource e usamos o `Vue.use` para adicioná-lo à instância Vue. Crie um novo componente que irá usar o resource, vamos adicioná-lo em `src/content/ResoureceContent.vue`, veja:

```
<template>
    Resuorce Content

    <button @click="onButtonClick">get foo.json</button> 
    {{fooMessage}}

</template>
<script>
    export default{
        data () {
            return {
                fooMessage: ''
            }
        },
        methods :{
            onButtonClick() {
                this.$http.get('/foo.json').then(
                (response) => {
                    this.fooMessage = JSON.parse(response.data).msg
                },
                (error) => {
                     console.error(error.statusText)
                })
            }
        }
    }    
</script>
```

Este componente, um pouco mais complexo, possui um botão que irá chamar o método `onButtonClick`. Neste método, usamos `this.$http.get` para efetuar uma chamada Ajax ao endereço "/foo.json", e usamos promise para exibir a mensagem que veio do Ajax na variável `fooMessage`. A ideia aqui é apenas apresentar um exemplo simples de leitura Ajax mostrar uma resposta na página.

Para testarmos este componente, volte ao `routerconfig.js` e adicione a seguinte rota:

```
import MainContent from './content/MainContent.vue'
import ResourceContent from './content/ResourceContent.vue'

const RouterConfig = {
    '/': {
        component: MainContent
    },
    '/resourceExample': {
        component: ResourceContent
    }
}

export default RouterConfig;
```

Veja que a rota `/resourceExample` irá carregar o componente `ResourceContent.vue`. Para testarmos esta rota (pois ainda nao criamos um menu), acesse diretamente: `http://127.0.0.1:8080/#!/resourceExample`. Clique no botão para obter uma tela semelhante a figura a seguir:

![](/content/images/2016/07/2016-07-01-16_33_16-projectname.png)

### Vuex

Agora vamos incluir um exemplo de Vuex no projeto. Aproveitando o [artigo sobre Vuex](http://www.vuejs-brasil.com.br/vuex/) do Fábio Vedovelli, vamos criar:

- O diretório `src/vuex`
- O arquivo `src/vuex/store.js`

**src/vuex/store.js**:
```
import Vue from 'vue'  
import Vuex from 'Vuex'

Vue.use(Vuex)

export default new Vuex.Store({  
    state: {
      user: {
        name: '',
        email: ''
      }
    },
    mutations: {
      SET_USER (store, obj) {
        store.user = obj.user
      }
    }
  })
```

Após criar o store, vamos criar o componente `VuexContent.vue`, que irá usar o store:

```
<template>
    Vuex Content
    <button @click="trySetUser">Vuex doAction</button>
    {{user | json }}    
</template>
<script>
    export default{
        vuex: {  
            getters: {
                user: store => store.user
            },
            actions: {
                setUser ({dispatch}, obj) {
                dispatch('SET_USER', obj)
                }
            }
        },
        methods: {
            trySetUser(){
                  let user = {
                    user: {
                        username: 'New username',
                        email: 'email@email.com'
                    }
                  }
                  this.setUser(user);
            }
        }
    }    
</script>
```

O que temos neste componente é o uso dos conceitos do Vuex, temos as actions e os getters funcionando. 

Precisamos adicionar o store no App.vue:

```
<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <div>
        <router-view></router-view>
    </div>
  </div>
</template>

<script>
import store from './vuex/store'

export default {
  data () {
    return {
      msg: 'Hello Vue!'
    }
  },
  store
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}
</style>
```

Veja que importamos o store de `vuex/store` e usamos na configuração do componente App.vue.

Para terminar esta parte do Vuex, vamos adicionar uma rota para o componente, no arquivo routerconfig.js:

```
import MainContent from './content/MainContent.vue'
import ResourceContent from './content/ResourceContent.vue'
import VuexContent from './content/VuexContent.vue'


const RouterConfig = {
    '/': {
        component: MainContent
    },
    '/resourceExample': {
        component: ResourceContent
    },
    '/vuexExample': {
        component: VuexContent
    }
}

export default RouterConfig;
```

Para que possamos testar o Vuex, acesse diretamente a seguinte url  `http://127.0.0.1:8080/#!/vuexExample` e veja se o resultado é semelhante a figura a seguir:

![](/content/images/2016/07/2016-07-01-17_07_07-projectname.png)

### Bootstrap CSS

Pode-se instalar qualquer framework css bootsrap que você considere mais util. Existem diversos com o bootstrap, materialize, semantiui, zurb, bulma entre outros. Neste artigo iremos usar o bulma, então inicialmente instale-o pelo npm:

```
npm i -S bulma
```

Após a instalação é preciso alterar o arquivo `index.html` e incluir o css do framework antes da tag `</head>`, veja:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>projectname</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="node_modules/bulma/css/bulma.css"/>
  </head>
  <body>
    <app></app>
    <script src="dist/build.js"></script>
  </body>
</html>
```
 
Perceba também que incluímos o `font-awesome`, no qual pode-se usar os ícones desta biblioteca. O font-awesome foi instalado através de CDN, linkando-o direto em um servidor web, que é uma outra forma de se usar as bibliotecas css/javascript em qualquer projeto. Fique a vontade em usar o que você achar que é melhor para o sue projeto.

### Finalizando o router

Agora que temos quase tudo pronto para terminar o template, precisamos voltar ao Router e criar um simples menu, seguido do carregamento dos consecutivos componentes. 

```
<template>
    <div id="app">
        <nav class="nav">
            <div class="nav-left">
                PROJECTNAME
            </div>
            <span class="nav-item">
                <a v-link="{ path: '/' }" class="button is-primary">
                    <span class="icon">
                    <i class="fa fa-home"></i>
                    </span>
                    <span>Main Content</span>
                </a>
                <a v-link="{ path: '/resourceExample' }" class="button is-primary">
                    <span class="icon">
                    <i class="fa fa-link"></i>
                    </span>
                    <span>Resource example</span>
                </a>
                <a v-link="{ path: '/vuexExample' }" class="button is-primary">
                    <span class="icon">
                    <i class="fa fa-bolt"></i>
                    </span>
                    <span>Vuex example</span>
                </a>
            </span>
        </nav>
        <div class="container">
            <router-view></router-view>
        </div>
    </div>
</template>
<script>
import store from './vuex/store'

export default {
  data () {
    return {
      msg: 'Hello Vue!'
    }
  },
  store
}
</script>

<style>
    body {
        font-family: Helvetica, sans-serif;
    }
</style>
```

Usamos o `<nav>`, que é comum a quase todos os frameworks bootstrap, para criar uma barra de navegação simples, incluindo 3 botões que que são links do vue-router, e usam a propriedade `v-link="{ path: '/resourceExample' }"` para que o *routerconfig.js* possa encontrar o ser referente componente e carregá-lo no `<router-view>`.

![](/content/images/2016/07/2016-07-04-10_49_01-projectname.png)

Após reescrever o App.vue, temos a princípio um site simples com funcionalidades importantes sendo usadas. É um bom "starter" para qualquer projeto. Nossa primeira etapa está concluída! 

## 2 - Etapa de adaptação

Nesta etapa estamos com todo o layout pronto, funcionando como se fosse uma simples aplicação inicial. Agora devemos começar a pensar nessa aplicação como um TEMPLATE pra o vue-cli. 

Primeiro, é recomendável ter uma conta no github e conhecer git para que você possa compartilhar o seu template com outros, e também para que outros possam lhe ajudar a melhorar o seu template! Então, se você ainda não tem uma conta no github, chegou a hora de ter.

Após criar a conta, crie um novo repositório. No meu caso, vou usar essas configurações (vc pode copiá-las no seu também):

![](/content/images/2016/07/2016-07-04-10_56_21-Create-a-New-Repository.png)

Lembre-se de marcar o item "Initialize this repository with a README".

Após criar o repositório, precisamos fazer o clone dele no seu computador. Para isso, você precisará instalar o [git](https://git-scm.com/) no seu sistema operacional, se ainda não o fez.

Na linha de comando, digite:

```
git clone https://github.com/<USER_NAME>/vue-browserify-complete.git
```

Agora você tem o diretório "vue-browserify-complete" e "vue-browserify-complete-template" e isso foi feito de propósito, já que o template deve ter de seguir algumas regras destacadas a seguir:

- Um template **DEVE** ter um diretório chamado `template` e será nesse diretório que todos os arquivos do template ficarão
- Um template **DEVE** ter um arquivo chamado `meta.json` que contém informações sobre o projeto

Realize as seguintes etapas para iniciar a configuração do seu template:

- Crie o diretório `vue-browserify-complete/template`
- Copie TODO o conteúdo de `vue-browserify-complete-template` para `vue-browserify-complete/template` **EXETO** o diretório `vue-browserify-complete-template/node_modules`.

> Pode-se abrir o projeto `vue-browserify-complete` no seu editor de textos preferido. Usamos o Visual Studio Code por ter uma boa compatibilidade com projetos javascript e com git.

Agora precisamos configurar o arquivo `meta.json`. Este arquivo será responsável por algumas configurações do projeto. Na configuração mais simples, iremos apenas realizar algumas perguntas e aplicar as respostas no template.

Crie o arquivo `meta.json` com o seguinte conteúdo:

```
{
  "schema": {
    "name": {
      "type": "string",
      "required": true,
      "label": "Project name"
    },
    "description": {
      "type": "string",
      "required": true,
      "label": "Project description",
      "default": "A Vue.js + router + resource + vuex + bulma project"
    },
    "author": {
      "type": "string",
      "label": "Author"
    }
  }
}
```

Depois que você copiou o template, e criou o arquivo meta.json, podemos dar uma olhada nas alterações do repositório git que estão sendo feitas. Pode-se utilizar o comando "git status" que irá retornar algo semelhante a figura a seguir:

![](/content/images/2016/07/2016-07-04-11_22_53-npm.png)

No VSCode, pode clicar na aba GIT e ver as diferenças também:

![](/content/images/2016/07/2016-07-04-11_24_38-vue-browserify-complete---Visual-Studio-Code.png)

Vamos então comitar tudo isso para o repositório, com o seguinte comando:

```
git add .
git commit -m "First Commit"
git push
```

Todo o código será "pushado" para o github. 

> Se você não conhece bem o git e github, [leia este artigo](http://tableless.com.br/tudo-que-voce-queria-saber-sobre-git-e-github-mas-tinha-vergonha-de-perguntar/) para se informar melhor. 

O arquivo meta.json é responsável em configurar as perguntas que faremos aos usuários quando eles forem criar os seus projetos. Configuramos 3 perguntas: Nome do projeto, Descrição do projeto e autor. 

O que precisamos fazer agora é aplicar essas perguntas no template. Lembre-se que, o template a partir de agora não estará mais usável. Não iremos fazer um `npm install` ou então `npm run dev`, pois ao inserir as variáveis no template, iremos "quebrá-lo" como um projeto node/javascript, mas ele será válido para um template vue-cli, que é o nosso objetivo.

No início deste artigo, pedimos para guardar três nomes: projectname, projectdescription e projectauthor. Agora chegou o momento de usá-los, e isso é feito de forma muito simples, seguindo basicamente a regra a seguir:

- Se você criou no meta uma variável chamada "name", poderá aplicá-la no projeto com {{name}}

Ou seja, vamos fazer uma busca por "projectname" no projeto. Pelo VSCode, temos o seguinte resultado:

![](/content/images/2016/07/2016-07-04-11_42_48-index-html---vue-browserify-complete---Visual-Studio-Code.png)

Agora vamos percorrer cada `projectname` e trocar por `{{name}}` em todos os arquivos do template. Por exemplo, o arquivo `template/src/App.vue` ficará semelhante a imagem a seguir:

![](/content/images/2016/07/2016-07-04-11_45_37-App-vue---vue-browserify-complete---Visual-Studio-Code.png)

Faça o mesmo com `projectdescription` e `projectauthor` trocando por `{{description}}` e `{{author}}`.

Após estas mudanças, faça novamente o commit/push:

```
git add .
git commit -m "Replace variables"
git push
```

Pode-se usar o VSCode também para comitar, veja:

![](/content/images/2016/07/2016-07-04-11_50_55-package-json---vue-browserify-complete---Visual-Studio-Code.png)

Para realizar o PUSH no VSCode, clique no ícone de sync na barra azul inferior, conforme a imagem a seguir:

![](/content/images/2016/07/2016-07-04-11_52_41-Program-Manager.png)

Com a configuração inicial pronta, é preciso realizar um último passo antes de testarmos o template no vue-cli. Abra o arquivo `template/src/content/ResourceContent.vue` e verifique a linha 5, onde temos o `{{fooMessage}}`. Esta variável é da aplicação e não do template, ou seja, `foomessage` não é uma variável do `meta.json`. Isso significa que temos que alterar a variável de `{{fooMessage}}` para `\{{fooMessage}}`, ou seja, adicionar um caractere de escape antes da primeira chave. Com isso, o que é `\{{fooMessage}}` no template se torna `{{fooMessage}}` na aplicação gerada pelo vue-cli.

faça o mesmo para `{{user | json }}` no arquivo `template/src/content/VuexContent.vue`.

Após realizar estas modificações, execute o seguinte comando no terminal:

```
git diff
```

Isso irá mostrar as alterações que foram feitas desde o último commit, semelhante a figura a seguir:

![](/content/images/2016/07/2016-07-04-12_02_12-npm.png)

Faça novamente o commit/push:

```
git add .
git commit -m "Escape app vars"
git push
```

Com isso nós terminamos a etapa de adaptação, nosso template está pronto para ser testado. 

## 3 - Etapa de testes

A etapa de testes compreende no uso do vue-cli para criar a aplicação baseada no seu template. Como o template está no repositório do github, pode-se usar o seguinte comando:

```
vue init SEU_USERNAME/vue-browserify-complete teste1
```

Não esqueça de trocar o **SEU_USERNAME** pelo.... seu usuário, ok? 

Uma resposta do vue-cli é dada a seguir, conforme a figura a seguir:

![](/content/images/2016/07/2016-07-04-12_16_41-npm---vue--init-danielschmitz_vue-browserify-complete-teste1.png)

Estas são as variáveis que configuramos no *meta.json*. Após fornecer essas informações, podemos testar o projeto recém criado (nesse caso teste1) fazendo o `npm install` para instalar todas as bibliotecas, e o `npm run dev` para compilar tudo e abrir o servidor, no qual estará disponível em "localhost:8080". 

Se, ao executar `npm run dev`, uma mensagem de erro for disparada, é quase certo que a porta 8080 está sendo usada por outro processo. Localize-o e finalize para poder executar o "teste1" novamente.

Após executar o servidor, acesse a url e tenha um resultado semelhante a figura a seguir:

![](/content/images/2016/07/2016-07-04-12_23_10-teste1.png)

Parabéns! você criou o seu template vue com sucesso! A partir desse momento você pode partir para outras customizações, sempre lembrando de comitar as mudanças para o github e reaplicar o teste.

## 4 - Publicação

Esta etapa é opcional, se você acreditar que o seu template ficou realmente bom e pode ajudar outras pessoas, você pode submetê-lo ao repositório oficial do vue-cli. Desta forma, ao invés de usar SEU_USERNAME/NOME_DO_TEMPLATE, será possível usar somente NOME_DO_TEMPLATE. Lembre-se que todo o seu projeto, comentários e documentação devem estar em inglês.

Mesmo que o template não esteja no oficial, nada impede de usar o seu próprio repositório para uso, então se você criou um template legal e quer compartilhar, deixe o endereço nos comentários logo abaixo!



 






