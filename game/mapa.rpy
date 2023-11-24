# Mapa

screen map:
    image "bg map.jpg"
    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "Red_button_%s.png"
        action Hide(), Show("botaoQuarto", fade)
    
    imagebutton:
        xalign 1.0
        yalign 0.5
        auto "Red_button_%s.png"
        action Hide(), Show('botaoCasal', fade)

    imagebutton:
        xalign 0.0
        yalign 0.5
        auto "Red_button_%s.png"
        action Hide(), Show('botaoJornal', fade)

    imagebutton:
        xalign 1.0
        yalign 0.0
        auto "Red_button_%s.png"
        action Hide(), Show('botaoErika', fade)