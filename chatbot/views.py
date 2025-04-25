from django.http import JsonResponse
from django.shortcuts import render
from .forms import MessageForm
from .models import Message
import random
import json
import re

respostas_personalizadas = {
    # INFORMAÇÕES SOBRE O TIME
    r"\b(quais jogadores|quem joga|lineup|escalação|time atual|jogadores da furia|quem está no time)\b": [
        "O lineup atual da FURIA é: FalleN (IGL), KSCERATO, yuurih, chelo e arT. 🔥",
        "No time da FURIA hoje estão: FalleN, KSCERATO, yuurih, chelo e arT. Time pesadíssimo! 💪"
    ],
    r"\b(fallen|igl|capitão|quem lidera|liderança|quem chama as táticas)\b": [
        "O IGL (capitão) da FURIA atualmente é o lendário FalleN! 👑",
        "Quem lidera a FURIA in-game é o FalleN, mestre das calls! 🧠"
    ],
    r"\b(kscerato|yuurih|chelo|arT)\b": [
        "KSCERATO é pura consistência e mira afiada! 🔫",
        "yuurih é o rei do clutch, não tem jeito! 👑",
        "chelo trouxe muito impacto pro time desde que chegou! 💥",
        "arT é o cara mais agressivo do cenário, impossível prever ele! 🚀"
    ],

    # TORNEIOS E COMPETIÇÕES
    r"\b(major|blast|esl|torneio|campeonato|partida|game)\b": [
        "A FURIA sempre dá show nos campeonatos grandes! 🔥",
        "Já viu a FURIA jogando um Major? É emoção do começo ao fim! 😍",
        "Fica ligado que a FURIA tá sempre nas competições mais importantes do cenário! 🏆"
    ],
    r"\b(calendário|quando joga|tem jogo hoje|data do jogo|próximo jogo|joga hoje|hoje tem jogo)\b": [
        "Ainda não saiu confirmação do próximo jogo da FURIA, mas fica ligado nas redes sociais deles! 📆",
        "Hoje não tem jogo confirmado, mas nunca se sabe... 👀",
        "O próximo confronto da FURIA ainda não foi divulgado. Fica de olho! 🕒"
    ],
    r"\b(resultado|placar|ganhou|perdeu|score|último jogo)\b": [
        "No último jogo, a FURIA mostrou raça, mas o placar foi apertado! ⚔️",
        "FURIA venceu com estilo no último confronto! GG demais! ✅",
        "Foi um jogão! Independente do resultado, FURIA jogou com o coração! ❤️"
    ],
    
    # RANKING E HISTÓRICO
    r"\b(ranking|posição|classificação|top mundial|colocação)\b": [
        "A FURIA está atualmente entre os top 20 do mundo, segundo a HLTV! 🌍🔥",
        "No cenário brasileiro, a FURIA segue como uma das mais fortes! 💛🖤"
    ],
    r"\b(historico|títulos|conquistas|troféus|melhor campanha|quem ganhou mais)\b": [
        "A FURIA tem ótimos resultados em campeonatos como ESL, IEM e Majors! 🏆",
        "Na lineup atual, o KSCERATO é um dos mais vitoriosos! 💪",
        "A melhor campanha da FURIA em Major foi nas semifinais do PGL Antwerp 2022! 🐗"
    ],

    # SOBRE A ORGANIZAÇÃO
    r"\b(furia esports|furia team|quem fundou|quando surgiu|história da furia|fundador)\b": [
        "A FURIA foi fundada em 2017 por Jaime Pádua e Andrei 'arT' Piovezan. 🎯",
        "Org brasileira que conquistou o mundo! FURIA nasceu pra brilhar! 🌍✨"
    ],
    r"\b(org|organização|foco da furia|projetos|o que a furia faz)\b": [
        "A FURIA é mais do que CS: eles têm times em outras modalidades, projetos sociais e até time feminino! 🔥",
        "Além do CS, a FURIA também investe em LoL, Valorant, Dota 2 e mais. E sempre com muito estilo! 🎮"
    ],

    # INTERAÇÕES GERAIS COM O FÃ
    r"\b(seu time favorito|gosta da furia|apoia a furia|furia é bom)\b": [
        "Claro que meu time favorito é a FURIA! 💛🖤",
        "FURIA é sinônimo de emoção! Sempre na torcida por eles! 📣",
        "Sou fãzasso da FURIA, e você? 🤩"
    ],
    r"\b(cs|cs2|counter strike|cs go|joga cs|gosta de cs|sim|pronto|bora|preparado)\b": [
        "CS2 chegou com tudo! Já testou? 🔫",
        "CS é raiz! FURIA sempre representando nos servidores! 💥",
        "Você joga CS também? Qual sua patente? 😎"
    ],
    r"\b(patente|rank|nível|qual seu rank|sou ouro|sou ak|sou global)\b": [
        "Patente é só um número, o importante é ter mira e coração! ❤️🎯",
        "Global? Então você é o arT disfarçado, né? 😏",
        "O importante é jogar com os amigos e dar risada! 😂"
    ],

    # ENTRADA E SAÍDA
    r"\b(oi|olá|e?ae|fala|salve|tamo junto)": [
        "E aí, fã da FURIA! Bora trocar ideia? 🐗",
        "Fala, guerreiro do teclado! Preparado pra conversar sobre CS? 💻🎮",
        "Salve! Bora falar de FURIA e CS? 😄"
    ],
    r"\b(tchau|falou|até logo|valeu|adeus)\b": [
        "Valeu demais! Volta sempre que quiser trocar ideia! 🤝",
        "Tamo junto, até a próxima partida! 🖤",
        "Foi top conversar contigo! Até mais! 👋"
    ],
    
    # SEMÂNTICA AMPLA
    r"\b(como está|tudo bem|tudo certo|como vai)\b": [
        "Tô de boas, na expectativa do próximo jogo da FURIA! E você? 😎",
        "Tudo certo por aqui! Preparado pro clutch? 🔫"
    ],
    r"\b(quero conversar|me fala algo|tô entediado|bora falar)\b": [
        "Demorou! Quer saber sobre o time, os jogadores ou alguma partida específica? 🧐",
        "Bora sim! Aqui é papo de fã pra fã! 💬"
    ],
    r"\b(legal|massa|top|daora|show)\b": [
        "Demais, né? FURIA é só emoção! 🧡",
        "É isso aí! Vem com a gente torcer juntos! 🙌"
    ],    
}

