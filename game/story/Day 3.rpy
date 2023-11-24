label startday3:
    show bg quarto dia with dissolve
    scene bg quarto dia
    show halfblack
    "Quando o dia amanheceu, a primeira coisa que fiz foi ligar para Erika, eu precisava da ajuda dela afinal."
    "{i}trim trim{/i}"
    show erika n at right
    Erika "Bom dia, Nathan! Tem alguma novidade?"
    show nate n at left
    Nathan "Bom dia, Erika. Na verdade, tenho sim. Muitas coisas aconteceram ontem. Eu estava pensando... Será que você poderia me encontrar para conversarmos? Eu preciso da sua ajuda."
    hide erika
    show john n at right
    #123456789
    John "Não acredito, ele vai chamá-la pra sair?"
    hide john
    show camilla b at right
    Camilla "Shh, cala boca John, você tá atrapalhando."
    hide camilla
    show john f at right
    John "Parei."
    hide john
    show erika n2 at right
    Erika "Claro! Onde você vai?"
    Nathan "A gente pode se encontrar na rua mesmo. Eu saio de casa em no máximo 5 minutos e te espero por lá, pode ser?"
    show erika n
    Erika "Ótimo, chego lá rapidinho. Até logo!"
    "Terminando a ligação, eu saí correndo de casa."
    show bg rua dia with dissolve
    scene bg rua dia
    show halfblack
    show erika n at right
    Erika "Oiee, o que você tá precisando?"
    show nate n at left
    Nathan "Bem, você se lembra que eu estava estudando sobre o caso, né? Por mais que eu não tenha nada a ver, então ontem eu estava refletindo algumas ideias e levantei algumas suspeitas. Acho que o bibliotecário pode estar envolvido nos roubos."
    Nathan "Ele agiu de forma estranha quando me viu lendo o livro sobre os crimes."
    if "aliança" in inventory_items:
        Nathan "E, além disso, o anel roubado foi encontrado na porta da biblioteca. Ainda tenho que devolver pro Sebastian isso."
    Nathan "Parece que ele tem acesso aos arquivos e poderia manipular as coisas ao seu redor."
    Erika "Espera aí, e você descobriu tudo isso sozinho? Isso é bem impressionante na verdade. Talvez valha a pena investigar mais o bibliotecário e buscar um álibi para o dia do crime. Você então quer ajuda pra... falar com ele?"
    Nathan "Ontem ele já estava muito suspeito, olhando o que eu fazia. Então, prefiro que outra pessoa faça isso por mim. E aliás, podemos achar suas coisas nesse meio tempo também!"
    Erika "Hmmm... Até que isso não é uma má ideia... Vamos nos preparar para isso. O que você acha da gente conversar com os meninos antes? Eles talvez tenham visto a aparência do ladrão quando estavam fechando a loja."
    Nathan "Sim, precisamos buscar todas as pistas possíveis. Fico feliz que você tenha aceito ajudar tão fácil hahaha. Enfim, vamos lá!"
    jump lojaday3

label startday3alt:
    show bg quarto dia with dissolve
    scene bg quarto dia
    show halfblack
    if "aliança" in inventory_items:
        "{i}trim trim{/i}"
        show nate n at left
        Nathan "Alô?"
        show erika n at right
        Erika "Oi, Nathan! Desculpe por te ligar tão cedo, mas queria confirmar que eu vou te ajudar na investigação. Passei a noite pensando sobre isso, acho que isso pode dar certo."
        Nathan "Fico muito feliz que tenha aceitado!!! Deixa eu já te atualizar então. Acredito que o bibliotecário possa estar envolvido, mas preciso de mais provas antes de tirar conclusão."
        show erika s
        Erika "O bibliotecário? Mas ele é um carinha tão... normal."
        Nathan "Ele não gostou muito que eu trouxe o livro de crimes rasgado comigo, isso foi bem estranho da parte dele, e também, ele tem acesso aos arquivos criminais, o que impediria ele de apagar algum que o incriminasse, né."
        Erika "Até que é uma boa teoria. Mas não acho que ele faria algo assim, de qualquer forma, precisamos encontrar álibis, eu acho que podemos perguntar mais sobre a noite do crime pro Sebastian e o Lucas, o que pensa?."
        Nathan "Acho uma ótima ideia! Vamos fazer exatamente isso! Te encontro lá!"
        show erika n
        Erika "Até daqui a pouquinho!"
        jump lojaday3
    if "aliança" not in inventory_items:
        "Mais uma vez, eu acordei com os sons da minha porta batendo"
        show erika s at right
        Erika "Nathan! Precisamos conversar, agora."
        show nate s at left
        Nathan "Erika, o que aconteceu? Parece que algo sério está acontecendo."
        Erika "Passei a noite pensando sobre os roubos na cidade e sobre o seu envolvimento nisso. Cheguei a uma conclusão perturbadora. Eu ACHO que o bibliotecário possa estar diretamente envolvido."
        show nate n
        show erika n
        Nathan "Erika, você não pode ir por aí acusando os outros-"
        show erika s
        Erika "Antes que você fale ''Erika, você não pode sair por aí acusando os outros'', eu achei os anéis do Lucas e do Sebastian ontem naquela rachadura."
        Erika "Só não te contei porque eu queria entender o porquê eles estavam lá. Então, a partir de agora, eu vou te ajudar a investigar isso, okay? "
        show nate s
        Nathan "Primeiro: COMO ASSIM VOCÊ ACHOU AS ALIANÇAS? E segundo: por que elas estavam lá?"
        Erika "É, foi isso mesmo que você ouviu, e eu acho que estavam lá porque o ladrão é o bibliotecário, mas eu não tenho provas suficientes ainda, queria ir na loja perguntar algumas coisas para os meninos, você aceita?."
        show nate f
        Nathan "Obrigado, Erika. Sua ajuda significa muito para mim. E ir perguntar para os meninos sobre a noite do crime pode nos ajudar muito, vamos fazer isso."
        show erika n
        Erika "Ta bom, para de ser bobão e vamos logo"
        "E mais uma vez, ela me arrasta para outro lugar"
        jump lojaday3

