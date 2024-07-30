#{b}жирный текст {i}Курсив{/i} опять жирный{b}
define m = Character('sobaka', color="#2e1e00ff")

define s = Character('shkolnik', color="#ff0000ff")


define is_draw = False

init:
    $ left2 = Position(xalign=0.4, yalign=1.0)
    $ right2 = Position(xalign=0.8, yalign=1.0)

label start:
    scene bg bed
    with fade
    
    transform fade_in:
        alpha 0.0
        linear 3.0 alpha 1.0

    show maksim main at fade_in

    m "{cps=10}Ой maksim ты дома"

    hide m
    with dissolve 

    transform jjjj_in:
        xpos 0
        alpha 0
        linear 2.0 xpos 0.35 alpha 1.0
    show maksim main at jjjj_in
    with fade
    m "eshkere"
 
    hide maksim
    with fade


    transform stopuguf_pk:
        xpos 0.35
        linear 1 xpos 0 alpha 0
        linear 4 xpos 3 alpha 1.0
        repeat

    show maksim main at stopuguf_pk
    with fade

    
    
    "mmmmmmmmmmmmmm"
    
    hide maksim
    with fade

    transform stopuguf_pkf:
        xpos 0.35
        linear 1 ypos 0 alpha 0
        linear 4 ypos 3 alpha 1.0
        repeat
    show maksim main at stopuguf_pkf
    with fade
    
    xpos, ypos, xzoom, yzoom, alpha, protate, linear, 
    "dwedwedwedwed"



    #$ valide_name = False

    #while not valide_name:
    #    $ name = renpy.input('Введите имя: ')

    #    if name.isalpha() and len(name) <= 14:
    #        $ valide_name = True
    #     else:
    #        "Имя должно быть короче "
        

    #scene bg bed

    #show maksim main at left2
    #with 

    #m " Ой [name] ты дома"

    #m "а я думал ты @@@@@ пошёл"
    #menu :

    #    "ya bil tam":
    #        $ is_draw = True
    #        jump label1
    #    "ya bil v drugom meste":
    #        jump label1


 
#label label1:
#    "......."
#    if is_draw:
#        m "nu i kak tam?"

#        return
#    else:
#        m "a gde ti bil?"
#        play sound "sirena.mp3"
#        "{b} Воздушная {b} тревога "
#        m "chto proishodit"
#    return

#    show maksim main at left



#label 2:
#    scene bg bed 

#    show maksim main at center










# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
#define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
#label start:

#    scene bg room

#    show eileen happy

#    e "Вы создали новую игру Ren'Py."

#    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

#    return
