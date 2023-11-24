# # retorno conversas
# label retornoCasal:
#     call screen botaoCasal
# label retornoAbandonado:
#     call screen botaoErika with dissolve
# label retornoQuarto:
#     call screen botaoQuarto with dissolve
# label retornoBiblioteca:
#     call screen botaoJornal with dissolve    

# label shop:
#     scene bg shop conversa
#     # Isso inicia a música, com o sino antes
#     play audio "sfx sino.mp3"
#     show luca n:
#         pos (810, 110)
#     Lucas "Bem vindo a nossa loja!"
#     menu:
#         "Biblioteca":
#             stop music  # Stop the current playing music
#             play music "escritorio.mp3"
#             call screen botaoJornal with fade
#         "Local abandonado":
#             stop music
#             play music "wind.mp3"
#             call screen botaoErika with fade
#         "Quarto":
#             stop music
#             play music "escritorio.mp3"
#             call screen botaoQuarto with fade
#         "Chave" if "chave" in inventory_items:
#             Lucas "voce tem uma chave!"
#         "Retornar":
#             jump retornoCasal
# return 

# # label biblioteca:
# #     scene bg biblioteca conversa
# #     show jornalista neutro at right with dissolve
# #     Vivian "texto texto texto Nome"

# #     menu:
# #         "Loja":
# #             stop music
# #             play music "shop.mp3"
# #             call screen botaoCasal with fade
# #         "Local Abandonado":
# #             stop music
# #             play music "wind.mp3"
# #             call screen botaoErika with fade
# #         "Quarto":
# #             stop music
# #             play music "escritorio.mp3"
# #             call screen botaoQuarto with fade
# #         "Retornar" :
# #             jump retornoBiblioteca
# #     # Code for the "escritorio" scene
    

# label abandonado:
#     scene bg abandonado
#     show erika n at right with dissolve
#     show vivian n at left with dissolve
#     play music "wind.mp3"
#     Erika "beababdahdada"
#     Vivian "aaaaaaaaaaaaaaaaaaaa"
    
#     menu:
#         "Loja":
#             stop music
#             play music "shop.mp3"
#             call screen botaoCasal with fade
#         "Escritorio":
#             stop music
#             play music "escritorio.mp3"
#             call screen botaoJornal with fade
#         "Quarto":
#             stop music
#             play music "escritorio.mp3"
#             call screen botaoQuarto with fade
#         "Retornar" :
#             jump retornoAbandonado
    

# label Quarto:
#     scene bg quarto quadro
#     show images at right with dissolve
#     d "texto texto texto Nome"
#     $ inventory_items.append("key")
#     menu:
#         "Loja":
#             stop music
#             play music "shop.mp3"
#             call screen botaoCasal with fade
#         "Escritorio":
#             stop music
#             play music "escritorio.mp3"
#             call screen botaoJornal with fade
#         "Local Abandonado":
#             stop music
#             play music "wind.mp3"
#             call screen botaoErika with fade
#         "Retornar" :
#             jump retornoQuarto
#     # Código para a escolha 3
#     # Vá para o local desejado
  