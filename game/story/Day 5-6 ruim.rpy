label dia5finalruim:
    Nathan "Erika! Espera!"
    Erika "Oi, e ai? deu certo?  entregou as chaves pro David?"
    Nathan "Entreguei, mas ele não me passou confiança de que ia fazer um bom trabalho..."
    Nathan "O que você acha da gente ir pra biblioteca durante a noite para tentar investigar nós mesmos?"
    Erika "Não sei não Nathan, pode ser meio arriscado..."
    Nathan "Tudo bem, não quero fazer você se arriscar sem motivo."
    Erika "Não, eu vou junto. Acho que consigo te ajudar com uma coisa!"
    Nathan "E o que seria?"
    Erika "Você vai descobrir na hora."
    scene bg shop with dissolve
    "Então nós dois saímos e ficamos aguardando a noite cair enquanto conversávamos com os meninos."
    
    scene bg rua noite with dissolve
    Erika "Finalmente meu kit de {i}lockpick{/i} vai ser útil!"
    Nathan "Então esse era o segredo?"
    Nathan "Por que você tem um kit desses em casa?"
    Erika "..."
    Erika "Vai que... eu...{w=1.0} esqueço minha chave qualquer dia desses né?"
    Nathan "Você vai esquecer sua chave mas não uma gazua?"
    Erika "A gente pode focar no que é importante de verdade?"
    Nathan "Certo. A biblioteca."
    dJoseph "{i}Ai...{/i}"
    Erika "Que barulho foi esse?"
    dJoseph "Aqui..."
    "Olhamos pra caçamba de lixo convenientemente posicionada fora da tela."
    Nathan "Joseph?"
    Joseph "O-o que? O que aconteceu...? Como vim parar aqui? Não importa, eu preciso ir, preciso avisar a Vivian"
    Nathan "Avisar? do que você está falando?"
    Erika "Você precisa de um médico urgentemente!"
    Joseph "Agora não, preciso ver se a Vivian está bem."
    Joseph  "O David jogou um tijolo na janela dela!"
    Nathan "O quê? Mas por quê?!"
    Joseph "Eu não sei... mas tenho certeza que era ele, ele está tramando algo."
    Joseph "...Minhas chaves... Droga, perdi minhas chaves!"
    Nathan "Suas chaves? Droga... Eu as encontrei, mas entreguei elas para o David..."
    Joseph "VOCÊ O QUE?"
    Erika "Ei, calma ai, ele não sabia, e como a gente vai saber se você não ta inventando essa história inteira?"
    Joseph "Eu... Eu não posso."
    Nathan "Se o que você está dizendo é verdade precisamos ir até a biblioteca, talvez o David ainda esteja por lá, podemos grampear ele."
    Joseph "...Você tem razão, vamos."
    jump bibliotecaday5ruim

label bibliotecaday5ruim:
    scene bg biblioteca fora noite with dissolve
    "Chegamos na biblioteca mas não parece ter nada fora do comum."
    Joseph "Droga, está trancada! não temos como entrar agora."
    Erika "Minha hora de brilhar!"
    "Erika puxa um kit de gazuas e começa a destrancar as portas da biblioteca."
    "{i}Clack{/i}, a porta se abre."
    Erika "Eu sou boa demais diz aí."
    Joseph "Obrigado Erika, vamos!" 
    Nathan "Não parece ter nada de diferente aqui..."
    Joseph "De fato, melhor eu conferir as cameras, podemos descobrir o que David aprontou."
    Joseph "Enquanto vou verificar as gravações, será que vocês poderiam investigar e ver se nâo encontram nada de diferente?"
    "Joseph vai para os fundos verificar nas cameras o que ele pode encontrar"
    jump biblioteca5ruim
    
    
    
    
label biblioteca5ruim:
    scene bg biblioteca dentro noite with dissolve
    menu:
        "Estante":
            show halfblack
            show nate n at left
            Nathan "Aqui só tem alguns livros infantis, são muito finos pra esconder algo..."
            $ procuraestante += 1
            hide halfblack
        "Bancada principal" if procuraestante >= 1:
            show halfblack
            show nate n at left
            Nathan "Documentos sobre emprestar e devolver livros, parece que o Lucas pegou algo emprestado faz alguns meses e não devolveu ainda."
            show erika n at right
            Erika "Olha só, parece que o Lucas não é tão santinho como parece."
            hide nate
            $ procurabancada += 1
            hide halfblack
        "Prateleira" if procurabancada >= 1:
            show halfblack
            "Procurar essa prateleira me faz pensar quando eu comecei a investigar tudo isso. Não parece ter nada por aqui ainda."
            show nate n at left
            Nathan "Tem que ter alguma coisa por aqui, se aqui não tem nada, o David vai acabar saindo ileso."
            $ procuraprateleira += 1
            hide camilla 
            hide nate
            hide john
            hide halfblack

    if procuraprateleira >=1 and procurabancada >=1 and procuraestante >=1:
        "Joseph volta da sala dos fundos parecendo meio irritado."
        show joseph b at right
        Joseph "Droga, ele apagou tudo! até os backups!"
        show nate s at left
        Nathan "Não encontramos nada de estranho aparentemente"
        show joseph s
        Joseph "Isso é estranho..."
        hide joseph 
        show erika s at right
        Erika "Tem alguma coisa que fica escondida aqui na biblioteca? Sei lá, um {i}cofre{/i} talvez?"
        hide erika 
        show joseph f at right 
        Joseph "Na verdade, tem sim!"
        "Joseph puxa o tapete revelando um cofre escondido."
        show joseph n
        Joseph "Tem isso, mas... não tinha nada de valor lá dentro, de qualquer forma acho que deveríamos investigar."
        "Joseph coloca uma combinação no cofre mas não consegue abri-lo"
        show joseph s
        Joseph "Estranho... tenho certeza que era essa a senha."
        hide joseph 
        show erika n2 at right
        Erika "Deixa eu tentar. Erika tenta algumas combinações e abre o cofre."
        show nate n
        Nathan "Deixa eu adivinhar, você sabe abrir cofres pro caso de você esquecer a chave de casa também?"
        Erika ":P"
        "Ao abrirmos o cofre nos deparamos com todos os objetos roubados nos dias anteriores"
        hide erika 
        show joseph s at right with vpunch
        Joseph "Não faz sentido! eu não coloquei isso ai, deve ter sido o David!!"
        Joseph "Preciso falar com a Vivian, ela vai saber o que fazer."
        Joseph "Acho melhor vocês dois irem para a casa, é perigoso vocês dois ficarem por aqui."
        "Joseph fala isso praticamente empurrando a gente para fora da biblioteca"
        scene bg biblioteca fora noite with dissolve 
        show joseph n at right
        Joseph "Vou acompanha-los até em casa, não posso deixa-los irem sozinhos com esse maniaco do David a solta."
        jump casadia5ruim
            
    else:
        jump biblioteca5ruim

