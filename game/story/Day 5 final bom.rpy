label delegaciavivian2:
    show bg delegacia frente dia with dissolve
    pause 1.0
    show bg delegacia frente dia tarde with dissolve
    pause 1.0
    show bg delegacia dentro with dissolve
    pause 1.0
    "Vivian estava trabalhando na recepção, então assim que entrei ela vem me cumprimentar"
    Vivian "Nathan! Que surpresa vê-lo por aqui de novo. O que posso fazer por você hoje?"
    Nathan "Oi, Vivian. Desculpa te incomodar de novo, mas eu esbarrei com o Joseph ontem a noite enquanto voltava pra casa." 
    Nathan "Ele parecia bem apressado, acredito que ele tenha tramado alguma."
    Nathan "Ele derrubou essas chaves, acho que elas são dos cadeados da biblioteca. Achei melhor vir aqui falar com você sobre isso."
    Vivian "Ontem a noite? Você tem certeza?"
    Nathan "Sim, por que?"
    Vivian "O ladrão invadiu minha casa ontem a noite, mesma situação do tijolo e tudo mais, só que dessa vez ele não chegou a levar nada."
    Vivian "Você se importaria de me entregar essas chaves?"
    Nathan "Ah sim, claro!"
    $ renpy.notify("Você entrega a chave para Vivian analisar.")
    Vivian "Interessante. Essa são de fato as chaves da biblioteca."
    Nathan "Você acha que a gente poderia usar essa chave pra procurar algum tipo de evidência por lá?"
    Vivian "Poder a gente até pode, mas, eu não sei se seria muito legal sem um protocolo ou mandato. Invadir a biblioteca sem uma causa justificada pode ser bem problemático, eu poderia ser demitida."
    Nathan "Vivian, essa pode ser a única chance que nós temos de encontrar algo incriminador de verdade."
    Vivian "Você tem um bom ponto... Mas eu não posso."
    Nathan "Você também quer investigar lá não quer?"
    Vivian "..."
    Vivian "Talvez."
    Vivian "Eu prefiro acreditar que o Joseph não cometeria algo assim."
    Nathan "O máximo que pode acontecer é a gente não encontrar nada."
    Vivian "Se acontecer algo de ruim, o peso vai cair nas suas costas ouviu? Vamos logo antes que eu mude de ideia"
    "Então eu e Vivian fomos até a bilbioteca"
    hide nate 
    hide vivian
    jump bibliotecaday5

label bibliotecaday5:
    show bg biblioteca fora tarde with dissolve
    pause 1.0
    show bg biblioteca dentro tarde with dissolve
    pause 1.0
    "Joseph não veio a biblioteca hoje, deve ser porque pegamos a chave dele, essa hora ele deve estar procurando essa coisinha que nem louco em casa."
    Vivian "Tá bom, Nathan. Vamos investigar a biblioteca juntos. Mas lembre-se, estamos agindo sob nossa própria responsabilidade."
    Nathan "Blá, blá, blá. É só a gente seguir com cuidado que vai dar tudo certo. Quanto mais rápido encontrarmos algo, mais rápido a gente vaza."
    Vivian "Tudo bem, você pode investigar o que quiser aí, eu vou ver se encontro algo nas câmeras, se o Joseph for o mesmo da época que a gente namorava ele usa a mesma senha em tudo!."
    "A vivian entrou em uma sala apenas para funcionários para poder olhar as gravações antigas"
    Nathan "Agora é minha vez, por onde eu começo?"
    jump bibliotecaday5procura

label bibliotecaday5procura:
    menu:
        "Estante":
            Nathan "Aqui só tem alguns livros infantis, são muito finos pra esconder algo..."
            $ procuraestante += 1
            jump bibliotecaday5procura
        "Bancada principal" if procuraestante >= 1:
            Nathan "Documentos sobre emprestar e devolver livros, parece que o Lucas pegou algo emprestado faz alguns meses e não devolveu ainda."
            $ procurabancada += 1
            jump bibliotecaday5procura
        "Prateleira" if procurabancada >= 1:
            "Procurar essa prateleira me faz pensar quando eu comecei a investigar tudo isso. Não parece ter nada por aqui ainda."
            Nathan "Tem que ter alguma coisa por aqui, se aqui não tem nada, o ladrão vai acabar saindo ileso."
            Camilla "Eu acho que ainda pode ter um lugar que você não procurou, pode ser idiota, mas já tentou olhar embaixo do tapete?"
            John "É uma ideia bem besta mesmo, mas parando pra pensar, muitas das soluções até agora foram bem idiotas..."
            Nathan "Eu posso tentar, é nossa última chance de conseguir algo..."
            $ procuraprateleira += 1
            jump bibliotecaday5procura
        "Levantar o tapete" if procuraprateleira >= 1:
            "Assim que eu levanto o tapete, um cofre é revelado"
            show bg biblioteca segredo tarde with dissolve
            scene bg biblioteca segredo tarde
            Nathan "UM COFRE?"
            "Vivian volta da sala das câmeras"
            Vivian "Você encontrou um cofre? Eu não sabia que eles tinham um cofre na biblioteca"
            Nathan "Eu muito menos, você acha que a gente consegue abrir ele sem senha?"
            Vivian "Conseguir a gente até consegue, mas a pergunta mesmo é se a gente tem tempo pra fazer isso."
            John "Nathan, eu acho que a gente viu algo relacionado a como abrir esse tipo de cofre na sala do seu pai, não?"
            John "Você não acha que seria melhor a gente tentar buscar essa senha antes? Ficar aqui por tempo demais tentando pode chamar muita atenção, precisamos ser rápidos!."
            jump bibliotecaday5continuação
   
