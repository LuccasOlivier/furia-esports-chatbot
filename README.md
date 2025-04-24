# FURIA Chatbot

Este repositório contém o desenvolvimento de um chatbot interativo para fãs da FURIA Esports, criado como parte de um desafio.

O chatbot foi desenvolvido usando Django e outras tecnologias complementares, oferecendo uma interação divertida e informativa para os fãs de CS:GO e a equipe FURIA.

## Tecnologias Utilizadas

- **Django**: Framework web Python utilizado para o desenvolvimento do backend.
- **JavaScript (AJAX)**: Para a interação assíncrona com o servidor, possibilitando a comunicação em tempo real com o chatbot.
- **Tailwind CSS**: Para a estilização da interface de maneira moderna e responsiva.
- **Banco de Dados SQLite**: Para armazenar as mensagens e interações entre o usuário e o bot.

## Requisitos do Desafio

O desafio exigia a criação de um chatbot funcional com as seguintes especificações:

- **Interação com o usuário**: O chatbot deve ser capaz de responder de maneira inteligente a perguntas frequentes sobre o time FURIA.
- **Personalização de respostas**: O bot deve entender perguntas relacionadas ao time e ao jogo, oferecendo respostas personalizadas.
- **Armazenamento de mensagens**: As interações entre o usuário e o bot devem ser armazenadas no banco de dados.

## Funcionalidades Implementadas

- **Respostas baseadas em padrões**: O chatbot utiliza expressões regulares para identificar palavras-chave nas mensagens do usuário e retornar respostas personalizadas.
- **Armazenamento das mensagens**: As mensagens enviadas pelos usuários e as respostas do bot são armazenadas no banco de dados e exibidas na interface.
- **Interface simples e moderna**: A interface do chatbot foi desenvolvida utilizando o framework Tailwind CSS, com um design clean e responsivo.

## Melhorias e Implementações Adicionais

Além dos requisitos obrigatórios, algumas melhorias e implementações adicionais foram feitas para aprimorar a experiência do usuário:

- **Lógica de Respostas Melhorada**: A lógica do chatbot foi aprimorada para fornecer respostas mais dinâmicas e personalizadas. Utilizamos expressões regulares para identificar intenções específicas nas mensagens dos usuários e gerar respostas variadas com base nessas intenções. Embora o sistema não utilize inteligência artificial avançada, ele responde de forma mais inteligente, adaptando-se ao contexto da conversa.
- **Estilização personalizada**: Ajustes na fonte e na aparência do chatbot para criar uma interface mais condizente com a identidade do time FURIA, incluindo mudanças no estilo da interface para torná-la mais atraente.
- **AJAX para interações em tempo real**: A comunicação entre o frontend e o backend foi otimizada usando AJAX, permitindo respostas mais rápidas e sem a necessidade de recarregar a página.
- **Gestão de histórico de mensagens**: Foi implementado um botão para apagar o histórico de mensagens, oferecendo ao usuário mais controle sobre suas interações com o chatbot.

## Como Rodar o Projeto

Para rodar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:

