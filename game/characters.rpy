init python:

    def group_cbs(*callbacks):
        def __inner(*args, **kwargs):
            for cb in callbacks:
                cb(*args, **kwargs)
        return __inner



# Personagens conhecidos
define Camilla = Character("Camilla", color="#7164cf", window_background="images/textboxes/conhecidos/Textbox - Camilla.png" , cb_name='camilla' , callback=group_cbs(name_callback))
image camilla n = At('images/Personagens/Camilla/Camilla - 1.png', sprite_highlight('camilla'))
image camilla t = At('images/Personagens/Camilla/Camilla - 2.png', sprite_highlight('camilla'))
image camilla f = At('images/Personagens/Camilla/Camilla - 3.png', sprite_highlight('camilla'))
image camilla ch = At('images/Personagens/Camilla/Camilla - 4.png', sprite_highlight('camilla'))
image camilla b = At('images/Personagens/Camilla/Camilla - 5.png', sprite_highlight('camilla'))
image camilla ex  = At('images/Personagens/Camilla/Camilla - 6.png', sprite_highlight('camilla'))

define David = Character("David", color="#2c4046", window_background="images/textboxes/conhecidos/Textbox - David.png" , cb_name='david' , callback=group_cbs(name_callback))
image david n = At('images/Personagens/David/David - 1.png', sprite_highlight('david'))
image david t = At('images/Personagens/David/David - 2.png', sprite_highlight('david'))
image david f = At('images/Personagens/David/David - 3.png', sprite_highlight('david'))
image david b = At('images/Personagens/David/David - 4.png', sprite_highlight('david'))
image david ch = At('images/Personagens/David/David - 5.png', sprite_highlight('david'))
image david s  = At('images/Personagens/David/David - 6.png', sprite_highlight('david'))
image david ex = At('images/Personagens/David/David - 7.png', sprite_highlight('david'))

define Erika = Character("Erika", color="#96c7ca", window_background="images/textboxes/conhecidos/Textbox - Erika.png" , cb_name='erika' , callback=group_cbs(name_callback)) # Fantasma boa
image erika n = At('images/Personagens/Erika/Erika - 1.png', sprite_highlight('erika'))
image erika n2 = At('images/Personagens/Erika/Erika - 2.png', sprite_highlight('erika'))
image erika t = At('images/Personagens/Erika/Erika - 3.png', sprite_highlight('erika'))
image erika ch = At('images/Personagens/Erika/Erika - 4.png', sprite_highlight('erika'))
image erika s = At('images/Personagens/Erika/Erika - 5.png', sprite_highlight('erika'))
image erika s2 = At('images/Personagens/Erika/Erika - 6.png', sprite_highlight('erika'))
image erika b = At('images/Personagens/Erika/Erika - 7.png', sprite_highlight('erika'))

define John = Character("John", color="#cba24f", window_background="images/textboxes/conhecidos/Textbox - John.png" , cb_name='john' , callback=group_cbs(name_callback)) # Fantasma boa
image john n = At('images/Personagens/John/John - 1.png', sprite_highlight('john'))
image john f = At('images/Personagens/John/John - 2.png', sprite_highlight('john'))
image john n2 = At('images/Personagens/John/John - 3.png', sprite_highlight('john'))
image john b = At('images/Personagens/John/John - 4.png', sprite_highlight('john'))
image john b2 = At('images/Personagens/John/John - 5.png', sprite_highlight('john'))
image john ch = At('images/Personagens/John/John - 6.png', sprite_highlight('john'))
image john ex = At('images/Personagens/John/John - 7.png', sprite_highlight('john'))

define Joseph = Character("Joseph", color="#9f886f", window_background="images/textboxes/conhecidos/Textbox - Joseph.png" , cb_name='joseph' , callback=group_cbs(name_callback)) # Fantasma boa
image joseph n = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario- 1.png', sprite_highlight('joseph'))
image joseph b = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 2.png', sprite_highlight('joseph'))
image joseph b2 = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 3.png', sprite_highlight('joseph'))
image joseph s = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 4.png', sprite_highlight('joseph'))
image joseph s2 = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 5.png', sprite_highlight('joseph'))
image joseph f = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 6.png', sprite_highlight('joseph'))

