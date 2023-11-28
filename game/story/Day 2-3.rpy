label startday2: #Começo do dia 2 - Quarto - Dia 2
    show bg quarto dia with dissolve
    scene bg quarto dia
    show halfblack
    "{i}Toc toc{/i}"
    show mae f at right
    Mãe "Nathan querido, você já acordou? Queria pedir uma coisa para os meninos, será que é pedir demais?"
    show nate n at left
    Nathan "O que...? Acabei de levantar, será que posso fazer isso depois?"
    show mae b
    Mãe "Não, você não pode, a torta que eu fiz vai esfriar se você demorar."
    hide mae
    show john f at right
    John "Sua mãe fez torta? Eu adoro as tortas dela, você devia roubar um pedaço."
    hide john 
    show camilla b at right
    Camilla "Mas a gente não come, isso não faz sentido."
    hide camilla
    show john f at right
    John "Eu gosto do cheiro."
    show nate ns
    Nathan "Tá bom, eu já estou levantando, e não, John, não vou roubar um pedaço pra você."
    show john n
    John "É por isso que eu te odeio, sabia?"
    Nathan "Você odeia até sua própria sombra, John, sem mim você nem existiria. Fica quietinho aí."
    "Eu pego a torta das mãos da minha mãe, ela tem um cheiro exageradamente doce, e vou em direção ao mercadinho dos meninos mais uma vez."
    #adicionar uma torta no inventário?
    $ inventory_items.append("Torta")
    $ renpy.notify("Agora você tem uma torta")
    jump lojaday2

label lojaday2: #Fachada da loja aparece quebrada, você conhece David e Vivian - Dia 2
    scene bg mercado roubado dia
    show halfblack
    "Quando cheguei na loja, ela estava totalmente diferente do que eu lembrava ontem; A equipe policial também estava no local."
    show nate s at left
    Nathan "O que aconteceu aqui?"
    show david f at right
    dDavid "Uma testemunha!"
    "Ele se aproximou muito rápido, me pergunto se ele já sabia que eu estaria aqui de alguma forma..."
    show bg mercado roubado dia with hpunch
    David "Perito David se apresentando para o serviço, senhor!"
    show nate a
    Nathan "David, do departamento de polícia? Você por acaso não trabalha com o meu pai, o Delegado Fábio, né?"
    show bg mercado roubado dia with hpunch
    show david s
    David "O QUÊÊÊ??? VOCÊ É O FILHO DO DELEGADO?? MINHAS SINCERAS DESCULPAS, FILHO DO DELEGADO, SENHOR!"
    show nate s
    "{i}Ele acha que eu tenho algum tipo de controle sobre ele por ser filho do patrão dele?, talvez eu possa usar isso ao meu favor pra que ele me conte o que aconteceu aqui.{/i}"
    Nathan "David, você sabe me dizer o que aconteceu por aqui?"
    show david f
    David "Sim, senhor! Durante a noite, alguém quebrou a janela do mercado com um tijolo, senhor!"
    David "Por sorte ninguém se feriu, porém os dois funcionários estão no departamento sendo interrogados agora mesmo, senhor!"
    Nathan "Entendi, será que eu posso ir vê-los? São meus amigos, e também, não precisa ficar me chamando de senhor."
    show david t
    David "Perdão, senhor!, desculpe, como posso te chama-lo, senhor?, desculpe."
    show nate n
    Nathan "Pode me chamar só de Nathan mesmo."
    show david f
    David "Ok, senhor Nathan! Posso te levar imediatamente!"
    show nate n
    Nathan "..."
    Nathan "Obrigado!"
    Nathan "{i}Não adiantou nada...{/i}"
    "Enquanto David me guiava até a delegacia, uma moça de cabelos longos me parou"
    show bg rua dia with dissolve
    scene bg rua dia
    show halfblack
    show vivian n at right
    dVivian "Com licença moço, você tem um tempinho?"
    show nate ns at left
    Nathan "Eu acho que tenho, por quê?"
    show vivian f2
    Vivian "Eu me chamo Vivian, sou uma investigadora local que trabalha para o departamento de polícia, queria saber se você conhece as vítimas desse assalto, ou qualquer informação relevante."
    show nate a
    Nathan "Eu acho que tenho..."
    menu:  
        "Falar mais sobre o caso":
            Nathan "Até onde eu me lembro, ontem as vítimas não estavam esperando por nada desse nível, por mais que o Sebastian tenha me dito pra tomar cuidado com alguma coisa."
            Nathan "Infelizmente, fui cortado por uma amiga nessa hora, então eu não sei bem o que ele quis dizer nessa hora."
        "Responder apenas o necessário":
            Nathan "O que eu sei sobre o caso? Tudo que eu sei é que quebraram a janela deles, só isso, pra ser sincero."
    show vivian s
    Vivian "Entendi... Bom, obrigada de qualquer forma. Se souber de algo, por favor, me procure. Já é o segundo assalto desse ladrão, não queremos deixar ele escapar."
    hide vivian
    show david f at right
    David "Certíssima, senhorita Vivian! Bela e inteligente como sempre!"
    David "Vem cá, eu tava pensando que tal se a gent—{w=2.0}{nw}"
    hide david
    show vivian b at right
    Vivian "Não, David, obrigada, mas eu não vou sair com você."
    hide vivian
    show david t at right
    David "Bom, valeu a pena a tentativa."
    "Esses dois são muito esquisitos..."
    show nate ns at left
    hide david
    Nathan "Desculpa a pergunta, dona Vivian, mas como assim segundo assalto?"
    show vivian n at right
    Vivian "É, então, parece que alguns dias atrás o mesmo ladrão assaltou a casa de uma garota de roupas estilosas azul ciano."
    show nate n
    Nathan "Calma, e como vocês sabem que foi o mesmo ladrão?"
    show vivian f2
    Vivian "Bom, aparentemente é a assinatura dele tacar tijolos na janela do lugar que ele vai assaltar, esse cara parece bem estúpido, logo logo a gente deve pegar ele."
    Vivian "O problema é que ele parece saber o como a gente investiga as coisas e consegue limpar bem as evidências que poderiam apontar para alguma pessoa"
    hide vivian
    show david b at right
    David "Senhor! Me desculpe, mas não temos mais tempo para conversas."
    "Já não basta a Erika me puxando pra todos os lugares, o David veio me puxar também."
    "Eu preciso encontrar essa moça de novo, essa garota de azul ciano... Será que era a Erika??."

    jump delegaciaday2