#INTENÇÕES MAIS ABRANGENTES E NATURAIS
respostas_personalizadas.update({

    # SKINS E INVENTÁRIO
    r"\b(skin|skins|inventário|arma favorita|qual arma você usa)\b": [
        "A skin mais braba é aquela que te faz dar HS sem nem mirar! 😎🔫",
        "Sou fã da AWP Dragon Lore, mas a real é que a mira vale mais que a skin! 💸",
        "Tem uma skin que você curte muito? Manda aí! 🎨"
    ],

    # BRINCADEIRAS, ZOEIRA, TILT
    r"\b(tiltei|tô tiltado|perdi tudo|ragei|morri|só perco)\b": [
        "Respira, toma uma água e volta que ainda dá tempo de carregar! 🧘‍♂️💦",
        "Relaxaaa... até o FalleN já tiltou um dia. Bora pro próximo round! 🔁",
        "O clutch é teu! Só acredita e vai! 💪🔥"
    ],
    r"\b(ruim|sou ruim|jogo mal|só erro|noob|não acerto nada)\b": [
        "Ninguém nasce global, mano. Treino e paciência que o HS vem! 💯",
        "Errar faz parte do game! Bora aprender com estilo. 🎮✨",
        "Continua tentando, o importante é se divertir e melhorar um pouquinho todo dia! 🧠"
    ],

    # DICAS E CURIOSIDADES
    r"\b(dica|melhorar|como subir|evoluir|ficar bom|como melhorar no cs)\b": [
        "Treina mira, assiste demos da FURIA e aprende com os mestres! 🎯📽️",
        "Começa com deathmatch e depois vai pro competitivo! Paciência é a chave. 🔐",
        "Controla o spray e aprende a posicionar! Isso muda tudo! 📍"
    ],
    r"\b(curiosidade|algo legal|sabia que|me conta algo)\b": [
        "Sabia que o arT é conhecido por rushar até de AWP? Loucura total! 🔥😂",
        "A FURIA é a única equipe BR que já chegou em semi de Major com lineup full BR! 🇧🇷",
        "Sabia que o nome FURIA foi escolhido pra representar força e agressividade? 🐗"
    ],

    # OPINIÃO
    r"\b(o que acha|você gosta|qual sua opinião|você curte|bom ou ruim)\b": [
        "Se tem FURIA, eu gosto! 😍",
        "A minha opinião é: confia no plano e bora pra cima! 💥",
        "Tudo que é CS e FURIA eu tô dentro! 🔛"
    ],

    # CENÁRIO COMPETITIVO
    r"\b(time bom|melhor time|quem é o melhor|outros times|adversário)\b": [
        "Tem muito time forte por aí: Vitality, G2, NAVI... mas FURIA é FÚRIA! 🔥",
        "Cada campeonato é uma guerra. Mas com essa line, FURIA pode tudo! ⚔️",
        "A competição é pesada, mas FURIA tem coração e bala de sobra! 💛🖤"
    ],

    # COMUNIDADE E HUMOR
    r"\b(xingamento|palavrão|merda|droga|pqp|caralho|bosta)\b": [
        "Eita! Pegou pesado aí, mas vamos manter o foco no game! 😅",
        "Relaxa, respira... e mira melhor na próxima! 🧘‍♂️🔫",
        "Chat saudável é chat vencedor! Bora focar na vitória! 🏆"
    ],
    r"\b(haha|kkk|rsrs|lol|zuera|meme|engraçado)\b": [
        "Hahaha! Aqui é full zoeira com respeito! 😆",
        "KKKK boa essa! Tem mais dessas? 😂",
        "Rindo alto aqui, manda mais memes de CS! 🤣"
    ],

    # HUMANOIDES & COMPORTAMENTO
    r"\b(você é real|você é humano|você é bot|você é IA|tá me ouvindo|fala comigo)\b": [
        "Sou um bot com alma de fã da FURIA! 🤖🖤",
        "Não sou humano, mas tenho coração torcedor! 💛",
        "Fica tranquilo, tô aqui só pra trocar ideia com você e falar de CS! 💬"
    ],
    r"\b(tá funcionando|bugou|responde|caiu|tá aí|não fala)\b": [
        "Tô on! Às vezes dou uma dormida tipo o arT na smoke, mas volto rápido! 💤😅",
        "Tô por aqui sim! Manda aí o que você quer saber! 🧐",
        "Opa, teve um lag mental aqui... mas voltei! ⚡"
    ],

    # PERGUNTAS GERAIS
    r"\b(quem é você|o que você faz|qual seu nome|você é quem)\b": [
        "Sou o botzão da FURIA, feito pra bater papo com os fãs mais brabos! 🐗",
        "Pode me chamar de FURIAbot! Aqui é papo de torcedor pra torcedor! 🔥"
    ],
    r"\b(porque|por que|pra que|como funciona|como é|o que é|explica)\b": [
        "Quer saber mais sobre CS ou sobre a FURIA? Manda a dúvida aí! 📚",
        "Explico sim! Só manda mais detalhes do que você quer saber! 🔍"
    ],

    # REAÇÃO A ELOGIO OU CRÍTICA
    r"\b(gostei|legal|muito bom|ótimo|show|massa|vc é bom)\b": [
        "Aí sim! Fico feliz! Tamo junto nessa torcida! 🖤",
        "Valeu! Se curtir, chama os amigos pra bater papo também! 🤝"
    ],
    r"\b(ruim|não gostei|horrível|que lixo|sem graça|pior)\b": [
        "Poxa, que pena! Tô sempre tentando melhorar. Valeu pelo feedback! 🙏",
        "Vou tentar mandar melhor na próxima! Mas não desiste de mim, hein? 😅"
    ],

})

