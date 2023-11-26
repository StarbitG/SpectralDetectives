label startday3:
    show bg quarto com pistas dia with dissolve
    scene bg quarto com pistas dia
    show halfblack
    "Quando o dia amanheceu, a primeira coisa que fiz foi ligar para Erika, eu precisava da ajuda dela afinal."
    "{i}trim trim{/i}"
    show erika n at right
    Erika "Bom dia, Nathan! Tem alguma novidade?"
    show nate n at left
    Nathan "Bom dia, Erika. Na verdade, tenho sim. Muitas coisas aconteceram ontem. Eu estava pensando... Será que você poderia me encontrar para conversarmos? Eu preciso da sua ajuda."
    hide erika
    show john n at right
    #123456789
    John "Não acredito, ele vai chamá-la pra sair?"
    hide john
    show camilla b at right
    Camilla "Shh, cala boca John, você tá atrapalhando."
    hide camilla
    show john f at right
    John "Parei."
    hide john
    show erika n2 at right
    Erika "Claro! Onde você vai?"
    Nathan "A gente pode se encontrar na rua mesmo. Eu saio de casa em no máximo 5 minutos e te espero por lá, pode ser?"
    show erika n
    Erika "Ótimo, chego lá rapidinho. Até logo!"
    "Terminando a ligação, eu saí correndo de casa."
    show bg rua dia with dissolve
    scene bg rua dia
    show halfblack
    show erika n at right
    Erika "Oiee, o que você tá precisando?"
    show nate n at left
    Nathan "Bem, você se lembra que eu estava estudando sobre o caso, né? Por mais que eu não tenha nada a ver, então ontem eu estava refletindo algumas ideias e levantei algumas suspeitas. Acho que o bibliotecário pode estar envolvido nos roubos."
    Nathan "Ele agiu de forma estranha quando me viu lendo o livro sobre os crimes."
    if "aliança" in inventory_items:
        Nathan "E, além disso, o anel roubado foi encontrado na porta da biblioteca. Ainda tenho que devolver pro Sebastian isso."
    Nathan "Parece que ele tem acesso aos arquivos e poderia manipular as coisas ao seu redor."
    Erika "Espera aí, e você descobriu tudo isso sozinho? Isso é bem impressionante na verdade. Talvez valha a pena investigar mais o bibliotecário e buscar um álibi para o dia do crime. Você então quer ajuda pra... falar com ele?"
    Nathan "Ontem ele já estava muito suspeito, olhando o que eu fazia. Então, prefiro que outra pessoa faça isso por mim. E aliás, podemos achar suas coisas nesse meio tempo também!"
    Erika "Hmmm... Até que isso não é uma má ideia... Vamos nos preparar para isso. O que você acha da gente conversar com os meninos antes? Eles talvez tenham visto a aparência do ladrão quando estavam fechando a loja."
    Nathan "Sim, precisamos buscar todas as pistas possíveis. Fico feliz que você tenha aceito ajudar tão fácil hahaha. Enfim, vamos lá!"
    jump lojaday3

