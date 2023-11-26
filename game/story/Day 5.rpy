label startday5:
    show bg quarto com pistas dia with dissolve
    scene bg quarto com pistas dia
    pause
    show halfblack
    "{i}trim... trim... trim...{/i}"
    Nathan "... Alô?"
    Erika "Nathan! Finalmente consegui entrar em contato, você dormiu mais do que o normal hoje, tá tudo bem ai?."
    Nathan "Tá sim, só dormi um pouco mais tarde ontem"
    Erika "Entendi, mas enfim, tenho uma ótima notícia! O mercadinho foi reaberto e os meninos já estão esperando a gente por lá."
    Nathan "Sério? Isso é incrível! Vou me arrumar rapidinho e já já estarei por lá okay?"
    Erika "Ai que ótimo! Te encontro na frente da loja então tudo bem? Até mais tarde!"
    "Erika encerra a ligação*"
    Camilla "Espera aí Nate, antes de sair, você sabe o que vai fazer com a chave do Joseph?"
    Nathan "Ah, é verdade. Ainda não sei o que fazer com ela. Acho que vou conversar com a Erika primeiro e ver o que ela acha." #não sei escrever no geral
    John "Boa, aí você já aproveita e chama ela pra sair de novo hehehe" #não sei fazer risada
    Camilla "John, para de provocar o Nathan com isso, você sabe que não funciona assim."
    Nathan "Tá tudo bem Camilla, Só vou fingir que não escutei dessa vez."
    Nathan "Vamos logo para o mercado dos meninos, temos muito a fazer hoje."
    jump lojadia5

label lojadia5:
    # if manteve torta = 0 algo acontece, tem que colocar aqui um dialogo remetente a voce ter entregado a torta la no dia 2
    show bg mercado dia with dissolve
    scene bg mercado dia
    "Chegando na frente do mercado, Erika já estava lá me esperando"
    Erika "Nate você chegou! Até que foi rápido."
    Nathan "A gente não teve a chance de passar tanto tempo com os meninos por conta do assalto, então eu decidi vir correndo haha"
    Erika "Bom, se você está com tanta pressa assim, a gente podia entrar logo né."
    "Assim que nos aproximamos da porta da loja, alguém a abre para nós dois, e uma voz familiar ecoa."
    David "Bom dia filho do delegado, senhor!"
    Erika "{i}Você conhece ele?{/i}"
    Nathan "{i}Ele trabalha pro meu pai, e como eu sou filho do chefe dele, ele pensa que eu posso mandar nele também.{/i}"
    Erika "{i}Ahhh, entendi, senhor filho do chefe{/i}"
    Nathan "Obrigado por abrir a porta David."
    David "É nois, tamo junto, senhor!"
    "Entramos no mercado com pressa para evitar que o David falasse mais alguma coisa estranha."
    show bg shop with dissolve
    Lucas "Nathan! Erika! Que bom ter vocês aqui de novo! Ficamos muito felizes com a reabertura do mercado!"
    Nathan "Só uma pergunta, como vocês reabriram a loja tão rápido? achei que vocês iam demorar um pouco mais para poder reabri-la" 
    Sebastian "Acontece que o pai do Lucas é um cara bem influente pelo que parece, ele conseguiu um pessoal que consertou tudo rapidinho."
    Nathan "Outra coisa, Por que o David tá ali do lado de fora?"
    Lucas "Aparentemente o departamento de policia quer aumentar a segurança na região enquanto eles não encontrarem o ladrão, e o David foi selecionado pra cuidar daqui."
    Sebastian "Cá entre nós, eu acho que eles escolheram o policial mais folgado possível. A cada 30 minutos ele vem aqui e pega um saldinho e sai sem pagar!."
    Lucas "Ah, eu não me importo muito com isso, eu acho válido já que ele está se arriscando pra nos proteger."
    Sebastian "Vocês nos dão um minuto, eu vou ter que explicar novamente pro Lucas o porque entregar produtos de graça nos gera prejuízo."
    "Os dois vão para os fundos da loja, o Sebastian parece estar dando uma bronca no Lucas"
    Nathan "Erika, aproveitando que eles sairam, deixa eu te contar o que achei ontem."
    Erika "O que é que você encontrou? é de comer?"
    Nathan "O que? Não, a não ser que você goste de comer chaves"
    Nathan "Enquanto eu estava voltando pra casa eu me encontrei com o Joseph, ele estava bem sério, parecia ter aprontado alguma coisa... Fico imaginando o que"
    Erika "Nossa que medo, e ai?"
    Nathan "E ai que a gente se trombou, e nisso ele derrubou essas chaves aqui."
    "Eu tiro a chave do meu bolso e mostro pra Erika"
    Nathan "Só não sei muito bem o que eu devo fazer com elas, você tem alguma ideia?"
    Erika "Hmmm..."
    Erika "Eu até tenho algumas."
    Erika "Você pode tentar entrega-las para a policia, ou se você preferir a gente pode tentar investigar a biblioteca juntos, o que acha?" 
    Nathan "Deixa eu pensar..."
    if vivianescolha >= 1:
        "Se for para falar com alguém da policia, acho que a Vivian pode ser uma opção mais confiável."
    elif moralfinalruim >= 1:
        "Bom, o David parece ter entregado os arquivos corretamente da última vez, talvez ele ajude de fato com a chave"
    menu:
        "Falar com a Vivian" if vivianescolha >= 1:
            Nathan "Acho que eu deveria falar com a Vivian na delegacia, ela é mais confiável que o David, afinal."
            Erika "Vivian? Ah sim, a moça que me interrogou quando eu fui assaltada antes da loja, ela é bem gente boa, você vai agora?"
            Nathan "Acho que melhor eu ir agora, não quero perder muito tempo, entende? Consegue dar tchau pros meninos por mim?"
            Erika "Consigo sim e entendo completamente! Boa sorte falando com ela Nate!"
            "Então eu saio da loja, e vou correndo até a delegacia"
            jump delegaciavivian2
        "Investigar por conta própria":
            Nathan "Acho melhor investigarmos por conta própria mesmo, a policia não tem provas o suficiente para investiga-lo, então acho que eles não vão ajudar."
            Erika "Justo, na frente da bilbioteca hoje a noite então?"
            Nathan "isso, a gente se vê por lá"
            pause
        "Entregar as chaves para o David":
            "O David entra na loja pra roubar mais um salgadinho, eu abordo ele antes que ele pegue"
            Nathan "David!"
            David "Oi!? eu ia pagar!" 
            Nathan "Anh? Tá... bom...?"
            Nathan "Enfim, eu tenho algo pra você aqui, pensei que poderia ser algo útil para a investigação."
            David "E o que você têm aí com você meu bom?"
            David "...Senhor!"
            Nathan "Eu encontrei essas chaves aqui, acredito que elas pertencem ao bibliotecario."
            David "?"
            Nathan "A gente pode investigar a biblioteca juntos, acredito que lá tenham evidências que provam que o Joseph seja o culpado!"
            David "AAAAAAH, entendi, mas quem é Joseph?"
            Nathan "O bibliotecário...?"
            David "Hmm, interessante. Vou levar essas chaves comigo, e ver se elas se encaixam em alguma evidência. Obrigado, Senhor!"
            Nathan "Espera! Eu não vou ajudar?"
            David "Claro que não, isso é muito arriscado para envolver um cívil, deixa isso nas mãos do Super David!" 
            "David tenta fazer uma pose de super herói mas fica ridículo e ele vai embora."
            pause
            


    
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

