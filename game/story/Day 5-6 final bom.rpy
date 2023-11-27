label delegaciavivian2:
    show bg delegacia frente dia with dissolve
    pause 1.0
    show bg delegacia frente dia tarde with dissolve
    pause 1.0
    show bg delegacia dentro with dissolve
    pause 1.0
    show halfblack
    "Vivian estava trabalhando na recepção, então assim que entrei ela vem me cumprimentar"
    show vivian f2 at right 
    Vivian "Nathan! Que surpresa vê-lo por aqui de novo. O que posso fazer por você hoje?"
    show nate n at left
    Nathan "Oi, Vivian. Desculpa te incomodar de novo, mas eu esbarrei com o Joseph ontem a noite enquanto voltava pra casa." 
    Nathan "Ele parecia bem apressado, acredito que ele tenha tramado alguma."
    Nathan "Ele derrubou essas chaves, acho que elas são dos cadeados da biblioteca. Achei melhor vir aqui falar com você sobre isso."
    show vivian n
    Vivian "Ontem a noite? Você tem certeza?"
    show nate s
    Nathan "Sim, por que?"
    show vivian b
    Vivian "O ladrão invadiu minha casa ontem a noite, mesma situação do tijolo e tudo mais, só que dessa vez ele não chegou a levar nada."
    show vivian n
    Vivian "Você se importaria de me entregar essas chaves?"
    show nate ns
    Nathan "Ah sim, claro!"
    $ renpy.notify("Você entrega a chave para Vivian analisar.")
    Vivian "Interessante. Essa são de fato as chaves da biblioteca."
    Nathan "Você acha que a gente poderia usar essa chave pra procurar algum tipo de evidência por lá?"
    Vivian "Poder a gente até pode, mas, eu não sei se seria muito legal sem um protocolo ou mandato. Invadir a biblioteca sem uma causa justificada pode ser bem problemático, eu poderia ser demitida."
    show vivian f
    Nathan "Vivian, essa pode ser a única chance que nós temos de encontrar algo incriminador de verdade."
    show vivian n
    Vivian "Você tem um bom ponto... Mas eu não posso."
    show nate n
    Nathan "Você também quer investigar lá não quer?"
    Vivian "..."
    Vivian "Talvez."
    show vivian b
    Vivian "Eu prefiro acreditar que o Joseph não cometeria algo assim."
    Nathan "O máximo que pode acontecer é a gente não encontrar nada."
    show vivian f
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
    show vivian n at right
    Vivian "Tá bom, Nathan. Vamos investigar a biblioteca juntos. Mas lembre-se, estamos agindo sob nossa própria responsabilidade."
    show nate n
    Nathan "Blá, blá, blá. É só a gente seguir com cuidado que vai dar tudo certo. Quanto mais rápido encontrarmos algo, mais rápido a gente vaza."
    Vivian "Tudo bem, você pode investigar o que quiser aí, eu vou ver se encontro algo nas câmeras, se o Joseph for o mesmo da época que a gente namorava ele usa a mesma senha em tudo!."
    "A vivian entrou em uma sala apenas para funcionários para poder olhar as gravações antigas"
    Nathan "Agora é minha vez, por onde eu começo?"
    hide nate 
    hide vivian
    jump bibliotecaday5procura

label bibliotecaday5procura:
    menu:
        "Estante":
            Nathan "Aqui só tem alguns livros infantis, são muito finos pra esconder algo..."
            $ procuraestante += 1
            jump bibliotecaday5procura
        "Bancada principal" if procuraestante >= 1:
            show nate n at left
            Nathan "Documentos sobre emprestar e devolver livros, parece que o Lucas pegou algo emprestado faz alguns meses e não devolveu ainda."
            hide nate
            $ procurabancada += 1
            jump bibliotecaday5procura
        "Prateleira" if procurabancada >= 1:
            "Procurar essa prateleira me faz pensar quando eu comecei a investigar tudo isso. Não parece ter nada por aqui ainda."
            show nate n at left
            Nathan "Tem que ter alguma coisa por aqui, se aqui não tem nada, o ladrão vai acabar saindo ileso."
            show camilla n at right
            Camilla "Eu acho que ainda pode ter um lugar que você não procurou, pode ser idiota, mas já tentou olhar embaixo do tapete?"
            hide camilla
            show john n at right
            John "É uma ideia bem besta mesmo, mas parando pra pensar, muitas das soluções até agora foram bem idiotas..."
            Nathan "Eu posso tentar, é nossa última chance de conseguir algo..."
            $ procuraprateleira += 1
            jump bibliotecaday5procura
        "Levantar o tapete" if procuraprateleira >= 1:
            "Assim que eu levanto o tapete, um cofre é revelado"
            show bg biblioteca segredo tarde with dissolve
            scene bg biblioteca segredo tarde
            pause
            show halfblack
            show nate n at left
            Nathan "UM COFRE?"
            "Vivian volta da sala das câmeras"
            show vivian n at right
            Vivian "Você encontrou um cofre? Eu não sabia que eles tinham um cofre na biblioteca"
            Nathan "Eu muito menos, você acha que a gente consegue abrir ele sem senha?"
            Vivian "Conseguir a gente até consegue, mas a pergunta mesmo é se a gente tem tempo pra fazer isso."
            hide vivian
            show john n at right
            John "Nathan, eu acho que a gente viu algo relacionado a como abrir esse tipo de cofre na sala do seu pai, não?"
            John "Você não acha que seria melhor a gente tentar buscar essa senha antes? Ficar aqui por tempo demais tentando pode chamar muita atenção, precisamos ser rápidos!."
            hide nate
            hide john
            hide vivian
            jump bibliotecaday5continuação
   
label bibliotecaday5continuação:
    menu:
        "Chutar a senha":
            show nate n at left
            Nathan "Acho que podemos tentar chutar a senha. Talvez tenhamos sorte e acertemos de primeira."
            Nathan "Vivian, você conhece bem o Joseph né? Vou precisar da sua ajuda aqui."
            show vivian f2 at right
            Vivian "Claro! Do que você precisa?"
            Nathan "Pode me dizer o dia do aniversário do Joseph?"
            "Disse deitando no tapete e encostando meu ouvido a porta do cofre"
            show vivian f
            Vivian "Que eu me lebre é dia 26 de março. Por quê?"
            show nate ns
            Nathan "Quero testar algumas senhas fáceis antes de algo difícil, só isso."
            "Vou escutando os {i}tics{/i} do cofre, mas não parece que essa combinação fez algo."
            show nate n
            Nathan "Ta bom... Não era essa, mais uma pergunta, seu aniversário é quando?"
            show vivian n
            Vivian "Por que o meu aniversário seria a senha?"
            show nate ns
            Nathan "Vocês namoravam não era? Talvez ele tenha colocado essa senha na época que o cofre foi instalado."
            show vivian f
            Vivian "Faz sentido..."
            Vivian "O meu é dia 8 de maio."
            "Vou escutando os {i}tics{/i} do cofre, mas não parece que essa combinação fez algo, de novo."
            show nate n
            Nathan "Nada também, mais uma pergunta, essa é meio pessoal mas acho que funcionaria também."
            show vivian n
            Vivian "Que pergunta?"
            show nate ns
            Nathan "Você por acaso se lembra da data de quando vocês começaram a namorar?"
            Vivian "Ah... Isso, tenho certeza de que foi dia 13 de Janeiro."
            "Com um pouco de ansiedade eu giro a senha do cofre mais uma vez... Infelizmente nada de mais acontece."
            show nate b
            Nathan "Nada..."
            hide vivian
            show camilla t at right
            Camilla "Nathan antes que você se envergonhe de novo perguntando essas coisas, você ja pensou em só colocar '1, 2, 3, 4'?"
            show camilla f
            Camilla "Pode até ser idiota, mas de novo, a última ideia idiota que a gente teve nos revelou o cofre não foi?"
            show nate ns
            Nathan "...Tá, valeu, deixa eu testar isso então."
            hide camilla
            show vivian n at right
            Vivian "Com quem você tá falando?"
            show nate f2
            Nathan "Ahn!? Não, eu tava falando sozinho mesmo"
            Vivian "Okay?"
            show nate n
            Nathan "Desculpa as perguntas meio invasisvas aliás."
            Vivian "Não não, tudo bem."
            hide vivian
            show john n
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
            jump invasao2


            
        #nessa opçao ainda ta de tarde e quando vc chega na delegacia ta de noite

label invasao2:
    show bg delegacia frente dia tarde with dissolve
    show bg delegacia frente dia noite with dissolve
    Nathan "Vocês acham que isso é uma boa ideia mesmo?"
    John "É seu pai, não é como se você tivesse a melhor reputação com ele já né"
    Camilla "E além do mais, se você não pegar essa senha hoje, o emprego da Vivian está em jogo agora."
    menu:
        "Invadir quando a delegacia estiver vazia":
            Nathan "A gente consegue esperar até a delegacia esvaziar, aí a gente entra"
            John "Vai querer invadir de novo? Gostei disso."
            Camilla "Eu não posso opinar dessa vez, é uma ideia boa mesmo."
            Nathan "Ta bom então, é agora ou nunca."
            jump invadir2
        "Tentar pegar o livro enquanto seu pai está lá":
            Nathan "Ta bom então, é agora ou nunca."
            jump delegaciapai2

label invadir2:
    "Após uns 30 minutos esperando do lado de fora em um dos arbustos, a delegacia fica vazia."
    Nathan "Agora é a hora, vamos nessa."
    show bg delegacia dentro with dissolve
    pause (1.5)
    show bg sala do pai escuro with dissolve
    John "Você lembra onde estava o livro? A sala ta bem escura, mais do que a última vez."
    Nathan "Eu acho que estava.."
    jump escolhainvasao

label escolhainvasao:
    menu:
        "Na mesa dele":
            Nathan "Eu acho que estava na mesa dele, mas eu não lembro, vamos dar uma olhada."
            "Me aproximo da mesa dele, ainda estava bem escuro mas eu toquei em algo que parecia um livro."
            John "Eu acho que esse deve ser o livro, vamos embora antes que fique tarde demais, sua mãe já deve estar bem preocupada pelo horário."
            hide john 
            hide nate 
            jump casadia5
        "Nas gavetas":
            Camilla "Acho que faria sentido guardar um livro em uma das gavetas, não?"
            Nathan "Pode ser, vamos olhar"
            "Faço força para abrir as gavetas novamente."
            Nathan "Que nem da última vez, ela continua emperrada."
            Camilla "Valeu a pena a tentativa..."
            jump escolhainvasao
        "No armário" if avalanche == 0:
            "Quando eu abro o armário, uma cachoeira de documentos caem, alguém não aprendeu a se organizar nessa sala."
            $ avalanche +=1
            jump escolhainvasao
            pause

label delegaciapai2:
    show bg sala do pai clara with dissolve 
    scene bg sala do pai clara
    "Eu entro na sala do meu pai devagar, pra não deixá-lo estressado."
    Nathan "Opa, consegue conversar?"
    Pai "O que você tá fazendo aqui? É Bom que você não tenha vindo até pra falar sobre esse caso recente, já estou cansado de dizer pra não se meter nos assuntos do meu trabalho."
    Nathan "Não é nada disso não, eu tava passando por aqui e queria perguntar se você conseguiria me deixar em casa depois que terminar o trabalho"
    Pai "Ah, se é só isso, consigo sim, só sai da minha sala por favor."
    Nathan "Mas por quê? Eu não to te atrapalhando nem nada."
    Pai "Mas você vai me atrapalhar se continuar falando."
    Nathan "Tá bom tudo bem, eu fico quieto, bem aqui."
    "Me aproximo da mesa dele, e vejo o mesmo livro que tinha visto aquele dia"
    John "Alí. É ele, o livro! ''Manual da polícia de como destrancar cofres e fechaduras''!"
    Camilla "Agora é a sua chance! Pega ele!"
    Pai "Nathan eu imploro, só espera do lado de fora da minha sala por favor."
    Nathan "Tá bom eu saio, não vou te atrapalhar mais eu juro."
    "Assim que eu termino a frase, aproveito que ele se distraiu e puxo o livro da mesa, saindo o mais rápido possivel da sala com o livro na mão."

label casadia5:
    show bg quarto com pistas noite with dissolve
    scene bg quarto com pistas noite
    "Chegando em casa, me sinto extremamente aliviado, todo esse meu trabalho duro finalmente vai chegar em algum lugar."
    Camilla "E aí detetive? Como você se sente?"
    Nathan "Exausto, esses ultimos 5 dias tem sido.. algo, definitivamente."
    John "Algo bom, você tem evoluído bastante, pelo menos tem feito algo a mais do que ficar trancado no quarto o dia todo."
    Camilla "De qualquer forma, você tem tudo que precisa pra provar a culpa do Joseph."
    John "Agora é só esperar o contato da Vivian. Por hora acho que você merece pelo menos uma noite de sono."
    Nathan "Certo, boa noite vocês dois."
    hide nate 
    hide camilla 
    hide john
    jump startday6

