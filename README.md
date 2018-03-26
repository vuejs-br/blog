

# Blog Vuejs-Brasil

Este é o site do Blog vuejs-brasil.com.br. Qualquer pessoa pode contribuir com o nosso Blog! É fácil, bastando apenas alguns conhecimentos sobre Git e Markdown. 


## Notas de migração

Esse Blog está sendo migrado para o jekyll. Algumas coisas ainda não funcionam! 

O que está faltando:

- [x] Comentários do disquss
- [ ] Importar as imagens de capa de artigo
- [ ] Configurar os autores de cada artigo
- [ ] Configurar as tags e criar uma página de tags


### Atenção autores

Para terem o nome de vocês novamente no artigo, é preciso adicionar uma entrada no _config.yml, conforme o exemplo abaixo:

```
danielschmitz:
    name: Daniel Schmitz
    gravatar: b2da8fcc6cfdaf3bbe1f17aa9fabde39
    web: http://danielschmitz.com.br
    description: Daniel Schmitz é autor de vários livros sobre programação e desenvolvimento de sistemas
    github: danielschmitz
```

Depois, é preciso ir em cada artigo que você escreveu e adicionar o seu nome, assim:

```
---
layout: post
title: 'Trabalhando com arquivos .env no Vue'
date: 2018-03-05 12:11:59 
layout: post
author: danielschmitz                # <<<< aqui !!
---

Uma dúvida interessante que recebi de um leitor foi em como trabalhar de forma correta com configurações distintas entre o servidor de........
```

Faça isso e mande um PR para nós