label delegaciaday2: #Você chega na delegacia com David e Vivian, encontrando Lucas e Sebastian - Dia 2
    show bg delegacia frente dia with dissolve
    scene bg delegacia frente dia
    show halfblack
    show david b at right
    David "Senhor! Chegamos! As vítimas estão sendo interrogadas no momento, porém irão retornar em um instante. Irei checar como o processo está indo!"
    hide david
    #David sai da sala
    show nate n at left
    Nathan "Não pensei que eu ia voltar pra esse lugar tão cedo. A última vez que vim foi para passar um dia com meu pai no trabalho."
    hide nate
    show bg delegacia dentro with dissolve
    scene bg delegacia dentro
    show halfblack
    "Eu entro na delegacia, logo após David. Alguns minutos se passam enquanto observo a sala, ela parece menor que antes... E então o casal aparece."
    show lucas ch at right
    Lucas "N-Nathan...{i}sniff{/i} O que você...{i}sniff{/i} faz por aqui?"
    "É muito difícil entender o que o Lucas tem a dizer, ele parece muito abalado."
    show nate n at left
    Nathan "Ah, eu vim ver como vocês estavam. É algo muito difícil de se lidar, sabe..."
    Lucas "Muito {i}sniff{/i} obrigado, Nathan {i}sniff{/i}. Você é muito gentil..."
    "Nesse momento, Sebastian se aproxima para conversar."
    hide lucas
    show seb n at right
    Sebastian "Sabe o que é pior? Além de terem levado todo o nosso dinheiro, eles levaram as alianças que eu queria dar pro Lucas em breve. Fiquei meses guardando dinheiro pra comprá-las."
    Nathan "Sinto muito, Sebastian..."
    Sebastian "Pois é, não é só você que queria fazer uma surpresa, sabe? Voltando assim de repente."
    Nathan "Seb, eu sei que isso é bem insensível da minha parte, mas você pode me dar um segundo?"
    show seb c
    Sebastian "Hm? Ta bom..."
    hide seb
    Nathan "{i}John, Camilla, conseguem me dar uma ajudinha aqui?{/i}"
    show john b at right
    John "Agora você precisa de ajuda, né? Achei que a gente ficasse atrapalhando você. O que você quer?"
    Nathan "...Desculpe."
    Nathan "Então, pode ser coincidência, mas achei muito estranho esse ladrão ter assaltado só pessoas que eu conheço até agora. Não acho justo meus amigos estarem perdendo tudo."
    Nathan "Talvez eu devesse ajudá-los de alguma forma, já que meu pai trabalha na polícia. Talvez investigar por conta própria, sabe?"
    hide john 
    show camilla t at right
    Camilla "Me desculpa, Nathan, mas eu sou totalmente contra essa ideia. Você pode acabar se colocando em perigo! Além do mais, nem sabemos se a garota que aquela Vivian comentou é de fato a Erika."
    Nathan "Não se preocupe, não vou me arriscar. Aliás, é aí que vocês entram. Vocês podem, por favorzinho, me ajudar a tentar recuperar as coisas deles e pegar esse ladrão antes que ele machuque alguém?"
    hide camilla
    show john n2 at right
    John "Você pode tentar perguntar pro David, já que ele tá tão na sua haha."
    show nate f
    Nathan "Ótima ideia! David! Preciso de sua ajuda aqui!"
    show john n
    John "Ei, eu tava zoando, volta aqui!"
    hide john
    Nathan "David! Posso perguntar uma coisa?"
    show david f at right
    David "Sim, Nathan Senhor!"
    show nate ns
    Nathan "{i}(Isso ta começando a me dar nos nervos){/i}"
    Nathan "Sabe me dizer se tem algum arquivo criminal desse ladrão aí? Tô ficando meio preocupado."
    show david t
    David "Eles até existem, mas você não pode acessá-los já que não trabalha aqui. Se pudesse, eu até buscava eles na sala do seu pa—"
    show david s
    David "Digo, não senhor..."
    show nate f
    Nathan "Entendo, muito obrigado, David. Sebastian, Lucas, eu preciso ir mas espero encontrar vocês por aí, okay? Se cuidem!"
    "Verdade, acho deveria entregar a torta para o Lucas e pro Sebastian, mas será que esse é um bom momento?"
    menu:
        "Entregar a torta":
            Nathan "Antes que eu me esqueça, minha mãe pediu pra entregar essa torta pra vocês como agradecimento pelas compras"
            hide david
            show lucas n at right
            Lucas "Obrigado Nathan, agradeça sua mãe pela gente também"
            hide lucas 
            show david f at right
            David "Nossa que torta bonita! Posso pegar um pedaço?"
            hide david
            show lucas f at right
            Lucas "Pode sim!"
            hide lucas
            show john ch at right
            John "Ele comeu tudo!! NÃÃÃÃOOOO!!"
            "Então me despedi dos meus amigos e fui diretamente para casa. Precisava pensar no que fazer."
            $ inventory_items.remove("Torta")
        "Não parece ser uma boa hora":
            show nate n
            "Acho que não é o melhor momento pra isso, melhor entregar isso outra hora"
            $ mantevetorta += 1
    #menu de entregar a torta ou não, se entregar a torta lá no dia 5 eles mencionam ela dnv

    jump quartodia2
    
