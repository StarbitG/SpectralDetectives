label dianeutro:
    scene bg shop with dissolve
    show halfblack
    show david f at right
    David "O que tem na frente da biblioteca?"
    "David aparece atrás da gente com um salgadinho {i}Torresminos{/i} na mão"
    show nate s at left
    Nathan "Ahn? Biblioteca?{nw}{w=1.5}"
    show nate ns
    Nathan "Ahn? Biblioteca?{fast} acho que você está ouvindo coisa"
    hide david 
    show erika n at right
    Erika "{size=*0.75}Lucas, Sebastian, ajudem a gente aqui...{/size}"
    hide erika 
    show david f at right
    David "Tenho certeza que ouvi vocês dizendo que iam para a biblioteca a noite, não posso deixar vocês irem sem estarem acompanhados senhor!"
    show nate s
    Nathan "Não, não, tenho certeza que você está ouvindo coisas"
    menu:
        "Mandar um sinal para o Sebastian":
            hide david 
            show seb b at right 
            Sebastian "Ei, cara, quando que você vai pagar por esses salgadinhos ai"
            hide seb 
            hide seb 
            show david s at right
            David "{i}*Gulp*{/i} err, você ta falando comigo? haha, eu já ia pagar agorinha mesmo!"
            hide david 
        "Mandar um sinal para o Lucas":
            hide david
            show lucas f at right
            Lucas "David! Uma carga nova de salgadinhos chegou! Você é forte né? Pode ajudar?"
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
            Sebastian "{size=*0.75}Ah tá entendi.{/size}{fast} Ah não... Eu me sinto tão fraco de repente, David nos socorra por favor!"
            "Lucas puxa o David para longe de mim e Erika"
            hide seb 
            hide lucas 
            hide david 

    show erika s at right 
    Erika "Vamos aproveitar e sair daqui"
    hide erika 
    show lucas f at right 
    Lucas "{size=*0.75} Vão logo, a gente mantém ele aqui."
    "Eu e Erika corremos para fora e vamos para a biblioteca"
    
label ruaneutra:
    scene bg rua dia with dissolve
    scene bg rua tarde with dissolve
    show nate f at right
    show halfblack
    Nathan "Acho que vamos ter que ir agora de tarde mesmo, se não o David vai atrapalhar a gente"
    show erika n at right
    Erika "Sim, vamos aproveitar que os meninos estão distraindo ele"

    scene bg delegacia frente dia tarde with dissolve
    show nate n at left
    Nathan "É isso, vamos entrar."

    scene bg biblioteca dentro tarde with dissolve
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

    if procuraprateleira >=1 and procurabancada >=1 and procuraestante >=1:
        show nate n at left
        Nathan "Nada..."
        Nathan "Acho que devíamos desistir e sair daqui antes qu—"
        "Erika tropeça no tapete e se esborracha no chão revelando um cofre escondido."
        show bg biblioteca dentro tarde with hpunch
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
        "Erika encosta a cabeça no cofre e começa a testar varias combinações, até que ouvimos um *Clack* e o cofre se abre."
        scene bg biblioteca segredo tarde with dissolve
        show erika s2 at right
        Erika "Isso é o que eu to pensando que é?"
        show nate s2 at left 
        Nathan "Todas os objetos roubados..."
        show nate b
        Nathan "A gente estava certo, o Joseph é o ladrão!"
        show erika b
        Erika "Precisamos avisar alguém da policia, tipo, agora."
        jump bibliotecaneutra2
    
    else:
        jump biblioteca5neutro
    
    #cena da biblioteca com o cofre
    

#Fora da biblioteca (ainda de tarde?)
label bibliotecaneutra2:
    scene bg biblioteca segredo with dissolve 
    show david f at right
    David "Finalmente alcancei vocês. O que vocês viram ai dentro?"
    hide david
    show erika s at right
    Erika "David! precisávamos falar com você!"
    hide erika
    show david b at right
    David "E o que seria?" 
    show nate s at left
    Nathan "O Joseph, é ele, ele é o ladrão."
    show david n
    David "É?... Quem é Joseph, Senhor!?"
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
    Erika "{size=*0,75}Nós nem conseguimos dizer quais eram as provas...{/size}"
    "Sem muita opções eu e Erika nos despedimos e voltamos para casa"
    jump quartodia5neutro

label quartodia5neutro:
    scene bg quarto com pistas noite with dissolve
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
    Nathan "Vocês tem razão, vou fazer isso."
    Nathan "Vou me deitar agora."
    jump dia6neutro

