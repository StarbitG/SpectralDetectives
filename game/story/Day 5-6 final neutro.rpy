label dianeutro:
    scene bg shop with dissolve
    show halfblack
    show david f at right
    David "O que tem na frente da biblioteca?"
    "David aparece atrás da gente com um salgadinho {i}Torresminos{/i} na mão."
    show nate s at left
    Nathan "Ahn? Biblioteca?{nw}{w=1.5}"
    show nate ns
    Nathan "Ahn? Biblioteca?{fast} Acho que você está ouvindo coisas."
    hide david 
    show erika n at right
    Erika "{size=*0.75}Lucas, Sebastian, ajudem a gente aqui...{/size}"
    hide erika 
    show david f at right
    David "Tenho certeza que ouvi vocês dizendo que iam para a biblioteca à noite. Não posso deixar vocês irem sem estarem acompanhados, senhor!"
    show nate s
    Nathan "Não, não, tenho certeza que você está ouvindo coisas."
    menu:
        "Mandar um sinal para o Sebastian":
            hide david 
            show seb b at right 
            Sebastian "Ei, cara, quando que você vai pagar por esses salgadinhos aí?"
            hide seb 
            hide seb 
            show david s at right
            David "{i}*Gulp*{/i} Err, você tá falando comigo? Haha, eu já ia pagar agora mesmo!"
            hide david 
        "Mandar um sinal para o Lucas":
            hide david
            show lucas f at right
            Lucas "David! Uma carga nova de salgadinhos chegou! Você é forte, né? Pode ajudar?"
            hide lucas
            show seb c at right
            Sebastian "Mas eu também sou fort—" #nite
            hide seb
            show lucas b at right
            Lucas "{size=*0.75}Segue o plano seu besta.{/size}"
            hide lucas
            show seb s at right
            Sebastian "{size=*0.75}Ah tá entendi.{/size}{nw}{w=1.0}"
            show seb n
            Sebastian "{size=*0.75}Ah tá entendi.{/size}{fast} Ah não... Eu me sinto tão fraco de repente, David, nos socorra por favor!"
            "Lucas puxa o David para longe de mim e Erika."
            hide seb 
            hide lucas 
            hide david 

    show erika s at right 
    Erika "Vamos aproveitar e sair daqui."
    hide erika 
    show lucas f at right 
    Lucas "{size=*0.75}Vão logo, a gente mantém ele aqui.{/size}"
    "Eu e Erika corremos para fora e vamos para a biblioteca."
   
label ruaneutra:
    scene bg rua dia with dissolve
    scene bg rua tarde with dissolve
    show halfblack
    show nate f at left
    Nathan "Acho que vamos ter que ir agora de tarde mesmo, se não o David vai atrapalhar a gente."
    show erika n at right
    Erika "Sim, vamos aproveitar que os meninos estão distraindo ele."

    scene bg biblioteca fora tarde with dissolve
    show halfblack
    show nate n at left
    Nathan "É isso, vamos entrar."

    scene bg biblioteca dentro tarde with dissolve
    show halfblack
    show erika s at right 
    Erika "Vamos procurar o que pudermos o mais rápido possível, não sabemos quanto tempo Lucas e Sebastian vão segurar o David."
    show nate s at left 
    Nathan "Certo!"
    Erika "Por onde a gente começa?"

label biblioteca5neutro:
    scene bg biblioteca dentro tarde with dissolve
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

    if procuraprateleira >= 1 and procurabancada >= 1 and procuraestante >= 1:
        show nate n at left
        Nathan "Nada..."
        Nathan "Acho que devíamos desistir e sair daqui antes qu—"
        "Erika tropeça no tapete e se esborracha no chão revelando um cofre escondido."
        show bg biblioteca segredo tarde with hpunch
        show halfblack
        show erika n2 at right
        Erika "Viu só o que eu encontrei de maneira totalmente proposital?"
        show nate s at left 
        Nathan "Err,{nw}{w=1}"
        show nate ns
        Nathan "Err{fast}, bom trabalho?" 
        show nate n
        Nathan "Mas como vamos abri-lo?"
        show erika n
        Erika "Deixa isso comigo."
        "Erika encosta a cabeça no cofre e começa a testar várias combinações, até que ouvimos um *Clack* e o cofre se abre."
        scene bg biblioteca segredo tarde with dissolve
        show halfblack
        show erika s2 at right
        Erika "Isso é o que eu to pensando que é?"
        show nate s2 at left 
        Nathan "Todos os objetos roubados..."
        show nate b
        Nathan "A gente estava certo, o Joseph é o ladrão!"
        show erika b
        Erika "Precisamos avisar alguém da polícia, tipo, agora."
        jump bibliotecaneutra2
    
    else:
        jump biblioteca5neutro
    
    #cena da biblioteca com o cofre

label bibliotecaneutra2:
    scene bg biblioteca segredo tarde with dissolve 
    show halfblack
    show david f at right
    David "Finalmente alcancei vocês. O que vocês viram aí dentro?"
    hide david
    show erika s at right
    Erika "David! Precisávamos falar com você!"
    hide erika
    show david b at right
    David "E o que seria?" 
    show nate s at left
    Nathan "O Joseph, é ele, ele é o ladrão."
    show david n
    David "É?... Quem é Joseph, senhor!?"
    hide david 
    show erika s at right
    Erika "O bibliotecário??"
    hide erika 
    show david n at right
    David "Ah sim, entendo, então eu assumo daqui!"
    show nate s
    Nathan "Mas—"
    show david f at right
    David "Não se preocupe, o Super David vai cuidar de tudo, senhor!"
    hide david 
    show erika s at right
    Erika "{size=*0.75}Nós nem conseguimos dizer quais eram as provas...{/size}"
    "Sem muita opção, eu e Erika nos despedimos e voltamos para casa."
    jump quartodia5neutro