label quartodia2: #Você vai para seu quarto e tem a ideia de roubar os arquivos do caso - Dia 2
    show bg quarto tarde with dissolve
    scene bg quarto tarde
    show halfblack
    show nate f at left
    Nathan "Achei que você tava me zoando, John, isso foi extremamente útil."
    show john b at right
    John "MAS EU TAVA TE ZOANDO, só não achei que o David seria burro ao nível de entregar informações confidenciais..."
    show john n
    John "..."
    
    if "Torta" in inventory_items:
        show john f
        John "Pô, e aquela torta lá? não vai comer não?"
        Nathan "Eu ia entregar pra eles amanhã"
        John "Mas ela vai estar ruim até lá, por que você não come?"
        Nathan "Verdade, acho que eles não vão ligar, vou mandar pra dentro!"
        $ inventory_items.remove("Torta")
        $ renpy.notify("Você ficou de buchinho cheio")

    John "Eu tive uma ideia."
    hide john 
    show camilla b at right 
    Camilla "John, não ouse."
    hide camilla 
    show john n2 at right
    John "O que vocês acham da gente invadir a delegacia hoje à noite pra pegar esses arquivos? Não é como se a gente fosse conseguir agora cedo, ou seguir com essa tal investigação a qualquer outra hora."
    hide john 
    show camilla b at right 
    Camilla "Eu acho isso uma péssima ideia."
    show nate s
    Nathan "..."
    show nate ns
    Nathan "Acho que pode dar certo."
    Camilla "Eu não ajudar vocês a fazer isso!"
    menu:
        "Camilla, por favor!":
            show nate n
            Nathan "Camilla, vai, ajuda a gente, por favor!!!"
            show camilla b
            Camilla "Tá, tá, eu não tenho escolha de qualquer maneira, tô presa a vocês mesmo, vamos fazer isso logo vai, mas saibam que eu não tô nada feliz com isso."
            show nate ns
            Nathan "Certo, vamos lá então"
            Camilla "Espera, vocês vão assim? tipo, sem um plano nem nada?"
            hide camilla 
            show john f at right
            John "É assim que a gente faz minha filha, tudo no improviso mesmo."
            Nathan "isso ai"
            hide john
            show camilla b at right
            Camilla "..."
            Camilla "Por que vocês não tentam pegar a chave do pai do Nathan, isso não seria tipo, mil vezes mais fácil?"
            show nate f
            Nathan "Isso é uma ideia muito boa! Obrigado John!"
            hide camilla
            show john ex at right
            John "Não tem de quê, Nathan!"
            hide john
            show camilla b at right
            Camilla "Vocês são ridículos, não sei porque ainda tento ajudar..."
            Camilla "Isso é tipo, a primeira coisa que vocês tinham que pensar, vocês se quer pensam?"
            hide camilla
            show john n at right
            John "..."
            show nate n
            Nathan "..."
            hide john
            show camilla t at right
            Camilla "Acho que isso responde."
            menu:
                "É isso, vou pegar as chaves dele":
                    $ inventory_items.append("chave")
                    hide camilla
                    jump delegaciacomcamilla
                "Melhor não, isso pode dar problemas depois...":
                    show camilla b
                    Camilla "Já que vocês vão me ignorar, eu não vou ajudar mais"
                    show nate ex
                    Nathan "Desculpa Camilla, tenho menos medo de ser preso do que lidar com meu Pai de mau humor, melhor não arriscar mexer nas coisas dele."
                    show nate n
                    Camilla "Boa sorte na prisão então!"
                    hide camilla
                    jump delegaciasemcamilla
                    
        "Tudo bem, você não precisa ajudar":
            show nate a
            Nathan "Tá bom, se você não quer, você que perde a diversão."
            hide camilla 
            show john n at right
            John "É, você pode continuar sendo uma nerd chata."
            hide john 
            show camilla b at right
            Camilla "Eu não sou uma nerd chata."
            show camilla t
            Camilla "Sou?"
            show nate n
            Nathan "Eu tenho que concordar com ele dessa vez, desculpa."
            Camilla "..."
            hide camilla
            jump delegaciasemcamilla  

label delegaciacomcamilla: #Você invade a delegacia com a camilla - Dia 2
    "Decidi tirar um cochilo durante a tarde para não ter a chance de desmaiar de sono durante minha invasão."
    show bg quarto noite with dissolve
    pause
    show nate ns at left
    Nathan "Vocês estão prontos?"
    show john b at right
    John "Nasci pronto."
    hide john
    show camilla t at right
    Camilla "..."
    hide camilla 
    show john b at right
    John "Você tá pronta?"
    hide john 
    show camilla b at right 
    Camilla "Eu só vou acompanhar vocês pra que não se matem fazendo isso, ok?"
    Nathan "Bom o suficiente pra mim."
    "Eu abri a janela e senti o vento frio da noite. Com muito nervosismo, segui correndo para a delegacia mais uma vez."
    hide nate 
    hide camilla
    show bg delegacia frente dia noite with dissolve
    show nate n at left
    Nathan "Eu nunca fiz algo assim antes."
    Nathan "John, você tem cara de que cometeria um crime. Como eu faço pra entrar?"
    show john b at right
    John "Como assim eu tenho cara de que cometeria um crime?"
    hide john 
    show camilla f at right
    Camilla "É, você tem mesmo HAHAHAHA."
    hide camilla 
    show john n at right
    John "Não sei, tenta quebrar o cadeado ali ou aquela ventilação na parede da porta. Você parece caber."
    show nate ns
    Nathan "Eu sabia que podia contar com você."
    menu:
        "Destrancar o cadeado" if "chave" in inventory_items:
            hide john
            show camilla t at right 
            Camilla "Na verdade Nathan, você tem a chave do seu pai, por que você não só abre o cadeado que nem uma pessoa normal?"
            show nate f2 at left
            Nathan "Ah é né, esqueci."
            "Destranco o cadeado, aparentemente ele nem estava trancado, então só bastou um toquinho."
            scene bg delegacia dentro
            show halfblack
            show john ex at right
            John "Você pelo menos se lembra onde fica a sala do seu pai?"
            show nate n at left
            Nathan "Se eu não me engano, é nessa porta aqui."
            hide nate
            hide camilla 
            hide john 
            jump saladopai
        "Quebrar o cadeado" if "chave" not in inventory_items:
            "Eu me aproximo da porta, pego uma pedra e tento bater no cadeado"
            hide nate
            hide camilla 
            hide john 
            show camilla t at right
            Camilla "Espera, espera, e se o David esqueceu de trancar o cadeado? Ele é meio burrinho mesmo."
            show nate n at left
            Nathan "Eu acho que ele não seria tão idiota, mas eu posso tentar."
            "No momento em que eu toco no cadeado com as mãos, o cadeado cai"
            hide camilla 
            show john b at right
            John "Eu me recuso a acreditar que isso acabou de acontecer"
            John "Vamos só entrar antes que eu fique maluco"
            scene bg delegacia dentro
            show halfblack
            show john ex at left
            John "Você pelo menos se lembra onde fica a sala do seu pai?"
            show nate n at right
            Nathan "Se eu não me engano, é nessa porta aqui..."
            jump saladopai
        "Usar a ventilação" if "chave" not in inventory_items:
            $ foisus += 1
            "Eu me aproximo da ventilação, estando lá, percebo que a tampa da ventilação estava meio solta, com pouca força ela se solta"
            show nate s
            Nathan "Isso soltou muito mais fácil do que deveria"
            show john ex
            John "Não sei do que você tá reclamando, pela ventilação a gente consegue chegar direto na sala do seu pai, vamos logo!"
            jump saladopai

