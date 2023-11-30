label delegaciavivian2:
    show bg delegacia frente dia with dissolve
    pause 1.0
    show bg delegacia frente dia tarde with dissolve
    pause 1.0
    show bg delegacia dentro with dissolve
    pause 1.0
    show halfblack
    "Vivian estava trabalhando na recepção, então assim que entrei, ela vem me cumprimentar."
    show vivian f2 at right 
    Vivian "Nathan! Que surpresa vê-lo por aqui de novo. O que posso fazer por você hoje?"
    show nate n at left
    Nathan "Oi, Vivian. Desculpa te incomodar de novo, mas eu esbarrei com o Joseph ontem à noite enquanto voltava pra casa." 
    Nathan "Ele parecia bem apressado, acredito que ele tenha tramado alguma."
    Nathan "Ele derrubou essas chaves, acho que elas são dos cadeados da biblioteca. Achei melhor vir aqui falar com você sobre isso."
    show vivian n
    Vivian "Ontem à noite? Você tem certeza?"
    show nate s
    Nathan "Sim, por que?"
    show vivian b
    Vivian "O ladrão invadiu minha casa ontem à noite, mesma situação do tijolo e tudo mais, só que dessa vez ele não chegou a levar nada."
    show vivian n
    Vivian "Você se importaria de me entregar essas chaves?"
    show nate ns
    Nathan "Ah sim, claro!"
    $ renpy.notify("Você entrega a chave para Vivian analisar.")
    Vivian "Interessante. Essas são de fato as chaves da biblioteca."
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
    "Então eu e Vivian fomos até a biblioteca."
    hide nate 
    hide vivian
    jump bibliotecaday5

label bibliotecaday5:
    show bg biblioteca fora tarde with dissolve
    pause 1.0
    show bg biblioteca dentro tarde with dissolve
    pause 1.0
    show halfblack
    "Joseph não veio à biblioteca hoje, deve ser porque pegamos a chave dele. Nesta hora, ele deve estar procurando essa coisinha como louco em casa."
    show vivian n at right
    Vivian "Tá bom, Nathan. Vamos investigar a biblioteca juntos. Mas lembre-se, estamos agindo sob nossa própria responsabilidade."
    show nate n at left
    Nathan "Blá, blá, blá. É só a gente seguir com cuidado que vai dar tudo certo. Quanto mais rápido encontrarmos algo, mais rápido a gente vaza."
    Vivian "Tudo bem, você pode investigar o que quiser aí, eu vou ver se encontro algo nas câmeras. Se o Joseph for o mesmo da época que a gente namorava, ele usa a mesma senha em tudo!"
    "A Vivian entrou em uma sala apenas para funcionários para poder olhar as gravações antigas."
    Nathan "Agora é minha vez. Por onde eu começo?"
    hide nate 
    hide vivian
    hide halfblack
    jump bibliotecaday5procura

label bibliotecaday5procura:
    menu:
        "Estante":
            show halfblack
            show nate n at left
            Nathan "Aqui só tem alguns livros infantis, são muito finos pra esconder algo..."
            $ procuraestante += 1
            hide halfblack
            jump bibliotecaday5procura
        "Bancada principal" if procuraestante >= 1:
            show halfblack
            show nate n at left
            Nathan "Documentos sobre emprestar e devolver livros, parece que o Lucas pegou algo emprestado faz alguns meses e não devolveu ainda."
            hide nate
            $ procurabancada += 1
            hide halfblack
            jump bibliotecaday5procura
        "Prateleira" if procurabancada >= 1:
            show halfblack
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
            hide camilla 
            hide nate
            hide john
            hide halfblack
            jump bibliotecaday5procura
        "Levantar o tapete" if procuraprateleira >= 1:
            show halfblack
            "Assim que eu levanto o tapete, um cofre é revelado."
            show bg biblioteca segredo tarde with dissolve
            scene bg biblioteca segredo tarde
            pause
            show halfblack
            show nate n at left
            Nathan "UM COFRE?"
            "Vivian volta da sala das câmeras."
            show vivian n at right
            Vivian "Você encontrou um cofre? Eu não sabia que eles tinham um cofre na biblioteca."
            Nathan "Eu muito menos. Você acha que a gente consegue abrir ele sem senha?"
            Vivian "Conseguir a gente até consegue, mas a pergunta mesmo é se a gente tem tempo pra fazer isso."
            hide vivian
            show john n at right
            John "Nathan, eu acho que a gente viu algo relacionado a como abrir esse tipo de cofre na sala do seu pai, não?"
            John "Você não acha que seria melhor a gente tentar buscar essa senha antes? Ficar aqui por tempo demais tentando pode chamar muita atenção, precisamos ser rápidos!"
            hide nate
            hide john
            hide vivian
            hide halfblack
            jump bibliotecaday5continuação
   
