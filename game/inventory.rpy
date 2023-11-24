screen inventory_display_toggle:
    zorder 92 #ordem de aparaição por camadas, 0 sendo o mais baixo, aqui ta 92 pra ter certeza que ele fique por cima de tudo
   


default item_descriptions = {
    "chave": "a chave da casa da erika",
    "aliança": "talvez o lucas saiba algo sobre isso",
    "distintivo": "o david deve precisar disso",
    "caderno fechado": "o caderno de anotações da vivian",
    "caderno aberto": "o caderno de anotações da vivian",
    "arquivos": "arquivos suspeitos",
    "luvas": "está escrito donovan em uma delas...",
    "Lista de compras": "Uma tarefa que sua mãe lhe deu"
}
default inventory_items = []
default item_description = ""


default item_images = {
    "chave": "images/chave.png",
    "aliança": "images/aliança.png",
    "distintivo": "images/distintivo.png",
    "caderno fechado": "images/caderno anotação fechado.png",
    "caderno aberto": "images/caderno anotação aberto.png",
    "arquivos": "images/arquivos.png",
    "luvas": "images/luvas.png",
    "Lista de compras": "images/Lista de compras.png"
} # imagens devem ser pequenas para caber no inventário


style inv_button:
    xsize 300
    ysize 250


#style inv_button_text:
    #xalign 0.5
    #yalign 0.5


screen inventory_item_description:
    # use this based on your preference
    modal True
    imagebutton:
        xalign 0.0
        yalign 1.0
        auto "Mochila %s.png"
        action ToggleScreen("inventory_item_description")
    window:
        background "#FFFFFF" #pode ser trocado por uma imagem
        xsize 600 #o tamanho do inventário na tela, lembre desses numero caso queira trocar por uma imagem
        ysize 150
        xalign 0.5
        yalign 0.1
        text item_description:
            xfill True
            yfill True
            xalign 0.5  # Adicione esta linha para centralizar horizontalmente
            yalign 0.5  # Adicione esta linha para centralizar verticalmente
            color "#000000"


    window:
        background "gui/fundo inv.png" #pode ser trocado por uma imagem
        xsize 1290 #o tamanho do inventário na tela, lembre desses numero caso queira trocar por uma imagem
        ysize 600
        xalign 0.5
        yalign 0.7
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in inventory_items:
                button:
                    image item_images.get(item)
                    action [SetVariable("item_description", item_descriptions.get(item)), SetVariable("selected_item", item)]
                    selected False




    on "hide" action SetVariable("item_description", "")