label delegaciasemcamilla: #Você invade a delegacia sem a camilla - Dia 2
    "Decidi tirar um cochilo durante a tarde para não ter a chance de desmaiar de sono durante minha invasão."
    show bg quarto noite with dissolve
    show nate n at left
    Nathan "Você está pronto?"
    show john n at right
    John "Nasci pronto."
    Nathan "Ótimo, vamos fazer isso."
    "Eu abri a janela e senti o vento frio da noite. Com muito nervosismo, segui correndo para a delegacia mais uma vez."
    show bg delegacia frente dia noite with dissolve
    show nate s2
    Nathan "Eu nunca fiz algo assim antes."
    Nathan "John, você tem cara de que cometeria um crime. Como eu faço pra entrar?"
    show john b at right
    John "Como assim eu tenho cara de que cometeria um crime?"
    John "Não sei, tenta quebrar o cadeado ali ou aquela ventilação na parede da porta, você parece caber."
    show nate f 
    Nathan "Eu sabia que podia contar com você."
    menu:
        "Quebrar o cadeado":
            "Eu me aproximo da porta, pego uma pedra e tento bater no cadeado."
            "No momento em que eu acerto o cadeado com a pedra, o cadeado cai, quebrado."
            show nate s
            Nathan "Eu me sinto mal por fazer isso."
            John "Vamos só entrar antes que você desista. Só de você quebrar esse cadeado não tem mais volta."
            scene bg delegacia dentro
            show halfblack
            show john ex at right
            John "Você pelo menos se lembra onde fica a sala do seu pai?"
            show nate n at left
            Nathan "Se eu não me engano, é nessa porta aqui."
            jump saladopai
        "Usar a ventilação":
            "Eu me aproximo da ventilação, estando lá, percebo que a tampa da ventilação estava meio solta, com um pouco de força ela se solta."
            show nate n
            Nathan "Isso soltou muito mais fácil do que deveria."
            show john n
            John "Não sei do que você tá reclamando, pela ventilação a gente consegue chegar direto na sala do seu pai, vamos logo!"
            jump saladopai

label saladopai: #Você invade a delegacia e vai para a sala do seu pai - Dia 2
    show bg sala do pai escuro with dissolve
    scene bg sala do pai escuro
    show john n at right 
    John "Eu não sabia que a sala do seu pai tinha tantos armários."
    show nate n at left
    Nathan "Nem eu lembrava. Me pergunto onde devo começar a procurar..."
    jump saladopaiprocura
    
label saladopaiprocura: #Voce procura os arquivos na sala do seu pai - Dia 2
    menu:
        "Mesa":
            show john n at right
            Nathan "Há um livro escrito ''Manual da polícia de como destrancar cofres e fechaduras'', mas acho que não seria útil agora."
            $ procuramesapai += 1
            hide john
            jump saladopaiprocura
        "Escrivaninha" if procuramesapai >= 1:
            show nate n at left
            Nathan "Aqui está cheio de arquivos, mas nenhum que a gente precise."
            $ procuraescrivaninhapai += 1
            hide nate
            jump saladopaiprocura
        "Gavetas" if procuraescrivaninhapai >= 1:
            $ procuragavetaspai += 1
            "Eu faço força para tentar abrir as gavetas."
            Nathan "Estão emperradas. Não vamos achar nada aqui."
            jump saladopaiprocura
        "Armário" if procuragavetaspai >= 1:
            $ inventory_items.append("arquivos")
            John "Nathan, por acaso o que você está procurando é isso aqui? Não tem nenhum nome escrito nele."
            Nathan "Estranho... Mas eu acho que é sim. Vamos levar e sair daqui antes que alguém nos veja."
            $ renpy.notify("Você pegou os arquivos!")
            jump quartodia21

label quartodia21: #voce volta para casa e encerra o dia 2 - Dia 2
    "Saímos pelo mesmo caminho que entramos, com sorte não vimos ninguém na rua."
    show bg quarto noite with dissolve
    scene bg quarto noite
    show halfblack
    "Após entrar no meu quarto pela janela, jogo os arquivos na minha mesa."
    show nate n at left
    Nathan "Será que eu devia checar esses arquivos hoje? Já está bem tarde..."
    Nathan "Posso ver isso amanhã com certeza."
    "Guardo os arquivos na gaveta da minha mesa, espero que ninguém mexa neles enquanto eu durmo."
    show black with fade
    "Enquanto eu dormia, John e Camilla tiveram uma conversa."
    scene bg quarto noite
    show halfblack
    show camilla t at right
    Camilla "John, vem aqui um minutinho."
    hide camilla
    show john b2 at right
    John "Ah, lá vem você de novo. O que foi agora?"
    hide john
    show camilla n at right
    Camilla "Eu estava pensando..."
    hide camilla
    show john ex at right
    John "Ah, então agora você pensa também?"
    hide john
    show camilla b at right
    Camilla "Não começa. Eu estava pensando em algo importante, sério."
    hide camilla
    show john n at right
    John "Tá bom, foi mal. No que você tá pensando?"
    hide john
    show camilla n at right
    Camilla "E se a gente se metesse na investigação do Nathan? Acho que ele tá precisando de uma mãozinha."
    hide camilla
    show john n at right
    John "Nuh uh."
    hide john
    show camilla b at right
    Camilla "Como assim nuh uh?"
    Camilla "Você tava ai todo animado pra ajudar ele a invadir a delegacia agora."
    hide camilla
    show john b at right
    John "Pode até parecer que não, mas eu também me preocupo com o Nathan e você sabe o quanto as pessoas já tratam ele como maluco, não quero que a gente acabe piorando a situação."
    hide john
    show camilla f at right
    Camilla "Nossa, então você tem um coração?"
    show camilla n
    Camilla "Mas, se formos bons o suficiente, isso pode ser bom pra ele! E também, a gente meio que cometeu um crime já hoje mais cedo então..."
    hide camilla
    show john b2 at right
    John "É..."
    hide john
    show camilla n at right
    Camilla "E então...? O que você diz?"
    hide camilla
    show john b2 at right
    John "Eu não tenho muita escolha, tenho?"
    hide john
    show camilla f at right
    Camilla "Não!"
    hide camilla
    show john n2 at right
    John "Tá bom, a gente pode ajudar o Nathan sim."
    hide john
    show camilla f at right
    Camilla "Eba!"
    hide camilla
    "O tempo passa..."
    jump actualday2