label startday3alt:
    show bg quarto com pistas dia with dissolve
    scene bg quarto com pistas dia
    show halfblack
    if "aliança" in inventory_items:
        "{i}trim trim{/i}"
        show nate n at left
        Nathan "Alô?"
        show erika n at right
        Erika "Oi, Nathan! Desculpe por te ligar tão cedo, mas queria confirmar que eu vou te ajudar na investigação. Passei a noite pensando sobre isso, acho que isso pode dar certo."
        Nathan "Fico muito feliz que tenha aceitado!!! Deixa eu já te atualizar então. Acredito que o bibliotecário possa estar envolvido, mas preciso de mais provas antes de tirar conclusão."
        show erika s
        Erika "O bibliotecário? Mas ele é um carinha tão... normal."
        Nathan "Ele não gostou muito que eu trouxe o livro de crimes rasgado comigo, isso foi bem estranho da parte dele, e também, ele tem acesso aos arquivos criminais, o que impediria ele de apagar algum que o incriminasse, né."
        Erika "Até que é uma boa teoria. Mas não acho que ele faria algo assim, de qualquer forma, precisamos encontrar álibis, eu acho que podemos perguntar mais sobre a noite do crime pro Sebastian e o Lucas, o que pensa?."
        Nathan "Acho uma ótima ideia! Vamos fazer exatamente isso! Te encontro lá!"
        show erika n
        Erika "Até daqui a pouquinho!"
        jump lojaday3
    if "aliança" not in inventory_items:
        "Mais uma vez, eu acordei com os sons da minha porta batendo"
        show erika s at right
        Erika "Nathan! Precisamos conversar, agora."
        show nate s at left
        Nathan "Erika, o que aconteceu? Parece que algo sério está acontecendo."
        Erika "Passei a noite pensando sobre os roubos na cidade e sobre o seu envolvimento nisso. Cheguei a uma conclusão perturbadora. Eu ACHO que o bibliotecário possa estar diretamente envolvido."
        show nate n
        show erika n
        Nathan "Erika, você não pode ir por aí acusando os outros-"
        show erika s
        Erika "Antes que você fale ''Erika, você não pode sair por aí acusando os outros'', eu achei os anéis do Lucas e do Sebastian ontem naquela rachadura."
        Erika "Só não te contei porque eu queria entender o porquê eles estavam lá. Então, a partir de agora, eu vou te ajudar a investigar isso, okay? "
        show nate s
        Nathan "Primeiro: COMO ASSIM VOCÊ ACHOU AS ALIANÇAS? E segundo: por que elas estavam lá?"
        Erika "É, foi isso mesmo que você ouviu, e eu acho que estavam lá porque o ladrão é o bibliotecário, mas eu não tenho provas suficientes ainda, queria ir na loja perguntar algumas coisas para os meninos, você aceita?."
        show nate f
        Nathan "Obrigado, Erika. Sua ajuda significa muito para mim. E ir perguntar para os meninos sobre a noite do crime pode nos ajudar muito, vamos fazer isso."
        show erika n
        Erika "Ta bom, para de ser bobão e vamos logo"
        "E mais uma vez, ela me arrasta para outro lugar"
        jump lojaday3

