label dia5finalruim:
    show nate s at left
    Nathan "Erika! Espera!"
    show erika n at right 
    Erika "Oi, e ai? deu certo?  entregou as chaves pro David?"
    show nate n
    Nathan "Entreguei, mas ele não me passou confiança de que ia fazer um bom trabalho..."
    show nate ns
    Nathan "O que você acha da gente ir pra biblioteca durante a noite para tentar investigar nós mesmos?"
    show erika s
    Erika "Não sei não Nathan, pode ser meio arriscado..."
    show nate n
    Nathan "Tudo bem, não quero fazer você se arriscar sem motivo."
    show erika n
    Erika "Não, eu vou junto. Acho que consigo te ajudar com uma coisa!"
    Nathan "E o que seria?"
    Erika "Você vai descobrir na hora."
    scene bg shop with dissolve
    "Então nós dois saímos e ficamos aguardando a noite cair enquanto conversávamos com os meninos."
    
    scene bg rua noite with dissolve
    show erika n2 at right 
    Erika "Finalmente meu kit de {i}lockpick{/i} vai ser útil!"
    show nate f at left    
    Nathan "Então esse era o segredo?"
    Nathan "Por que você tem um kit desses em casa?"
    show erika s
    Erika "..."
    Erika "Vai que... eu...{w=1.0} esqueço minha chave qualquer dia desses né?"
    show nate n
    Nathan "Você vai esquecer sua chave mas não uma gazua?"
    Erika "A gente pode focar no que é importante de verdade?"
    show nate ns
    Nathan "Certo. A biblioteca."
    dJoseph "{i}Ai...{/i}"
    show erika s2
    Erika "Que barulho foi esse?"
    dJoseph "Aqui..."
    "Olhamos pra caçamba de lixo convenientemente posicionada fora da tela."
    show nate s2
    Nathan "Joseph?"
    hide erika 
    show joseph s2 at right
    Joseph "O-o que? O que aconteceu...? Como vim parar aqui? Não importa, eu preciso ir, preciso avisar a Vivian"
    show nate s
    Nathan "Avisar? do que você está falando?"
    hide joseph 
    show erika s at right
    Erika "Você precisa de um médico urgentemente!"
    hide erika 
    show joseph s at right
    Joseph "Agora não, preciso ver se a Vivian está bem."
    Joseph  "O David jogou um tijolo na janela dela!"
    Nathan "O quê? Mas por quê?!"
    Joseph "Eu não sei... mas tenho certeza que era ele, ele está tramando algo."
    Joseph "...Minhas chaves... Droga, perdi minhas chaves!"
    Nathan "Suas chaves? Droga... Eu as encontrei, mas entreguei elas para o David..."
    show joseph s2
    Joseph "VOCÊ O QUE?"
    hide joseph 
    show erika s at right
    Erika "Ei, calma ai, ele não sabia, e como a gente vai saber se você não ta inventando essa história inteira?"
    hide erika 
    show joseph s at right
    Joseph "Eu... Eu não posso."
    show nate n
    Nathan "Se o que você está dizendo é verdade precisamos ir até a biblioteca, talvez o David ainda esteja por lá, podemos grampear ele."
    Joseph "...Você tem razão, vamos."
    jump bibliotecaday5ruim

label bibliotecaday5ruim:
    scene bg biblioteca fora noite with dissolve
    "Chegamos na biblioteca mas não parece ter nada fora do comum."
    show joseph s2 at right
    Joseph "Droga, está trancada! não temos como entrar agora."
    hide joseph 
    show erika n at right
    Erika "Minha hora de brilhar!"
    "Erika puxa um kit de gazuas e começa a destrancar as portas da biblioteca."
    "{i}Clack{/i}, a porta se abre."
    show erika n2 at right
    Erika "Eu sou boa demais diz aí."
    hide erika 
    show joseph f at right
    Joseph "Obrigado Erika, vamos!" 
    show nate n at left
    Nathan "Não parece ter nada de diferente aqui..."
    show joseph n at right
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
    show camilla n at right
    Camilla "Nossa, quanta informação."
    hide camilla 
    show john n at right 
    John "De fato, quem imaginária que o culpado era o David esse tempo todo?"
    show ante n at left
    Nathan "Estou preocupado com Joseph... será que ele vai conseguir se provar inocente?"
    Nathan "Acho que mais atrapalhei do que ajudei nesse caso..."
    John "...Não fica pensando nisso cara."
    hide john 
    show camilla t at right
    Camilla "Acho que o melhor a se fazer agora é dormir, tenho certeza que a Vivian vai conseguir ajudar."
    show nathan ns at left
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
    show nate s
    Nathan "Droga, preciso ligar para o Joseph"
    "Disco o número de Joseph no meu celular"
    show nate n
    Joseph "Alô? Nathan? Aconteceu alguma coisa?"
    Nathan "Não, eu só liguei para saber se estava tudo bem."
    Joseph "Está sim... Na verdade não está tão bem... Estou com a Vivian aqui na biblioteca."
    Joseph "Será que você pode vir até aqui? acho que vou precisar da sua ajuda."
    show nate ns
    Nathan "Ok, estou a caminho!"
    jump bibliotecadia6ruim