#BARRACO AQUI EM BAIXO
label actualday2:
    show bg quarto dia with dissolve
    scene bg quarto dia
    show halfblack
    "{i}Toc toc toc{/i}"
    show pai f at right
    Pai "Nathan? Você está já está de pé?"
    
    show nate s at left
    if brigacompai >= 1:
        menu:
            "Continuar a discussão do outro dia ":
                #FALTAM AS EXPRESSOES
                show nate n
                Nathan "Tô... eu acho, não dormi muito bem."
                show pai n
                Pai "Desculpa por anteontem. Eu sei que tava estressado e ando sendo fechado demais. Não é desculpa para o meu comportamento, mas eu estava passando por um momento estressante e acabei descontando em você. Sinto muito."
                show nate b
                Nathan "O problema não é esse, é que você não me respeita nunca, sempre me diminuindo e me tratando mal sem nenhum motivo"
                Nathan "Queria que você tentasse me entender um pouco mais antes de julgar em tudo que eu faço!"
                show pai s
                Pai "..."
                Pai "Desculpe Nathan, acho que devíamos conversar mais sobre esse tipo de coisa, eu não sei como me conectar com você as vezes"
                Pai "Esse é o meu jeito de tentar fazer você ver que tem que ser mais responsável com algumas coisas e pensar um pouco no que deve fazer com a sua vida de agora em diante"
                hide pai
                show mae b at right
                Mãe "Vocês dois estão discutindo de novo?"
                show nate ns
                Nathan "Dessa vez não mãe, acho que finalmente estamos tentando entender um ao outro na verdade."
                show mae f
                Mãe "Que bom! ainda bem que estão se entendendo melhor, fico muito feliz com isso"
                "Eu e meu pai continuamos a conversar por um tempo até que ele sai para trabalhar"
            "Não continuar a discussão do outro dia":
                Nathan "Tô... eu acho, não dormi muito bem."
                hide black
                show pai s at right
                Pai "Bom dia, filho. Desculpa por anteontem. Eu sei que fui estressado e fechado demais. Não é desculpa para o meu comportamento, mas eu estava passando por estressado e acabei descontando em você. Sinto muito."
                show nate ns at left
                Nathan "Foi a mãe que fez você se desculpar, não foi?"
                show pai s2
                Pai "Não, claro que não."
                show bg quarto dia with hpunch
                show halfblack with dissolve
                Mãe "Foi sim!!!"
                "Minha mãe grita da cozinha"
                Pai "B-bom, eu vou indo pro trabalho, se você precisar de alguma coisa, pode falar comigo, beleza? É isso que eu queria dizer."
                show nate f
                Nathan "Tudo bem, obrigado."
                hide pai

    "Assim que meu pai sai da sala, eu pego os arquivos que antes peguei na sala dele e começo a analisá-los."
    show nate n
    Nathan "Estranho, eu não vejo nenhuma foto nesse documento, apenas o histórico criminal desse cara. Será que ele chegou lá antes?"
    Nathan "Acho que isso explica a entrada que eu usei estar quebrada... Será que a biblioteca tem algum arquivo do caso? Posso tentar pegar uma versão mais completa por lá."
    "Me levanto, guardo os arquivos na minha mochila novamente e vou à biblioteca."        
    jump biblioteca

label biblioteca:
    show bg biblioteca fora dia with dissolve
    scene bg biblioteca fora dia
    show halfblack
    "Esta é a biblioteca da cidade. Não venho aqui desde pequeno; costumava ser um lugar bem cheio, mas hoje em dia só tem um funcionário já que é tão vazia."
    show bg biblioteca dentro dia with dissolve
    scene bg biblioteca dentro dia
    show halfblack 
    show joseph f at right
    dJoseph "Bom dia! Posso te ajudar em algo, jovem?"
    show nate ns at left
    Nathan "Na verdade, eu só estava procurando uma área de estudo ou algo do tipo. Pode me ajudar com isso?"
    dJoseph "Você pode usar aquela mesa atrás da prateleira à sua direita, tudo bem?"
    Joseph "Se precisar de alguma coisa, me chamo Joseph."
    "Eu me sentei na mesa que o moço me indicou e comecei a ler os arquivos novamente."
    hide nate 
    hide joseph
    hide halfblack
    pause(2.0)
    show halfblack with vpunch
    dErika "BOO!"
    show nate s2 at left with vpunch
    Nathan "AHHH!"
    Nathan "Ah, é só você, Erika. Que susto."
    show erika n at right
    Erika "O que você está lendo?"
    "Ela disse colocando as mãos nos meus ombros."
    show nate n
    Nathan "Estou lendo alguns dos arquivos sobre o roubo recente. Queria tentar resolver isso."
    show erika s
    Nathan "Por que você não me contou que assaltaram sua casa?"
    show erika t
    Erika "Desculpa, não queria te preocupar com isso, sei que já tem muita coisa passando na sua cabeça, principalmente com relação ao seu relacionamento com seu pai."
    Erika "Você não acha que ta se arriscando demais se metendo nisso? Acho meio impossível resolver um caso da polícia inteiro sozinho."
    Nathan "Não consigo confiar que meu pai vai conseguir fazer alguma coisa a respeito. Se esperar por ele talvez você e os meninos nunca vejam suas coisas outra vez!"
    show erika s2
    Erika "... acho que entendi. Bom, se conseguir alguma coisa, pode me procurar, viu?"
    show nate f
    Nathan "Tudo bem, eu te chamo se precisar, sim."
    hide erika
    show nate n
    Nathan "..."
    Nathan "... ..."
    Nathan "... ... ..."
    Nathan "Não parece que isso vai dar em algum lugar..."
    Nathan "Acho que eu devia tirar uma cópia dos arquivos, só por precaução."
    "Me aproximo da antiga impressora da biblioteca, ela estava meio empoeirada mas ainda funcionava bem, então tirei uma cópia de todos os arquivos."
    $ inventory_items.append("cópia arquivos")
    $ renpy.notify("Você agora tem uma cópia dos arquivos")
    Nathan "Agora eu deveria..."
    menu:
        "Continuar procurando sozinho":
            show nate n
            Nathan "Continuar sozinho não ia causar nenhum problema, né? Tenho certeza disso. Além do mais, fazer esse trabalho é mais fácil só."
            "Volto a me concentrar no papel."
            Nathan "..."
            Nathan "...?"
            Nathan "Espera aí, o que é isso?"
            Nathan "Os nomes não estão rasgados, eles só estão meio... borrados?"
            "Eu não percebi na hora, mas por não ter dormido direito, eu estava à beira de um desmaio."
            Nathan "E se eu tentar fazer isso aqu—{w=1.5}{nw}"
            show halfblack with vpunch
            hide nate
            jump conversabibliotecario
        "Ligar para Erika pedindo ajuda":
            $ saiucomerika +=1
            show nate s
            Nathan "Sei que ela acabou de sair, mas eu estou precisando de ajuda de verdade."
            "{i}Trim trim{/i}"
            show nate ns
            Nathan "Erika, preciso falar com você. Sei que acabou de sair, mas eu preciso da sua ajuda."
            show erika n2 at right
            Erika "Oi, Nathan. Encontrou alguma coisa?" 
            Nathan "Oi,não na verdade, você acha que consegue me encontrar do lado de fora da biblioteca para conversarmos sobre isso? Não sei muito pra onde ir a partir daqui"
            Erika "Está bom, já já estou chegando aí. Me dá uns 15 minutinhos, não estou muito longe."
            "Antes de sair percebo que o bibliotecário estava observando de longe os arquivos cima da mesa, mas não dou muita atenção e vou me encontrar com Erika"
            hide nate
            hide erika 
            jump conversaerikadia2