label bibliotecaday5continuação:
    menu:
        "Chutar a senha":
            show halfblack
            show nate n at left
            Nathan "Acho que podemos tentar chutar a senha. Talvez tenhamos sorte e acertemos de primeira."
            Nathan "Vivian, você conhece bem o Joseph né? Vou precisar da sua ajuda aqui."
            show vivian f2 at right
            Vivian "Claro! Do que você precisa?"
            Nathan "Pode me dizer o dia do aniversário do Joseph?"
            "Disse deitando no tapete e encostando meu ouvido a porta do cofre."
            show vivian f
            Vivian "Que eu me lembre é dia 26 de março. Por quê?"
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
            Camilla "Nathan antes que você se envergonhe de novo perguntando essas coisas, você já pensou em só colocar '1, 2, 3, 4'?"
            show camilla f
            Camilla "Pode até ser idiota, mas de novo, a última ideia idiota que a gente teve nos revelou o cofre não foi?"
            show nate ns
            Nathan "...Tá, valeu, deixa eu testar isso então."
            hide camilla
            show vivian n at right
            Vivian "Com quem você tá falando?"
            show nate f2
            Nathan "Ahn!? Não, eu tava falando sozinho mesmo."
            Vivian "Okay?"
            show nate n
            Nathan "Desculpa as perguntas meio invasivas aliás."
            Vivian "Não não, tudo bem."
            hide vivian
            show john n at right
            John "Eita, essa foi por pouco, quase que ela pensa que você é maluco."
            "Respiro fundo e tento uma última vez, com medo do cofre se trancar sozinho."
            "1...{w=0.5} 2...{w=0.5} 3...{w=0.5} 4...{w=2.0}{nw}"
            "{i}Clink!{/i}"
            $ arrombaranel += 1
            "O cofre se abre revelando todos os objetos roubados nos crimes recentes."
            show john b2
            John "Não é possível que a senha era algo estúpido assim."
            hide john
            show vivian s2 at right
            Vivian "Não pode ser..."
            Nathan "Acho que minhas suspeitas não eram tão infundamentadas assim."
            Nathan "Mas ainda precisamos interroga-lo para saber o porque dele ter cometido os crimes."
            Vivian "Enquanto eu olhava as câmeras, percebi que o Joseph não estava na biblioteca durante o horário dos crimes, mas..."
            show vivian n
            Vivian "Ainda é difícil de acreditar que ele cometeria tais atos, vou me encontrar com ele depois pra interrogá-lo."
            Vivian "Acho que é melhor a gente se separar agora, vou te passar o meu número e você já pode ir pra casa, qualquer coisa eu entro em contato."
            $ renpy.notify("Vivian te passou o número dela.")
            "Após Vivian me entregar o número dela, ela sai pela porta. Eu vou logo em seguida, direto pra casa."
            hide vivian
            hide nate
            hide halfblack
            jump casadia5
            #se você tenta chutar as senhas ao sair da biblioteca já está escurecendo
            
        "Ir buscar a senha":
            show halfblack
            show nate n at left
            Nathan "Você tem razão, é melhor não mexermos no cofre por agora, acha que teria alguma forma de descobrir a senha sem a tentar abrir ele aqui?"
            show vivian n at right
            Vivian "O Joseph deve saber a senha... O cofre é dele afinal, vou tentar perguntar pra ele mais tarde."
            Vivian "Na verdade, acho melhor eu ir atrás dele agora mesmo, até outra hora Nathan, toma meu telefone, você sabe onde me achar se precisar."
            Vivian "Antes que eu me esqueça, de acordo com as câmeras, Joseph não estava por aqui no horário do crime, não queria ter que fazer isso, mas vou ter que interrogar ele mais a fundo."
            Nathan "Ele não estava aqui? Mas ele praticamente nunca sai da biblioteca."
            Vivian "Essa é a parte esquisita, a câmera é meio ruim por ser antiga, mas eu consegui ver ele saindo daqui claramente."
            show vivian f
            Vivian "Bom, parece que nós dois conseguimos ótimas informações nesse tempinho. Acho que devíamos nos separar por agora, se eu descobrir algo a mais sobre o Joseph, vou te ligar ok?"
            hide vivian 
            show john n at right
            John "Ei, não tinha um documento na sala do seu pai falando sobre destrancar cofres? Talvez ele seja útil."
            Nathan "Você tem razão, mas com certeza eles melhoraram a segurança da delegacia desde que a gente roubou os arquivos."
            hide john 
            show camilla n at right
            Camilla "Acho que não custa tentar, qualquer coisa você poderia enganar o seu pai e pegar enquanto ele está distraído."
            Nathan "Hmm, vou pensar no que fazer e decido quando chegarmos na delegacia."
            "A vivian então saiu da biblioteca anotando sobre as coisas que ela descobriu por aqui."
            hide vivian 
            hide camilla 
            hide john 
            hide nate 
            hide halfblack
            jump invasao2


            
        #nessa opçao ainda ta de tarde e quando vc chega na delegacia ta de noite