label lojaday3:
    show bg mercado roubado dia with dissolve
    scene bg mercado roubado dia
    show halfblack
    "Chegando na loja, vemos apenas o Sebastian por lá, além da equipe de polícia, claro."
    show erika n at right
    Erika "Sebastian!! A gente pode falar com você rapidinho?"
    hide erika
    show seb c at right
    Sebastian "Erika, Nathan?"
    show nate n at left
    Nathan "Ué, cadê o Lucas? Vocês não estão sempre juntos?"
    Sebastian "Ah, ele? Não sai de casa desde o incidente, abalou muito ele. Eu vim aqui só pra ver como andava a operação, mas já estou de saída."
    hide seb
    show erika s at right
    Erika "Você tem só um tempinho? Queríamos tirar algumas dúvidas com você."
    hide erika
    show seb c at right
    Sebastian "Claro, não vejo o motivo para não ficar."
    hide seb
    show erika n at right
    Erika "Ótimo! Primeira coisa, o que você estava fazendo na hora do crime?"
    hide erika
    show seb n at right
    Sebastian "Eu tinha acabado de fechar a loja, então estava indo para casa."
    Nathan "E você por acaso viu algo estranho nesse meio tempo?"
    Sebastian "Agora que você diz, eu acho que vi alguém passando por aqui. Ele era meio alto, mas já estava escuro, então esse é o máximo que eu pude ver."
    show nate s 
    Nathan "Isso não ajuda tanto quanto a gente queria, mas já é alguma coisa. Se você achar mais alguma pista ou prova de quem fez isso, por favor, nos conte, beleza?"
    Sebastian "Tudo bem, digo sim."
    hide seb
    show erika s at right
    Erika "Nathan, acho que a gente podia ir de volta para a biblioteca. Talvez encontremos algo novo por lá dessa vez, é a melhor chance que temos no momento."
    
    if "aliança" in inventory_items:
        show nate n
        Nathan "Você pode ir na frente, eu já te alcanço."
        Erika "Tudo bem! Te vejo lá."
        menu:
            "Devolver a aliança":
                Nathan "Sebastian, eu tenho algo seu aqui comigo."
                hide erika
                show seb c at right
                Sebastian "Hm? Como assim?"
                Nathan "Lembra que você tinha me pedido para encontrar os seus anéis? Então, eu encontrei eles. Aqui, olha."
                $ inventory_items.remove("aliança")
                $ renpy.notify("Você devolveu as alianças")
                $ mostraranel += 1
                Sebastian "NATHAN, VOCÊ É UM ANJO. MUITO OBRIGADO, CARA."
                "Eu sinto o Sebastian quase quebrando minhas costelas com a força com a qual ele me abraçou."
                Nathan "Que nada, cara. Estamos aqui para isso. Bom, agora eu vou indo. Até depois, amigão."
            "Não devolver (Guardar como evidência)":
                Nathan "{i}Acho melhor guardar o anel como evidência, pode ser útil mais tarde{/i}"
                Nathan "É verdade, né? Bom, se cuida, Sebastian. A gente vai conseguir resolver isso alguma hora, não se preocupa."
                Sebastian "Boa sorte para vocês dois!"
        jump bibliotecaday3
    if "aliança" not in inventory_items:
        Nathan "É verdade, né? Bom, se cuida, Sebastian. A gente vai conseguir resolver isso alguma hora, não se preocupa."
        Sebastian "Boa sorte para vocês dois!"
    jump bibliotecaday3

label bibliotecaday3:
    show bg biblioteca fora dia with dissolve
    scene bg biblioteca fora dia
    show halfblack
    show erika s at right
    Erika "Bom, chegamos, vamos procurar lá dentro"
    hide erika 
    show bg biblioteca dentro dia with dissolve
    scene bg biblioteca dentro dia 
    show halfblack
    "Assim que entramos na biblioteca e começamos a vasculhar entre as prateleiras, tirando e colocando livros do lugar." 
    pause
    show bg biblioteca dentro tarde with dissolve
    "Até que acabamos derrubando alguns deles."
    hide halfblack 
    show bg biblioteca tarde with hpunch
    show halfblack
    "Assim que os livros caem, o bibliotecário joseph se aproxima de nós, aparentemente ele não sabia que estávamos por lá."
    show erika s2 at left with vpunch
    Erika "Ahh!{nw}{w=0.5}"
    hide erika
    show joseph f at right
    Joseph "Tudo bem por aqui? Posso ajudar vocês com alguma coisa, jovens?"
    show nate s at left
    Nathan "N-não, não precisa, obrigado."
    show joseph s
    Joseph "Tem certeza? você parece meio assustado, está tudo bem?"
    hide nate 
    show erika s at left
    Erika "Nós já vimos tudo o que precisavamos, obrigado, já estamos de saída"
    Joseph "Esperem!{nw}{w=2.0}"
    hide joseph
    hide nate 
    hide erika 
    show bg biblioteca fora tarde with dissolve
    scene bg biblioteca fora tarde 
    show halfblack
    show erika s at right
    Erika "Cara, que medo, achei que ele ia esfaquear a gente, sei lá."
    show nate s at left
    Nathan "Nem me fala, já a segunda vez que ele faz isso e eu saio correndo de lá, melhor tomarmos mais cuidado de agora em diante"
    Nathan "Mas consegui perceber uma coisa."
    show erika n
    Erika "O quê?"
    show nate n
    Nathan "Ele estava com a perna machucada e mancando."
    show erika t
    Erika "E o que isso tem a ver?"
    Nathan "O ladrão tem assaltado as lojas entrando pelas janelas, ele deve ter se cortado no vidro."
    show erika n2
    Erika "Realmente, faz sentido!"
    show erika n
    Erika "O que a gente faz agora?"
    Nathan "Acho que vou procurar alguém que possa nos ajudar"
    Erika "Certo, eu acho que vou pra casa então, ta ficando tarde, não gosto de sair a noite."
    Erika "Você devia ir pra casa também"
    show nate f
    Nathan "Tá tranquilo, posso pegar carona com meu pai depois alguém na delegacia deve saber de algo"
    show erika n2
    Erika "Tudo bem então, te vejo amanha nate!"
    hide nate
    hide erika
    jump delegaciaday3