label conversaerikadia2:
    show bg biblioteca fora tarde with dissolve
    scene bg biblioteca fora tarde
    show halfblack
    show erika n at right
    Erika "Oiê, cheguei. Do que você queria falar?"
    show nate s at left
    Nathan "Esses arquivos parecem ter algo importante, {i}o dono ficou me seguindo por aí enquanto eu lia{/i}, mas eu não consigo decifrar. Precisava de sua ajuda."
    show erika s
    Erika "Antes de qualquer coisa, o que é aquilo ali?"
    "Ela disse apontando para uma rachadura na parede que eu não fazia ideia que existia."
    Nathan "Que estranho aquele brilho, não parece ser o sol naquela rachadura." 
    Erika "A biblioteca não é tão velha para ter uma rachadura desse jeito, e ainda tem umas pedrinhas no chão, parece ser recente."
    Nathan "Será que tem algo aí?"
    menu:
        "Investigar rachadura":
            "Eu me aproximei da rachadura e tentei ver o que tinha lá dentro. Parecia algum tipo de pedrinha brilhante. Assim que eu puxei essa pedrinha brilhante para fora da rachadura..."
            show bg biblioteca fora tarde with hpunch
            show halfblack
            Nathan "AS ALIANÇAS??"
            $ inventory_items.append("aliança")
            $ renpy.notify("Você recuperou as alianças!")
            $ pegaranel += 1
            Nathan "Eu não acredito que achei isso aqui, mas por que aqui?"
            show bg biblioteca fora tarde with hpunch
            show halfblack
            Erika "O QUE, COMO ASSIM?"
            show nate n
            Nathan "Erika, acho que vou precisar de ajuda para investigar essas coisas. Sozinho, tenho uma chance menor de encontrar pistas ou até arquivos novos."
            Erika "Não sei, Nathan, talvez seja muito arriscado. Não queria me meter tão a fundo nos assuntos do seu pai."
            show nate ns
            Nathan "Eu sei que pode ser um risco, porque eu estou te envolvendo nisso. Prometo que nada vai cair em você."
            Erika "Eu também quero recuperar minhas coisas e ajudar nossos amigos, mas preciso de um tempo para pensar sobre isso. É uma decisão séria e envolve riscos. Vou refletir e conversaremos novamente em breve, está bem?"
            Nathan "Tudo bem, espero que pense bem nisso. A gente se vê amanhã, beleza? Preciso investigar mais."
            show erika n2
            Erika "Tchau tchau, Nate!"
            jump ruadavid
        "Não quero incomodar mais o bibliotecário":
            show nate n at left
            Nathan "Deve ser só uma pedrinha brilhante, nada de mais."
            Erika "Eu vou dar uma olhada, só pra ter certeza."
            hide erika
            "Ela se aproxima da rachadura, e logo depois volta, sem nada em mãos."
            show erika s at right
            Erika "É, não tinha nada la mesmo"
            Nathan "A gente se vê amanhã, beleza? Preciso investigar mais."
            show erika n2
            Erika "Tchau tchau, Nate!"
            hide nate 
            hide erika
            jump ruadavid

label conversabibliotecario:
    "Eu acordei mais tarde com o bibliotecário Joseph me dando alguns tapinhas nas costas."
    show joseph s at right
    Joseph "Licença jovem, você está bem? E isso, por acaso, são documentos policiais?"
    menu:
        "Resposta mais rude":
            show nate s at left
            Nathan "Não, por que eu teria uma coisa dessas comigo? Isso são só contas-"
            Joseph "Não, mas aquilo ali é um selo policial, e até onde eu sei, você precisa de permissão minha para ler um desses."
            "Assim que ele falou isso, senti um frio na espinha e uma sensação de urgência. Assim que percebi, estava correndo com os arquivos na mão para fora da biblioteca."
            Joseph "Espera, garoto!{w=1.5}{nw}"
            hide nate 
            hide joseph
            jump rachadura1
        "Resposta Ansiosa":
            show nate s2 at left
            Nathan "N-não, claro que não. O que um civil como eu estaria fazendo com casos policiais, né?"
            Joseph "Desculpa, mas eu sei muito bem uma pasta confidencial quando eu vejo uma."
            Nathan "Desculpa, mas eu tenho que ir."
            Joseph "Espera-"
            "Levantei de minha mesa e saí andando, fingindo estar calmo quando estava morrendo de pânico."
            hide nate 
            hide joseph
            jump rachadura1

label rachadura1:
    show bg biblioteca fora tarde with vpunch
    scene bg biblioteca fora tarde
    show halfblack
    "Quando saí da biblioteca, olhei para trás só para ter certeza de que o bibliotecário não estava me seguindo, e foi aí que eu percebi um brilho próximo à porta."
    show nate n at left
    Nathan "Estranho, esse brilhinho não estava aqui quando eu entrei."
    
    menu:
        "Investigar rachadura":
            Nathan "O Joseph vai demorar um pouco pra me alcançar, acho que não tem problema se eu tentar colocar minha mão aqui."
            "Eu me aproximei da rachadura e tentei ver o que tinha lá dentro. Parecia algum tipo de pedrinha brilhante. Assim que eu puxei essa pedrinha brilhante para fora da rachadura..."
            show bg biblioteca fora tarde with hpunch
            show nate s
            Nathan "AS ALIANÇAS??"
            $ inventory_items.append("aliança")
            $ renpy.notify("Você recuperou as alianças!")
            $ pegaranel += 1
            Nathan "Eu não acredito que eu achei isso aqui, mas por que aqui? Bom, isso é coisa do eu futuro pensar. Por agora, eu vou para casa."
            jump ruadavid
        "Correr pra casa":
            show nate s
            Nathan "Deve ser só uma pedrinha brilhante, e além disso, o bibliotecário deve estar vindo atrás de mim ainda."
            show black with dissolve
            jump ruadavid


