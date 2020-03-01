---
layout: post
title: 'Conhecendo e desenvolvendo filtros no Vue.js'
date: 2020-02-10 08:03:44 
tags: vue vuejs filters components
author: fsenaweb
---

Nos componentes do Vue, os filtros são funcionalidades que nos permitem obter diversas formatações na saída dos dados dinâmicos do seu estado. Ou seja, eles não alteram os dados de um componente, apenas podem formatar seus dados na renderização.

![](https://miro.medium.com/max/978/1*Xb8RD3_8I_uiX3749QhB5Q.png)

Olá pessoal!

Nesse artigo, de forma especial, irei falar sobre uma funcionalidade que na minha opinião é pouco utilizada (ou comentada) dentro da comunidade Vue.js, que são os Filtros. Assim como os Plugins, Diretivas Personalizadas e os [Mixins](http://vuejs-brasil.com.br/trabalhando-com-mixins-no-vuejs/), os filtros fazem parte das funcionalidades reutilizáveis dentro do Vue, auxiliando no processo de criação de componentes.

> Nos componentes do Vue, os filtros são funcionalidades que nos permitem obter diversas formatações na saída dos dados dinâmicos do seu estado. Ou seja, eles não alteram os dados de um componente, apenas podem formatar seus dados na renderização.

## Filtros locais
Conforme a documentação oficial, a utilização dos filtros ocorrem dentro de interpolações mustache e expressões v-bind. Veja um exemplo da formatação do filtro no template:

```html
<!-- em interpolações de texto --> 
{{ message | capitalize }}  

<!-- em interligações de atributos --> 
<div v-bind:text="message | capitalize"></div>
```

Criando de forma local, dentro do componente, podemos ter:

```javascript
filters: {
   capitalize(value) {
     if (!value) return ''
     value = value.toString()
     return value.charAt(0).toUpperCase() + value.slice(1)
   }
}
```

Nesse primeiro exemplo, extraído da própria documentação, podemos analisar que a função capitalize apenas pega o valor passar e faz o tratamento com os métodos necessários para que se obtenha o resultado, não existindo nenhuma interferência no valor original do estado do componente.

Em algumas situações, os **Filtros** podem ser bem semelhantes as **Propriedades Computadas**, com a diferença de que nos filtros, os dados não são transformados, eles apenas alteram a saída e retornam uma versão com o determinada filtragem da informação. Assim, não é gerado um novo valor para aquele dado do componente.

## Filtros Globais
Tem certas situações onde determinado filtro poderá ser usado em diversos componentes dentro da sua aplicação, principalmente naqueles projetos maiores, onde pode ocorrer diversas interações do sistema ao longo do projeto.

Para isso, existe a possibilidade de se criar os filtros globais, e assim como disse anteriormente, igualmente aos mixins, plugins, entre outros, eles ficam disponíveis em qualquer parte do seu projeto, facilitando a sua utilização e o reaproveitamento dos códigos.

```javascript
Vue.filter('capitalize', function (value) {
   if (!value) return ''
   value = value.toString()
   return value.charAt(0).toUpperCase() + value.slice(1)
})
new Vue({
   // sua instância do Vue...
})

```

Nesse exemplo vemos a criação de um filtro global, utilizando a propriedade .filter dentro do arquivo main.js. Caso sua aplicação utilize muitos filtros, por questão de organização, é recomendado criar um arquivo separado e colocar todos os filtros neles e fazer o import dentro do arquivo main.js. E tem um detalhe que é muito importante e deve sempre ser lembrado: quando um filtro global possuir o mesmo nome de um filtro local, o filtro local terá prioridade.


Como os filtros são funções JavaScript, eles aceitam o valor a ser transformado como o primeiro parâmetro. Você também pode passar quantos argumentos achar necessários de acordo com a necessidade da sua aplicação.

```javascript
{{ message | filterA('arg1', arg2) }}
```

Assim como podemos passar diversos argumentos, é possível encadear diversos filtros, para isso basta utilizarmos o símbolo pipe (|) e através de diversos filtros transformadores, obtermos único valor.

```javascript
filters: {
    Upper(value) {
       return value.toUpperCase();
    },
        
    Lower(value) {
       return value.toLowerCase();
    },
}

```

E dentro do valor, utilizamos da seguinte forma:

```javascript
{{ message | Upper | Lower }}
```


Claro que esse exemplo não teria nenhuma funcionalidade, mas apenas para exemplificar que é possível colocarmos diversos filtros dentro de um único valor, e como eu mencionei que são encadeadas, a função Lower será executada após obter o resultado de Upper, sendo passado como o único argumento de Lower.

Explore um pouco os seus conhecimentos e estudos nessa funcionalidade do Vue.js que te permite ajudar em diversas tarefas nas suas aplicações. Veja mais na [documentação oficial](https://vuejs.org/).

---
Se você gostou desse artigo, não deixe de compartilhar e comentar. Se você quiser saber um pouco mais, trocar algumas idéias, poderá deixar nos comentários sua opinião sobre o assunto e até sugerir algo para os próximos artigos.

Aproveite e conheça um pouco dos meus trabalhos, visite o site [www.fsenaweb.me](https://www.fsenaweb.me) , ele tem o meu portfólio, minhas redes sociais (inclusive o [*GitHub*](https://github.com/fsenaweb/) , onde você tem a disposição algumas aplicações de exemplos para praticar com o Vue.js), e um pequeno espaço para contatos.

E não deixe de participar de nosso grupo no Telegram ( [VueJS Brasil](https://t.me/vuejsbrasil) ), tem uma galeria muito especial pronta trocar outras experiências.

E é isso, até a próxima! Meu nome é *Matheus Ricelly*, e pela sua atenção, o meu *muito obrigado*!