label invasao2:
    show bg delegacia frente dia tarde with dissolve
    show bg delegacia frente dia noite with dissolve
    show halfblack
    show nate s2 at left
    Nathan "Vocês acham que isso é uma boa ideia mesmo?"
    show john n at right
    John "É seu pai, não é como se você tivesse a melhor reputação com ele já, né?"
    hide john
    show camilla n at right
    Camilla "E além do mais, se você não pegar essa senha hoje, o emprego da Vivian está em jogo agora."
    hide camilla
    hide john
    hide nate
    hide halfblack
    menu:
        "Invadir quando a delegacia estiver vazia":
            show halfblack
            show nate n at left 
            Nathan "A gente consegue esperar até a delegacia esvaziar, aí a gente entra."
            show john f at right
            John "Vai querer invadir de novo? Gostei disso."
            hide john
            show camilla n at right
            Camilla "Eu não posso opinar dessa vez, é uma ideia boa mesmo."
            Nathan "Ta bom então, é agora ou nunca."
            hide halfblack
            hide camilla
            hide nate
            jump invadir2
        "Tentar pegar o livro enquanto seu pai está lá":
            show halfblack
            Nathan "Ta bom então, é agora ou nunca."
            hide halfblack
            hide camilla
            hide john
            hide nate
            jump delegaciapai2

label invadir2:
    "Após uns 30 minutos esperando do lado de fora em um dos arbustos, a delegacia fica vazia."
    show nate b at left
    Nathan "Agora é a hora, vamos nessa."
    hide nate
    show bg delegacia dentro with dissolve
    pause (1.5)
    show bg sala do pai escuro with dissolve
    show halfblack
    show john n at right
    John "Você lembra onde estava o livro? A sala tá bem escura, mais do que da última vez."
    show nate n at left
    Nathan "Eu acho que estava..."
    hide john
    hide nate
    jump escolhainvasao

label escolhainvasao:
    menu:
        "Na mesa dele":
            show nate n at left
            Nathan "Eu acho que estava na mesa dele, mas eu não lembro, vamos dar uma olhada."
            "Me aproximo da mesa dele, ainda estava bem escuro, mas toquei em algo que parecia um livro."
            John "Eu acho que esse deve ser o livro, vamos embora antes que fique tarde demais, sua mãe já deve estar bem preocupada pelo horário."
            hide john 
            hide nate 
            jump casadia5
        "Nas gavetas":
            show camilla n at right
            Camilla "Acho que faria sentido guardar um livro em uma das gavetas, não?"
            show nate n at left
            Nathan "Pode ser, vamos olhar."
            "Faço força para abrir as gavetas novamente."
            show nate b
            Nathan "Que nem da última vez, ela continua emperrada."
            Camilla "Valeu a pena a tentativa..."
            hide camilla 
            hide nate
            jump escolhainvasao
        "No armário" if avalanche == 0:
            "Quando eu abro o armário, uma cachoeira de documentos cai; alguém não aprendeu a se organizar nessa sala."
            $ avalanche += 1
            jump escolhainvasao
            pause

label delegaciapai2:
    scene bg sala do pai clara with dissolve 
    scene bg sala do pai clara
    show halfblack
    "Eu entro na sala do meu pai devagar, pra não deixá-lo estressado."
    show nate ns at left
    Nathan "Opa, consegue conversar?"
    show pai b at right
    Pai "O que você tá fazendo aqui? É bom que você não tenha vindo até pra falar sobre esse caso recente. Já estou cansado de dizer para não se meter nos assuntos do meu trabalho."
    Nathan "Não é nada disso não, eu tava passando por aqui e queria perguntar se você conseguiria me deixar em casa depois que terminar o trabalho."
    show pai n
    Pai "Ah, se é só isso, consigo sim. Só sai da minha sala por favor."
    Nathan "Mas por quê? Eu não to te atrapalhando nem nada."
    show pai b
    Pai "Mas você vai me atrapalhar se continuar falando."
    Nathan "Tá bom, tudo bem, eu fico quieto, bem aqui."
    "Me aproximo da mesa dele, e vejo o mesmo livro que tinha visto aquele dia."
    hide pai
    show john n at right
    John "Ali. É ele, o livro! ''Manual da polícia de como destrancar cofres e fechaduras''!"
    hide john
    show camilla n at right
    Camilla "Agora é a sua chance! Pega ele!"
    hide camilla
    show pai n at right
    Pai "Nathan, só espera do lado de fora da minha sala por favor."
    Nathan "Tá bom, eu saio, não vou te atrapalhar mais, eu juro."
    "Assim que eu termino a frase, aproveito que ele se distraiu e puxo o livro da mesa, saindo o mais rápido possível da sala com o livro na mão."
    hide john
    hide pai
    hide camilla
    hide nate

