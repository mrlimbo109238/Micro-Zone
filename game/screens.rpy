################################################################################
## Micro Zone — Кастомные экраны интерфейса
################################################################################
## Здесь переопределены только те экраны, которые отличаются от
## стандартных Ren'Py: главное меню (с грозой) и настройки (с тремя
## отдельными ползунками громкости). Остальные экраны (сохранение,
## загрузка, паузная навигация и т.п.) использует встроенные
## стандартные Ren'Py.
################################################################################


################################################################################
## АНИМИРОВАННЫЙ ФОН ГЛАВНОГО МЕНЮ
################################################################################
## Спокойная картинка с долгими паузами и редкими "вспышками молнии"
## (двойными и одиночными). Не идеально под бит, но создаёт ощущение
## живой грозы — глаз и ухо ловят ритм.
##
## Limbo: если хочешь поменять "ритм" — крути цифры в pause. Маленькие
## (0.1, 0.2) — длительность вспышки. Большие (3-7) — пауза между ними.
################################################################################

image bg_main_menu:
    # масштабируем под игру 1920x1080
    Transform("bg_menu_calm.jpg", size=(1920, 1080))
    pause 4.5
    Transform("bg_menu_lightning.jpg", size=(1920, 1080))
    pause 0.18
    Transform("bg_menu_calm.jpg", size=(1920, 1080))
    pause 0.07
    Transform("bg_menu_lightning.jpg", size=(1920, 1080))
    pause 0.13
    Transform("bg_menu_calm.jpg", size=(1920, 1080))
    pause 6.2
    Transform("bg_menu_lightning.jpg", size=(1920, 1080))
    pause 0.22
    Transform("bg_menu_calm.jpg", size=(1920, 1080))
    pause 3.8
    Transform("bg_menu_lightning.jpg", size=(1920, 1080))
    pause 0.10
    Transform("bg_menu_calm.jpg", size=(1920, 1080))
    pause 0.05
    Transform("bg_menu_lightning.jpg", size=(1920, 1080))
    pause 0.16
    Transform("bg_menu_calm.jpg", size=(1920, 1080))
    pause 7.5
    repeat


################################################################################
## ГЛАВНОЕ МЕНЮ
################################################################################

screen main_menu():

    tag menu

    ## Фон с грозой.
    add "bg_main_menu"

    ## Лёгкая виньетка слева, чтобы белые буквы кнопок читались поверх
    ## дерева/неба независимо от вспышек.
    add Solid("#00000099") xpos 0 ypos 0 xsize 720 ysize 1080

    ## Музыка главного меню. Если файл ещё не залит — Ren'Py молча
    ## пропустит и не упадёт.
    on "show" action Play("menu_music", "menu_start.mp3", fadein=1.5, if_changed=True)
    on "replace" action Play("menu_music", "menu_start.mp3", fadein=1.5, if_changed=True)
    on "hide" action Stop("menu_music", fadeout=1.0)

    ## Большая надпись "MICRO ZONE" сверху.
    text "MICRO ZONE":
        xpos 70
        ypos 70
        size 110
        bold True
        color "#ffffff"
        outlines [(4, "#000000", 0, 0)]

    ## Вертикальный столбик кнопок слева.
    vbox:
        xpos 70
        ypos 280
        spacing 35

        textbutton _("ИГРАТЬ"):
            text_size 90
            text_color "#ffffff"
            text_hover_color "#CE93D8"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            action Start()

        textbutton _("НАСТРОЙКИ"):
            text_size 64
            text_color "#ffffff"
            text_hover_color "#CE93D8"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            action ShowMenu("preferences")

        textbutton _("ПРОДОЛЖИТЬ"):
            text_size 56
            text_color "#dddddd"
            text_hover_color "#CE93D8"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            action Continue()

        textbutton _("ВЫЙТИ"):
            text_size 56
            text_color "#dddddd"
            text_hover_color "#ff6b6b"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            action Quit(confirm=False)

    ## Подпись автора в правом нижнем углу (как на твоём макете).
    text "MR LIMBO":
        xpos 1920 - 70
        ypos 1080 - 70
        xanchor 1.0
        yanchor 1.0
        size 42
        color "#ffffffcc"
        outlines [(2, "#000000", 0, 0)]
        italic True


################################################################################
## НАСТРОЙКИ (с тремя отдельными ползунками громкости)
################################################################################
## Limbo, тут отображается то же что Ren'Py показывает по умолчанию,
## плюс три ползунка громкости: меню-музыка, игровая музыка, звуковые
## эффекты. SFX-канал называется "sfx" — пока он не используется в
## коде, ползунок будет работать "впрок" (когда добавим звуковые
## эффекты).
################################################################################

screen preferences():

    tag menu

    ## Полупрозрачный фон, чтобы текст и ползунки читались.
    add "bg_main_menu"
    add Solid("#000000cc")

    ## Заголовок.
    text _("НАСТРОЙКИ"):
        xpos 80
        ypos 60
        size 80
        bold True
        color "#ffffff"
        outlines [(3, "#000000", 0, 0)]

    ## Основной блок настроек.
    vbox:
        xpos 80
        ypos 200
        spacing 40

        label _("Громкость"):
            text_size 50
            text_color "#ffffff"
            text_bold True

        hbox:
            spacing 30
            text _("Музыка в меню"):
                size 38
                color "#ffffff"
                xsize 420
            bar value Preference("menu_music volume") xsize 700 ysize 40

        hbox:
            spacing 30
            text _("Музыка в игре"):
                size 38
                color "#ffffff"
                xsize 420
            bar value Preference("music volume") xsize 700 ysize 40

        hbox:
            spacing 30
            text _("Звуковые эффекты"):
                size 38
                color "#ffffff"
                xsize 420
            bar value Preference("sound volume") xsize 700 ysize 40

        null height 25

        label _("Прочее"):
            text_size 50
            text_color "#ffffff"
            text_bold True

        hbox:
            spacing 30
            text _("Скорость текста"):
                size 38
                color "#ffffff"
                xsize 420
            bar value Preference("text speed") xsize 700 ysize 40

        hbox:
            spacing 30
            textbutton _("Окно"):
                text_size 38
                text_color "#ffffff"
                text_hover_color "#CE93D8"
                action Preference("display", "window")
            textbutton _("Полный экран"):
                text_size 38
                text_color "#ffffff"
                text_hover_color "#CE93D8"
                action Preference("display", "fullscreen")

    ## Кнопка возврата в правом нижнем углу.
    textbutton _("НАЗАД"):
        xpos 1920 - 80
        ypos 1080 - 80
        xanchor 1.0
        yanchor 1.0
        text_size 48
        text_color "#ffffff"
        text_hover_color "#CE93D8"
        text_outlines [(3, "#000000", 0, 0)]
        text_bold True
        action Return()