label dia6neutro:
    scene bg quarto com pistas dia with dissolve 
    "Acordo bem cedo e já me preparo para sair para delegacia."
    show camilla f at right
    Camilla "Você vai lá ver se o David conseguiu levar as evidências para delegacia?"
    show nate ns at left
    Nathan "Sim, melhor ir lá conferir só pra ter certeza"
    hide camilla 
    show john ex at right
    John "Também acho, esse cara costuma ser meio idiota..."
    jump delegaciadia6neutra

label delegaciadia6neutra:
    scene bg delegacia frente dia 

#delegacia (faz a cutscene como se ele fosse entrando na delegacia, parte de fora e depois parte de dentro, a cena vai rolar na recepção) [ok]
#Joseph "ISSO É UM ABSURDO, COMO VOCÊS PODEM ME PRENDER? EU NÃO FIZ NADA, ISSO É UM ABSURDO!"
#Pai "Você pode dizer tudo isso no tribunal, agora andando"
#John "É, parece que ele não é tão idiota assim."
#"Meu pai me ignora completamente enquanto leva o Joseph para os fundos, é como se ele nem tivesse me visto passar pela recepção"
#"David e Vivian entram logo em seguida"
#David "Ei Vivian, agora que eu solucionei esse mistério SOZINHO com meu incrível intelecto, você gostaria de sair comigo?"
#Vivian "Você ficou maluco? não, não entendo nem como você pode estar me perguntando algo assim agora!"
#Vivian "Algo claramente está errado com esse caso, o Joseph nunca cometeria um crime, ele é uma das melhores pessoas que eu já conheci."
#David "Hmpf, que seja."
#"Não tem mais nada que eu possa fazer aqui pelo jeito, vou embora." (meme do napoleao) [🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖]

label quartodia7neutro:
    scene black with dissolve
    with Pause(1)

    show text "{color=#FFFFFF}Um tempo depois...{/color}"
    with Pause(3)
    hide text 


#parte de dentro do mercadinho
#Lucas "Nathan!, muito obrigado por ajudar a gente a recuperar as alianças cara, você é um anjo!!"
#Nathan "Que isso, eu não fiz nada..."
#Sebastian "Não esquenta, a Erika contou tudo a gente sabe que foram vocês que descobriram quem era o ladrão."
#Lucas "Nunca imaginei que o Joseph fosse o culpado... Ele sempre foi tão gente boa comigo, mesmo comigo atrasando as devoluções dos livros"
#Erika "Apesar do David ter ficado com toda a glória... Pelo menos a gente sabe quem foi que realmente descobriu o caso, não é Nathan?"
#Nathan "É... Acho que já vou pra casa galera."
#Erika "Tudo bem, você merece um descanso, senhor detetive!"
#Nathan "É... haha"


#(Cutscenete, parte de fora do mercado, rua, parte de fora da casa, quarto)
#John "Ei, Nathan. Você tá bem cara?"
#John "Você ta estranho desde que resolveu o caso do bibliotecário."
#Camilla "É, você devia estar orgulhoso! Acho até que seria um bom momento pra você chamar a Erika pra sair!"
#Nathan "Não, eu não consigo. Sinto que tem algo errado nesse caso, mas não sei dizer o que é."
#Nathan "É como se faltasse uma peça do quebra-cabeça"
#Nathan "O que será?..."
#"Me deito e vou dormir um pouco"

#Final mediocre, o mistério não parece ter sido solucionado corretamente.







#=============================================================================================================================================================================================================================================================

#  No dia seguinte voce decide ir até a delegacia para saber o que aconteceu
#  chegando na recepção voce se depara com o joseph algemado e sendo levado preso enquanto gritava que era inocente
#  O David diz que o ladrão foi pego graças a sua ajuda
#  A Vivian aparece logo em seguida e diz que algo está errado mas que ela n sabe e que ela não vai parar até descobrir o que
#  Voce vai até a loja contar o que aconteceu para o Lucas, Sebastian e Erika
#  lucas, sebastian e Erika agradecem voce por ter solucionado o misterio e ficam felizes que vão ter suas coisas de volta
#  Voces passam o dia juntos até que você vai para casa dormir
#  em casa voce conversa com john e camilla, vc não está feliz com a solução do caso, algo parece estar errado e a fala de vivian te convence cada vez mais
#  John e Camilla dizem que voce está muito cansado e john sugere que voce chame erika para sair
#  Voce não se sente confiante para isso e vai dormir
#  final mediocre, as coisas ficaram em aberto

# =============================================================================================================================================================================================================================================================