label bibliotecaday5continuação:
    menu:
        "Chutar a senha":
            Nathan "Acho que podemos tentar chutar a senha. Talvez tenhamos sorte e acertemos de primeira."
            Nathan "Vivian, você conhece bem o Joseph né? Vou precisar da sua ajuda aqui."
            Vivian "Claro! Do que você precisa?"
            Nathan "Pode me dizer o dia do aniversário do Joseph?"
            "Disse deitando no tapete e encostando meu ouvido a porta do cofre"
            Vivian "Que eu me lebre é dia 26 de março. Por quê?"
            Nathan "Quero testar algumas senhas fáceis antes de algo difícil, só isso."
            "Vou escutando os {i}tics{/i} do cofre, mas não parece que essa combinação fez algo."
            Nathan "Ta bom... Não era essa, mais uma pergunta, seu aniversário é quando?"
            Vivian "Por que o meu aniversário seria a senha?"
            Nathan "Vocês namoravam não era? Talvez ele tenha colocado essa senha na época que o cofre foi instalado."
            Vivian "Faz sentido..."
            Vivian "O meu é dia 8 de maio."
            "Vou escutando os {i}tics{/i} do cofre, mas não parece que essa combinação fez algo, de novo."
            Nathan "Nada também, mais uma pergunta, essa é meio pessoal mas acho que funcionaria também."
            Vivian "Que pergunta?"
            Nathan "Você por acaso se lembra da data de quando vocês começaram a namorar?"
            Vivian "Ah... Isso, tenho certeza de que foi dia 13 de Janeiro."
            "Com um pouco de ansiedade eu giro a senha do cofre mais uma vez... Infelizmente nada de mais acontece."
            Nathan "Nada..."
            Camilla "Nathan antes que você se envergonhe de novo perguntando essas coisas, você ja pensou em só colocar '1, 2, 3, 4'?"                    
            Camilla "Pode até ser idiota, mas de novo, a última ideia idiota que a gente teve nos revelou o cofre não foi?"
            Nathan "...Tá, valeu, deixa eu testar isso então."
            Vivian "Com quem você tá falando?"
            Nathan "Ahn!? Não, eu tava falando sozinho mesmo"
            Vivian "Okay?"
            Nathan "Desculpa as perguntas meio invasisvas aliás."
            Vivian "Não não, tudo bem."
            John "Eita, essa foi por pouco, quase que ela pensa que você é maluco."
            "Respiro fundo e tento uma última vez, com medo do cofre se trancar sozinho"
            "1...{w=0.5} 2...{w=0.5} 3...{w=0.5} 4...{w=2.0}{nw}"
            "{i}Clink!{/i}"
            "O cofre se abre revelando todos os objetos roubados nos crimes recentes"
            John "Não é possível que a senha era algo estúpido assim."
            Vivian "Não pode ser..."
            Nathan "Acho que minhas suspeitas não eram tão infundamentadas assim."
            Nathan "Mas ainda precisamos interroga-lo para saber o porque dele ter cometido os crimes."
            Vivian "Enquanto eu olhava as câmeras, percebi que o Joseph não estava na biblioteca durante o horário dos crimes mas..."
            Vivian "Ainda é dificil de acreditar que ele cometeria tais atos, vou me encontrar com ele depois pra interrogá-lo."
            Vivian "Acho que é melhor a gente se separar agora, vou te passar o meu número e você já pode ir pra casa, qualquer coisa eu entro em contato."
            $ renpy.notify("Vivian te passou o número dela.")
            "Após Vivian me entregar o número dela, ela sai pela porta. Eu vou logo em seguida, direto pra casa."
            hide vivian
            hide nathan
            jump casadia5
            #se voce tenta chutar as senhas ao sair da biblioteca ja ta escurecendo

            
        "Ir buscar a senha":
            Nathan "Você tem razão, é melhor não mexermos no cofre por agora, acha que teria alguma forma de descobrir a senha sem a tentar abrir ele aqui?"
            Vivian "O Joseph deve saber a senha... O cofre é dele afinal, vou tentar perguntar pra ele mais tarde."
            Vivian "Na verdade, acho melhor eu ir atrás dele agora mesmo, até outra hora nathan, toma meu telefone, você sabe onde me achar se precisar."
            Vivian "Antes que eu me esqueça, de acordo com as câmeras, Joseph não estava por aqui no horário do crime, não queria ter que fazer isso, mas vou ter que interrogar ele mais a fundo."
            Nathan "Ele não estava aqui? Mas ele praticamente nunca sai da biblioteca."
            Vivian "Essa é a parte esquisita, a câmera é meio ruim por ser antiga, mas eu consegui ver ele saindo daqui claramente."
            Vivian "Bom, parece que nós dois conseguimos ótimas informações nesse tempinho. Acho que deviamos nos separar por agora, se eu descobrir algo a mais sobre o Joseph, vou te ligar ok?"
            John "Ei, não tinha um documento na sala do seu pai falando sobre destrancar cofres? Talvez ele seja útil"
            Nathan "Você tem razão, mas com certeza eles melhoraram a segurança da delegacia desde que a gente roubou os arquivos."
            Camilla "Acho que não custa tentar, qualquer coisa você poderia enganar o seu pai e pegar enquanto ele está distraído."
            Nathan "Hmm, vou pensar no que fazer e decido quando chegarmos na delegacia"
            "A vivian então saiu da bilbioteca anotando sobre as coisas que ela descobriu por aqui."
            hide vivian 
            hide camilla 
            hide john 
            hide nate 
            jump delegaciapai2


            
        #nessa opçao ainda ta de tarde e quando vc chega na delegacia ta de noite