define Lucas = Character("Lucas", color="#e3c8d6", window_background="images/textboxes/conhecidos/Textbox - Lucas.png" , cb_name='lucas' , callback=group_cbs(name_callback)) # Fantasma boa
image lucas n = At('images/Personagens/Lucas/Lucas - 1.png', sprite_highlight('lucas'))
image lucas f = At('images/Personagens/Lucas/Lucas - 2.png', sprite_highlight('lucas'))
image lucas s = At('images/Personagens/Lucas/Lucas - 3.png', sprite_highlight('lucas'))
image lucas s2 = At('images/Personagens/Lucas/Lucas - 4.png', sprite_highlight('lucas'))
image lucas ch = At('images/Personagens/Lucas/Lucas - 5.png', sprite_highlight('lucas'))
image lucas b = At('images/Personagens/Lucas/Lucas - 6.png', sprite_highlight('lucas'))
image lucas b2 = At('images/Personagens/Lucas/Lucas - 7.png', sprite_highlight('lucas'))
image lucas ex = At('images/Personagens/Lucas/Lucas - 8.png', sprite_highlight('lucas'))

define Mãe = Character("mae", color="#7c8761", window_background="images/textboxes/conhecidos/Textbox - Mãe do protagonista.png" , cb_name='mae' , callback=group_cbs(name_callback)) # Fantasma boa
image mae n = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 1.png', sprite_highlight('mae'))
image mae f = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 2.png', sprite_highlight('mae'))
image mae b = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 3.png', sprite_highlight('mae'))
image mae t = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 4.png', sprite_highlight('mae'))
image mae s = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 5.png', sprite_highlight('mae'))
image mae s2 = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 6.png', sprite_highlight('mae'))

define Nathan = Character("Nathan", color="#636363", window_background="images/textboxes/conhecidos/Textbox - Nathan.png" , cb_name='nate' , callback=group_cbs(name_callback))
image nate b = At('images/Personagens/Nathan/Nathan Final - 1.png', sprite_highlight('nate'))
image nate s2 = At('images/Personagens/Nathan/Nathan Final - 2.png', sprite_highlight('nate'))
image nate s = At('images/Personagens/Nathan/Nathan Final - 3.png', sprite_highlight('nate'))
image nate a = At('images/Personagens/Nathan/Nathan Final - 4.png', sprite_highlight('nate'))
image nate n = At('images/Personagens/Nathan/Nathan Final - 5.png', sprite_highlight('nate'))
image nate f = At('images/Personagens/Nathan/Nathan Final - 6.png', sprite_highlight('nate'))
image nate f2 = At('images/Personagens/Nathan/Nathan Final - 7.png', sprite_highlight('nate'))
image nate ch = At('images/Personagens/Nathan/Nathan Final - 8.png', sprite_highlight('nate'))
image nate ex = At('images/Personagens/Nathan/Nathan Final - 9.png', sprite_highlight('nate'))
image nate ns = At('images/Personagens/Nathan/Nathan Final - 10.png', sprite_highlight('nate'))


define Pai = Character("Pai", color="#254153", window_background="images/textboxes/conhecidos/Textbox - Pai do protagonista.png" , cb_name='pai' , callback=group_cbs(name_callback))
image pai n = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 1.png', sprite_highlight('pai'))
image pai n2 = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 2.png', sprite_highlight('pai'))
image pai b = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 3.png', sprite_highlight('pai'))
image pai s = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 4.png', sprite_highlight('pai'))
image pai s2 = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 5.png', sprite_highlight('pai'))
image pai n3 = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 6.png', sprite_highlight('pai'))
image pai f = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 7.png', sprite_highlight('pai'))