label bibliotecadia6ruim:
    scene bg delegacia dentro with dissolve
    "Chegando lá, Me encontro com Joseph e Vivian que parecem agitados."
    show vivian b at left
    Vivian "Caramba Joseph, eu quero acreditar no que você está dizendo, mas não tem nada que comprove sua inocên—"
    show joseph s at right
    Joseph "Nathan! Desculpe faze-lo vir até aqui"
    hide vivian
    show nate s2 at left
    Nathan "O que houve, está tudo bem?"
    show joseph s2 
    Joseph "Não muito na verdade, não posso provar minha própria inocência!"
    hide joseph 
    show vivian n at right
    Vivian "Nathan, você acha que tem alguma pista que pode comprovar o que o Joseph está dizendo?"
    show nate s at left
    Nathan "Não... acredito que só posso agir como testemunha a esse ponto."
    Vivian "Entendo... Bom, é nossa melhor chance agora."
    Vivian "Vamos para a delegacia, talvez o delegado Fábio consiga nos ajudar"
    show nate f at left
    Nathan "Certo!"
    jump delegaciadia6ruim

label delegaciadia6ruim:
    scene bg delegacia frente dia with dissolve 
    pause(1.0)
    scene bg delegacia dentro with dissolve
    "Chegando na delegacia nós nos deparamos com David e meu pai que já estavam a caminho da biblioteca para prender o Joseph"
    show pai s at right
    Pai "Nathan, Vivian? O que está acontecendo aqui? Afastem-se desse homem imediatamente!"
    show nate s at left
    Nathan "Calma pai, ele não é o ladrão"
    hide pai 
    show david b at right
    David "Mas é claro que é! tenho todas as provas bem aqui!"
    hide david 
    show joseph s2 at right
    Joseph "Mas não fui eu que coloquei essas coisas no cofre e você sabe disso, até por que você é o verdadeiro culpado!"
    hide joseph 
    show david b at right
    David "Cofre? então você admite?"
    hide david 
    show joseph b at right
    Joseph "O que!? Eu sei que foi você, pare de tentar distorcer a história!"
    hide joseph 
    show david b at right
    David "Mas que acusação absurda! você precisa provar o que está falando, ou as coisa vão ficar ainda pior pro seu lado."
    hide david 
    show joseph b at right
    Joseph "Não tenho como provar, você deletou as gravações das cameras!"
    hide joseph 
    show david b at right
    David "Como que eu poderia deletas as SUAS, gravações?"
    hide david 
    show vivian b at right
    Vivian "{size=*0,75}Joseph... Pare de falar, está só piorando sua situação{/size}"
    hide vivian 
    show pai b at right 
    Pai "Já ouvi o bastante, prendam esse homem!"
    show nate s2
    Nathan "Pai, escuta, você ta cometendo um erro! ele ta falando a verdade, ele só não tem provas agora, mas se você der mais tempo a ele tenho certeza qu—"
    Pai "BASTA! Pare de agir como se você fosse algum tipo de investigador, você é só um moleque!"
    Nathan "..."
    hide pai 
    show joseph f at right
    Joseph "Tudo bem Nathan, vai dar tudo certo, sei que você tentou ajudar..."
    "Meu pai leva o Joseph algemado para uma sala nos fundos da delegacia."
    hide joseph with dissolve 
    show vivian n
    Vivian "Está tudo bem Nathan, isso foi uma armadilha, não estávamos preparados, mas não se preocupe, não vou descansar até provar a inocência do Joseph"
    Vivian "Vai pra casa... Imagino que esteja bem cansado, obrigado pela ajuda."

label casadia6ruim:
    scene bg quarto com pistas tarde with dissolve
    show camilla t at right 
    Camilla "Nathan... Está tudo bem?"
    hide camilla 
    show john n at right 
    John "Você não falou uma palavra desde que saiu da delegacia cara."
    show nate n at left
    Nathan "Eu só não to afim... Isso tudo foi culpa minha, se eu não tivesse me envolvido tanto não teria atrapalhado a investigação e o Joseph não teria sido preso"
    Nathan "Não sei onde eu estava com a cabeça com essa ideia de investigação..."
    "Tiro todas as pistas de minha parede, não vejo mais motivo para fazer isso..."
    scene bg quarto tarde with dissolve
    show camilla t at right 
    Camilla "Você não podia fazer nada ali Nathan, o David armou pra ele."
    show nate n at left
    Nathan "Acho que só vou dormir, não quero pensar mais nisso..."

label quartodia7ruim:
    scene black with dissolve
    with Pause(1)

    show text "{color=#FFFFFF}Alguns dias depois, o Joseph acabou sendo julgado como culpado por todos os crimes recentes e logo após isso meu pai foi demitido do cargo por adulteração de arquivos {/color}"
    with Pause(3)
    hide text 
    show text "{color=#FFFFFF}Acredito que tenha sido obra do David também, mas decidi que era melhor não me envolver mais nesse tipo de coisa...{/color}"
    with Pause(3)
    hide text 
    show text "{color=#FFFFFF}...Será que eu podia ter feito algo diferente?{/color}"
    hide text
    with Pause(3)
    scene black with dissolve
    with Pause(1.5)