label casadia5:
    scene bg quarto com pistas noite with dissolve
    show halfblack
    "Chegando em casa, me sinto extremamente aliviado, todo esse meu trabalho duro finalmente vai chegar em algum lugar."
    show camilla f at right
    Camilla "E aí, detetive? Como você se sente?"
    show nate n at left
    Nathan "Exausto, esses últimos 5 dias têm sido... algo, definitivamente."
    hide camilla
    show john f at right
    John "Algo bom, você tem evoluído bastante, pelo menos tem feito algo a mais do que ficar trancado no quarto o dia todo."
    hide john
    show camilla f at right
    Camilla "De qualquer forma, você tem tudo que precisa pra provar a culpa do Joseph."
    hide camilla 
    show john n at right
    John "Agora é só esperar o contato da Vivian. Por hora acho que você merece pelo menos uma noite de sono."
    show nate f2 at left
    Nathan "Certo, boa noite vocês dois."
    hide nate 
    hide camilla 
    hide john
    pause
    jump startday6

label startday6:
    scene bg quarto com pistas dia with dissolve
    show halfblack
    "Eu acho que a primeira vez nessa semana que eu consigo levantar tranquilamente, que milagre!"
    show camilla f at right
    Camilla "Bom dia, Nathan! Como se sente?"
    show nate ns at left
    Nathan "Revigorado, não durmo bem assim faz um tempo."
    Nathan "Vou ligar pra Vivian agora mesmo, não quero perder tempo."
    "Pego o telefone e disco o número que a Vivian me deu ontem. Ela atende bem rápido."
    hide camilla
    Vivian "Bom dia, esse é o celular da Vivian, quem fala?"
    show nate f
    Nathan "Oi Vivian! Aqui é o Nathan, descobriu algo de ontem pra hoje?"
    Vivian "Ah! Nathan! Eu achei o Joseph, venha nos encontrar na biblioteca agora, não consigo falar tudo pelo telefone, é bem importante."
    show nate ns
    Nathan "Ah, sim, claro. Encontro vocês lá!"
    "Desligo o telefonema."
    show nate f2
    Nathan "Vamos rápido!"
    show john ex at right
    John "Não sei se você já percebeu, mas meio que a gente tá preso a você e não consegue andar."
    show nate ch
    Nathan "Eu esqueci."
    show nate ns
    Nathan "Só vamos logo, por favor."
    hide nate 
    hide john
    hide halfblack
    "Saio correndo de casa até a biblioteca."
    jump bibliotecaday6

label bibliotecaday6:
    show bg biblioteca dentro dia with dissolve
    scene bg biblioteca dentro dia
    show halfblack
    show vivian f at right
    Vivian "Aí está você, Nathan! O Joseph está ali nos fundos."
    Vivian "Você descobriu mais alguma coisa nesse meio tempo?"
    show nate n at left
    Nathan "Não muito, na verdade."
    "Joseph chega, ele ainda estava mancando um pouco."
    hide vivian 
    show joseph f at right
    Joseph "Bom dia, Vivian! E garoto que saiu correndo da biblioteca no outro dia, nunca cheguei a perguntar seu nome, perdão."
    Nathan "É Nathan, senhor."
    Joseph "Não precisa me chamar de senhor, está tudo bem."
    hide joseph
    show vivian n at right
    Vivian "Joseph, precisamos te perguntar algumas coisas."
    hide vivian 
    show joseph f at right
    Joseph "Certo! O que vocês precisam perguntar?"
    hide joseph 
    show vivian n at right
    Vivian "Sobre o dia do crime, pode responder?"
    hide vivian
    show joseph n at right
    Joseph "Ah... Com certeza."
    jump perguntasjoseph
    
