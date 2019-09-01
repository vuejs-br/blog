---
layout: post
title: 'Construindo sua aplicação com Styled Components no Vue.js'
date: 2019-09-01 20:23:44 
tags: vue vuejs styled-components components
author: fsenaweb
---

O Styled-Components é uma biblioteca muito popular dentro da comunidade React e do React Native, e agora você poderá utilizá-la no Vue.js.

![](https://miro.medium.com/max/1200/1*V8B2hh70R6GLsy7khGBJ2w.jpeg)

Olá pessoal, estou de volta!

Para quem não conhece, o Styled-Components é uma biblioteca muito popular dentro da comunidade React e do React Native, onde ela proporciona ao desenvolvedor criar seus códigos CSS dentro do JavaScript.

Quem desenvolve com Vue sabe a facilidade que é trabalhar com a estilização dos componentes, utilizando o CSS juntamente com o HTML e o JavaScript num único arquivo; e tudo isso graças ao poder do SFC (Single File Components). Esse foi sem dúvida, um ponto muito positivo e que ajudou a impulsionar a popularidade do Vue na comunidade Front-end.

Porém, nos últimos meses, tenho utilizado o React no desenvolvimento de um projeto de grande porte, e foi a partir daí, que conheci essa biblioteca e tenho utilizado na parte da estilização do mesmo; e até confesso que deixei a aplicação muito mais organizada e prática. No início é até meio confuso, mas depois você começa a gostar muito dessa biblioteca.

Mas como a maior parte dos meus projetos eu utilizo o Vue, então decidi pesquisar uma forma de unir a praticidade da biblioteca Style-Components com o poder do Vue.js e seu ecossistema. Foi então então que descobri que existe uma biblioteca específica pra o Vue, mantida pelos mesmos criadores do styled-components do React, e que se chama [vue-styled-components](https://github.com/styled-components/vue-styled-components).

E caso você tenha projetos no React e queira fazer a mudança para o Vue (sim, o processo de mudança também ocorre nesse sentido e tem aumentado muito), com os estilos criados com o styled-components, podem ser facilmente migrados, ganhando assim, agilidade, performance e escalabilidade.

# Primeiros Passos
Mas vamos deixar a conversa de lado e vamos ao código! O processo de instalação e utilização do vue-styled-components é bem simples e prático. Já com o seu projeto criado, basta apenas instalar a biblioteca utilizando seu gerenciador de pacotes preferido (Yarn, NPM).

![](https://miro.medium.com/max/1584/1*W7RBObyMNUNkK6PrlkY1tg.png)

Não é nada complicado, e rapidamente você poderá utilizar o potencial dessa biblioteca na sua aplicação. No meu GitHub eu deixei um projeto com exemplos de tags estilizadas e algumas formas de interagir com elas utilizando o vue-styled-components.

Cada elemento/tag utilizado nos exemplos podem ser tratadas pelo vue-styled-components como um Componente isolado e com suas propriedades individuais, ou recebendo dados de outros componentes.

No nosso primeiro exemplo, de forma mais introdutória e básica possível, vamos criar um botão com um estilo padrão. Não se preocupe nesse momento, em personalizar essas tags, vamos aos poucos evoluindo até um processo em que esse componente poderá ser mapeado e permitir atualizações de estilo de forma dinâmica.

```javascript
import styled from "vue-styled-components";

const CButton = styled.button`
  font-size: 1em;
  text-align: center;
  color: #FFFFFF;
  border-radius: 5px;
  padding: 10px 15px;
  background-color: #0057AA;
`;

export default CButton;
```

Após criar o arquivo Button.js, basta ser utilizado da mesma forma que estaria importando qualquer componente dentro do Vue e atribuindo ao arquivo um nome para a tag dentro do código HTML no SFC (Vou considerar aqui, que você já tem familiaridade com o uso do Vue.js e toda a sua arquitetura).

Eu costumo utilizar a letra C como um prefixo (que remete a palavra Componente), para atribuir os nomes as tags personalizadas que utilizo no Vue; é uma boa prática que aprendi com o Angular. Nesse instante, em qualquer lugar em nosso aplicativo, poderemos utilizar esse componente estilizado.

```javascript
<script>
    import CButton from '@/components/elements/Button'
    export default {
        name: 'app',
        components: {
            CButton
        },
    }
</script>
```

## Passando propriedades

No vue-styled-components você pode definir estilos a um componente de forma dinâmica, passando esses valores através de propriedades. Vamos aperfeiçoar o nosso componente Button, colocando a possibilidade de modificar o estilo de botão, de acordo com os parâmetros passados. Nesse exemplo estamos informando que ao ser passado o atributo `primary`, o botão irá receber um novo estilo de background e cor da fonte.

```javascript
import styled from "vue-styled-components";

const typeButton = { primary: Boolean };

const CButtonProps = styled('button', typeButton)`
  font-size: 1em;
  text-align: center;
  color: ${props => props.primary ? '#0057AA' : '#FFFFFF'};
  border-radius: 5px;
  padding: 10px 15px;
  background-color: ${props => props.primary ? '#FFFFFF' : '#0057AA'};
`;

export default CButtonProps;
```

Não há segredo nesse código, de forma simples, apenas fizemos um ternário informando caso existe o atributo primary ele retorna uma cor, caso não exista, retornará outra. O exemplo acima pode ser melhorado e até acrescentada novas propriedades (é possível passar quantos atributos quiser); tudo vai de acordo com a sua necessidade dentro do projeto.

## Aprimorando as propriedades
Manipular as propriedades recebidas nos dá uma chance de obter componentes diversificados em um único arquivo, colocando condições que satisfaçam a determinados estilos. No exemplo abaixo, você tem a oportunidade de escolher qual o esquema de cores deseja atribuir ao seu botão, sem que isso afete aos demais, diversificando assim sua aplicação.

```javascript
import styled from "vue-styled-components";

const typeButton = {
    type: String,
    radius: Boolean
};

const styleButton = type => {
    switch (type) {
        case "primary":
            return `
                background-color: #FFFFFF;
                color: #0057AA;
            `;
        case "error":
            return `
                background-color: #B4000B;
                color: #FDFDFD;
            `;
        case "success":
            return `
            background-color: #00C887;
            color: #37435F;
        `;
        default:
            return `
                background-color: #0057AA;
                color: #FFFFFF;
            `;
    }
}

const CButtonPropsCond = styled('button', typeButton)`
  font-size: 1em;
  text-align: center;
  padding: 10px 15px;
  border-radius: ${({ radius }) => radius ? "6px" : null};
  ${(props) => styleButton(props.type)}
`;

export default CButtonPropsCond;

```

Explicando melhor o processo de criação desse botão: iniciamos (sempre) chamando o vue-styled-components, logo após (*da linha 3 a linha 6*), precisamos definir qual os tipos de propriedades que serão passadas ao componente, nesse caso criamos dois tipos, que são type e radius; essa segunda propriedade é apenas para mostrarmos se vamos querer um botão com bordas arredondadas ou não.

Da *linha 8 até a 31*, criamos uma função, que pega o valor da propriedade type e faz uma condicional (nesse caso utilizamos o switch) e ver o valor informado, de acordo com o que foi passado, ele retorna os atributos de background-color e color dos seus respectivos case, caso nada seja passado como propriedade, então o botão receberá um valor padrão.

A partir desse conhecimento, você poderá implementar novos atributos, como *tamanho da fonte, padding, margin*, entre outros atributos que poderão deixar seu componente personalizado de forma bem dinâmica e sendo utilizada em toda a aplicação.

Deixei [pequenos](https://github.com/fsenaweb/vue-styled-components) exemplos no meu GitHub para que você possa dá o passo inicial para implementar essa biblioteca. Aproveite e envie novos campos estilizados para ajudar aos demais amigos que também desejam aprender.

Se você gostou desse artigo, não deixe de compartilhar e comentar. Se você quiser saber um pouco mais, trocar algumas idéias, poderá deixar nos comentários sua opinião sobre o assunto e até sugerir algo para os próximos artigos.

Aproveite e conheça um pouco dos meus trabalhos, visite o site [www.fsenaweb.me](https://www.fsenaweb.me) , ele tem o meu portfólio, minhas redes sociais (inclusive o [*GitHub*](https://github.com/fsenaweb/) , onde você tem a disposição algumas aplicações de exemplos para praticar com o Vue.js), e um pequeno espaço para contatos.

E não deixe de participar de nosso grupo no Telegram ( [VueJS Brasil](https://t.me/vuejsbrasil) ), tem uma galeria muito especial pronta trocar outras experiências.

E é isso, até a próxima! Meu nome é *Matheus Ricelly*, e pela sua atenção, o meu *muito obrigado*!