label delegaciaday3:
    show bg delegacia frente dia tarde with dissolve
    scene bg delegacia frente dia tarde
    show halfblack
    "Antes de entrar na delegacia, john e camilla me abordam"
    show john n at right
    John "Cara, eu acho que você devia falar direto com seu pai, será que ele conseguiria entender o que você ta fazendo? Ele se desculpou afinal."
    show nate n at left
    hide john 
    Nathan "Não sei, não parece uma boa ideia..."
    show camilla n at right
    Camilla "Não confio tanto no seu pai não, você lembra daquela moça de verde? Achei ela legal, talvez seja melhor falar com ela."
    Nathan "A vivian?"
    show camilla f
    Camilla "É, ela mesmo."
    hide camilla
    hide nate
    menu:
        "Falar com a Vivian":
            Nathan "Talvez a Camilla tenha razão, vou tentar falar com ela."
            jump delegaciavivian   
        "Falar com seu Pai":
            Nathan "Talvez o John tenha razão dessa vez, vou tentar falar com ele."
            jump delegaciapai

label delegaciavivian:
    Nathan "{i}(Espero que aquele David não esteja por aqui, assim poderia falar com a Vivian com tranquilidade.){/i}"
    "Entrando no prédio me deparo com a Vivian na recepção e nenhum sinal de David"
    show bg delegacia dentro with dissolve
    scene bg delegacia dentro
    show halfblack
    show nate f at left
    Nathan "Com licença, você é a Vivian, certo?"
    show vivian f at right
    Vivian "Oii, você é o garoto daquele dia né? Precisa de alguma coisa, só peço que seja breve, preciso ir até a sala do Delegado discutir alguns assuntos."
    show nate ns
    Nathan "Vou ser breve, na verdade, acho que tenho algumas informações importantes para o caso."
    show vivian f2
    Vivian "Sério? Que bom! Desembuxa ai."
    
    if pegaranel >= 1:
        show nate n
        Nathan "Acho que sei quem está cometendo os crimes recentes."
        Nathan "Encontrei uma das alianças na entrada da biblioteca e o bibliotecario de lá estava com a perna mancando por conta de um corte que parece ter sido feito com vidro."
        Nathan "O nome dele é Joseph"
        show vivian s2
        Vivian "O Joseph?? impossível, eu conheço ele a anos, já até namoramos, ele nunca faria uma coisa dessas"
        Nathan "Eu estou com uma das alianças aqui, veja"
        show vivian n
        Vivian "hmm, isso é estranho, te garanto que ele não faria nada assim, deve ter sido um engano"
        if mostraranel >= 1:
            "Procuro a aliança no meu bolso, mas esqueci que já tinha entregado ela pro Sebastian"
            Nathan "Na verdade, eu tinha a alianças comigo, só que eu ja devolvi ela pro respectivo dono"
            show vivian b
            Vivian "Então você vem no meu trabalho, acusa alguém, e não me mostra prova nenhuma?"
            show nate s
            Nathan "Eu juro pra você que eu tinha a aliança comigo"
            Vivian "Olha garoto, somos policiais, não trabalhamos na base do ''eu acho''"
            
        else:
            "Pego a aliança no meu bolso e entrego para Vivian"
            $ inventory_items.remove("aliança")
            $ renpy.notify("Você entregou a aliança para a Vivian")
            show nate f
            Nathan "Veja, a aliança que encontrei na entrada da biblioteca."
            show vivian n
            Vivian "Tem certeza de que achou isso lá?"
            show nate ns
            Nathan "Sim, eu juro!"
            show vivian f
            Vivian "Vou ficar com ela então, quero questiona-lo pessoalmente"
            Nathan "Okay"
            $ vivianescolha += 1
            $ moralfinalbom += 1
    else:
        show nate n
        Nathan "Acredito que o culpado possa ser o bibliotecário, ele tem agido de forma estranha e estava mancando por um corte de vidro em sua perna"
        show vivian b
        Vivian "O Joseph?? impossível, eu conheço ele a anos, já até namoramos, ele nunca faria uma coisa dessas"
        Vivian "Olha, isso não serve como evidência, não posso fazer nada sem provas concretas, não trabalhamos com achismos e suspeitas infudamentadas"
        show nate s
        Nathan "Mas—" 
    "Antes que pudessemos concluir a conversa meu pai aparece na recepção" 

    
    