label perguntasjoseph:
    hide vivian 
    hide nate 
    hide joseph 
    menu:
        "Perguntar o motivo da pressa dois dias atrás" if doisdiasatras == 0:
            show nate n at left
            Nathan "Queria saber o por que você estava correndo tanto na noite em que a casa da Vivian foi assaltada, pelo horário do crime, se alinha perfeitamente com a teoria de que você é o culpado."
            show joseph s at right
            Joseph "Não, não, eu nunca faria uma coisa dessas, eu só estava correndo aquele dia porque eu vi o David jogando algo na janela dela, parecia um tijolo."
            Joseph "Logo após me encontrar com você eu fui nocauteado e jogado em uma lixeira."
            hide joseph
            show vivian n at right
            Vivian "É verdade, eu que encontrei ele."
            show vivian f2
            Vivian "Você estava bem fedido a lixo por sinal, hahaha."
            hide vivian
            show joseph s at right
            Joseph "Foi mal, não foi bem uma escolha minha ser jogado em uma caçamba..."
            show joseph n
            Joseph "Outra coisa, eu perdi a minha chave nesse dia, vocês por acaso viram ela?"
            hide joseph 
            show vivian n at right
            Vivian "Ah sim, o Nathan me entregou elas, usamos elas pra coletar as evidências aqui."
            $ doisdiasatras += 1
            
        "Perguntar o motivo de estar mancando" if mancada == 0:
            show nate n at left
            Nathan "Uma coisa vem me incomodando, por que você vem mancando? Vi que tinha um corte na sua perna, se o ladrão tem entrado pelas janelas, faria sentido ele se machucar dessa forma."
            show joseph n at right
            Joseph "Ah isso? Eu estava limpando o meu aquário antigo em casa e acabei derrubando ele, quando ele quebrou, ele cortou minha perna em alguns lugares, tenho mancado desde então."
            hide joseph 
            show vivian s at right
            Vivian "Mas você ta bem? Espero que isso melhore logo..."
            hide vivian 
            show joseph s at right
            Joseph "Não tive tempo de passar no hospital ainda, mas eu planejo ir o mais cedo possível."
            show joseph f
            Joseph "Obrigado por se importar Vivian. Também é por isso que a biblioteca estava fechada alguns dias atrás, não tive como vir trabalhar por conta da lesão."
            $ mancada += 1
            
        "Perguntar sobre o cofre embaixo do tapete" if perguntacofre == 0:
            show nate ns at left
            Nathan "Ontem nós encontramos o cofre que tem embaixo de um dos tapetes."
            show joseph f at right
            Joseph "Ah! Vocês o encontraram? Eu instalei ele uns tempos atrás, mas percebi que eu não tinha utilidade nenhuma para ele."
            if arrombaranel >= 1:
                show nate n at left
                Nathan "Nós o abrimos e encontramos vários dos objetos roubados nos crimes dos últimos dias, como você explica isso?"
                show joseph s at right
                Joseph "Como??? Não faz sentido, eu nunca cheguei a usar esse cofre."
                hide joseph 
                show vivian n at right
                Vivian "É verdade Joseph, eu estava com ele e vi tudo."
                "Abrimos o cofre e mostramos as provas irrefutáveis para o Joseph."
                hide vivian
                show joseph s at right
                Joseph "Isso não faz o menor sentido! Eu posso provar que não fui eu, tenho as gravações nas cameras!"
                hide joseph 
                show vivian s2 at right
                Vivian "Eu já verifiquei. As gravações foram deletadas!"
                hide vivian 
                show joseph s at right
                Joseph "Eu guardo um backup extra de todas as gravações por um mês, veja!"
                "Joseph nos mostra as gravações completas e nitidamente conseguimos ver o rosto de David no momento em que ele derruba uma das alianças do casal."
            else:
                show nate n at left
                Nathan "Ainda não conseguimos abri-lo, não temos a senha."
                show joseph n at right
                Joseph "Eu uso a senha..."
                show joseph f
                Joseph "Nossa que vergonha!"
                Joseph "A senha é o aniversário da Vivian..."
                hide joseph 
                show vivian s at right
                Vivian "..."
                hide vivian 
                show camilla ex at right
                Camilla "Eita!"
                show nate s
                Nathan "Nos já tentamos isso, não é essa senha!"
                hide camilla 
                show joseph s at right
                Joseph "Estranho..."
                "Joseph tenta destrancar o cofre sem sucesso e então eu pego o livro que roubei da sala do meu pai."
                show nate ns
                Nathan "Vamos tentar usar isso."
                hide joseph 
                show vivian f at right
                Vivian "Um livro de destrancar cofres? Que conveniente."
                "Abro o livro e a primeira coisa escrita é, tentar senhas simples como 1, 2, 3 e 4."
                hide vivian 
                show john ex at right
                John "Isso é tão ridículo que eu fico me perguntando porque de não termos testado, mas acho que é impossível ser isso."
                "Tento a senha 1, 2, 3 e 4 e cofre se abre."
                show nate s at left
                Nathan "..."
                show john n at right
                John "..."
                hide john 
                show camilla n at right
                Camilla "..."
                hide camilla
                show joseph s at right
                Joseph "..."
                hide joseph 
                show vivian s at right
                Vivian "..."
                "Ao abrir o cofre, encontramos todas as provas necessárias, todos os objetos roubados nos crimes recentes."
                hide vivian 
                show joseph s at right
                Joseph "Não pode ser, não faz sentido nenhum, eu nunca faria uma coisa dessas."
                hide joseph 
                show vivian n at right
                Vivian "Joseph, eu quero acreditar em você, mas tudo que está aqui prova o contrário..."
                hide vivian 
                show joseph s at right
                Joseph "Espere, eu tenho como provar que não fui eu, eu tenho as gravações das cameras!"
                hide joseph
                show vivian s at right
                Vivian "Eu já verifiquei. As gravações foram deletadas!"
                hide vivian 
                show joseph s at right
                Joseph "Eu guardo um backup extra de todas as gravações por um mês, veja!"
                "Joseph nos mostra as gravações completas e nitidamente conseguimos ver o rosto de David no momento em que ele derruba uma das alianças do casal."
                # ඞ
            $ perguntacofre += 1

    if perguntacofre >= 1 and mancada >= 1 and doisdiasatras >= 1:
        jump bibliotecaday6continua
    else:
        jump perguntasjoseph

