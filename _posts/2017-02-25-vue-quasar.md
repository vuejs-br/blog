---
layout: post
title: 'Vue 2 no mundo mobile com Quasar'
main-class: 'dev'
date: 2017-02-25 22:44:07 
description: derscricao
color: '#637a91'
tags: quasar
 - mobile
 - hibrido
layout: post
introduction: introducao
---

É muito comum ver no mercado de trabalho desenvolvedores web que também se disponibilizam na área de desenvolvimento móvel, isso se deve ao fato de termos cada vez mais ferramentas para a construção de aplicativos híbridos, não só isso, como também temos cada vez mais ferramentas que estão usando linguagens e frameworks web para construir essas aplicações.

Entrando no ambiente da biblioteca Vue JS, temos pelo menos três opções para o desenvolvimento móvel:

* [Weex](https://github.com/alibaba/weex) - framework que permite desenvolvimento de aplicativos híbridos e nativos com o VueJS.

* [Quasar](http://quasar-framework.org/guide/) - framework que se equipara muito com o [Ionic Framework](http://ionicframework.com/docs/v2/), porém trabalha com o VueJS e não Angular.

* Trivialmente usando apenas [Cordova](https://cordova.apache.org), esse método consiste em fazer tudo manualmente, importando o Cordova para o VueJS, construído a aplicação como um website, e ao seu término é usado um software como o [Intel XDK](https://software.intel.com/pt-br/intel-xdk) para gerar o aplicativo.

Por já ter conhecimento no Ionic e ver semelhanças entre ele e o Quasar decidi iniciar o meu estudo nesse framework, nesse post irei dar um *Getting Started* para que desenvolvedores que têm dificuldade com inglês entendam como a ferramenta funciona, vocês verão que é basicamente ter conhecimento de VueJS. Aqui iremos criar uma aplicação básica, onde utilizaremos a API do [GitHub](https://developer.github.com/v3/) como base de dados, pegando dela algumas informações sobre um repositório e organização.

Irei dar início considerando que você tenha instalado na sua máquina o [NodeJS](https://nodejs.org) e o gerenciador de pacotes [NPM](https://www.npmjs.com/), o próximo passo será instalar o Quasar globalmente para podermos criar nosso app:

    npm install -g quasar-cli

Após o processo de instalação terminar, podemos entrar em um diretório no qual ficará nosso aplicativo e executar os seguintes comandos para cria-lo e instalar suas dependências:

    quasar init github-client
    cd github-client
    npm install

Vale destacar que `github-client` é o nome da nossa aplicação. Com o término dessa etapa basta executarmos nosso aplicativo, mas como fazemos isso?

**A resposta é:** depende, caso você tenha um aparelho com Android, é possível executar o aplicativo diretamente nele em live, assim facilitando sua vida, para isso usamos o app [Quasar Play App](https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png), executamos o seguinte comando:

    quasar dev --play

Será exibido um QRCode que basta ser lido pelo aparelho com o aplicativo instalado. Caso não tenha um aparelho com Android (como é o meu caso, usuário de Windows Mobile), podemos executar o aplicativo em um navegador usando:

    quasar dev

Ao terminar o processo de compilação, será aberto o link `http://localhost:8080/#/` no seu navegador padrão, com a seguinte página:

 ![Tela inicial app Quasar](http://image.prntscr.com/image/ec5a25c7b0fc4f51bc2b324f4d136712.jpeg)

A página apresentada será a página inicial do seu aplicativo, localizada em `src/components/Index.vue`, mas não iremos usar ela, para mostrar nossos repositórios iremos criar um novo componente `Repositories` com esse comando:

    quasar new component Repositories

**Dica:** para manter a produtividade sempre abra dois terminais no diretório do seu projeto, deixe um sempre responsável por manter a live no Play App ou navegador, e outro para executar comandos como esse acima.

O próximo passo é vincular esse componente a rota `/`, para isso usamos o arquivo `src/router.js`, modificando:

    { path: '/', component: load('Index') }, // Default

Para:

    { path: '/', component: load('Repositories'), name: 'root' },

Note que a live no browser ou android apresenta uma tela vazia, agora iremos construir nosso design do componente, para o artigo não ficar gigante irei colocar o código pronto de cada componente e comentar o que foi adicionado.

Para que você entenda, resumidamente é como estamos acostumados a trabalhar com o Vue e componentes de terceiros, o Quasar conta com [componentes próprios](http://quasar-framework.org/components) que podem ser usados no seu aplicativo apenas copiando e colando o código, e foi isso que fiz no nosso componente `Repositories`:

    <template>
      <q-layout>
        <div slot="header" class="toolbar">
          <q-toolbar-title :padding="1">
            {{owner.name}}
          </q-toolbar-title>
          <button @click="$refs.modalOwner.open()">
            <i>build</i>
          </button>
        </div>

        <div class="layout-view">
          <ul class="breadcrumb">
            <li><a><i>list</i> Lista de repositórios</a></li>
          </ul>

          <div v-if="owner.repositories.length > 0" class="list item-delimiter">
            <div class="item" v-for="rep in owner.repositories" @click="details(rep)">
              <div class="item-content">
                <p>
                  {{rep.name}}
                  <span style="float: right"><i>star</i> {{rep.stars}}</span>
                </p>
              </div>
            </div>
          </div>

          <div v-if="owner.repositories.length <= 0">
            <p>Sem repositórios</p>
          </div>
        </div>


        <q-modal ref="modalOwner" position="right" :content-css="{padding: '30px'}">
          <strong>Trocar de organização</strong>
          <hr>
          <div class="floating-label">
            <input required v-model="owner.link" class="full-width">
            <label>Nome no link do GitHub</label>
            <button class="primary small full-width" @click="register()">
              Pesquisar repositórios
            </button>
          </div>
        </q-modal>
      </q-layout>
    </template>

    <script>
    import { Loading, Toast } from 'quasar'
    import { repositories } from '../resources/github'

    export default {
      data () {
        return {
          owner: {
            name: 'Sem organização selecionada',
            link: '',
            repositories: []
          }
        }
      },
      created () {
        if ('owner' in this.$route.params) {
          this.owner.link = this.$route.params.owner
          setTimeout(() => {
            this.register()
          }, 500)
        }
      },
      methods: {
        register () {
          if (this.owner.link !== '') {
            this.owner.repositories = []
            this.$refs.modalOwner.close()
            Loading.show({ message: 'Procurando repositórios' })

            repositories(this.owner.link).then((result) => {
              result = result.data
              if (result.length > 0) {
                this.owner.name = result[0].owner.login
                for (var i = 0; i < result.length; i++) {
                  this.owner.repositories.push({
                    name: result[i].name,
                    stars: result[i].stargazers_count,
                    full: result[i].full_name
                  })
                }
                Loading.hide()
              }
            }).catch(() => {
              Loading.hide()
              this.$refs.modalOwner.open()
              Toast.create({ html: 'Organização não foi encontrada ou o tempo limite expirou' })
            })
          }
        },
        details (r) {
          this.$router.push({name: 'details', params: {repository: r, owner: this.owner.link}})
        }
      }
    }
    </script>

No `template` desse componente meu elemento raiz será um `q-layout`, e dentro dele terei os elementos da minha tela, nesse caso temos:

* `header` - que representará nossa barra de ferramentas, onde teremos o título da organização e um botão para trocar de organização.

* `layout-view` - classe que indica onde colocamos nosso corpo da página, dentro dessa tenho um título secundário e uma lista para carregar nossos repositórios.

* `q-modal` - nosso último elemento é como o nome diz rs, trata-se de um modal, com um formulário para trocar nossa organização atual.

No `script` é feita a importação de alguns elementos do Quasar, como o Toast (notificações) e Loading (tela de carregamento), são componentes a parte do Quasar usados para deixa-lo mais parecido com um aplicativo. Notem que além disso importei um método `repositories` de um resource (o qual falarei abaixo). O resto do código é aquilo que já conhecemos do Vue:

* `data` - tenho atributos no componente que representam um `owner` do GitHub, com informações como nome, link e repositórios.

* `methods` - há dois métodos nesse componente: o `register` trata de buscar os repositórios usando o método importado do resource e transporta-los para nosso `data`, além de toda firula de mostrar tela de carregamento, etc; o `details` apenas navega para a página de *commits* usando o *vue-router* e enviando parâmetros como: owner e repository.

* `created` - se você sabe um pouco de VueJS, sabe que esse método é executado sempre que o componente é criado, nele eu vejo se estou recebendo um `owner` por parâmetro, caso esteja então executo automaticamente a busca por repositórios, isso será útil quando essa página for acionada pelo back button.


Em resumo, esse componente é uma tela na qual o usuário poderá buscar os repositórios de uma organização no `GitHub`, ao pressionar em um repositório será redirecionado para o componente `Details`, então vamos cria-lo:


    quasar new component Details

Adicionar uma rota para ele, em `/src/router.js`:

    routes: [
      { path: '/', component: load('Repositories'), name: 'root' }, // Default
      { path: '/details', component: load('Details'), name: 'details' }, // Default
      { path: '*', component: load('Error404') } // Not found
    ]

E seu código fica assim:

    <template>
      <q-layout>
        <div slot="header" class="toolbar">
          <q-toolbar-title :padding="1">
            {{repository.name}}
            <i>star</i>
            {{repository.stars}}
          </q-toolbar-title>
          <button @click="$router.push({name: 'root', params: {owner: $route.params.owner}})">
            <i>home</i>
          </button>
        </div>

        <div class="layout-view">
          <ul class="breadcrumb">
            <li><a><i>list</i> Lista de commits</a></li>
          </ul>

          <div v-if="repository.commits.length > 0" class="list item-delimiter">
            <div class="card" v-for="com in repository.commits">
              <div class="card-title">
                {{com.author}}
              </div>
              <div class="card-content">
                {{com.message}}
              </div>
            </div>
          </div>

          <div v-if="repository.commits.length <= 0">
            <p>Sem commits</p>
          </div>
        </div>
      </q-layout>
    </template>

    <script>
    import { Loading, Toast } from 'quasar'
    import { commits } from '../resources/github'

    export default {
      data () {
        return {
          repository: {
            name: '',
            commits: []
          }
        }
      },
      created () {
        this.repository.name = this.$route.params.repository.full
        this.repository.stars = this.$route.params.repository.stars

        this.repository.commits = []
        Loading.show({ message: 'Procurando por commits' })

        commits(this.repository.name).then((result) => {
          result = result.data
          if (result.length > 0) {
            for (var i = 0; i < result.length; i++) {
              this.repository.commits.push({
                author: result[i].commit.author.name,
                message: result[i].commit.message
              })
            }
            Loading.hide()
          }
        }).catch(() => {
          Loading.hide()
          this.$refs.modalOwner.open()
          Toast.create({ html: 'Repositório não foi encontrado ou o tempo limite expirou' })
        })
      }
    }
    </script>

Podemos ver que o `template` desse componente é bem parecido com o anterior, a única coisa que fiz foi apagar o `q-modal`, retirar a ação de clique de cada item da lista e trocar o atributo `owner` por `repository`. Além disso, no `header` há um botão para voltar para tela anterior.

No `script` temos novamente o Toast e Loading, além de outro método do resource que agora buscará pelos commits de um repositório:

* `data` - atributo que representa um repositório, contendo nome e uma lista de commits.

* `created` - quando esse componente for criado irá exibir uma tela de carregamento enquanto executamos o método `commits` do nosso resource para retornar e distribuir os dados recuperados na tela.

Com as duas telas criadas precisamos criar nosso 'backend', para manter a organização criei uma pasta chamada `resources` dentro de `/src` e lá criei dois arquivos.

**config.js**

    import axios from 'axios'

    export default axios.create({
      baseURL: 'https://api.github.com/',
      timeout: 10000
    })

Responsável por configurar e exportar uma instância do `axios` usando como link de base a API do GitHub, para isso funcionar instale o axios:

    npm install axios --save

**github.js**

    import Client from './config'

    export const repositories = (owner) => {
      return Client.get(`orgs/${owner}/repos`)
    }

    export const commits = (fullname) => {
      return Client.get(`repos/${fullname}/commits`)
    }

É aquele arquivo que importamos nos dois componentes, aqui temos dois métodos:

* `repositories` - retorna um Promisse com requisição na api que pega todos repositórios de uma organização.

* `commits` - retorna uma Promisse com requisição na api que pega todos os commits feitos em um repositório.

E com isso nosso aplicativo estará funcionando, veja um exemplo:

![Exemplo de aplicativo rodando](https://github.com/leonardovilarinho/quasar-example01/blob/master/demo.gif?raw=true)


No exemplo coloquei uma organização inexistente, então foi exibido um Toast com o erro, logo em seguida inseri uma existente então foi me mostrado seus repositórios e estrelas de cada um, ao selecionar um, fui enviado para a tela com os commits do mesmo, mostrando o autor do commit e a mensagem dele, ao pressionar na casinha voltei para a tela inicial onde o ciclo recomeçou.

Espero que tenham gostado dessa simples postagem, como podem ver não é muito diferente do que simplesmente usar o Vue. Nesse final quero deixar minha opinião sobre o framework, dado que já tenho alguma experiência com os demais concorrentes:

>Precisa de melhorias, isso é fato, alguns(poucos) componentes não respondem muito bem, como estou acostumado com Ionic, as vantagens que vi são: leveza e VueJS. O linter padrão pode ser chato para desenvolvedores que não conhecem, mas faz ter qualidade e padrão no código. No mais precisa melhorar, ter um lab como o Ionic ajudaria para ver os comportamentos em outras plataformas ao mesmo tempo, pois deixou a sensação que em toda plataforma terá design de Android, a não ser que o desenvolvedor construa um estilo para cada plataforma.  Mas não levem isso a sério, também sou newbie nesse framework!

Caso tenham dúvidas, comentários, sugestões de novos posts ou mesmo críticas deixem nos comentários, sempre estou buscando eles. Deixo o [link do GitHub com esse app](https://github.com/leonardovilarinho/quasar-example01) ~~para quem tem preguiça~~ e abaixo algumas referências da própria documentação do Quasar:

* [Guia inicial](http://quasar-framework.org/guide)
* [Quasar CLI](http://quasar-framework.org/guide/quasar-cli.html)
* [Componentes Quasar](http://quasar-framework.org/components/)
* [API](http://quasar-framework.org/api/)