label delegaciapai:
    show bg sala do pai clara with dissolve 
    scene bg sala do pai clara
    show halfblack
    "Chego na sala do meu pai e aguardo um pouco, até que a Vivian entra na sala"
    show vivian f at right
    Vivian "Você não é aquele garoto do outro dia? O que faz aqui?"
    "Antes de poder responder meu pai entra na sala"
    hide vivian
    show pai s at right
    Pai "Nathan?"
    show nate s at left
    Nathan "Pai?"
    Pai "O que está fazendo aqui?"
    hide pai 
    show vivian s at right
    Vivian "''Filho?'' Você é filho do delegado Fábio? por que não me contou antes?"
    show nate n
    Nathan "Desculpe, não achei que fosse necessário falar sobre isso"
    show vivian n
    Vivian "Ele estava me passando informações sobre o caso dos assaltos recentes"
    hide vivian 
    show pai b at right
    Pai "Eu já não falei para você não se meter nos assuntos da polícia?"
    show nate s
    Nathan "Mas eu posso ajudar!"
    Pai "Não, você não pode! você só vai atrapalhar mais ainda a investigação!"
    Nathan "Mas—"
    show nate b
    Nathan "Ah quer saber, não tô com paciência pra discutir com você hoje, vou pra casa a pé mesmo"
    hide nate
    "Não estava afim de continuar a discussão com o meu pai então decido ir para casa e saio da delegacia"
    show vivian n at left
    Vivian "Se me permite senhor, acho que você ter sido um pouco duro demais, ele é um bom garoto, entendo sua preocupação mas você podia ter pego um pouco mais leve com ele."
    Pai "Se eu não agir dessa forma ele nunca vai aprender."
    hide pai 
    hide vivian
    show bg delegacia frente dia tarde with dissolve
    pause
    show bg delegacia frente dia noite with dissolve
    scene bg delegacia frente dia noite
    show halfblack
    "Do lado de fora da delegacia John e Camilla tentam me acalmar"   
    show nate b at left
    Nathan "Não entendo porque ele sempre faz isso. Estou de saco cheio dele ser sempre assim!"
    show camilla t at right
    Camilla "Nate... Tenta não levar isso pro coração, você sabe que no fundo ele te ama e só está preocupado com você, ele só não sabe como expressar isso"
    Nathan "Não, ele só acha que eu sou incapaz de fazer qualquer coisa sozinho, só isso!"
    hide camilla
    show john b at right
    John "Pô cara, acho que se ta viajando porque ta com raiva, tenta esfriar a cabeça um pouco"
    hide john 
    show camilla t at right
    Camilla "Ter que ouvir e concordar com o John é dificil, mas ele ta certo."
    Nathan "..."
    show nate n
    Nathan "Não quero mais falar sobre isso, só quero ir pra casa"
    show camilla n
    Camilla "Certo, qualquer coisa chama a gente, vamos estar aqui, ok?"
    hide camilla 
    hide nate 
    show bg rua noite with dissolve 
    scene bg rua noite
    show halfblack
    "Caminhando por não prestar atenção esbarro em alguma pessoa"
    show joseph d at center with vpunch
    Nathan "Desculp—"
    show joseph n at center with dissolve
    show joseph n at right
    Joseph "Desculpe, estou com um pouco de pressa."
    show joseph n at offscreenright with move
    show nate s2 at left
    Nathan "Aquele era o Joseph? Se ele está aqui fora significa que pode ter acontecido alguma coisa"
    show john n at right
    John "Você tá bem cara? Foi uma batida meio feia..."
    show nate s
    Nathan "Sim sim eu to bem, valeu por perguntar."
    hide john 
    show camilla n at right 
    Camilla "Que bom! Ah, parece que o joseph derrubou algo quando bateu em você agora."
    show nate n
    Nathan "Sério?"
    "Olho para a calçada para ver se realmente tem algo por ali"
    Nathan "O que é isso?"
    "Me abaixo e pego o objeto estranho"
    Nathan "Parece ser um jogo de chaves"
    $ inventory_items.append("chave")
    $ renpy.notify("Você pegou as chaves do Joseph")
    Nathan "Ei! você derrubou suas chaves!"
    "Ele saiu correndo e não me escutou."
    show camilla b 
    Camilla "Acho bom você nem pensar em devolver isso, afinal, ele é o único suspeito até agora."
    hide camilla
    show john n at right
    John "Ela tem razão, isso pode nos dar uma chance maior de descobrir se ele realmente roubou algo."
    Nathan "Tudo bem, então vamos para casa por hoje, teremos um dia longo amanhã..."
    pause
    show black with dissolve
    jump falamaecasa

