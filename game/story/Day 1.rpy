image splash = "Ods splash.png"

label splashscreen:
    scene black
    with Pause(1)

    show text "{color=#FFFFFF}Esse jogo se trata da ODS número 16, que aborda ''Paz, Justiça e Instituições Eficazes''{/color}"
    with Pause(2.5)
    hide text
    show splash with dissolve:
        xalign 0.5
        yalign 0.5
    with Pause(4)

    scene black with dissolve
    with Pause(1)

    return

label start:
    window hide
    show black with fade
    jump intro
# screens (User interface)

label intro: #Intro no quarto - Dia 1
    "{i}trim, trim{/i}"
    show nate n at left
    Nathan "Alô?"
    show erika n at right
    dErika "Nathan, sou eu, Erika! Você vai voltar pra cidade essa semana, não é? Bastante coisa aconteceu desde que você saiu, acho que seria legal a gente se atualizar."
    show nate f at left
    Nathan "Erika! Claro! Na verdade, meus pais já tinham me convidado pra jantar um pouco antes do esperado."
    Nathan "Então eu meio que já estou por aqui, você acha que amanhã é um bom momento para nos encontrarmos?"
    Erika "Mhm! Com certeza, pensei que a gente podia conversar com os meninos também, eles têm bastante assunto pra falar com você."
    Nathan "Acho que isso é uma ótima ideia, bom, então te vejo amanhã, Erika!"
    Erika "Obrigada, Nathan. Mal posso esperar para ver você novamente. Nos encontramos em breve!"
    show bg quarto dia with fade
    scene bg quarto dia
    show halfblack
    show erika n at right
    show nate n at left
    Erika "Nathan!! Tá acordado?"
    Nathan "Só mais 5 minutinhos por favor..."
    Erika "5 minutinhos nada, a gente vai sair agora, sua mãe já até me deu uma lista de coisas que você tem que fazer hoje seu preguiçoso."
    Nathan "Tá bom... Só deixa eu me trocar e eu te encontro lá na frente da loja ok?"
    Erika "Certo! Te vejo lá então! Beijinhos!"

    hide erika
    show john n at right
    John "Huh, ela tá bem mais animada em te ver hoje, vem cá Nathan, quando é que você vai parar de ser um covarde e vai contar pra ela que você gosta dela hein?"
    hide john 
    show camilla n at right
    Camilla "John, por favor, você sabe que ele não é covarde, ele só... ele só é..."
    Nathan "Ele tem razão, Camilla, eu sou meio cagão pra essas coisas mesmo, mas isso não é prioridade agora, faz um tempinho que não vejo meus amigos, preciso encontrar eles agora, ok?"
    Nathan "Não quero vocês dois falando um piu enquanto eu estou fora, beleza?"
    hide camilla 
    show john n at right
    John "Se você pode ver e ouvir a gente não é problema nosso, você que decidiu ser diferentão e nasceu com a capacidade de ver seus guardiões."
    John "E nós nunca atrapalhamos nenhuma conversa sua, rapaz!"
    hide john 
    show camilla n at right
    Camilla "É verdade, sempre somos incrivelmente legais, divertidos e respeitosos com você, senhor Nathan!"
    Nathan "Tá, tá, só prometam que não vão ficar aparecendo do nada."
    hide camilla 
    show john n at right
    John "Hmpf, pode deixar, não vamos atrapalhar, vai lá ver seus amigos e sua namoradinha logo, vai."
    hide john 
    show camilla n at right
    Camilla "Bom passeio, Nathan, divirta-se!"
    jump intro2