define Sebastian = Character("Sebastian", color="#242424", window_background="images/textboxes/conhecidos/Textbox - Sebastian.png" , cb_name='seb' , callback=group_cbs(name_callback))
image seb n = At('images/Personagens/Sebastian/Sebastian - 1.png', sprite_highlight('seb'))
image seb f = At('images/Personagens/Sebastian/Sebastian - 2.png', sprite_highlight('seb'))
image seb f2 = At('images/Personagens/Sebastian/Sebastian - 3.png', sprite_highlight('seb'))
image seb c = At('images/Personagens/Sebastian/Sebastian - 4.png', sprite_highlight('seb'))
image seb s = At('images/Personagens/Sebastian/Sebastian - 5.png', sprite_highlight('seb'))
image seb s2 = At('images/Personagens/Sebastian/Sebastian - 6.png', sprite_highlight('seb'))
image seb b = At('images/Personagens/Sebastian/Sebastian - 7.png', sprite_highlight('seb'))

define Vivian = Character("Vivian", color="#8b8b59", window_background="images/textboxes/conhecidos/Textbox - Vivian.png" , cb_name='vivian' , callback=group_cbs(name_callback))
image vivian n = At('images/Personagens/Vivian/Vivian - 1.png', sprite_highlight('vivian'))
image vivian f = At('images/Personagens/Vivian/Vivian - 2.png', sprite_highlight('vivian'))
image vivian f2 = At('images/Personagens/Vivian/Vivian - 3.png', sprite_highlight('vivian'))
image vivian b = At('images/Personagens/Vivian/Vivian - 4.png', sprite_highlight('vivian'))
image vivian s = At('images/Personagens/Vivian/Vivian - 5.png', sprite_highlight('vivian'))
image vivian s2 = At('images/Personagens/Vivian/Vivian - 6.png', sprite_highlight('vivian'))
image vivian t = At('images/Personagens/Vivian/Vivian - 7.png', sprite_highlight('vivian'))


#Personagens desconhecidos

define dCamilla = Character("Camilla", color="#7164cf", window_background="images/textboxes/desconhecidos/Textbox - Camilla.png" , cb_name='camilla' , callback=group_cbs(name_callback))
image camilla n = At('images/Personagens/Camilla/Camilla - 1.png', sprite_highlight('camilla'))
image camilla t = At('images/Personagens/Camilla/Camilla - 2.png', sprite_highlight('camilla'))
image camilla f = At('images/Personagens/Camilla/Camilla - 3.png', sprite_highlight('camilla'))
image camilla ch = At('images/Personagens/Camilla/Camilla - 4.png', sprite_highlight('camilla'))
image camilla b = At('images/Personagens/Camilla/Camilla - 5.png', sprite_highlight('camilla'))
image camilla ex  = At('images/Personagens/Camilla/Camilla - 6.png', sprite_highlight('camilla'))

define dDavid = Character("David", color="#2c4046", window_background="images/textboxes/desconhecidos/Textbox - David.png" , cb_name='david' , callback=group_cbs(name_callback))
image david n = At('images/Personagens/David/David - 1.png', sprite_highlight('david'))
image david t = At('images/Personagens/David/David - 2.png', sprite_highlight('david'))
image david f = At('images/Personagens/David/David - 3.png', sprite_highlight('david'))
image david b = At('images/Personagens/David/David - 4.png', sprite_highlight('david'))
image david ch = At('images/Personagens/David/David - 5.png', sprite_highlight('david'))
image david s  = At('images/Personagens/David/David - 6.png', sprite_highlight('david'))
image david ex = At('images/Personagens/David/David - 7.png', sprite_highlight('david'))