label casadia5ruim:
    scene bg casa fora noite with dissolve
    "Deixamos a Erika em casa primeiro e depois fomos para a minha."
    show nate n at left
    Nathan "O senhor está bem? posso tentar falar com meu pai para te ajudar com toda essa situação, ele tem um cargo alto na policia."
    show joseph f at right
    Joseph "Não se preocupe, err..."
    show nate ns at left
    Nathan "Nathan, acho que nunca me apresentei propriamente."
    show joseph f at right
    Joseph "Desculpe, acho que tem muita coisa na minha cabeça esses tempos."
    Joseph "Não se preocupe Nathan, eu sou adulto e sei que não cometi nenhum crime, vou falar com a Vivian amanhã cedo e vamos resolver esse mal-entendido."
    show nate ns
    Nathan "Pode me deixar um número pra contato? para caso descubra mais alguma coisa."
    Joseph "Ah, sim, claro."
    "Anoto o número de Joseph e entro para minha casa."
    jump quartodia5ruim

label quartodia5ruim:
    scene bg quarto com pistas noite with dissolve
    Camilla "Nossa, quanta informação."
    John "De fato, quem imaginária que o culpado era o David esse tempo todo?"
    Nathan "Estou preocupado com Joseph... será que ele vai conseguir se provar inocente?"
    Nathan "Acho que mais atrapalhei do que ajudei nesse caso..."
    John "...Não fica pensando nisso cara."
    Camilla "Acho que o melhor a se fazer agora é dormir, tenho certeza que a Vivian vai conseguir ajudar."
    Nathan "É... Melhor não pensar muito nisso agora."
    "Me deito para dormir..."
    jump quartodia6ruim

label quartodia6ruim:
    scene bg quarto com pistas dia with dissolve
    "Acordo um pouco mais tarde que o normal, o cansaço parece finalmente ter me encontrado."
    show john f at right
    John "Finalmente acordou, bela adormecida!"
    show nate n at left
    Nathan "...Que horas são?"
    hide john 
    show camilla n at right
    Camilla "Não sei, mas ta meio tarde já."
    Nathan "Droga, preciso ligar para o Joseph"
    "Disco o número de Joseph no meu celular"
    Joseph "Alô? Nathan? Aconteceu alguma coisa?"
    Nathan "Não, eu só liguei para saber se estava tudo bem."
    Joseph "Está sim... Na verdade não está tão bem... Estou com a Vivian aqui na biblioteca."
    Joseph "Será que você pode vir até aqui? acho que vou precisar da sua ajuda."
    Nathan "Ok, estou a caminho!"
    jump bibliotecadia6ruim

label bibliotecadia6ruim:
    "Chegando lá, Me encontro com Joseph e Vivian que parecem agitados."
    Vivian "Caramba Joseph, eu quero acreditar no que você está dizendo, mas não tem nada que comprove sua inocência!—"
    Joseph "Nathan! Desculpe faze-lo vir até aqui"
    Nathan "O que houve, está tudo bem?"
    Joseph "Não muito na verdade, não posso provar minha própria inocência!"
    Vivian "Nathan, você acha que tem alguma pista que pode comprovar o que o Joseph está dizendo?"
    Nathan "Não... acredito que só posso agir como testemunha a esse ponto."
    Vivian "Entendo... Bom, é nossa melhor chance agora."
    Vivian "Vamos para a delegacia, talvez o delegado Fábio consiga nos ajudar"
    Nathan "Certo."
    jump delegaciadia6ruim

label delegaciadia6ruim:

#voce vai com ele para a delegacia onde toda a armadilha já estava armada
#logo após ele explicar a situação o David aparece com um mandato de prisão para o Joseph com "provas" de que ele era o culpado pelos crimes recentes
#voce e vivian ficam indignados mas não podem fazer nada, e voce vai embora para casa
#chegando em casa camilla e john tentam te animar mas não conseguem 
#no dia seguinte voce acorda e encontra seu pai desolado, aparentemente ele sofreu uma denuncia por alterar arquivos confidenciais da policia e perdeu o emprego, mesmo não tendo feito nada disso
#você se sente sem rumo e decide passar o dia isolado em seu quarto acreditando que só piorou toda a situação desse caso.