label intro2: #Intro indo no mercado pela primeira vez - Dia 1
    scene bg mercado dia with dissolve
    show halfblack
    show nate n at left
    Nathan "Pronto, cheguei, o que tem na lista da minha mãe?"
    show erika n at right
    Erika "Como eu não sou xereta, eu não li, mas você pode ficar com ela, tá pronto pra ver os meninos?"
    "Eu não tive a chance de responder, ela me puxou pra dentro da loja quase de imediato."
    hide erika 
    hide nate
    scene bg shop
    show halfblack
    show erika n at right
    Erika "Oi gente! Olha quem eu trouxe pra ver vocês!"
    show seb b at left
    Sebastian "Erika eu juro pela minha vida se você soltar mais um gato de rua dentro da loja eu juro que—"
    hide erika with move
    show lucas f at right with vpunch
    Lucas "NATHAN!!!" #Lucas chega tremendo a tela, empurrando a erika pra fora do frame
    show lucas ch at right with vpunch
    Lucas "NÃO ACREDITO VOCÊ TA VIVO! POR QUE VOCÊ NÃO FALOU COM A GENTE ESSE TEMPO TODO?"

    menu:
        "Eu não tava muito afim.":
            hide seb
            show nate s at left
            Nathan "Eu não tava muito afim, tinha muitas coisas pra resolver e não pensei que vocês sentiam tanta falta pra ser sincero."
            show lucas b at right
            Lucas "Mas é claro que a gente sentiu sua falta, bobão."
            hide lucas
            show seb f2 at right
            Sebastian "Por que a gente não sentiria falta de um cara tão divertido quanto você?"
            hide seb
            hide nate

        "Eu queria fazer uma surpresa!":
            hide lucas
            show nate f at right
            Nathan "Eu queria que isso fosse surpresa... sabe? E funcionou! Haha."
            show seb f2 at left
            Sebastian "A gente sabe que você só esqueceu de mandar mensagem, não precisa inventar desculpas, haha."
            hide seb
            show lucas n at left
            Lucas "Que isso, Seb, aposto que o Nathan tem seus motivos, não fica pesando tanto na dele."
            show nate ex
            Nathan "Bom, eu..."
            hide lucas
            show erika n2 at left
            Erika "Ele esqueceu de mandar mensagem, foi isso, mas tudo bem, ele tá aqui agora, não precisam brigar."

    show erika n2 at left
    Erika "Ah é! Conta as novidades pro Nathan, sobre você sabe o que."
    hide nate
    show lucas f at right
    Lucas "Ah sim! Já tava quase esquecendo, se não fosse por você nos apresentar antes no colégio, eu e o Sebastian não estaríamos namorando hoje, sabia?"
    hide erika
    show nate ns at left
    Nathan "Vocês estão namorando!? Que ótimo, fico muito feliz por vocês dois!!"
    hide lucas
    show seb f at right
    Sebastian "Foi algo que aconteceu meio de repente, você ainda estava fora da cidade, mas com certeza uma das melhores escolhas que podíamos ter feito. Mas enfim, o que é isso aí na sua mão, cara?"
    show nate n at left
    Nathan "Ah é, antes que eu esqueça, isso aqui é uma lista de compras que minha mãe me passou, vocês conseguem resolver isso pra mim? Não parece ser muita coisa."
    hide seb
    show lucas f at right
    Lucas "Claro, claro, deixa que eu tomo conta disso."
    hide lucas
    #Lucas pega a lista das minhas mãos e sai por um tempo
    Nathan "Você pode me contar essa história do gato de rua?"
    show seb b at right
    Sebastian "Basicamente, a genia ali soltou um gato feroz dentro da loja que derrubou TUDO de TODAS as prateleiras. Foi bem complicado de explicar pro pai do Lucas que a gente não conseguiu vender nada no dia porque ficou arrumando a loja depois."
    show seb f at right
    Sebastian "Você teve sorte de não ser banida de entrar nesse mercado, Erika, hahaha."
    hide nate
    show erika s at left
    Erika "Não foi bem assim..."
    #Lucas retorna
    hide erika
    show lucas f at left
    Lucas "Aqui estão suas coisas! Fala pra sua mãe que deixamos um oi, e só porque faz tempo que a gente não te vê, pode levar as compras por conta da casa, ok?"
    Sebastian "Você realmente tem que parar de dar os produtos de graça pra quem você acha legal. A gente vai falir desse jeito."
    Sebastian "E também, vocês dois, tomem cuidado, principalmente você, Erika! Hoje cedo as notícias falaram que—{nw}"
    hide lucas
    show erika s at left with vpunch
    Erika "Obrigada, meninos! A gente vai indo agora, até outra hora, beleza?"
    "Erika de novo me puxa pra fora da loja e me leva pra casa. Tentei falar com ela no caminho sobre cortar a fala do Sebastian, mas ela continuou evitando o assunto."
    show black with dissolve
    jump quartodia1