define dErika = Character("Erika", color="#96c7ca", window_background="images/textboxes/desconhecidos/Textbox - Erika.png" , cb_name='erika' , callback=group_cbs(name_callback)) # Fantasma boa
image erika n = At('images/Personagens/Erika/Erika - 1.png', sprite_highlight('erika'))
image erika n2 = At('images/Personagens/Erika/Erika - 2.png', sprite_highlight('erika'))
image erika t = At('images/Personagens/Erika/Erika - 3.png', sprite_highlight('erika'))
image erika ch = At('images/Personagens/Erika/Erika - 4.png', sprite_highlight('erika'))
image erika s = At('images/Personagens/Erika/Erika - 5.png', sprite_highlight('erika'))
image erika s2 = At('images/Personagens/Erika/Erika - 6.png', sprite_highlight('erika'))
image erika b = At('images/Personagens/Erika/Erika - 7.png', sprite_highlight('erika'))

define dJohn = Character("John", color="#cba24f", window_background="images/textboxes/desconhecidos/Textbox - John.png" , cb_name='john' , callback=group_cbs(name_callback)) # Fantasma boa
image john n = At('images/Personagens/John/John - 1.png', sprite_highlight('john'))
image john f = At('images/Personagens/John/John - 2.png', sprite_highlight('john'))
image john n2 = At('images/Personagens/John/John - 3.png', sprite_highlight('john'))
image john b = At('images/Personagens/John/John - 4.png', sprite_highlight('john'))
image john b2 = At('images/Personagens/John/John - 5.png', sprite_highlight('john'))
image john ch = At('images/Personagens/John/John - 6.png', sprite_highlight('john'))
image john ex = At('images/Personagens/John/John - 7.png', sprite_highlight('john'))

define dJoseph = Character("Joseph", color="#9f886f", window_background="images/textboxes/desconhecidos/Textbox - Joseph.png" , cb_name='joseph' , callback=group_cbs(name_callback)) # Fantasma boa
image joseph n = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario- 1.png', sprite_highlight('joseph'))
image joseph b = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 2.png', sprite_highlight('joseph'))
image joseph b2 = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 3.png', sprite_highlight('joseph'))
image joseph s = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 4.png', sprite_highlight('joseph'))
image joseph s2 = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 5.png', sprite_highlight('joseph'))
image joseph f = At('images/Personagens/Joseph - Bibliotecario/Bibliotecario - 6.png', sprite_highlight('joseph'))

define dLucas = Character("Lucas", color="#e3c8d6", window_background="images/textboxes/desconhecidos/Textbox - Lucas.png" , cb_name='lucas' , callback=group_cbs(name_callback)) # Fantasma boa
image lucas n = At('images/Personagens/Lucas/Lucas - 1.png', sprite_highlight('lucas'))
image lucas f = At('images/Personagens/Lucas/Lucas - 2.png', sprite_highlight('lucas'))
image lucas s = At('images/Personagens/Lucas/Lucas - 3.png', sprite_highlight('lucas'))
image lucas s2 = At('images/Personagens/Lucas/Lucas - 4.png', sprite_highlight('lucas'))
image lucas ch = At('images/Personagens/Lucas/Lucas - 5.png', sprite_highlight('lucas'))
image lucas b = At('images/Personagens/Lucas/Lucas - 6.png', sprite_highlight('lucas'))
image lucas b2 = At('images/Personagens/Lucas/Lucas - 7.png', sprite_highlight('lucas'))
image lucas ex = At('images/Personagens/Lucas/Lucas - 8.png', sprite_highlight('lucas'))

define dmae = Character("mae", color="#7c8761", window_background="images/textboxes/desconhecidos/Textbox - Mãe do protagonista.png" , cb_name='mae' , callback=group_cbs(name_callback)) # Fantasma boa
image mae n = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 1.png', sprite_highlight('mae'))
image mae f = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 2.png', sprite_highlight('mae'))
image mae b = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 3.png', sprite_highlight('mae'))
image mae t = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 4.png', sprite_highlight('mae'))
image mae s = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 5.png', sprite_highlight('mae'))
image mae s2 = At('images/Personagens/Mãe do protagonista/Mãe do protagonista - 6.png', sprite_highlight('mae'))