label bibliotecaday6continua:
    show nate n at left
    Nathan "Agora estou vendo um padrão aqui... Joseph, você mencionou que viu o David jogando algo na janela da Vivian naquela noite, certo?"
    show joseph n at right
    Joseph "Sim, exatamente. Ele parecia estar causando problemas."
    show nate b
    Nathan "Tudo se encaixa perfeitamente. Não acredito muito no que estou dizendo mas... Joseph, você é inocente. O verdadeiro ladrão é o David."
    show nate n
    Nathan "E as gravações provam que foi ele."
    show joseph s
    Joseph "Mas por quê ele faria isso?"
    Nathan "Eu não sei, mas precisamos encontrar ele e fazê-lo admitir tudo!"
    hide joseph
    show vivian n at right
    Vivian "..."
    Vivian "Eu sei que eu posso estar sendo super chata, mas Joseph, você acha que consegue colocar uma cópia das gravações nesse pendrive?"
    Vivian "Vou precisar de mais do que ''Foi ele'', para provar esse caso, entende?"
    show vivian b
    Vivian "Não consigo acreditar que o David é uma pessoa tão suja!"
    hide vivian
    show joseph f at right
    Joseph "Claro com certeza, vamos lá pra dentro."
    hide joseph
    hide nate
    scene bg biblioteca segredo dia with dissolve 
    show halfblack
    show vivian n at right
    Vivian "Você fica aí Nathan."
    hide vivian
    show joseph f at right
    Joseph "Voltamos em no máximo 10 minutos, isso se o sistema não travar de novo."
    hide joseph
    show john n at right
    John "Nossa... Será que eles foram se pegar?"
    hide john
    show camilla b at right
    Camilla "JOHN!!"
    hide camilla
    show john f at right
    John "Foi mal, não podia perder essa oportunidade, haha."
    hide john
    hide camilla
    hide nate
    pause(2.0)
    "Joseph e Vivian saem da sala de segurança."
    pause(1.0)

    show bg biblioteca segredo dia with hpunch
    show halfblack
    show vivian b at left
    Vivian "Nathan, Joseph!"
    show bg biblioteca segredo dia with hpunch
    show halfblack
    Vivian "Vamos para a delegacia agora mesmo!"
    hide vivian
    show joseph n at right
    Joseph "Vivian, respira fundo."
    "Ela parou pra respirar fundo e se acalmar."
    show vivian n at left
    Vivian "Perdão. Vamos para a delegacia."
    show joseph s
    Joseph "Eu tenho que ir junto? A biblioteca está uma bagunça."
    show vivian b
    Vivian "Claro que você tem que ir, você é a vítima."
    hide vivian 
    show nate n at left
    Nathan "{i}Acho bom você não tentar discordar dela agora Joseph.{/i}"
    show joseph n
    Joseph "{i}Você tem razão garoto, vamos seguir o plano dela.{/i}"
    "Vivian sai andando com passos pesados da biblioteca, eu e Joseph seguimos ela logo depois."
    jump delegaciadia6
            