label quartodia1: # Quarto e final do dia 1 - Dia 1
    show bg quarto tarde with dissolve
    scene bg quarto tarde
    show halfblack
    show camilla b at right
    Camilla "Ei, será que a gente pode falar agora? Tá difícil segurar o tagarela aqui."
    show nate ns at left
    Nathan "Podem falar sim, não vejo problema agora."
    hide camilla
    show john b at right
    John "Ah, tá bom, eu sou o tagarela, tá certo, se não fosse por mim essa daí teria interrompido sua conversa diversas vezes só pra perguntar da história do gato!"
    hide john
    show camilla b at right
    Camilla "Ah tá, como se eu fosse a única que estava curiosa, né?"
    show nate b
    Nathan "Se acalmem vocês dois!"
    hide camilla
    show john n2 at right
    John "Não tô afim de discutir hoje mesmo! Mas aí, eu queria entender o que a Erika tava querendo esconder tanto. É normal ela cortar os outros falando mesmo, mas parece que o Sebastian ia dizer algo importante..."
    show nate n at left
    Nathan "Sim, foi estranho ver ela agindo dessa forma. Eu também me perguntei o que o Sebastian estava querendo dizer. Talvez seja algo que a deixou ansiosa ou que ela não queria discutir naquele momento. Eu posso tentar perguntar pra ela amanhã."
    "O tempo passa..."
    show bg quarto noite with dissolve
    hide john
    show pai n2 at right
    Pai "E aí, filho, tá aqui a quase dois dias e nem fala comigo? O que foi? Prefere falar com seus amiguinhos imaginários? Hahaha."
    Pai "Já decidiu o que vai fazer da vida, ou vai continuar gastando o dinheiro que tínhamos guardado pra sua faculdade com mais viagens inúteis?"
    menu:
        "Responder com ironia":
            Nathan "Oi, pai, também senti saudades de você, obrigado pela consideração, e eles não são amigos imaginários, você sabe disso!"
            show pai b at right
            Pai "Err, sei... Só acho que você deveria—"
            hide pai
            show mae b at right
            Mãe "Ora, ora, vocês dois, parem já com isso! Deveriam estar felizes em se ver, não brigando na primeira oportunidade. Vamos, a janta já está na mesa, tenho certeza que vão se entender melhor de barriga cheia!"
            hide mae
            show pai s at right
            Pai "Ok, desculpe, querida."
            hide pai
            show nate ns at left
            Nathan "Certo, vamos lá!"
            $ brigacompai += 1

        "Responder de forma agressiva":
            show nate b
            Nathan "Se você vai falar comigo desse jeito, eu realmente prefiro falar com os meus 'amigos imaginários' mesmo."
            show pai b
            Pai "Além de não conversar comigo, ainda é ignorante. Sinceramente, garoto, você é incorrigível, eu—"
            hide nate
            show mae b at left
            Mãe "O que está acontecendo aqui?"
            hide mae
            show nate ch at left
            Nathan "O mesmo de sempre vindo do papai, só isso."
            Pai "O mesmo de sempre vindo de mim? Olha como você me trata, garoto, não esqueça que você ainda mora debaixo do meu teto!"
            hide nate
            show mae b at left
            Mãe "Chega disso! Vocês dois! Não vou tolerar brigas hoje, entendidos?"
            hide mae
            show nate n at left
            Nathan "..."
            Pai "..."
            Pai "Desculpe, querida."
            hide nate
            show mae b at left
            Mãe "Vamos, vocês dois, a janta já está na mesa."
            hide mae
            show nate ns at left
            Nathan "Certo, obrigado, mãe!"
            $ brigacompai += 1

        "Não responder nada":
            show nate n at left
            Nathan "..."
            show pai b at right
            Pai "Vai continuar sem falar nada? De verdade, garoto, você—"
            hide pai
            show mae b at right
            Mãe "Fábio!!! Já está provocando o Nathan? O que nós conversamos hoje mais cedo?"
            hide mae
            show pai s at right
            Pai "..."
            show pai f at right
            Pai "Desculpe, querida, você tem razão." 
            hide pai
            show mae b at right
            Mãe "Venham, vamos jantar, vocês dois, a comida já está na mesa. Nathan, quero que nos conte tudo sobre como foi sua viagem, querido!"
            show nate ns
            Nathan "Com todo o prazer!"
    scene black
    "E assim se finaliza o meu primeiro dia na cidade."
    jump startday2

