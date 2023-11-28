label startday5:
    show bg quarto com pistas dia with dissolve
    scene bg quarto com pistas dia
    pause
    show halfblack
    "{i}trim... trim... trim...{/i}"
    show nate n at left
    Nathan "... Alô?"
    show erika n at right
    Erika "Nathan! Finalmente consegui entrar em contato, você dormiu mais do que o normal hoje, tá tudo bem ai?."
    Nathan "Tá sim, só dormi um pouco mais tarde ontem"
    Erika "Entendi, mas enfim, tenho uma ótima notícia! O mercadinho foi reaberto e os meninos já estão esperando a gente por lá."
    show nate f 
    Nathan "Sério? Isso é incrível! Vou me arrumar rapidinho e já já estarei por lá okay?"
    show erika n
    Erika "Ai que ótimo! Te encontro na frente da loja então tudo bem? Até mais tarde!"
    hide erika
    "Erika encerra a ligação*"
    show camilla n at right
    Camilla "Espera aí Nate, antes de sair, você sabe o que vai fazer com a chave do Joseph?"
    show nate n
    Nathan "Ah, é verdade. Ainda não sei o que fazer com ela. Acho que vou conversar com a Erika primeiro e ver o que ela acha."
    hide camilla
    show john f at right
    John "Boa, aí você já aproveita e chama ela pra sair de novo hehe"
    hide john
    show camilla b at right
    Camilla "John, para de provocar o Nathan com isso, você sabe que não funciona assim."
    Nathan "Tá tudo bem Camilla, Só vou fingir que não escutei dessa vez."
    Nathan "Vamos logo para o mercado dos meninos, temos muito a fazer hoje."
    hide nate
    hide camilla
    jump lojadia5