label lojaday3:
    show bg mercado roubado dia with dissolve
    scene bg mercado roubado dia
    show halfblack
    "Chegando na loja, vemos apenas o Sebastian por lá, além da equipe de polícia, claro."
    show erika n at right
    Erika "Sebastian!! A gente pode falar com você rapidinho?"
    hide erika
    show seb c at right
    Sebastian "Erika, Nathan?"
    show nate n at left
    Nathan "Ué, cadê o Lucas? Vocês não estão sempre juntos?"
    Sebastian "Ah, ele? Não sai de casa desde o incidente, abalou muito ele. Eu vim aqui só pra ver como andava a operação, mas já estou de saída."
    hide seb
    show erika s at right
    Erika "Você tem só um tempinho? Queríamos tirar algumas dúvidas com você."
    hide erika
    show seb c at right
    Sebastian "Claro, não vejo o motivo para não ficar."
    hide seb
    show erika n at right
    Erika "Ótimo! Primeira coisa, o que você estava fazendo na hora do crime?"
    hide erika
    show seb n at right
    Sebastian "Eu tinha acabado de fechar a loja, então estava indo para casa."
    Nathan "E você por acaso viu algo estranho nesse meio tempo?"
    Sebastian "Agora que você diz, eu acho que vi alguém passando por aqui. Ele era meio alto, mas já estava escuro, então esse é o máximo que eu pude ver."
    show nate s 
    Nathan "Isso não ajuda tanto quanto a gente queria, mas já é alguma coisa. Se você achar mais alguma pista ou prova de quem fez isso, por favor, nos conte, beleza?"
    Sebastian "Tudo bem, digo sim."
    hide seb
    show erika s at right
    Erika "Nathan, acho que a gente podia ir de volta para a biblioteca. Talvez encontremos algo novo por lá dessa vez, é a melhor chance que temos no momento."
    
    if "aliança" in inventory_items:
        show nate n
        Nathan "Você pode ir na frente, eu já te alcanço."
        Erika "Tudo bem! Te vejo lá."
        menu:
            "Devolver a aliança":
                Nathan "Sebastian, eu tenho algo seu aqui comigo."
                hide erika
                show seb c at right
                Sebastian "Hm? Como assim?"
                Nathan "Lembra que você tinha me pedido para encontrar os seus anéis? Então, eu encontrei eles. Aqui, olha."
                $ inventory_items.remove("aliança")
                $ renpy.notify("Você devolveu as alianças")
                $ mostraranel += 1
                Sebastian "NATHAN, VOCÊ É UM ANJO. MUITO OBRIGADO, CARA."
                "Eu sinto o Sebastian quase quebrando minhas costelas com a força com a qual ele me abraçou."
                Nathan "Que nada, cara. Estamos aqui para isso. Bom, agora eu vou indo. Até depois, amigão."
            "Não devolver (Guardar como evidência)":
                Nathan "{i}Acho melhor guardar o anel como evidência, pode ser útil mais tarde{/i}"
                Nathan "É verdade, né? Bom, se cuida, Sebastian. A gente vai conseguir resolver isso alguma hora, não se preocupa."
                Sebastian "Boa sorte para vocês dois!"
        jump bibliotecaday3
    if "aliança" not in inventory_items:
        Nathan "É verdade, né? Bom, se cuida, Sebastian. A gente vai conseguir resolver isso alguma hora, não se preocupa."
        Sebastian "Boa sorte para vocês dois!"
    jump bibliotecaday3