label ruadavid:
    show bg rua tarde with dissolve
    scene bg rua tarde
    show halfblack
    "Enquanto estava indo pra casa, me encontrei com o David."
    show david f at right
    David "Perito David se apresentando para o serviço senhor filho do delegado, Senhor!"
    show nate n at left
    Nathan "..."
    show nate f at left
    Nathan "David!... Oi!"
    show david n
    David "Precisa de ajuda com alguma coisa, Senhor?"
    show nate ns
    Nathan "Acredito que não, só estou indo pra casa no momento, mas obrigado!"
    hide david 
    show camilla n at right
    Camilla "Nathan, você podia pedir pra ele devolver os arquivos originais do caso para o escritório do seu pai."
    Camilla "Não acho que ele seja muito confiavel pra isso, mas não devolver pode ser ruim para o seu pai."
    hide camilla
    show john ex at right
    John "Eu não vou muito com a cara dele não, mas a Camilla pode estar certa."
    hide john 
    show david f at right
    David "Bom, já vou indo então, Senhor!"
    menu:
        "Espera! (Devolver os arquivos)":
            show nate s2
            Nathan "Espera!"
            show david n 
            David "O que precisa, Senhor?"
            show nate n
            Nathan "Você poderia deixar esses arquivos no armário da sala do meu pai? Mas ele não pode saber de jeito nenhum!"
            show david t
            David "Hmm, um pouco suspeito senhor! Mas posso sim."
            show nate f
            Nathan "Perfeito! Aqui estão os arquivos."
            $ inventory_items.remove("arquivos")
            $ renpy.notify("Você devolveu os arquivos")
            $ moralfinalruim += 1
            pause 0.5
            show david n
            David "Posso perguntar o motivo de você ter esses arquivos, senhor?"
            show nate b
            Nathan "Não."
            show david f
            David "Senhor, sim, senhor!"
        "Não confio nele, prefiro manter os arquivos comigo por agora.":
            show nate n
            Nathan "Nos vemos outra hora então, David."
            show david n
            David "Até mais ver, senhor!"
            hide nate
            hide david 
    jump casadia2
    # if saiucomerika >=1:
    #     jump casadia2alt
    # else:
    #     jump casadia2
            

label casadia2:
    show black with dissolve
    scene bg casa fora noite with dissolve
    show halfblack
    "Chegando em casa, vi meu pai abalado por algo."
    show nate n at left
    Nathan "Oi, pai, você está bem?"
    show pai n at right
    Pai "São só coisas do trabalho. Você não precisa se preocupar com isso."
    Nathan "Ah, fala ai, que mal isso poderia causar?"
    Pai "...Certo, acho que posso falar sobre isso."
    Pai "Parece que alguém roubou os arquivos do caso dos assaltos que tem ocorrido recentemente, sem eles eu não consigo progredir muito na investigação."
    Pai "Isso tem cara de coisa do David, ele só faz besteira, desse jeito, mais gente pode acabar se prejudicando..."
    if "arquivos" in inventory_items:
        menu:
            "Admitir que pegou os arquivos":
                show nate n
                Nathan "Pai... Na verdade preciso te contar algo..."
                show pai n2
                Pai "O que?"
                show nate s2
                Nathan "Fui eu quem pegou os arquivos... Me desculpe, estava tentando investigar por conta própria para ajudar meus amigos."
                show pai b
                Pai "VOCÊ O QUÊ??? VOCÊ FICOU MALUCO? TEM NOÇÃO DO QUANTO ISSO ATRAPALHOU NA INVESTIGAÇÃO?"
                show nate ch
                Nathan "..."
                hide pai 
                show mae b at right
                Mãe "Calma Fábio, Ele não fez isso de má intenção."
                Mãe "Mas isso realmente foi uma decisão muito idiota Nathan! Você não devia atrapalhar o trabalho do seu pai."
                show nate ex
                Nathan "Foi mal... Vou para o meu quarto..."

            "Não falar nada sobre os arquivos e mante-los com você":
                Nathan "Entendo... Espero que consiga pegar esse cara logo"
    "Eu subo em silêncio para o meu quarto."
    show bg quarto noite with dissolve
    scene bg quarto noite
    show halfblack
    show nate n at left
    Nathan "Vou só fazer uma coisa, acho que investigar assim pode ajudar"
    show bg quarto com pistas noite with dissolve
    Nathan "Pronto, muito melhor."
    scene bg quarto com pistas noite
    pause
    show halfblack
    if "aliança" in inventory_items:
        show camilla n at right
        Camilla "Ei, vocês não acharam estranho o Joseph ficar nervoso quando viu os arquivos?"
        hide camilla
        show john n at right 
        John "Não reparei muito no homem em sí, estava focado em pensar nos arquivos."
        hide john
        show camilla b at right
        Camilla "Claro que não prestou, você nunca presta atenção."
        hide camilla 
        show john b at right
        John "Olha só sua-"
        show nate b at left
        Nathan "Não é hora de discutir, vamos manter o foco. Realmente, aquele homem ficou um pouco receoso com as coisas, mas pode ser apenas uma coincidência. Pode ser que o verdadeiro culpado tenha feito isso para tirar a sua suspeita."
        show john ex at right
        John "O Nathan tem razão nisso. De tudo que vimos sobre esse ladrão, ele parece ser muito inteligente. Tem uma chance alta de ter planejado isso."
        show nate n at left
        Nathan "Não tem como decretarmos nada ainda. Tem muitas pessoas por aqui, qualquer um pode ser culpado. É muita coisa pra lidar sozinho."
        show nate ns
        Nathan "O que vocês acham de eu tentar chamar a Erika pra me ajudar?"
        hide john
        show camilla f at right
        Camilla "Eu acho que pode ser uma boa ideia. Ela pode ser meio estabanada, mas ela sempre te ajudou quando precisava."
        hide camilla 
        show john n2 at right
        John "Pode ser paranoia minha, mas ele parecia estar te rondando enquanto você estava lendo o livro. Não sei se isso é normal. Talvez valha a pena pedir pra ele um álibi do dia do crime, sabe?"
        Nathan "Vocês dois têm um bom ponto. Vou tentar ver isso amanhã mesmo. Muito obrigado por estarem me ajudando."
        show black with dissolve
        jump startday3
    if "aliança" not in inventory_items:
        show nate s at left
        Nathan "Acho que isso não vai levar a nada. Esses arquivos, tem muitas coisas que foram perdidas. Provavelmente, as mais importantes foram perdidas."
        show camilla t at right 
        Camilla "Sabemos que você quer ajudar, mas você precisa manter a calma. Não se joga tão de cabeça assim."
        show john n at right
        hide camilla
        John "Você gosta de ajudar seus amigos, mas você precisa pensar em você. Pode correr vários riscos se investigar de forma imprudente." 
        show nate ns
        Nathan "Vocês têm razão. Estou realmente correndo alguns riscos. Vou tentar pensar um pouco mais antes de sair tomando decisões."
        Nathan "Melhor eu ir descansar. Amanhã eu vou tentar descobrir mais sobre as coisas. Tentar falar com alguém sobre esses casos."
        hide john 
        show camilla t at right
        Camilla "Já pensou em falar com a Erika sobre? Ela pode te ajudar. Você pode tentar falar com ela durante a manhã."
        John "Queria tentar manter esse caso mais baixo, mas eu penso que a Camilla tem razão. Você pode tentar falar com ela mesmo."
        Nathan "Entendi. De qualquer forma, obrigado por estarem me ajudando com o que vocês podem."
        show black with dissolve
        jump startday3