label lojadia5:
    show bg mercado dia with dissolve
    scene bg mercado dia
    show halfblack
    "Chegando na frente do mercado, Erika já estava lá me esperando"
    show erika n at right
    Erika "Nate você chegou! Até que foi rápido."
    show nate f at left
    Nathan "A gente não teve a chance de passar tanto tempo com os meninos por conta do assalto, então eu decidi vir correndo haha"
    show erika n
    Erika "Bom, se você está com tanta pressa assim, a gente podia entrar logo né."
    hide erika
    hide nate
    "Assim que nos aproximamos da porta da loja, alguém a abre para nós dois, e uma voz familiar ecoa."
    show david b
    David "Bom dia filho do delegado, senhor!"
    hide david
    show erika n at right
    Erika "{i}Você conhece ele?{/i}"
    show nate n at left
    Nathan "{i}Ele trabalha pro meu pai, e como eu sou filho do chefe dele, ele pensa que eu posso mandar nele também.{/i}"
    Erika "{i}Ahhh, entendi, senhor filho do chefe{/i}"
    show nate f
    Nathan "Obrigado por abrir a porta David."
    hide erika
    hide nate
    show david n
    David "É nois, tamo junto, senhor!"
    hide david
    "Entramos no mercado com pressa para evitar que o David falasse mais alguma coisa estranha."
    show bg shop with dissolve
    show halfblack
    show lucas f at right
    Lucas "Nathan! Erika! Que bom ter vocês aqui de novo! Ficamos muito felizes com a reabertura do mercado!"
    if mantevetorta == 0:
        Lucas "Antes que eu me esqueça, agradeça sua mãe pela torta daquele dia, estava muito boa!"
        Lucas "Ela ajudou muito naquele dia, eu tava bem triste com a situação da loja."
        hide lucas
        show sebastian b at right
        Sebastian "Por mais que só pudemos comer metade já que o David comeu quase tudo sozinho."
        Sebastian "Não vou muito com a cara dele, algo me parece estranho nesse cara..."
        hide seb
        show lucas b at right
        Lucas "Sebastian, para com isso!"
        hide lucas
        show sebastian n
        Sebastian "..."
        hide seb
        hide lucas
    show nate n at left
    Nathan "Só uma pergunta, como vocês reabriram a loja tão rápido? achei que vocês iam demorar um pouco mais para poder reabri-la"
    hide lucas
    show seb f at right 
    Sebastian "Acontece que o pai do Lucas é um cara bem influente pelo que parece, ele conseguiu um pessoal que consertou tudo rapidinho."
    Nathan "Outra coisa, Por que o David tá ali do lado de fora?"
    hide seb
    show lucas n at right
    Lucas "Aparentemente o departamento de policia quer aumentar a segurança na região enquanto eles não encontrarem o ladrão, e o David foi selecionado pra cuidar daqui."
    hide lucas
    show seb b at right
    Sebastian "Cá entre nós, eu acho que eles escolheram o policial mais folgado possível. A cada 30 minutos ele vem aqui e pega um saldinho e sai sem pagar!."
    hide seb
    show lucas n at right
    Lucas "Ah, eu não me importo muito com isso, eu acho válido já que ele está se arriscando pra nos proteger."
    hide lucas
    show seb f2 at right
    Sebastian "Vocês nos dão um minuto, eu vou ter que explicar novamente pro Lucas o porque entregar produtos de graça nos gera prejuízo."
    hide seb
    hide lucas
    hide nate
    "Os dois vão para os fundos da loja, o Sebastian parece estar dando uma bronca no Lucas"
    show nate n at left 
    Nathan "Erika, aproveitando que eles sairam, deixa eu te contar o que achei ontem."
    show erika n at right
    Erika "O que é que você encontrou? é de comer?"
    show nate s
    Nathan "O que? Não, a não ser que você goste de comer chaves"
    show nate n
    Nathan "Enquanto eu estava voltando pra casa eu me encontrei com o Joseph, ele estava bem sério, parecia ter aprontado alguma coisa... Fico imaginando o que"
    show erika s
    Erika "Nossa que medo, e ai?"
    show erika n
    Nathan "E ai que a gente se trombou, e nisso ele derrubou essas chaves aqui."
    "Eu tiro a chave do meu bolso e mostro pra Erika"
    Nathan "Só não sei muito bem o que eu devo fazer com elas, você tem alguma ideia?"
    Erika "Hmmm..."
    Erika "Eu até tenho algumas."
    show erika n2
    Erika "Você pode tentar entrega-las para a policia, ou se você preferir a gente pode tentar investigar a biblioteca juntos, o que acha?" 
    Nathan "Deixa eu pensar..."
    if vivianescolha >= 1:
        "Se for para falar com alguém da policia, acho que a Vivian pode ser uma opção mais confiável."
    elif moralfinalruim >= 1:
        "Bom, o David parece ter entregado os arquivos corretamente da última vez, talvez ele ajude de fato com a chave"
        hide erika
        hide nate
    menu:
        "Falar com a Vivian" if vivianescolha >= 1:
            show nate n at left
            Nathan "Acho que eu deveria falar com a Vivian na delegacia, ela é mais confiável que o David, afinal."
            show erika n at right
            Erika "Vivian? Ah sim, a moça que me interrogou quando eu fui assaltada antes da loja, ela é bem gente boa, você vai agora?"
            Nathan "Acho que melhor eu ir agora, não quero perder muito tempo, entende? Consegue dar tchau pros meninos por mim?"
            show erika n2
            Erika "Consigo sim e entendo completamente! Boa sorte falando com ela Nate!"
            "Então eu saio da loja, e vou correndo até a delegacia"
            hide erika
            hide nate
            jump delegaciavivian2
        "Investigar por conta própria":
            show nate n at left
            Nathan "Acho melhor investigarmos por conta própria mesmo, a policia não tem provas o suficiente para investiga-lo, então acho que eles não vão ajudar."
            show erika n at right
            Erika "Justo, na frente da bilbioteca hoje a noite então?"
            Nathan "isso, a gente se vê por lá"
            jump dianeutro
            pause
        "Entregar as chaves para o David" if moralfinalruim >= 1:
            "O David entra na loja pra roubar mais um salgadinho, eu abordo ele antes que ele pegue"
            show nate n at left
            Nathan "Acho que vou falar com o David então"
            show erika n at right
            Erika "Ok, te vejo outra hora então!"
            Nathan "David!"
            hide erika
            show david n at right
            David "Oi!? eu ia pagar!"
            show nate s 
            Nathan "Anh? Tá... bom...?"
            show nate n
            Nathan "Enfim, eu tenho algo pra você aqui, pensei que poderia ser algo útil para a investigação."
            show david f
            David "E o que você têm aí com você meu bom?"
            David "...Senhor!"
            Nathan "Eu encontrei essas chaves aqui, acredito que elas pertencem ao bibliotecario."
            show david t
            David "?"
            Nathan "A gente pode investigar a biblioteca juntos, acredito que lá tenham evidências que provam que o Joseph seja o culpado!"
            show david f
            David "AAAAAAH, entendi, mas quem é Joseph?"
            Nathan "O bibliotecário...?"
            show david n
            David "Hmm, interessante. Vou levar essas chaves comigo, e ver se elas se encaixam em alguma evidência. Obrigado, Senhor!"
            show nate s
            Nathan "Espera! Eu não vou ajudar?"
            David "Claro que não, isso é muito arriscado para envolver um cívil, deixa isso nas mãos do Super David!" 
            "David tenta fazer uma pose de super herói mas fica ridículo e ele vai embora."
            hide david
            hide nate
            jump dia5finalruim
            pause
            
            #se vc seguir pelo final neutro, o David aparece e te atrapalha de conseguir resolver o caso quando vc tenta invadir a biblioteca com a Erika