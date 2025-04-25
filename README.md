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

Você não precisa instalar nada localmente para testar o chatbot! A aplicação está disponível online e pode ser acessada diretamente pelo link:

👉 [Acesse o chatbot aqui](https://furia-esports-chatbot.onrender.com/)

### Sugestões de Testes

Aqui estão algumas ideias de interações para você experimentar com o chatbot:

- **Saudações e boas-vindas**
  - "Oi"
  - "eae"
  - "Olá"
  - "fala!"

- **Perguntas sobre o time de CS da FURIA**
  - "Qual posição no ranking furia se encontra?"
  - "Hoje tem jogo do furia?"
  - "Quando é o próximo jogo da FURIA?"
  - "Quem é o líder do time?"
  - "Qual seu jogador preferido?"

- **Interações divertidas**
  - "Conta uma curiosidade sobre a FURIA"
  - "Qual seu time favorito?"
    
- **Despedidas**
  - "tchau"
  - "falou"
  - "até logo"
  - "adeus"
 
- **Funcionalidades**
  - Você pode limpar a conversa clicando no botão **"Limpar conversa"**
  - Veja a resposta sendo exibida com efeito de digitação, trazendo uma experiência mais interativa.

## Considerações Finais

Este projeto foi desenvolvido como parte de um desafio técnico com o objetivo de demonstrar habilidades em desenvolvimento web, lógica de programação e criatividade na construção de experiências interativas para usuários.

O FURIA Chatbot oferece uma experiência simples e divertida para os fãs da equipe, simulando uma conversa com um bot temático e personalizado. Embora não utilize inteligência artificial avançada, o sistema entrega respostas coerentes e contextuais, baseando-se em padrões pré-definidos.

A ideia é mostrar como é possível criar um chatbot funcional com tecnologias acessíveis e foco no usuário final. Este projeto foi desenvolvido exclusivamente para fins de processo seletivo e não está aberto para contribuições externas.

---

 **Feito por Lucas Oliveira**  
 **Desafio FURIA - 2024**