label casadia5:
    
    show bg quarto com pistas tarde with dissolve
    show bg quarto com pistas noite with dissolve
    scene bg quarto com pistas noite

label delegaciapai2:
    show bg delegacia fora dia tarde with dissolve
    show bg delegacia fora dia noite with dissolve
    Nathan "Vocês acham que isso é uma boa ideia mesmo?"
    John "É seu pai, não é como se você tivesse a melhor reputação com el já né"
    Camilla "E além do mais, se você não pegar essa senha hoje, é possível que o ladrão troque ela amanhã."
    Nathan "Ta bom então, é agora ou nunca."
    show bg sala do pai clara with dissolve 
    scene bg sala do pai clara
    "Eu entro na sala do meu pai devagar, pra não deixá-lo estressado."
    Nathan "Opa, consegue conversar?"
    Pai "O que você tá fazendo aqui filho? Já falei pra não se meter em assuntos policiais."
    Nathan "Não é nada disso não, eu tava passando por aqui e queria perguntar se você conseguiria me deixar em casa depois que terminar o trabalho aí"
    
    
    
    
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
#A noite você se prepara para outra invasão na delegacia mas a segurança lá parece ter sido reforçada (if foisus >=1 diálogo novo)
#Ainda sim você consegue entrar e ir até a sala do seu pai pegar o papel com as combinações
#eles ficam inacreditados da senha ser extremamente simples e que o ladrão não poderia ser burro o suficiente para deixar uma senha assim no cofre
#ninguem fala nada nessa hora
#Por estar muito tarde, john e camilla recomendam que você vá para casa descansar e avise Vivian no dia seguinte
#voce volta pra casa e fim do dia 5

#Dia 6, dia decisivo para a conclusão
#dividir em ifs
#No dia seguinte voce liga para vivian logo cedo e ela fala que encontrou o joseph e pede para que você vá direto para a biblioteca para explicar a situação
#Chegando lá o joseph explica a situação e esclaresse os mal-entendidos e o corte em sua perna, que não tinha nada a ver com os crimes cometidos
#O joseph explica que não sabe como as coisas foram parar naquele cofre, e ele diz que nunca nem chegou a usar aquele cofre desde que foi instalado
#ele tambem conta que o ferimento em sua perna foi porque ele derrubou um aquario velho enquanto tentava limpa-lo em sua casa e acabou se cortando
#e que na noite do dia 4 ele estava com pressa porque viu o David tacando o tijolo na janela da casa da vivian
#voce fica muito chocado ao descobrir que o culpado é o david 😯😯😯😯
#o Joseph consegue pegar as gravações do backup que conseguiam comprovar que David era o culpado
#voces pegam as gravações e vão para a delegacia, lá o David e seu pai estão no escritorio do seu pai, o David parecia estar prestes a denunciar que o Bibliotecario era o culpado pelos crimes
#voces chegam gritando OBJECTION
#voces mostram as provas e por ser incontestavel, o David é preso na hora e confessa o porque que ele fez os crimes
#seu pai fica orgulhoso de que você conseguiu pegar o verdadeiro culpado
#o dia se encerra

#dia 7 epilogo bom
# voce passa o dia com a Erika e convida para sair
# "E foi assim que eu resolvi o meu primeiro caso de muitos"