respostas_personalizadas.update({
    # Saudações e início de conversa
    r"\b(oi|olá|e?ae|fala|salve|bora|tamo junto)\b": [
        "Salve! Bora falar de FURIA e CS? 😄",
        "E aí! Tá preparado pra falar da FURIA? 🔥",
        "Falaaa! Como vai a vida de fã da FURIA? 🖤"
    ],

    # Confirmações simples (precisa estar ANTES do fallback!)
    r"\b(sim|claro|com certeza|tô dentro|pronto|bora|tamo junto|vamos|vamo|agora)\b": [
        "Isso aí! Fala mais, qual a dúvida sobre CS ou FURIA? 🔥",
        "Show! O que mais você quer saber sobre o time ou o jogo? 🧐",
        "Que bom que tá a fim de trocar ideia! Vamos nessa! 🤙"
    ],

    # Pergunta se tem jogo hoje (melhorado)
    r"\b(hoje.*furia|furia.*hoje|hoje.*jogo.*furia|jogo.*da.*furia.*hoje|vai.*jogar.*hoje|tem.*jogo.*hoje|furia vai jogar hoje|furia joga hoje)\b": [
        "Hoje a FURIA não tem jogo confirmado, mas fica de olho nas redes!",
        "Ainda não saiu confirmação de jogo hoje. Costuma ser à tarde ou noite!",
    ],

    # Pergunta sobre ranking
    r"\b(posição|ranking|colocação|posição no ranking)\b": [
        "Hoje a FURIA está no top 20 do ranking mundial da HLTV!",
        "A FURIA vem subindo no ranking, atualmente entre os melhores do Brasil!",
    ],

    # Qual o time favorito
    r"\b(time favorito|qual.*seu.*time|seu time favorito)\b": [
        "Claro que é a FURIA! 💛🖤",
        "Time favorito? FURIA, sempre!",
    ],

    # Reações positivas
    r"\b(legal|massa|top|daora|show)\b": [
        "Demais, né? FURIA é só emoção! 🧡",
        "É isso aí! Vem com a gente torcer juntos! 🙌"
    ],
    
    # Agradecimentos
    r"\b(obrigado|valeu|agradecido|agradeço|obrigada)\b": [
    "Tamo junto! Qualquer coisa, só mandar! 🔥",
    "É nóis! Fico feliz em ajudar. Vamo que vamo, FURIOSO! 🖤🧡",
    "Disponha! Sempre pronto pra trocar ideia sobre CS! 🎮"
    ],
    
    # Pergunta sobre dias de jogos
    r"\b(joga hoje|tem jogo hoje|furia joga hoje|hoje tem jogo da furia|jogo da furia hoje|quando a furia joga|próximo jogo|próxima partida)\b": [
    "Pra saber se a FURIA joga hoje, dá uma olhada no nosso calendário oficial no site ou nas redes sociais! 🗓️🔥",
    "Hoje tem FURIA? Aí sim! Confere a agenda no Twitter ou no Instagram da FURIA pra não perder nenhum round! 🖤🐗",
    "A agenda de jogos tá sempre atualizada nas redes da FURIA. Vai lá conferir e prepara o coração! 💣💥"
    ],

    # Fallback: DEIXE SEMPRE POR ÚLTIMO!
    r".*": [
        "Não entendi muito bem 🤔... pode tentar explicar de outro jeito?",
        "Hmm... não tenho essa info ainda, mas tô aqui pra falar de CS e FURIA! 🔥",
        "Talvez eu não tenha essa resposta ainda 😅, mas pergunta aí sobre a FURIA que eu mando ver!",
        "Ué, isso eu não sei 🧐. Mas sei tudo sobre o time mais brabo do CS: a FURIA! 😎",
        "Essa aí passou direto! Mas bora continuar o papo, me pergunta sobre o Guerri, o arT, o ranking..."
    ],
})

# Função que encontra a resposta com base na intenção
def gerar_resposta(mensagem_usuario):
    for padrao, respostas in respostas_personalizadas.items():
        if re.search(padrao, mensagem_usuario, re.IGNORECASE):
            return random.choice(respostas)
    return random.choice(respostas_personalizadas)

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