label delegaciadia6:
    scene bg delegacia frente dia with dissolve
    "Saímos às pressas para a delegacia para mostrar as evidências que possuíamos para o meu pai."
    David "Eu estou dizendo, senhor! Tenho todas as evidências que comprovam que o Bibliotecário Joseph é o culpado!"
    scene bg delegacia dentro with dissolve
    Pai "Certo, impressionantemente esse relatório está muito convincente, vou encaminhar um mandado para investigar a biblioteca-"
    scene bg sala do pai clara with dissolve
    show halfblack
    show nate b at left
    Nathan "ESPERE, PARADO JÁ AÍ, DAVID!"
    show pai s at right
    Pai "Nathan!? Vivian!? Que alvoroço é esse??"
    hide pai 
    show david s at right
    David "V-Vivian!? O que houve? E por que esse homem está aqui?"
    "David aponta para o Joseph."
    Nathan "Podemos provar que o culpado dos crimes é o David e não o Joseph!"
    show david f 
    David "Senhor Nathan! Que surpresa! Mas acho que o senhor está equivocado! Essa é uma acusação muito séria que está fazendo!"
    David "E como já ia falando ao senhor delegado Fábio, tenho provas que relatam que o culpado é o Joseph!! Só preciso de um mandato oficial para investigar a biblioteca e poderei provar o que estou dizendo!"
    hide david 
    show joseph b at right
    Joseph "Mas isso é um absurdo!! Você sabe muito bem que eu não fiz nada disso."
    hide joseph 
    show vivian b at right
    Vivian "Você tem como provar, é? Interessante, eu tenho gravações que dizem o contrário!"
    hide vivian
    show pai s2 at right
    Pai "Calma, o que está acontecendo aqui? Vivian, que gravações são essas?"
    hide pai 
    show vivian b at right
    Vivian "Veja você mesmo, delegado."
    hide vivian
    show david n at right
    David "Eu acho que não é necessário. Vamos acalmar os ânimos..."
    hide david 
    show pai b at right
    Pai "Deixe me ver essas gravações, Vivian."
    "Meu pai coloca as gravações e vê o David arrombando as fechaduras da biblioteca e colocando os itens roubados no cofre pouco tempo depois dos crimes terem acontecido oficialmente."
    Pai "Mas o que é isso?"
    hide pai 
    show david ex at right
    David "Eu posso explicar, err"
    "David tenta sair correndo pela porta da delegacia mas é impedido por Joseph."
    Nathan "Por que você fez isso David? Achei que você era um cara legal!"
    show david b at right
    David "Por que eu fiz isso? Sério? Todos me tratam como idiota, se eu conseguisse resolver um mistério que ninguém conseguiu eu seria visto como um herói e não teria mais que ouvir o delegado me diminuindo!"
    David "{size=*0.75}E de quebra esse malandro aí ia preso e eu finalmente poderia ficar com minha linda Vivian...{/size}"
    hide david
    show vivian s at right
    Vivian "???????"
    show vivian b
    Vivian "Você é maluco! Eu nunca ficaria com você!!"
    hide vivian 
    show pai b at right
    Pai "Acho que eu já vi o bastante. David, você está preso!"
    "Meu pai se levanta e algema David."
    Pai "Meus parabéns pelo seu trabalho Vivian, ótima resolução do caso."
    hide pai 
    show vivian f at right
    Vivian "Senhor, você deveria estar agradecendo ao seu filho por isso, foi ele que descobriu tudo! Eu só o ajudei."
    hide vivian 
    show pai s at right
    show nate ns
    Pai "Sério? Nathan, sei que fui duro com você e não tenho direito de dizer isso, mas, bom trabalho, filho! Estou orgulhoso de você."
    "Meu pai me abraça e leva o David algemado para fora, Vivian e Joseph se despedem e eu volto para casa."

    scene bg quarto com pistas noite with dissolve
    show halfblack
    show nate f2 at left
    Nathan "Finalmente, acabou, conseguimos!"
    show john f at right
    John "Parabéns por ter solucionado o mistério, Nathan!"
    hide john 
    show camilla f at right 
    Camilla "Estamos orgulhosos de você!"
    Nathan "Eu não teria conseguido sem vocês, obrigado!"
    show camilla ex
    Camilla "Que isso, estamos sempre aqui por você. O que você vai fazer agora?"
    show nate ns
    Nathan "Acho que vou tomar coragem e fazer algo que já devia ter feito há muito tempo."
    hide camilla 
    show john n at right
    John "Não pode ser, você vai?..."
    show nate f2
    Nathan "Sim, vou chamar a Erika pra sair."
    show nate n
    "Eu ligo para Erika, meu coração está bastante acelerado de ansiedade, cada vez que o telefone toca sinto uma leve parada cardíaca até que ela atende."
    hide john 
    Erika "Alô, Nate? Aconteceu alguma coisa? Está bem tarde."
    show nate ns 
    Nathan "Oi, Erika, desculpe, tá tudo bem sim, na verdade está tudo ótimo, conseguimos pegar o verdadeiro ladrão."
    Erika "Sério?? E aí?? O que aconteceu?"
    show nate f
    Nathan "Acontece que o ladrão era o David esse tempo todo, ele estava fazendo isso como uma forma de se vingar e solucionar o crime que ele mesmo cometeu."
    Nathan "Ele achou que fazendo isso as pessoas iam vê-lo como um herói e parariam de pegar no pé dele."
    Erika "Nossa... Dá até pra sentir um pouco de pena dele..."
    show nate n
    Nathan "É..."
    show nate s
    Nathan "Bom, na verdade eu não te liguei pra falar disso. Escuta, err, eu..."
    Erika "Você?..."
    show nate s2
    Nathan "Você quer sair comigo amanhã? Tipo, pra um encontro?"

    Erika "SIM, CLARO."
    Erika "..." 
    Erika "Quero dizer, sim, claro, eu adoraria."
    show nate f2
    Nathan "Ok, a gente se encontra amanhã na frente."
    menu: 
        "Mercado":
            Nathan "Ok, a gente se encontra amanhã na frente{fast} do mercado."
        "Biblioteca":
            Nathan "Ok, a gente se encontra amanhã na frente{fast} da biblioteca."
            $ fofoca += 1

    Erika "Pode ser! Te vejo lá amanhã então, boa noite Nate."
    show nate ns
    Nathan "Boa noite Erika, até amanhã."
    show nate n
    Nathan "..."
    show john f at right
    John "E aí? Como foi? Pela sua cara parece que deu bom."
    show nate f
    Nathan "Marcamos um encontro."
    hide john 
    show camilla f at right
    Camilla "BOAAA, Vamos ter certeza de não te atrapalhar amanhã Nate, não se preocupe."
    hide camilla 
    show john f at right
    John "Vai dormir agora campeão, que você vai ter um dia cheio amanhã."
    "Me deito cheio de ansiedade e tento dormir o melhor que posso para o dia seguinte."
    jump EpilogoBom

