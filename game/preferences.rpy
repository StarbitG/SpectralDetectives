 # preferences.rpy
screen preferences():
    add "gui/overlay/preference menu.png"
    tag menu

    if renpy.variant("pc") or renpy.variant("web"):

        frame:
            pos 450, 180
            padding (10, 0, 10, 10)
            xsize 250
            ysize 230
            vbox:
                style_prefix "radio"
                label _("  Tela")
                textbutton _("  Janela") action Preference("display", "window")
                textbutton _("  Tela cheia") action Preference("display", "fullscreen")
    frame:
        pos 830, 180
        padding (20, 0, 10, 10)
        xsize 350
        ysize 230
        vbox:
            style_prefix "check"
            label _("   Pular")
            textbutton _("Texto novo") action Preference("skip", "toggle")
            textbutton _("Após as escolhas") action Preference("after choices", "toggle")
            textbutton _("Transições") action InvertSelected(Preference("transitions", "toggle"))

    frame:
        pos 500, 490
        padding (20, 0, 10, 10)
        style_prefix "slider"
        xsize 560
        hbox:
            vbox:
                label _("   Velocidade do texto") 
                bar value Preference("text speed")
                label _("   Tempo de texto automático")
                bar value Preference("auto-forward time")

                

    frame:
            pos 1190, 490
            padding (20, 0, 10, 10)
            style_prefix "slider"
            xsize 560
            hbox:
                vbox:
                    if config.has_music:
                        label _("   Volume da música")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("   Volume do som")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("   Volume da voz")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("  Silenciar tudo"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


    textbutton _("  Voltar"):
        pos (150, 1090)
        text_size 75
        style "return_button"
        action Return()


                 
#   use game_menu(_("Preferences"), scroll="viewport"):

#     vbox:

#         hbox:
#             box_wrap True

#             if renpy.variant("pc") or renpy.variant("web"):

#                 vbox:
#                     style_prefix "radio"
#                     label _("Display")
#                     textbutton _("Window") action Preference("display", "window")
#                     textbutton _("Fullscreen") action Preference("display", "fullscreen")

#             vbox:
#                 style_prefix "check"
#                 label _("Skip")
#                 textbutton _("Unseen Text") action Preference("skip", "toggle")
#                 textbutton _("After Choices") action Preference("after choices", "toggle")
#                 textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

#                 # Additional vboxes of type "radio_pref" or "check_pref" can be
#                 # added here, to add additional creator-defined preferences.

#         null height (4 * gui.pref_spacing)

#         hbox:
#             style_prefix "slider"
#             box_wrap True

#             vbox:

#                 label _("Text Speed")

#                 bar value Preference("text speed")

#                 label _("Auto-Forward Time")

#                 bar value Preference("auto-forward time")

#             vbox:

#                 if config.has_music:
#                     label _("Music Volume")

#                     hbox:
#                         bar value Preference("music volume")

#                 if config.has_sound:

#                     label _("Sound Volume")

#                     hbox:
#                         bar value Preference("sound volume")

#                         if config.sample_sound:
#                             textbutton _("Test") action Play("sound", config.sample_sound)


#                 if config.has_voice:
#                     label _("Voice Volume")

#                     hbox:
#                         bar value Preference("voice volume")

#                         if config.sample_voice:
#                             textbutton _("Test") action Play("voice", config.sample_voice)

#                 if config.has_music or config.has_sound or config.has_voice:
#                     null height gui.pref_spacing

#                     textbutton _("Mute All"):
#                         action Preference("all mute", "toggle")
#                         style "mute_all_button"