#(Tarde)
#(BRANCH DO FINAL BOM) Pedir ajuda da Vivian
#Caso você peça ajuda da Vivian, vocês se encontra com ela na recepção da delegacia
#Você mostra o jogo de chaves pra ela e fala o que aconteceu na noite anterior, por ela estar desconfiada devido as pistas que você tinha apresentado anteriormente, e pelo fato da casa dela ter sido invadida na noite anterior ela decide ajudar
#vocês dois vão até a biblioteca e começam a investigar
#fazer um menu igual o da sala do pai dele kkkkkkjjj se fodeu
#após procurar em todos os cantos da bilbioteca eles não acham nada, até que camilla sugerem que o tapete parece suspeito
#você levanta o tapete e encontra um cofre escondido, mas vocês não tem a combinação para abri-lo
#Voce tem duas opções para gerar a cena exclusiva, tentar chutar a senha do cofre, ou seguir o conselho do john de ir atrás da combinação na sala do seu pai e isso levanta varias duvidas na cabeça de Nathan que já estava de mal humor com seu pai
#se tentar chutar a combinação vc erra 3 vezes até o camilla sugerir 1,2, 3 e 4, se você chutar essa combinação você corta a cena de ir até a delegacia  
#A Vivian então desacreditada que o Joseph podia ter feito tal coisa decide verificar nas câmeras, e percebe que ele sai antes da hora do crime do dia anterior
#A Vivian diz que precisa ir atrás de Joseph para conseguir respostas e te passa o contato dela e caso voce tente ir atrás de tentar descobrir a combinação do cofre antes vc vai até a delegacia

#voce pode tentar acertar a combinação do cofre ou não (bagulho q a gente falou com o saulo e a gi)

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