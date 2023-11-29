label dianeutro:
    #David "O que tem na frente da biblioteca?"
    #"David aparece atrás da gente com um salgadinho Torresminos na mão"
    #Nathan "Ahn? Biblioteca? acho que você está ouvindo coisa"
    #Erika "{size=*0.75}Lucas, Sebastian, ajudem a gente aqui...{/size}"
    #David "Tenho certeza que ouvi vocês dizendo que iam para a biblioteca a noite, não posso deixar vocês irem sem estarem acompanhados senhor!"
    #Nathan "Não, não, tenho certeza que você está ouvindo coisas"
    #Sebastian "Ei, cara, quando que você vai pagar por esses salgadinhos ai"
    #David "{i}*Gulp*{/i} err, você ta falando comigo? hehe, eu já ia pagar agorinha mesmo!"
    #Erika "Vamos aproveitar e sair daqui"
    #Lucas "{size=*0.75} Vão logo, a gente mantém ele aqui."
    #"Eu e Erika corremos para fora e vamos para a biblioteca"
    
    #rua
    #Nathan "Acho que vamos ter que ir agora de tarde mesmo, se não o David vai atrapalhar a gente"
    #Erika "Sim, vamos aproveitar que os meninos estão distraindo ele"

    #Frente da delegacia
    #Nathan "É isso, vamos entrar."

    #Dentro da biblioteca
    #Erika "Vamos procurar o que pudermos o mais rápido possível, não sabemos quanto tempo Lucas e Sebastian vão segurar o David."
    #Nathan "Certo!"
    #Erika "Por onde a gente começa?"

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
        Nathan "Nada..."
        Nathan "Acho que devíamos desistir e sair daqui antes qu—"
        "Erika tropeça no tapete e se esborracha no chão revelando um cofre escondido."
        Erika "Viu só o que eu encontrei de maneira totalmente proposital?"
        Nathan "Err, bom trabalho?"
        Nathan "Mas como vamos abri-lo?"
        Erika "Deixa isso comigo."
        "Erika encosta a cabeça no cofre e começa a testar varias combinações, até que ouvimos um *Clack* e o cofre se abre."
    
    else:
        jump biblioteca5neutro
    
    #cena da biblioteca com o cofre
    Erika "Isso é o que eu to pensando que é?"
    Nathan "Todas os objetos roubados..."
    Nathan "A gente estava certo, o Joseph é o ladrão!"
    Erika "Precisamos avisar alguém da policia, tipo, agora."

#Fora da biblioteca (ainda de tarde?)

#David "Finalmente alcancei vocês. O que vocês viram ai dentro?"
#Erika "David! precisávamos falar com você!"
#David "E o que seria?" (coloca ele com uma expressão brava aqui)
#Nathan "O Joseph, é ele, ele é o ladrão."
#David "É?... Quem é Joseph, Senhor!?" (coloca ele normal de volta aqui)
#Erika "O bibliotecário??"
#David "Ah sim, entendo, então eu assumo daqui!"
#Nathan "Mas—"
#David "Não se preocupe, o Super David vai cuidar de tudo, senhor!"
#Erika "{size=*0,75}Nós nem conseguimos dizer quais eram as provas...{/size}"



# No dia seguinte voce decide ir até a delegacia para saber o que aconteceu
# chegando na recepção voce se depara com o joseph algemado e sendo levado preso enquanto gritava que era inocente
# O David diz que o ladrão foi pego graças a sua ajuda
# A Vivian aparece logo em seguida e diz que algo está errado mas que ela n sabe e que ela não vai parar até descobrir o que
# Voce vai até a loja contar o que aconteceu para o Lucas, Sebastian e Erika
# lucas, sebastian e Erika agradecem voce por ter solucionado o misterio e ficam felizes que vão ter suas coisas de volta
# Voces passam o dia juntos até que você vai para casa dormir
# em casa voce conversa com john e camilla, vc não está feliz com a solução do caso, algo parece estar errado e a fala de vivian te convence cada vez mais
# John e Camilla dizem que voce está muito cansado e john sugere que voce chame erika para sair
# Voce não se sente confiante para isso e vai dormir
# final mediocre, as coisas ficaram em aberto

#=============================================================================================================================================================================================================================================================