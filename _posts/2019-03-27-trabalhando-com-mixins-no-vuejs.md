---
layout: post
title: 'Trabalhando com Mixins no Vue.js'
date: 2019-03-27 20:23:44 
tags: vue vuejs mixins components
author: fsenaweb
---

![](https://cdn-images-1.medium.com/max/800/1*mGLyzR9e51d_DEYWyQ1Hog.jpeg)

Fala galera! 

Dentro dos meus trabalhos com Vue, eu venho adquirindo muita experiência no desenvolvimento de componentes e reaproveitamento dos mesmos nas aplicações, ganhando assim, agilidade, tempo, recursos, entre outros. E nos últimos projetos eu vinha percebendo que alguns dos meus componentes tinham códigos bastante semelhantes, entre os quais, alguns methods, computed properties.

Era muito código que eu praticamente copiava e colava de um componente para outro, mudando pequenos detalhes e isso me chamou a atenção, ai fui buscar mais informações na internet, principalmente na documentação do próprio Vue.js, e também no telegram, no grupo Vuejs Brasil. Acabei descobrindo que existe uma funcionalidade fantástica que são os Mixins , onde a própria documentação dá uma clara explicação:

> Mixins são uma forma flexível de distribuir funcionalidade reutilizável em diversos componentes Vue. Um objeto mixin pode conter quaisquer opções de componente. Quando um componente utiliza um mixin, todas as opções deste serão misturadas (em inglês, mixed in) com as opções do próprio componente.

Mais claro que isso, impossível, não é?! Os Mixins permitem que você tenha métodos, props, dados, propriedades computadas aplicados a vários componentes. Eles lembram bem uma abordagem para termos uma composição sobre herança (aquelas mesmas heranças que encontramos no C#, Java e outras linguagens). Pois bem, depois disso, vi que o meu trabalho com a reutilização de códigos diminuiu muito, agilizando ainda mais na criação dos meus aplicativos. Mas vamos deixar de conversas e vamos praticar.

## Vamos ao exemplo
Dentro da sua aplicação no Vue, vamos criar um pasta chamada mixins, nela colocaremos aquivos com extensão .js para importamos nos componentes onde iremos aproveitar os códigos na aplicação.

![](https://cdn-images-1.medium.com/max/800/1*1dJ50HokwxdxG_2FEwVvkw.png)

Nesse primeiro exemplo (nomeMixins.js) criei uma constante chamada nomeMixins e nela retornei um objeto, igual fazemos na própria instância do Vue contendo três simples propriedades para o nosso estudo. Agora podemos importar o arquivo nomeMixins.js dentro do componente:

![](https://cdn-images-1.medium.com/max/800/1*4Qt1hLC-h7mTOY8OYBCiaQ.png)

Inicialmente fizemos a importação (import nomeMixins … ) e declaramos o mixins e atribuimos o valor declarado no import, no caso ficando como **mixins: [nomeMixins]**, onde você pode inserir diversos outros arquivos através de um array.

Não só com o data() que podemos trabalhar, como falei anteriormente, você pode trabalhar com métodos, propriedades computadas, e muitas outras. Dando continuidade, no mesmo arquivo nomeMixins.js, vamos inserir uma propriedade computada, onde ela unirá 2 propriedades do objeto em data(), que segue:

![](https://cdn-images-1.medium.com/max/800/1*HqXi0aVSXreueCTQx2k-mA.png)

No componente .vue, não precisaremos acrescentar nada, pois ele já entende que aquela propriedade computada fará parte dele, dessa forma, basta apenas você chamá-lo dentro da tag <template></template> ou através de um console.log() para visualizar o resultado:

![](https://cdn-images-1.medium.com/max/800/1*ZOvufRYZ62MKSJF07aEPtA.png)

Dessa forma, você economiza linha e mais linhas de códigos para atividades que são repetitivas no seu site ou aplicativo com Vue.js. Existem diversas possibilidades desse reaproveitamento, inclusive há uma forma de se produzir um **mixin global**, onde você poderá utilizá-lo em todas as instâncias do Vue, mas a própria documentação recomenda ter cuidado, pois isso pode afetar outras partes dos seus códigos.

Você pode encontrar mais informações na [documentação oficial do Vue.js](https://br.vuejs.org/v2/guide/mixins.html) (totalmente em português), contendo muitos exemplos da utilização dos mixins na sua aplicação, acesse lá e confere. E não deixe de participar no nosso grupo no Telegram ([VueJS Brasil](https://t.me/vuejsbrasil)), tem uma galera muito especial pronta trocar umas experiências.

Em breve trarei mais assuntos para compartilhar com a comunidade. Irei escrever algumas das minhas experiências com diversas tecnologias juntamente com o Vue, entre elas o Docker, React, Laravel e até com os microframeworks.

Se você gostou desse artigo, não deixe de compartilhar e comentar. Se quiser saber um pouco mais, trocar umas ideias, você pode deixar nos comentários a sua opinião sobre o assunto, e até sugerir algo para os próximos artigos.

Aproveite e conheça um pouco dos meus trabalhos, visitando o site [www.fsenaweb.me](https://www.fsenaweb.me), lá tem o meu portfólio, minhas redes sociais (inclusive o meu [GitHub](https://github.com/fsenaweb/), onde disponibilizo algumas aplicações exemplos para praticarem com Vue.js), tem ainda espaço para contatos e até artigos que eu publico e compartilho de outros colegas programadores, como forma de difundir conhecimentos.

E é isso, até a próxima! Meu nome é Matheus Ricelly, e pela sua atenção, o meu muito obrigado!