# label casadia2alt:
#     hide nate
#     hide david
#     show bg quarto noite with dissolve
#     scene bg quarto noite
#     show halfblack
#     show pai b at right
#     Pai "Você que fez isso, né? Você roubou os meus arquivos. Eu vi nas câmeras você invadindo a minha sala e pegando os arquivos ontem."
#     hide pai 
#     show mae b at right
#     Mãe "Pare com isso Fábio, não tem como ter sido o Nathan se eles estavam na delegacia."
#     Mãe "Se os seus arquivos sumiram provavelmente foi porque você não os guardou direito. Não tente culpar o Nathan por causa disso."
#     hide mae
#     menu:
#             "Admitir que pegou os arquivos":
#                 show nate s at left
#                 Nathan "Pai... Na verdade preciso te contar algo..."
#                 show pai n2 at right
#                 Pai "O que?"
#                 show nate s2
#                 Nathan "Fui eu quem pegou os arquivos... Me desculpe, estava tentando investigar por conta própria para ajudar meus amigos."
#                 show pai b
#                 Pai "VOCÊ O QUÊ??? VOCÊ FICOU MALUCO? TEM NOÇÃO DO QUANTO ISSO ATRAPALHOU NA INVESTIGAÇÃO?"
#                 show nate ch
#                 Nathan "..."
#                 hide pai 
#                 show mae b at right
#                 Mãe "Calma Fábio, Ele não fez isso de má intenção."
#                 Mãe "Mas isso realmente foi uma decisão muito idiota Nathan! Você não devia atrapalhar o trabalho do seu pai."
#                 show nate ch
#                 Nathan "Foi mal... Vou para o meu quarto..."
#             "Mentir sobre os arquivos e mante-los com você":
#                 show nate b at left
#                 Nathan "Você tá doido? Como eu ia roubar os seus arquivos? Não vem tentar me culpar sem motivos!"
#                 show pai s at right
#                 Pai "Você tem razão... Desculpe, acho que ando muito estressado."
#                 show nate n 
#                 "Essa foi por pouco.."
                
#     "Eu subo em silêncio para o meu quarto."

#     show mae n at right
#     "Minha mãe então me puxou de canto para conversar."
#     Mãe "Nathan, eu sei que seu pai está chateado agora, mas você precisa entender que ele está preocupado com a segurança dos arquivos."
#     Mãe "Talvez seja melhor conversarmos sobre isso mais tarde, quando as coisas estiverem mais calmas."
#     hide nate
#     hide mae
#     Nathan "Vou aproveitar que peguei uma cópia de tudo, e colocar eles ali, vai me ajudar bastante."
#     show bg quarto com pistas noite with dissolve
#     scene bg quarto com pistas noite
#     if "aliança" in inventory_items:
#         show camilla n at right
#         Camilla "Ei, vocês não acharam estranho o Joseph ficar nervoso quando viu os arquivos?"
#         hide camilla
#         show john n at right 
#         John "Não reparei muito no homem em si, estava focado em pensar nos arquivos."
#         hide john
#         show camilla b at right
#         Camilla "Claro que não prestou, você nunca presta atenção."
#         hide camilla 
#         show john b at right
#         John "Olha só sua-"
#         show nate b at left
#         Nathan "Não é hora de discutir, vamos manter o foco. Realmente, aquele homem ficou um pouco receoso com as coisas, mas pode ser apenas uma coincidência. Pode ser que o verdadeiro culpado tenha feito isso para tirar a sua suspeita."
#         show john ex at right
#         John "O Nathan tem razão nisso. De tudo que vimos sobre esse ladrão, ele parece ser muito inteligente. Tem uma chance alta de ter planejado isso."
#         show nate n at left
#         Nathan "Não tem como decretarmos nada ainda. Tem muitas pessoas por aqui, qualquer um pode ser culpado. É muita coisa pra lidar sozinho."
#         show nate ns
#         Nathan "O que vocês acham de eu tentar chamar a Erika pra me ajudar?"
#         hide john 
#         show camilla f at right
#         Camilla "Eu acho que pode ser uma boa ideia. Ela pode ser meio estabanada, mas ela sempre te ajudou quando precisava."
#         hide camilla 
#         show john n2 at right
#         John "Pode ser paranoia minha, mas ele parecia estar te rondando enquanto você estava lendo o livro. Não sei se isso é normal. Talvez valha a pena pedir pra ele um álibi do dia do crime, sabe?"
#         Nathan "Vocês dois têm um bom ponto. Vou tentar ver isso amanhã mesmo. Muito obrigado por estarem me ajudando."
#         show black with dissolve
#         jump startday3alt
#     if "aliança" not in inventory_items:
#         show nate s at left
#         Nathan "Acho que isso não vai levar a nada. Esses arquivos, tem muitas coisas que foram perdidas. Provavelmente, as mais importantes foram perdidas."
#         show camilla t at right 
#         Camilla "Sabemos que você quer ajudar, mas você precisa manter a calma. Não se joga tão de cabeça assim."
#         show john n at right
#         hide camilla
#         John "Você gosta de ajudar seus amigos, mas você precisa pensar em você. Pode correr vários riscos se investigar de forma imprudente." 
#         show nate ns
#         Nathan "Vocês têm razão. Estou realmente correndo alguns riscos. Vou tentar pensar um pouco mais antes de sair tomando decisões."
#         Nathan "Melhor eu ir descansar. Amanhã eu vou tentar descobrir mais sobre as coisas. Tentar falar com alguém sobre esses casos."
#         hide john 
#         show camilla t at right
#         Camilla "Já pensou em falar com a Erika sobre? Ela pode te ajudar. Você pode tentar falar com ela durante a manhã."
#         John "Queria tentar manter esse caso mais baixo, mas eu penso que a Camilla tem razão. Você pode tentar falar com ela mesmo."
#         Nathan "Entendi. De qualquer forma, obrigado por estarem me ajudando com o que vocês podem."
#         show black with dissolve
#         jump startday3alt