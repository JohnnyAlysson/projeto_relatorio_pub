
# <Nome da aplicação> 	:emoji:

## Tabela de conteúdos

<p align="left">

 <a href ="#sobre"> > Sobre</a>

 <a href ="#logica"> > Lógica</a>
 
 <a href ="#comousar"> > Como Usar</a>

 <a href ="#status"> > Status</a>

 <a href = "#demo"> > Demonstração </a>

 <a href = "#tecnologias"> > Tecnologias </a>

 <a href = "#autor"> > Autor</a>

 <a href = "#licenca"> > Licença </a>

<!-- <p id=sobre></p>

## Sobre -->
<h2 id=sobre> Sobre </h2>    

Este projeto de portfólio tem como objetivo criar um programa prático para ser apreciado por empresas e outras pessoas, demonstrando minha habilidade como programador.
O projeto consiste em um programa que analisa um banco de dados, calcula informações-chave e envia um e-mail com o relatório completo.
Este projeto surge dos meus estudos na área de programação e inclui minhas anotações e reflexões durante o processo de estudo e criação do programa.


<h2 id=logica> Lógica de Programação </h2>

1. Importar módulos;
2. Ler e manipular dados com Pandas;
3. Enviar email com as credenciais corretas.

<h2 id=comousar> Como usar </h2>
Para utilizar a aplicação é necessário instalar as seguintes bibliotecas:

>smtplib

>email.message

Nos seguintes campos é necessário colocar o seu email no campo remetente e no campo password você deve colocar a senha criada pela conta google do "Senha de app do google" conforme o link abaixo:

[Criar senha de APP](https://support.google.com/accounts/answer/185833?hl=pt-BR#:~:text=Uma%20senha%20de%20app%20tem,verifica%C3%A7%C3%A3o%20em%20duas%20etapas%20ativada.)

<code>   
    msg['From'] = 'Remetente' <br>
    msg['To'] = input_email <br>
    password = 'senhasdeappdogoogle' <br>
</code>



<h2 id=status> Status </h2>

> Finished :white_check_mark:

<h2 id=demo> Demonstração </h2>

![Email example](https://raw.githubusercontent.com/JohnnyAlysson/portifolio-web/master/assets/emailgif.gif "Email example")

<h2 id=tecnologias> Tecnologias </h2>
Nessa aplicação foram utilizadas as seguintes tecnologias:

1. Python ;   
2. Pandas.

<h2 id=autor> Autor </h2>

 <a href="https://johnnyalysson.github.io/portifolio-web/">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/149841185?v=4" width="100px;" alt=""/>
 <br />


    Feito com ❤️ por Johnny Alysson 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Johnny-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/johnnyalysson)](https://www.linkedin.com/in/johnnyalysson) 
[![Gmail Badge](https://img.shields.io/badge/-johnalysson30@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:johnalysson30@gmail.com)](mailto:johnalysson30@gmail.com)

<h2 id=licenca> Licença </h2>

MIT License

Copyright (c) 2024 Johnny Alysson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
