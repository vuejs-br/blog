---
layout: post
title: 'Gerenciando idiomas no Vue'
main-class: 'dev'
date: 2017-04-17 18:11:09 
color: '#637a91'
tags: idioma vue2 plugins
layout: post
author: vedovelli
---

Temos um mundo cada vez mais conectado, em alguns lugares, o número de dispositivos ultrapassam o de habitantes. Esses dispositivos, por sua vez, têm o objetivo exclusivo de nos trazer informações, essas são apresentadas em idiomas, muitas vezes no inglês, mas em um planeta com diversos idiomas, é um diferencial disponibilizar dados em vários deles.

Entrando no ramo de desenvolvimento, com um sistema que disponibiliza dados em diversos idiomas podemos expandir o nosso alcance, além disso deixar o cliente orgulhoso pelo trabalho bem feito.

Na prática, nem sempre isso é tão lindo, ás vezes é bastante trabalhoso criar sistemas com suporte a mais de uma linguagem, visando isso criei um plugin para o Vue, com o objetivo de suprir essa necessidade de uma forma simples e rápida.


O [vue-multilanguage](https://github.com/leonardovilarinho/vue-multilanguage) disponibiliza uma variável indicando qual o idioma atual do sistema, ao ter o valor dessa variável modificado, a diretiva `v-lang` é executada, por sua vez atualizando todos componentes. Vide a figura abaixo:

![Funcionamento do vue-multilanguage](https://github.com/leonardovilarinho/vue-multilanguage/blob/master/vue-multilnguage.jpg?raw=true)

Nesse artigo vamos fazer um pequeno exemplo que usa esse plugin, iremos criar uma aplicação composta por três componentes, o `Perfil` que irá mostrar dados do usuário, `Painel` que mostrará a quantidade de amigos que o usuário tem, e o nosso querido `App`.

Para isso, com um projeto já criado, vamos instalar nosso plugin via NPM, com o comando:
```shell
npm install vue-multilanguage --save
```

### Registrando idiomas e plugin
Por padrão o plugin deve receber um objeto com atributos que permitem algumas configurações:

* o atributo `default` indica o idioma padrão do sistema, caso não seja informado irá entender que a linguagem do navegador é a padrão, e por último caso, irá definir o primeiro objeto de linguagem declarado como padrão (`en` nesse exemplo).

* os atributos de linguagem, seguindo padrão de dois caracteres, são objetos que englobam todas mensagens que o idioma irá ter, como exemplo a frase `titulo`.

Veja o exemplo a seguir:

```javascript
import Vue from 'vue'
import App from './App.vue'

import VueLanguage from 'vue-multilanguage'

Vue.use(VueLanguage, {
        default: 'pt',
	en: {
                titulo: 'My website',
	}
})

new Vue({
  el: '#app',
  render: h => h(App)
})

```
O código de exemplo foi criado no arquivo `main.js`, para já registrar o plugin na aplicação Vue.

Notem que temos algumas chaves (`{}`) em mensagens, o `vue-multilanguage` interpretará isso como parâmetros, quando se tem mais de um, você obrigatoriamente deve dar um nome a ele, quando temos apenas um podemos defini-lo como zero.

### Usando idiomas no template
Agora para usar o plugin em um `template`, podemos apenas fazer uso de sua diretiva `v-lang`, passando como modificadores o caminho completo da mensagem a ser exibida, como valor enviaremos os parâmetros, caso exista algum na mensagem.

Para testar, vamos criar o componente `Perfil` que exibe a mensagem de `descricao`, como nós não temos a mensagem `descricao` definida globalmente no plugin, podemos declara-la no atributo `messages` do componente deixando-a como local. 

Essa mensagem receberá dois atributos, `nome` e `idade`, então na diretiva passamos um objeto com esses valores para serem substituído na mensagem:

```vue
<template>
	<div>
        <h1 v-lang.titulo>Meu site</h1>
		<h3 v-lang.descricao="usuario">
            Seu nome {nome} e você tem {idade} anos
        </h3>
	</div>
</template>

<script>
export default{
	name: 'lv-perfil',
    messages: {
	    en: {
	        descricao: 'Your name is {nome} and you have {idade}
	    }
	}
	data() {
		return {
			usuario: {
				nome: 'Leonardo Vilarinho',
				idade: 20
			}
		}
	},
}
</script>
```
Note que como declaramos o idioma `pt` como padrão, não precisamos ter a declaração programática de suas mensagens, basta colocadas diretamente no `template` para termos o mesmo resultado, mas lembre-se, isso funcionará apenas para quando usarmos o `default`.


Vamos também criar o componente `Painel`, nele iremos importar o componente de `Perfil` e exibir a mensagem `amigos`, como ela recebe um único parâmetro podemos passa-lo diretamente, assim:

```vue
<template>
	<div>
		<lv-perfil></lv-perfil>
		<h4 v-lang.amigos="5">
            Você tem {0} amigos
        </h4>
	</div>
</template>

<script>
import LvPerfil from './Perfil.vue'
export default{
	name: 'lv-painel',
	components: {LvPerfil},
    messages: {
	    en: {
	        amigos: 'You have {0} friends'
		}
    }
}
</script>
```

E por fim, no `App` vamos importar o componente `Painel` para que possamos de fato ver tudo funcionando:
```vue
<template>
  <div id="app">
    <lv-painel></lv-painel>
  </div>
</template>

<script>
import LvPainel from './Painel.vue'
export default {
  name: 'app',
  components: {LvPainel}
}
</script>
```

Ao executar tudo com o `npm run dev` provavelmente você verá as mensagens em português, algo como:
>Seu nome Leonardo Vilarinho e você tem 20 anos

>Você tem 5 amigos

### Uso programático
O plugin não trabalha somente com a diretiva, caso queira traduzir uma mensagem no próprio javascript use o método global `translate` para definir uma propriedade computada com o valor da mensagem traduzida para o idioma ativo:

```javascript
computed: {
	welcome()  {
		return this.translate(this.$language, 'nome-mensagem', 'parametros')
	}
}
```

### Alterando linguagem do sistema
Caso queira mudar o idioma do seu sistema, basta em qualquer componente trocar o valor da variável `$language`, para testar coloque esse código em qualquer componente **que use a diretiva** `v-lang`:
```html
<button @click='$language = "pt"'>PT</button>
<button @click='$language = "en"'>EN</button>
```

Com isso, ao clicar nos botões você verá o seu sistema inteiro trocando de idioma em tempo real.

E com isso finalizamos o artigo, caso queira contribuir com o plugin basta entrar no [repositório do GitHub](https://github.com/leonardovilarinho/vue-multilanguage). Até a próxima!
