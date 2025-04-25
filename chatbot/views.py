from django.http import JsonResponse
from django.shortcuts import render
from .forms import MessageForm
from .models import Message
import random
import json
import re

# Respostas gerais
respostas_gerais = [
    "Que legal você mencionar isso!",
    "Interessante... quer me contar mais?",
    "Hum, boa pergunta. Pode explicar melhor?",
    "Haha, essa foi boa!",
    "Pode crer! E aí, o que mais?",
    "Você acompanha a FURIA faz tempo?",
    "Isso aí é raiz, ein!"
]

# Mapeamento de respostas para intenções específicas (padrões otimizados)
respostas_personalizadas = {
    r"\b(posição|ranking|colocação|posição no ranking)\b": [
        "Hoje a FURIA está no top 20 do ranking mundial da HLTV!",
        "A FURIA vem subindo no ranking, atualmente entre os melhores do Brasil!",
    ],
    r"\b(hoje.*jogo|tem.*jogo.*hoje|jogo.*hoje|vai jogar hoje)\b": [
        "Hoje a FURIA não tem jogo confirmado, mas fica de olho nas redes!",
        "Ainda não saiu confirmação de jogo hoje. Costuma ser à tarde ou noite!",
    ],
    r"\b(time favorito|qual.*seu.*time|seu time favorito)\b": [
        "Claro que é a FURIA! 💛🖤",
        "Time favorito? FURIA, sempre!",
    ],

    # Demais padrões
    r"\b(oi|olá|e?ae|fala|salve)\b": [
        "E aí, tudo certo? Pronto pra falar de CS e FURIA?",
        "Falaaa! Tá animado hoje?",
        "Salve! O que manda por aí?"
    ],
    r"\b(cs2?|counter[- ]?strike|jogo|patente|rank)\b": [
        "CS é brabo demais! Você joga? Qual patente?",
        "CS2 tá insano, né? Já testou?",
        "FURIA tá mandando bem no CS, hein!"
    ],
    r"\b(furia|furia esports|time da furia|furia team)\b": [
        "FURIA é paixão nacional!",
        "Acompanha o campeonato? A FURIA tá vindo forte!",
        "O arT é simplesmente diferenciado, né?"
    ],
    r"\b(art|kscerato|yuurih|fallen|chelo|jogador(es)?|lineup|elenco|quem joga|quem está no time)\b": [
        "Esse lineup tá pesado! Você tem um favorito?",
        "Esses caras tão representando demais!",
        "Fallen chegou pra somar, né?"
    ],
    r"\b(capitão|quem lidera|líder do time|igl)\b": [
        "Atualmente, o Fallen tá como capitão (IGL) da FURIA.",
        "O IGL da FURIA é o Fallen. Experiente demais!"
    ],
    r"\b(mais venceu|quem ganhou mais|histórico de vitórias|mais títulos)\b": [
        "Historicamente, a FURIA tem se destacado bastante na América do Sul!",
        "Na FURIA, o KSCERATO é um dos mais vitoriosos da lineup atual.",
        "FURIA teve campanhas fortes na ESL, IEM e Majors!"
    ],
    r"\b(campeonato|major|blast|esl|game|partida|torneio)\b": [
        "Esse campeonato promete!",
        "FURIA tá se preparando com força total!",
        "Vai assistir as partidas ao vivo?"
    ],
    r"\b(tchau|falou|até logo|adeus|valeu)\b": [
        "Valeu pela conversa! Volta sempre que quiser!",
        "Tamo junto, até a próxima!",
        "Foi daora trocar essa ideia contigo!"
    ],
}

# Função que encontra a resposta com base na intenção
def gerar_resposta(mensagem_usuario):
    for padrao, respostas in respostas_personalizadas.items():
        if re.search(padrao, mensagem_usuario, re.IGNORECASE):
            return random.choice(respostas)
    return random.choice(respostas_gerais)

# View padrão (formulário tradicional)
def furia_chatbot(request):
    if request.method == "POST":
        if 'delete_history' in request.POST:
            Message.objects.all().delete()
            return render(request, "chatbot/chat.html", {'messages': []})

        form = MessageForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data["message"]
            bot_response = gerar_resposta(user_message)

            Message.objects.create(user_message=user_message, bot_response=bot_response)

            # Verificar se há mensagens no banco de dados e passá-las para o template
            messages = Message.objects.all().order_by('-timestamp')  # Exibir mensagens mais recentes primeiro
            return render(request, "chatbot/chat.html", {'messages': messages})

        return render(request, "chatbot/chat.html", {'form': form, 'error': 'Mensagem inválida'})

    # Ao carregar a página, verificar se há mensagens
    messages = Message.objects.all().order_by('-timestamp')  # Exibir mensagens mais recentes primeiro
    if not messages:  # Se não houver mensagens, passa uma lista vazia
        messages = []

    return render(request, "chatbot/chat.html", {'messages': messages})

# View AJAX
def furia_chatbot_ajax(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
        except:
            return JsonResponse({'error': 'Erro ao processar dados'}, status=400)

        if user_message:
            bot_response = gerar_resposta(user_message)
            Message.objects.create(user_message=user_message, bot_response=bot_response)

            return JsonResponse({
                'user_message': user_message,
                'bot_response': bot_response
            })

    return JsonResponse({'error': 'Mensagem inválida'}, status=400)