label falamaecasa:
    show bg casa fora noite with dissolve
    scene bg casa fora noite
    show halfblack
    show mae s at right
    Mãe "Nathan! O que você faz fora de casa tão tarde? Até seu pai chegou antes de você."
    show nate ex at left
    Nathan "Oi mãe. Eu só estava resolvendo alguns asuntos com a Erika, nada de mais, desculpa te preocupar."
    Mãe "Quando for assim me avisa por favor, seu pai parecia irritado como sempre então eu nem tentei parguntar sobre, preferi esperar aqui fora."
    show nate n
    Nathan "Desculpa mãe, eu não vi o tempo passar dessa vez."
    show mae f
    Mãe "Você devia pelo menos comer algo e depois ir para o seu quarto, tá bom?"
    Nathan "Tudo bem mãe, desculpa mais uma vez"
    show black with dissolve
    scene black
    hide nate 
    hide mae 
    "Eu passei pela sala de estar quando ia pro meu quarto, nunca senti um clima tão pesado na vida, parecia que algúem tinha colocado uma montanha nas minhas costas"
    jump quartodia4

label quartodia4:
    show bg quarto com pistas noite with dissolve
    scene bg quarto com pistas noite 
    show halfblack
    show john b2 at right
    John "Mano, do que você acha que Joseph tava correndo mais cedo? Se ele é o culpado ele não devia estar correndo, talvez ele estivesse aprontando alguma coisa."
    show nate n at left
    Nathan "John, você consegue guardar esse pensamento pra amanhã? Eu tô muito cansado pra pensar, só quero dormir por agora"
    hide john
    show camilla n at right
    Camilla "Ele tem um ótimo ponto na verdade, mas você quem sabe Nathan, vamos te deixar em paz essa noite, boa noite."
    hide camilla
    hide nate
    "Assim um dos meus últimos dias nessa correria se encerram, se eu tenho algo não resolvido, é bom resolver agora e rápido..."
    jump startday5
    
    
    
