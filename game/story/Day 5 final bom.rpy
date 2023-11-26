label delegaciavivian2:
    show bg delegacia frente dia with dissolve
    pause 1.0
    show bg delegacia frente dia tarde with dissolve
    pause 1.0
    show bg delegacia dentro with dissolve
    pause 1.0
    "Vivian estava trabalhando na recepção, então assim que entrei ela me percebeu"
    Vivian "Nathan! Que surpresa vê-lo por aqui de novo. O que posso fazer por você hoje?"
    Nathan "Oi, Vivian. Desculpa te incomodar de novo, mas eu encontrei essa chave ontem a noite, acabei esbarrando no Joseph. Pensei que talvez você pudesse me ajudar."
    Vivian "Claro! Você se importa de me entregar a chave?"
    Nathan "Ah não, claro que não."
    $ renpy.notify("Você entrega a chave para Vivian analisar.")
    Vivian "Interessante. Essa chave parece ser da biblioteca em si."
    Nathan "Você acha que a gente poderia usar essa chave pra procurar algum tipo de evidência por lá?"
    Vivian "Poder a gente até pode mas, eu não sei se seria muito legal sem um protocolo ou mandato. A biblioteca é um local público e invadir sem uma causa justificada pode ser bem problemático."
    Nathan "Vivian, essa pode ser a única chance que nós temos de encontrar algo incriminador de verdade."
    Vivian "Você tem um bom ponto.. Mas eu não posso."
    Nathan "Você também quer investigar lá não quer?"
    Vivian "..."
    Vivian "Talvez."
    Nathan "O máximo que pode acontecer é a gente não encontrar nada."
    Vivian "Se acontecer algo de ruim, o peso vai cair nas suas costas ouviu? Vamos logo antes que eu mude de ideia"
    "Então eu e Vivian fomos até a bilbioteca"
    hide nate 
    hide vivian
    jump bibliotecaday5

label bibliotecaday5:
    show bg biblioteca fora dia with dissolve
    pause 1.0
    show bg biblioteca dentro dia with dissolve
    pause 1.0
    Vivian "Tá bom, Nathan. Vamos investigar a biblioteca juntos. Mas lembre-se, estamos agindo sob nossa própria responsabilidade."
    Nathan "Blá blá blá.é só a gente seguir com cuidado e dá tudo certo. Quanto mais rápido encontrarmos algo, mais rápido a gente vaza."
    Vivian "Tudo bem, você pode investigar o que quiser aí, eu vou ver se encontro algo nas câmeras, se a senha não mudou desde que o Joseph me mostrou, é fácil de acessar."
    "A vivian entrou em uma sala apenas para funcionários para poder olhar as gravações antigas"
    Nathan "Agora é minha vez, por onde eu começo?"
    menu:
        "Estante":
            $ procuraestante += 1
        "Bancada principal" if procuraestante >= 1:
            $ procurabancada += 1
        "Prateleira" if procurabancada >= 1:
            $ procuraprateleira += 1
        "Levantar o tapete" if procuraprateleira >= 1:
            show bg biblioteca segredo dia with dissolve
            scene bg biblioteca segredo dia