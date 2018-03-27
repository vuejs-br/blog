---
layout: post
title: 'Testes automatizados com Avoriaz'
main-class: 'dev'
date: 2017-02-28 04:28:04 
color: '#637a91'
tags: testes vue2
layout: post
author: vedovelli1
---

Uma parte essencial para que você possa dormir tranquilo sem ficar pensando naquela alteração de uma linha que você fez sem testar o restante do seu sistema.

Parece exagero, mas uma linha alterada em um código importante pode causar muitos danos ao sistema, muita caquinha pode acontecer, então pense melhor quando for construir um software, que tal usar testes automatizados?

Ah, mas esses testes só diminuem a produtividade, pois escrever código para testar código não faz o software andar, não é mesmo? **Errado!** 

Pense em um código complexo, como um gerador de nota fiscal, qualquer alteração pode causar diversos prejuízos para seu dono, e quando isso acontece a culpa será do querido desenvolvedor. Mas agora pense se fosse possível a cada alteração executar um comando e testar todo sistema automaticamente vendo se aquela mudança provocou um problema, seria maravilhoso não é? Agora imagine mostrar esses problemas gerados em vermelho... sensacional!! rsrs

É para isso que no mercado temos ferramentas para testes de unidade, muitos delas confesso que por si só já faz o desenvolvedor desistir de seguir esse caminho, pois são um verdadeiro pé no saco. Em uma busca profunda, testes e mais testes para integrar essas ferramentas no Vue, acabei encontrando e optando por uma solução caseira, chamada [Avoriaz](https://github.com/eddyerburgh/avoriaz).

Desenvolvida para o próprio Vue, tem uma sintaxe simples e amigável, dando prazer em escrever esses testes, porém para instalar precisamos de mais alguns pacotes, então execute o seguinte comando em um template `webpack-simple`:

    npm install avoriaz mocha mocha-webpack jsdom chai --save-dev

Além disso é necessário alterar o `package.json`:

    "scripts": {
      .
      .
      "test": "mocha-webpack --webpack-config webpack.config.js test --recursive --require test/.setup.js"
    },

E por fim, criar um diretório na raiz do projeto chamado `test`, dentro dele um arquivo nomeado `.setup.js` com o seguinte conteúdo:

	const jsdom = require('jsdom').jsdom;

	const exposedProperties = ['window', 'navigator', 'document'];

	global.document = jsdom('');
	global.window = document.defaultView;

	Object.keys(document.defaultView).forEach((property) => {
	  if (typeof global[property] === 'undefined') {
	    exposedProperties.push(property);
	    global[property] = document.defaultView[property];
	  }
	});

	global.navigator = {
	  userAgent: 'node.js'
	};

	documentRef = document;

O que fizemos além de instalar os pacotes, foi registrar um comando para executar o testes e um arquivo que inicia uma espécie de simulador de browser e executa nossos testes.

Para um exemplo simples vamos deixar nosso `src/App.vue` assim:

    <template>
      <div id="app">
        <h1>{{msg}}</h1>
        <button @click="change_message()">Change</button>
      </div>
    </template>

    <script>
    export default {
      name: 'app',
      data () {
        return {
          msg: 'Welcome to Your Vue.js App'
        }
      },
      methods: {
        change_message() {
          this.msg = 'My new message'
        }
      }
    }
    </script>

No componente temos um atributo `msg` padrão do Vue e um método para alterar ele, no nosso template temos um botão que executa esse método.

Não citei acima, então posso dizer que temos a **cereja do bolo**: com o Avoriaz além de testes de unidade, possuímos a alternativa de realizar testes de sistema, aqueles em que podemos de fato simular uma navegação no nosso sistema, cliques, preenchimentos de campos, ou seja, manipular o DOM(seu ser o de Deus).

Agora chegou a hora de instalar o Windows no Mac, opss, isso é pra sexta, mas então vamos criar o arquivo de teste mesmo, na pasta `test` optei por criar um arquivo chamado `App.test.js`, com o seguinte código:

    import { mount } from 'avoriaz'
    import { expect } from 'chai'
    import App from '../src/App.vue'

    describe('App.vue test', () => {
      const component = mount(App)

      it('testando texto inicial', () => {
        expect(component.data().msg).to.equal('Welcome to Your Vue.js App')
      });

      it('testando texto inicial com mutacao', () => {
        component.data().msg = 'Hello'
        component.update()
        expect(component.data().msg).to.equal('Hello')
      });

      it('testando clique botao para alterar', () => {
        let button = component.find('button')[0]
        button.simulate('click')
        expect(component.data().msg).to.equal('My new message')
      });
    });

Como podem ver, temos uma sintaxe bem explicativa, então eu poderia estar dormindo, mas vou deixar uma explicação zzz... com `describe` defino um nome para nossa suíte de testes e todos esses `it` são testes, notem que tenho uma constante que recebe o componente já montado, e então a partir dela executo minha lógica para cada teste. Em seguida descrevo cada teste feito:

* 1º - compara o atributo `msg` do componente com um texto fixo.
* 2º - altero o atributo `msg` do componente e vejo se ele realmente recebeu o novo valor.
* 3º - procuro por um botão no template desse componente e então simulo um clique nesse botão, logo após isso verifico se minha mensagem realmente foi trocada.

Para executar os testes use o comando que construímos no início do post:

    npm test

A saída será mais ou menos assim:

![saida do terminal](http://image.prntscr.com/image/d8031f350f4e4a02a5881d6a5f6d43fd.jpeg)

Não vou estender mais esse artigo pois o objetivo era simplesmente mostrar essa ferramenta simples que temos aí exclusiva para o Vue, então espero que estudem-la e aproveitem-la!

Provavelmente o próximo artigo será sobre desenvolver no Vue usando TDD com essa ferramenta, aguardem! Sayonara¨


[Documentação do Avoriaz](https://eddyerburgh.gitbooks.io/avoriaz/content/)