# label invteste:
#     screen botaoCasal():
#         image "bg shop.png"
#         if "chave" in inventory_items:
#             imagebutton:
#                 xpos 1620
#                 ypos 500
#                 auto "Red_button_%s.png"
#                 action Notify("Itens removidos"), Jump("removetudo")

#         if "chave" not in inventory_items:
#             imagebutton:
#                 xalign 0.5
#                 yalign 0.5
#                 auto "Red_button_%s.png"
#                 action Notify("Você tem todos os itens agora"), Jump("ColetaChave")
    
#         imagebutton:
#             xalign 0.0
#             yalign 1.0
#             auto "Mochila %s.png"
#             action ToggleScreen("inventory_item_description")

# label ColetaChave:
#     $ inventory_items.append("chave")
#     $ inventory_items.append("arquivos")
#     $ inventory_items.append("caderno aberto")
#     $ inventory_items.append("caderno fechado")
#     $ inventory_items.append("aliança")
#     $ inventory_items.append("distintivo")
#     $ inventory_items.append("luvas")
#     jump retornoCasal

# label removetudo:
#     $ inventory_items.remove("chave")
#     $ inventory_items.remove("arquivos")
#     $ inventory_items.remove("caderno aberto")
#     $ inventory_items.remove("caderno fechado")
#     $ inventory_items.remove("aliança")
#     $ inventory_items.remove("distintivo")
#     $ inventory_items.remove("luvas")
#     jump retornoCasal
# screen botaoJornal():
#     image "bg biblioteca.png"
#     imagebutton:
#         xalign 0.5
#         yalign 0.5
#         auto "Red_button_%s.png"
#         action Jump("biblioteca")

# # Mapa

# screen mapa():
#     image "bg map.jpg"
#     imagebutton:
#         xalign 0.5
#         yalign 0.5
#         auto "Red_button_%s.png"
#         action Hide(), Show("botaoQuarto", fade)
    
#     imagebutton:
#         xalign 1.0
#         yalign 0.5
#         auto "Red_button_%s.png"
#         action Hide(), Show('botaoCasal', fade)

#     imagebutton:
#         xalign 0.0
#         yalign 0.5
#         auto "Red_button_%s.png"
#         action Hide(), Show('botaoJornal', fade)

#     imagebutton:
#         xalign 1.0
#         yalign 0.0
#         auto "Red_button_%s.png"
#         action Hide(), Show('botaoErika', fade)



# label finalexemplo:
#     scene bg quarto
#     show halfblack:
#         alpha 0.2
#     pause
#     window hide
#     show halfblack with dissolve
#     show vivian test at left
#     show erika test at right
#     Erika "Lorem ipsum."
#     Vivian "Lorem ipsum."
#     show erika test at left with move
#     show vivian test at right with move
#     Erika "teste"
#     Vivian "Teste"
#     pause