label EpilogoBom:
    scene bg quarto com pistas dia with dissolve
    show halfblack
    "Acordo cedo e vou escovar os dentes e tomar um banho para meu encontro com a Erika."
    show john f at right
    John "É hoje, o grande dia, boa sorte lá, Nathan!"
    hide john 
    show camilla f at right
    Camilla "Estaremos torcendo por você!"
    hide camilla 
    "Termino de me aprontar e antes de sair de casa a Erika me liga."
    show nate f at left
    Erika "Nate? Tudo pronto? Já estou a caminho."
    Nathan "Já estou saindo, pode ficar tranquila."
    
    if fofoca == 0:
        scene bg mercado dia with dissolve
        show halfblack
        "Eu chego na frente do mercado praticamente ao mesmo tempo que Erika."
        show erika n2 at right
        Erika "E aí? Vamos?"
        show nate ns at left
        Nathan "Bora."
        show erika n
        Erika "Não quer passar pra ver os meninos? Eles estão bem felizes porque você conseguiu ajudar eles a recuperar as alianças e o dinheiro roubado do mercado."
        Nathan "Nah, outra hora eu falo com eles."

    else:
        if fofoca >= 1:
            scene bg biblioteca fora dia with dissolve
            show halfblack
            "Eu chego na biblioteca um pouco depois de Erika; ela parece um pouco surpresa."
            show nate s at left
            Nathan "Consegui! Cheguei. {i}*Ofegante{/i}"
            show erika n2 at right 
            Erika "Você não vai acreditar no que eu acabei de ver."
            show nate ns
            Nathan "O quê?"
            show erika n
            Erika "A Vivian e o bibliotecário... acho que eles estão namorando!"
            show nate f2 
            Nathan "O Joseph? Sério? Como você soube???"
            show erika n2
            Erika "Acabei de ver os dois se beijando bem aqui antes de você chegar."
            Erika "Bem que você podia fazer o mesmo..."
            show nate s2 
            Nathan "... ... ..."
            show erika n
            Erika "Brincadeira, vamos indo?"
            show nate f 
            Nathan "V-Vamos!"

    scene bg rua dia with dissolve
    show halfblack
    show erika n2 at right
    Erika "E aí, pra onde a gente vai?"
    show nate f at left
    Nathan "É surpresa."
    show erika n
    Erika "Hmm, tá bom, e aí? Já decidiu o que vai fazer da vida? Eu continuo com o plano de abrir minha floricultura."
    Erika "Ainda pretende continuar viajando pra descobrir o que fazer?"
    Nathan "Na verdade, já decidi sim. Eu descobri que quero ser um investigador da polícia; talvez eu tenha jeito pra isso."
    show erika n2
    Erika "Realmente, acho que você tem mesmo!"
    pause(0.5)
    show black with dissolve
    pause
    jump quartodia7bom

label quartodia7bom:
    scene black with dissolve
    with Pause(1)
    show text "{color=#FFFFFF}E foi assim que eu resolvi o meu primeiro caso investigativo e criei coragem pra chamar minha melhor amiga pra sair num encontro!{/color}"
    with Pause(3)
    scene black with dissolve
    with Pause(1.5)
pause