label startday6:
    "Eu acho que não levantei um dia normalmente a não ser nesse, um milagre."
    Camilla "Bom dia Nathan! Como se sente?"
    Nathan "Revigorado, não durmo bem assim faz um tempo."
    Nathan "Vou ligar pra Vivian agora mesmo, não quero perder tempo."
    "Pego o telefone e disco o número que a Vivian me deu ontem. Ela atende bem rápido até"
    Vivian "Bom dia, esse é o celular da Vivian, quem fala?"
    Nathan "Oi Vivian! Aqui é o Nathan, descobriu algo de ontem pra hoje?"
    Vivian "Ah! Nathan! Eu chamei o Joseph pra conversar daqui a pouco, vamos nos encontrar na biblioteca agora, caso queira vir junto."
    Nathan "Ah sim claro, encontro vocês lá!"
    "Desligo o telefonema"
    Nathan "Vamos rápido!"
    John "Não sei se você ja percebeu, mas meio que a gente tá preso a você e não consegue andar."
    Nathan "Eu esqueci."
    Nathan "Só vamos logo por favor."
    "Saio correndo de casa até a biblioteca"
    jump bibliotecaday6

label bibliotecaday6:
    show bg biblioteca fora dia with dissolve
    scene bg biblioteca fora dia
    Vivian "Aí está você Nathan! O Joseph teve um contratempo mas ele chega daqui a pouco."
    Vivian "Você descobriu mais alguma coisa nesse meio tempo?"
    Nathan "Não muito na verdade."
    "Joseph chega, ele ainda estava mancando um pouco."
    Joseph "Bom dia Vivian! E garoto que saiu correndo da biblioteca no outro dia, nunca cheguei a perguntar seu nome, perdão."
    Nathan "É Nathan, senhor."
    Joseph "Não precisa me chamar de senhor, está tudo bem."
    Vivian "Joseph, precisamos te perguntar algumas coisas."
    Joseph "Certo! O que vocês precisam perguntar?"
    Vivian "Sobre o dia do crime, pode responder?"
    Joseph "Ah... Com certeza."
    jump perguntasjoseph
    
label perguntasjoseph:
    menu:
        "Motivo da pressa dois dias atrás" if doisdiasatras == 0:
            Nathan "Queria saber o por que você estava correndo tanto na noite em que a casa da Vivian foi assaltada, pelo horário do crime, se alinha perfeitamente com a teoria de que você é o culpado."
            Joseph "Não, não, eu nunca faria uma coisa dessas, eu só estava correndo aquele dia porque eu vi o David jogando algo na janela dela, parecia um tijolo."
            Joseph "Outra coisa, eu perdi a minha chave nesse dia, vocês por acaso viram ela?"
            Vivian "Ah sim, o Nathan me entregou elas, usamos elas pra coletar as evidências aqui."
            $ doisdiasatras += 1
            
        "Motivo de estar mancando" if mancada == 0:
            Nathan "Uma coisa bem me incomodando, por que você vem mancando? Vi que tinha um corte na sua perna, se o ladrão tem entrado pelas janelas, faria sentido ele se machucar dessa forma"
            Joseph "Ah isso? Eu estava limpando o meu aquário antigo em casa e acabei derrubando ele, quando ele quebrou, ele cortou minha perna em alguns lugares, tenho mancado desde então."
            Vivian "Mas você ta bem? Espero que isso melhore logo..."
            Joseph "Não tive tempo de passar no hospital ainda, mas eu planejo ir o mais cedo possível."
            Joseph "Obrigado por se importar Vivian."
            $ mancada += 1
            
        "Motivo das provas estarem no cofre" if perguntacofre == 0:
            Nathan "Ontem nós olhamos o cofre que você"
            $ perguntacofre += 1
    if perguntacofre >= 1 and mancada >= 1 and doisdiasatras >= 1:
        jump bibliotecaday6continua
    else:
        jump perguntasjoseph
label bibliotecaday6continua:
    pause
            
    

#(a primeira coisa dita no livro de como abrir cofres antigos é testar senhas como 1, 2, 3 e 4)

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
# Lucas liga falando algo horrivel aconteceu sobre a erika, e na verdade ela só soltou outro gato na loja
#voce chama erika pra sair e voces conversam na rua
#ela pergunta o que você vai querer fazer da vida e voce responde que quer ser um investigador enquanto ela quer ser abrir a propria floricultura
# "E foi assim que eu resolvi o meu primeiro caso de muitos (frase de efeito final)"