label bibliotecaday3:
    show bg biblioteca fora dia with dissolve
    scene bg biblioteca fora dia
    show halfblack
    show erika s at right
    Erika "Bom, chegamos, vamos procurar lá dentro"
    hide erika 
    show bg biblioteca dentro dia with dissolve
    scene bg biblioteca dentro dia 
    show halfblack
    "Assim que entramos na biblioteca e começamos a vasculhar entre as prateleiras, tirando e colocando livros do lugar." 
    pause
    show bg biblioteca dentro tarde with dissolve
    "Até que acabamos derrubando alguns deles."
    hide halfblack 
    show bg biblioteca tarde with hpunch
    show halfblack
    "Assim que os livros caem, o bibliotecário joseph se aproxima de nós, aparentemente ele não sabia que estávamos por lá."
    show erika s2 at left with vpunch
    Erika "Ahh!{nw}{w=0.5}"
    hide erika
    show joseph f at right
    Joseph "Tudo bem por aqui? Posso ajudar vocês com alguma coisa, jovens?"
    show nate s at left
    Nathan "N-não, não precisa, obrigado."
    show joseph s
    Joseph "Tem certeza? você parece meio assustado, está tudo bem?"
    hide nate 
    show erika s at left
    Erika "Nós já vimos tudo o que precisavamos, obrigado, já estamos de saída"
    Joseph "Esperem!{nw}{w=2.0}"
    hide joseph
    hide nate 
    hide erika 
    show bg biblioteca fora tarde with dissolve
    scene bg biblioteca fora tarde 
    show halfblack
    show erika s at right
    Erika "Cara, que medo, achei que ele ia esfaquear a gente, sei lá."
    show nate s at left
    Nathan "Nem me fala, já a segunda vez que ele faz isso e eu saio correndo de lá, melhor tomarmos mais cuidado de agora em diante"
    Nathan "Mas consegui perceber uma coisa."
    show erika n
    Erika "O quê?"
    show nate n
    Nathan "Ele estava com a perna machucada e mancando."
    show erika t
    Erika "E o que isso tem a ver?"
    Nathan "O ladrão tem assaltado as lojas entrando pelas janelas, ele deve ter se cortado no vidro."
    show erika n2
    Erika "Realmente, faz sentido!"
    show erika n
    Erika "O que a gente faz agora?"
    Nathan "Acho que vou procurar alguém que possa nos ajudar"
    Erika "Certo, eu acho que vou pra casa então, ta ficando tarde, não gosto de sair a noite."
    Erika "Você devia ir pra casa também"
    show nate f
    Nathan "Tá tranquilo, posso pegar carona com meu pai depois alguém na delegacia deve saber de algo"
    show erika n2
    Erika "Tudo bem então, te vejo amanha nate!"
    hide nateral
    hide erika
    jump delegaciaday3

label delegaciaday3:
    show bg delegacia frente dia tarde with dissolve
    scene bg delegacia frente dia tarde
    "Antes de entrar na delegacia, john e camilla me abordam"
    John "Cara, eu acho que você devia falar direto com seu pai, será que ele conseguiria entender o que você ta fazendo? Ele se desculpou afinal."
    Nathan "Não sei, não parece uma boa ideia..."
    Camilla "Não confio tanto no seu pai não, você lembra daquela moça de verde? Achei ela legal, talvez seja melhor falar com ela."
    Nathan "A vivian?"
    Camilla "É, isso mesmo."
    menu:
        "Falar com o pai":
            jump delegaciapai
        "Falar com a Vivian":
            jump delegaciavivian


label delegaciavivian:
    Nathan "{i}Espero que aquele David não esteja por aqui, assim poderia falar com a Vivian com tranquilidade.{/i}"
    "Entrando no prédio me deparo com a Vivian na recepção"
    Nathan "Com licença, você é a Vivian, certo?"
    Vivian "Oii, você pe aquele garoto daquele dia né? Precisa de alguma coisa?"
    Nathan "Na verdade, eu acho que tenho algumas informações importantes para o caso."
    Vivian "Sério? Que bom! Desembuxa."
    Nathan "Acho que sei quem está cometendo os crimes recentes"
    Nathan "Encontrei uma das alianças na entrada da biblioteca e o bibliotecario de lá estava com a perna mancando por conta de um corte"
    Vivian "O Joseph?? impossivel, eu conheço ele a anos, já até namoramos, ele nunca faria uma coisa dessas"
    Nathan "Eu estou com uma das alianças aqui, veja"
    Vivian "hmm, isso é estranho, te garanto que ele não faria nada assim, deve ter sido um engano"
    if pegaranel >= 1:
        if mostraranel >= 1:
            "Procuro a aliança no meu bolso, mas esqueci que já tinha entregado ela pro Sebastian"
            Nathan "Na verdade, eu tinha a alianças comigo, só que eu ja devolvi ela pro respectivo dono"
            Vivian "Então você vem no meu trabalho, acusa alguém, e não me mostra prova nenhuma?"
            Nathan "Eu juro pra você que eu tinha a aliança comigo"
            Vivian "Olha garoto, somos policiais, não trabalhamos na base do ''eu acho''"
            "Antes que pudessemos concluir a conversa meu pai aparece na recepção"
        else:
            Vivian ":)"
            $ moralfinalbom += 1
    else:
        Vivian ":/"

label delegaciapai:
    pause
    show black with dissolve
    jump demoend


label demoend:
    "Obrigado por jogar a demo! Não esqueça de preencher o formulário. Se possível, também chame mais alguém para testar nosso jogo, por favor!"
    pause

"O biblioteca tenta vir atrás da gente mas não consegue acompanhar nosso ritmo, ao olhar para trás percebo que ele está com uma perna machucada e mancando"

