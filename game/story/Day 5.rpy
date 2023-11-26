label startday5:
    show bg quarto com pistas dia with dissolve
    scene bg quarto com pistas dia
    pause
    show halfblack
    "{i}trim... trim... trim...{/i}"
    Nathan "... Alô?"
    Erika "Nathan! Finalmente consegui entrar em contato, você dormiu mais do que o normal."
    Erika "Mas enfim, tenho uma ótima notícia! O mercadinho foi reaberto e eles nos esperando lá."
    Nathan "Sério? Isso é incrível! Vou me arrumar rapidinho e já já estarei por lá okay?"
    Erika "Ai que ótimo! Te encontro na frente da loja então tudo bem? Até mais tarde!"
    "Erika então desligou o celular, pelo menos agora eu sei o que eu tenho que fazer hoje"
    Camilla "Espera aí nate, antes de sair, você sabe o que vai fazer com a chave do Joseph?"
    Nathan "Ah, é verdade. Ainda não sei o que fazer com ela. Acho que vou conversar com a Erika quando depois e ver o que ela acha."
    John "Boa, aí você já chama ela pra sair de novo haha" #não sei fazer risada
    Camilla "John, para de provocar o Nathan com isso, você sabe que não funciona assim."
    Nathan "Tá tudo bem Camilla, vou só fingir que não escutei dessa vez."
    Nathan "Vamos logo para a loja dos meninos, temos muito a fazer hoje."
    jump lojadia5

label lojadia5:
    show bg mercado dia with dissolve
    scene bg mercado dia
    "Chegando na frente da loja, Erika já estava lá me esperando"
    Erika "Nate você chegou! Até que foi rápido."
    Nathan "A gente não teve a chance de passar tanto tempo com os meninos por conta do assalto e tal, então eu decidi vir correndo haha"
    Erika "Bom, se você está com tanta pressa assim, a gente podia entrar logo né."
    "Assim que nos aproximamos da porta da loja, alguém a abre para nós dois, e uma voz familiar ecoa."
    David "Bom dia filho do delegado, senhor!"
    Erika "{i}Você conhece ele?{/i}"
    Nathan "{i}Ele trabalha pro meu pai, e como eu sou filho do chefe dele, ele pensa que eu posso mandar nele também.{/i}"
    Erika "{i}Ahhh, entendi, senhor filho do chefe{/i}"
    Nathan "Obrigado por abrir a porta David."
    David "O prazer é todo meu, senhor!"
    "Para evitar uma conversa estranha com David, decidimos entrar na loja antes que ele falasse mais alguma coisa."
    show bg shop with dissolve
    Lucas "Nathan! Erika! Que bom ter vocês aqui de novo! Ficamos tão felizes com a reabertura do mercado."
    Sebastian "O Luca não parou de falar sobre a loja quando descobriu que ela estava completamente reparada após a investigação da polícia."
    Nathan "Só uma dúvida, vocês sabem o pq que o David ta na porta ali?"
    Sebastian "Aparentemente a policia quero aumentar a segurança em loja enquanto eles não encontrarem o ladrão, e o David foi selecionado pra cuidar daqui."
    Sebastian "Cá entre nós, eu acho que eles escolheram o policial mais folgado possível. Já vi ele roubando salgadinhos demais na loja."
    Lucas "Não me importo muito com isso, é tipo um pagamento por ele estar nos protegendo."
    Sebastian "Vocês nos dão um minuto, eu vou ter que explicar pro Lucas de novo o motivo do porque entregar produtos da loja de graça é ruim"
    "Os dois vão para os fundos da loja, o sebastian parece estar dando uma bronca no lucas"
    Nathan "Erika, aproveitando que eles sairam, deixa eu te contar o que achei ontem."
    Erika "Você achou alguma coisa ontem?"
    Nathan "Sim sim, enquanto eu estava voltando pra casa a pé, eu me bati com o Joseph, sabe, o bibliotecário, ele derrubou essa chave aqui."
    "Eu tiro a chave do meu bolso e mostro pra Erika"
    Nathan "Só não sei muito o que posso fazer com ela, você tem alguma ideia?"
    Erika "Hmmm..."
    Erika "Eu até tenho algumas.."
    Erika "Você pode tentar entregar pro David, ele deve saber o que fazer com uma chave assim, ou a gente pode tentar investigar a biblioteca juntos, o que acha?"
    Nathan "Deixa eu pensar.."
    menu:
        "Falar com a Vivian" if vivianescolha >= 1:
            Nathan "Acho que eu deveria falar com a Vivian na delegacia, ela é mais inteligente que o david afinal."
            Erika "Vivian? Ah sim, a moça que me interrogou quando eu fui assaltada antes da loja, ela é uma moça legal, você vai agora?"
            Nathan "Acho que é bom eu ir agora, não quero perder muito tempo do dia entende? Consegue dar tchau pros meninos por mim?"
            Erika "Consigo sim e entendo completamente! Boa sorte falando com ela Nate!"
            "Então eu saio da loja, e vou correndo até a delegacia"
            jump delegaciavivian2
        "Investigar por conta própria":
            pass
        "Entregar as chaves para o David":
            pass

label delegaciavivian2:
    show bg delegacia frente dia with dissolve
    pause 1.0
    show bg delegacia frente dia tarde with dissolve
    pause 1.0
    show bg delegacia dentro with dissolve
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