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
    show bg biblioteca fora tarde with dissolve
    pause 1.0
    show bg biblioteca dentro tarde with dissolve
    pause 1.0
    "Jospeh não veio a biblioteca hoje, deve ser porque pegamos a chave dele, essa hora ele deve estar procurando essa coisinha que nem louco em casa."
    Vivian "Tá bom, Nathan. Vamos investigar a biblioteca juntos. Mas lembre-se, estamos agindo sob nossa própria responsabilidade."
    Nathan "Blá blá blá.é só a gente seguir com cuidado e dá tudo certo. Quanto mais rápido encontrarmos algo, mais rápido a gente vaza."
    Vivian "Tudo bem, você pode investigar o que quiser aí, eu vou ver se encontro algo nas câmeras, se a senha não mudou desde que o Joseph me mostrou, é fácil de acessar."
    "A vivian entrou em uma sala apenas para funcionários para poder olhar as gravações antigas"
    Nathan "Agora é minha vez, por onde eu começo?"
    menu:
        "Estante":
            Nathan "Aqui só tem alguns livros infantis, são muito finos pra esconder algo.."
            $ procuraestante += 1
        "Bancada principal" if procuraestante >= 1:
            Nathan "Documentos sobre emprestar e devolver livros, parece que o Lucas pegou algo emprestado faz alguns meses e não devolveu ainda."
            $ procurabancada += 1
        "Prateleira" if procurabancada >= 1:
            "Procurar essa prateleira me faz pensar quando eu comecei a investigar tudo isso. Não parece ter nada por aqui ainda."
            Nathan "Tem que ter alguma coisa por aqui, se aqui não tem nada, o ladrão vai acabar saindo ileso."
            Camilla "Eu acho que ainda pode ter um lugar que você não procurou, pode ser idiota, mas já tentou olhar embaixo do tapete?"
            John "É uma ideia bem besta mesmo, mas parando pra pensar, muitas das soluções até agora foram bem idiotas.."
            Nathan "Eu posso tentar, é nossa última chance de conseguir algo.."
            $ procuraprateleira += 1
        "Levantar o tapete" if procuraprateleira >= 1:
            "Assim que eu levanto o tapete, um cofre é revelado"
            show bg biblioteca segredo tarde with dissolve
            scene bg biblioteca segredo tarde
            Nathan "UM COFRE?"
            "Vivian volta da sala das câmeras"
            Vivian "Você encontrou um cofre? Eu não sabia que eles tinham um cofre na biblioteca"
            Nathan "Eu muito menos, você acha que a gente consegue abrir ele sem senha?"
            Vivian "Conseguir a gente até consgue, mas a pergunta mesmo é se a gente tem tempo pra fazer isso."
            John "Nathan, eu acho que a gente viu algo relacionado a esse cofre quando a gente foi na delegacia pela primeira vez, não?"
            John "Você não acha que seria melhor a gente tentar buscar essa senha antes? Errar a senha demais pode travar o cofre por um tempo desnecessário."
            menu:
                "Chutar a senha":
                    Nathan "Acho que podemos tentar chutar a senha. Talvez tenhamos sorte e acertemos de primeira."
                "Ir buscar a senha":
                    Nathan "Você tem razão, é melhor não desbloquearmos o cofre por agora, acha que teria alguma forma de descobrir a senha sem a gente mexer nele?"
                    Vivian "O Joseph deve saber a senha, o cofre é dele afinal, vou tentar perguntar pra ele mais tarde."

    Vivian "Antes que eu me esqueça, de acordo com as câmeras, Joseph não estava por aqui no horário do crime, não queria ter que fazer isso, mas vou ter que interrogar ele mais a fundo."
    Nathan "Ele não estava aqui? Mas ele praticamente nunca sai da biblioteca."
    Vivian "Essa é a parte esquisita, a câmera é meio ruim por ser antiga, mas eu consegui ver ele saindo daqui claramente."
    Vivian "Bom, parece que nós dois conseguimos ótimas informações nesse tempinho. Acho que deviamos nos spearar por agora, se eu descobrir algo a mais sobre o Joseph, vou te ligar ok?"
    
    
    
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
#A noite você se prepara para outra invasão na delegacia mas a segurança lá parece ter sido reforçada
#Ainda sim você consegue entrar e ir até a sala do seu pai pegar o papel com as combinações
#eles ficam inacreditados da senha ser extremamente simples e que o ladrão não poderia ser burro o suficiente para deixar uma senha assim no cofre
#ninguem fala nada nessa hora
#Por estar muito tarde, john e camilla recomendam que você vá para casa descansar e avise Vivian no dia seguinte
#voce volta pra casa e fim do dia 5

#Dia 6, dia decisivo para a conclusão
#dividir em ifs
#No dia seguinte voce liga para vivian logo cedo e ela fala que encontrou o joseph e pede para que você vá direto para a biblioteca para explicar a situação
#Chegando lá o joseph explica a situação e esclaresse os mal-entendidos e o corte em sua perna, que não tinha nada a ver com os crimes cometidos
#