#Rua - Noite
#Ao olhar para cima, Nathan percebe que acabou esbarrando no bibliotecario que parecia bastante estressado e com pressa, Nathan congela e o homem vai embora.
#John aparece e pergunta como Nathan está. Nathan responde que está bem e camilla fala que o biblbiotecario parece ter derrubado alguma coisa
#Ao verificar, Nathan percebe que se trata de um jogo de chaves, ele as pega e vai para casa.
#Antes de entrar em casa a mãe de Nathan estava esperando por ele na entrada da casa por estar preocupada dele ter voltado sozinho para casa tão tarde, eles conversam brevemente e entram
# (contexto do porque o bibliotecario estava com pressa, ele viu o David sair de uma janela quebrada de uma casa e tirando a mascara que escondia seu rosto, após isso o David notou que o Joseph viu e foi atrás dele o nocauteando perto da delegacia)
#Fim do dia 4

#Dia 5
#(Dia)
#Nathan acorda e recebe uma ligação de Erika falando que o mercadinho foi reaberto e pede para que você vá até o mercado para ver seus amigos
#Antes de você sair os fantasmas perguntam sobre o que você pretende fazer com relação as chaves que você encontrou
#Você diz que que precisa pensar bem sobre isso e que talvez a Erika possa te ajudar a decidir isso melhor
#No mercado
#David está do lado de fora do mercado e te comprimenta da maneira estranha normal dele de sempre
#Entrando no mercado Nathan é recebido por seus amigos, o Lucas parece um pouco mais animado devido a reabertura do mercado
#Lucas explica que o mercado reabriu rapidamente devido ao fato de seu pai conhecer bastante gente na cidade e conseguiu resolver o problema do vidro rapidamente
#Você pergunta brevemente sobre o David e o Sebastian responde que a policia decidiu deixar uma ronda na frente da loja por questão de segurança e designaram o David pra isso
#O sebastian também menciona que o David é bem folgado e fica pegando salgadinhos sem pagar, mas o Lucas não se importa muito já que ele está "defendendo" a loja
#Você chama a Erika de canto e menciona das chaves que você encontrou, vocês conversam um pouco sobre o assunto e chegam em algumas opções
#Falar com a Vivian sobre o assunto (caso vc tenha feito a quest de mostrar o anel ( ͡° ͜ʖ ͡°)) entregar a chave para o David (péssima ideia, adiciona moral para o final ruim) e investigar por conta própria com a Erika (leva pro final neutro)
#menu de escolha aparece a historia se divide em rotas apartir daqui

#(Noite)
#A noite você se prepara para outra invasão na delegacia mas a segurança lá parece ter sido reforçada
#Ainda sim você consegue entrar e ir até a sala do seu pai pegar o papel com as combinações
#eles ficam inacreditados da senha ser extremamente simples e que o ladrão não poderia ser burro o suficiente para deixar uma senha assim no cofre
#ninguem fala nada nessa hora
#Por estar muito tarde, john e camilla recomendam que você vá para casa descansar e avise Vivian no dia seguinte
#voce volta pra casa e fim do dia 5

#Dia 6, dia decisivo para a conclusão
#dividir em ifs
#No dia seguinte voce liga para vivian logo cedo e ela fala que encontrou o joseph e pede para que você vá direto para a biblioteca para explicar a situação
#Chegando lá o joseph explica a situação e esclaresse os mal-entendidos e o corte em sua perna, que não tinha nada a ver com os crimes cometidos
#
#label demoend:
#3   "Obrigado por jogar a demo! Não esqueça de preencher o formulário. Se possível, também chame mais alguém para testar nosso jogo, por favor!"
#   pause

#"O biblioteca tenta vir atrás da gente mas não consegue acompanhar nosso ritmo, ao olhar para trás percebo que ele está com uma perna machucada e mancando"