label quartodia5neutro:
    scene bg quarto com pistas noite with dissolve
    show halfblack
    show camilla n at right
    Camilla "O que foi aquilo com o David, hein?"
    hide camilla 
    show john n at right
    John "É... foi um pouco estranho mesmo, mas com todas as provas lá na biblioteca não tem muito como o David fazer besteira."
    show nate ns at left
    Nathan "Então é isso? Acabou, resolvemos o caso?"
    show nate n
    Nathan "Sei lá, as coisas não pareceram... Fáceis demais?"
    show john ex at right
    John "Bom, acho que não adianta ficar pensando nessas coisas."
    hide john 
    show camilla f at right
    Camilla "Por que você não vai amanhã na delegacia e vê o que aconteceu?"
    show nate f
    Nathan "Vocês têm razão, vou fazer isso."
    Nathan "Vou me deitar agora."
    jump dia6neutro

label dia6neutro:
    scene bg quarto com pistas dia with dissolve 
    "Acordo bem cedo e já me preparo para sair para a delegacia."
    show halfblack
    show camilla f at right
    Camilla "Você vai lá ver se o David conseguiu levar as evidências para a delegacia?"
    show nate ns at left
    Nathan "Sim, melhor ir lá conferir só pra ter certeza."
    hide camilla 
    show john ex at right
    John "Também acho, esse cara costuma ser meio idiota..."
    jump delegaciadia6neutra

label delegaciadia6neutra:
    scene bg delegacia frente dia with dissolve
    scene bg delegacia dentro with dissolve
    show halfblack
    show joseph b at right with hpunch
    Joseph "ISSO É UM ABSURDO, COMO VOCÊS PODEM ME PRENDER? EU NÃO FIZ NADA, ISSO É UM ABSURDO!"
    show pai b at left 
    Pai "Você pode dizer tudo isso no tribunal, agora andando."
    hide joseph 
    show john n at right 
    John "É, parece que ele não é tão idiota assim."
    hide pai with dissolve 
    "Meu pai me ignora completamente enquanto leva o Joseph para os fundos, é como se ele nem tivesse me visto passar pela recepção."
    "David e Vivian entram logo em seguida."
    hide john
    show david f at right
    David "Ei Vivian, agora que eu solucionei esse mistério SOZINHO com meu incrível intelecto, você gostaria de sair comigo?"
    show vivian b at left
    Vivian "Você ficou maluco? Não, não entendo nem como você pode estar me perguntando algo assim agora!"
    Vivian "Algo claramente está errado com esse caso, o Joseph nunca cometeria um crime, ele é uma das melhores pessoas que eu já conheci."
    show david b
    David "Hmpf, que seja."
    "Não tem mais nada que eu possa fazer aqui, pelo jeito, vou embora."

label quartodia7neutro:
    scene black with dissolve
    with Pause(1)

    show text "{color=#FFFFFF}Um tempo depois...{/color}"
    with Pause(3)
    hide text
    jump mercadoneutro

label mercadoneutro:
    scene bg shop with dissolve
    show halfblack 
    show lucas f at right
    Lucas "Nathan!, muito obrigado por ajudar a gente a recuperar as alianças, cara. Você é um anjo!!"
    show nate ns at left
    Nathan "Que isso, eu não fiz nada..."
    hide lucas 
    show seb f at right
    Sebastian "Não esquenta, a Erika contou tudo. A gente sabe que foram vocês que descobriram quem era o ladrão."
    hide seb 
    show lucas f at right
    Lucas "Nunca imaginei que o Joseph fosse o culpado... Ele sempre foi tão gente boa comigo, mesmo comigo atrasando as devoluções dos livros."
    hide lucas 
    show erika n at right
    Erika "Apesar do David ter ficado com toda a glória... Pelo menos a gente sabe quem foi que realmente descobriu o caso, não é Nathan?"
    show nate n at left
    Nathan "É... Acho que já vou pra casa, galera."
    show erika n2 at right
    Erika "Tudo bem, você merece um descanso, senhor detetive!"
    show nate ns at left
    Nathan "É... Haha."
    jump finalneutrofinalmesmo

label finalneutrofinalmesmo:
    scene bg mercado dia with dissolve
    pause(1.0)
    scene bg rua dia with dissolve
    pause(1.0) 
    scene bg casa fora dia with dissolve 
    pause(1.0) 
    scene bg quarto com pistas dia with dissolve
    show halfblack
    show john n at right
    John "Ei, Nathan. Você tá bem, cara?"
    John "Você tá estranho desde que resolveu o caso do bibliotecário."
    hide john 
    show camilla t at right 
    Camilla "É, você devia estar orgulhoso! Acho até que seria um bom momento pra você chamar a Erika pra sair!"
    show nate n at left
    Nathan "Não, eu não consigo. Sinto que tem algo errado nesse caso, mas não sei dizer o que é."
    Nathan "É como se...{w=1} faltasse uma peça do quebra-cabeça."
    Nathan "O que será?..."
    "Me deito e vou dormir um pouco."
    jump finalPiacabouamém

label finalPiacabouamém:
    scene black with dissolve
    with Pause(1)

    show text "{color=#FFFFFF}Será que cometi algum erro?{/color}" with dissolve
    with Pause(3)
    hide text with dissolve
    pause(2.0)
pause