define dNathan = Character("Nathan", color="#636363", window_background="images/textboxes/desconhecidos/Textbox - Nathan.png" , cb_name='nate' , callback=group_cbs(name_callback))
image nate b = At('images/Personagens/Nathan/Nathan Final - 1.png', sprite_highlight('nate'))
image nate s2 = At('images/Personagens/Nathan/Nathan Final - 2.png', sprite_highlight('nate'))
image nate s = At('images/Personagens/Nathan/Nathan Final - 3.png', sprite_highlight('nate'))
image nate a = At('images/Personagens/Nathan/Nathan Final - 4.png', sprite_highlight('nate'))
image nate n = At('images/Personagens/Nathan/Nathan Final - 5.png', sprite_highlight('nate'))
image nate f = At('images/Personagens/Nathan/Nathan Final - 6.png', sprite_highlight('nate'))
image nate f2 = At('images/Personagens/Nathan/Nathan Final - 7.png', sprite_highlight('nate'))
image nate ch = At('images/Personagens/Nathan/Nathan Final - 8.png', sprite_highlight('nate'))
image nate ex = At('images/Personagens/Nathan/Nathan Final - 9.png', sprite_highlight('nate'))

define dPai = Character("Pai", color="#254153", window_background="images/textboxes/desconhecidos/Textbox - Pai do protagonista.png" , cb_name='pai' , callback=group_cbs(name_callback))
image pai n = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 1.png', sprite_highlight('pai'))
image pai n2 = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 2.png', sprite_highlight('pai'))
image pai b = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 3.png', sprite_highlight('pai'))
image pai s = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 4.png', sprite_highlight('pai'))
image pai s2 = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 5.png', sprite_highlight('pai'))
image pai n3 = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 6.png', sprite_highlight('pai'))
image pai f = At('images/Personagens/Pai do Protagonista - Fabio - Delegado Fabio/Pai do protagonista - 7.png', sprite_highlight('pai'))

define dSebastian = Character("Sebastian", color="#242424", window_background="images/textboxes/desconhecidos/Textbox - Sebastian.png" , cb_name='seb' , callback=group_cbs(name_callback))
image seb n = At('images/Personagens/Sebastian/Sebastian - 1.png', sprite_highlight('seb'))
image seb f = At('images/Personagens/Sebastian/Sebastian - 2.png', sprite_highlight('seb'))
image seb f2 = At('images/Personagens/Sebastian/Sebastian - 3.png', sprite_highlight('seb'))
image seb c = At('images/Personagens/Sebastian/Sebastian - 4.png', sprite_highlight('seb'))
image seb s = At('images/Personagens/Sebastian/Sebastian - 5.png', sprite_highlight('seb'))
image seb s2 = At('images/Personagens/Sebastian/Sebastian - 6.png', sprite_highlight('seb'))
image seb b = At('images/Personagens/Sebastian/Sebastian - 7.png', sprite_highlight('seb'))

define dVivian = Character("Vivian", color="#8b8b59", window_background="images/textboxes/desconhecidos/Textbox - Vivian.png" , cb_name='vivian' , callback=group_cbs(name_callback))
image vivian n = At('images/Personagens/Vivian/Vivian - 1.png', sprite_highlight('vivian'))
image vivian f = At('images/Personagens/Vivian/Vivian - 2.png', sprite_highlight('vivian'))
image vivian f2 = At('images/Personagens/Vivian/Vivian - 3.png', sprite_highlight('vivian'))
image vivian b = At('images/Personagens/Vivian/Vivian - 4.png', sprite_highlight('vivian'))
image vivian s = At('images/Personagens/Vivian/Vivian - 5.png', sprite_highlight('vivian'))
image vivian s2 = At('images/Personagens/Vivian/Vivian - 6.png', sprite_highlight('vivian'))