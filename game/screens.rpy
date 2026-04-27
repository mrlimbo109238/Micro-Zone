################################################################################
## Micro Zone — Кастомные экраны интерфейса
################################################################################
## Здесь переопределены только два экрана: главное меню (со спокойным
## фоном леса и музыкой) и настройки (с тремя ползунками громкости).
## Остальное — дефолтное Ren'Py (сохранение, загрузка, история и т.д.).
################################################################################


## Объявление картинки меню — масштабируем под игру 1920x1080.
## Исходник 5120x3413, без масштаба Ren'Py показывал бы только кусок.
image bg_main_menu = Transform("bg_menu_calm.jpg", size=(1920, 1080))


################################################################################
## ГЛАВНОЕ МЕНЮ
################################################################################

screen main_menu():

    tag menu

    ## Спокойный фон без грозы.
    add "bg_main_menu"

    ## Полупрозрачная виньетка слева, чтобы белые буквы кнопок читались.
    add Solid("#000000aa") xpos 0 ypos 0 xsize 720 ysize 1080

    ## Музыка в меню. Канал menu_music регистрируется в options.rpy.
    on "show" action Play("menu_music", "audio/music/menu_start.mp3", fadein=1.5, if_changed=True)
    on "replace" action Play("menu_music", "audio/music/menu_start.mp3", fadein=1.5, if_changed=True)
    on "hide" action Stop("menu_music", fadeout=1.0)

    ## Заголовок.
    text "MICRO ZONE":
        xpos 70
        ypos 70
        size 110
        bold True
        color "#ffffff"
        outlines [(4, "#000000", 0, 0)]

    ## Кнопки.
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

    ## Подпись автора.
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
## НАСТРОЙКИ (с тремя ползунками громкости)
################################################################################

screen preferences():

    tag menu

    ## Фон.
    add "bg_menu_calm.jpg":
        size (1920, 1080)
    add Solid("#000000cc")

    ## Заголовок.
    text _("НАСТРОЙКИ"):
        xpos 80
        ypos 60
        size 90
        bold True
        color "#ffffff"
        outlines [(3, "#000000", 0, 0)]

    ## Блок громкости.
    vbox:
        xpos 80
        ypos 220
        spacing 35

        text _("ГРОМКОСТЬ"):
            size 60
            color "#CE93D8"
            bold True

        hbox:
            spacing 30
            text _("Музыка в меню"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
            bar value Preference("menu_music volume"):
                xsize 900
                ysize 50
                yalign 0.5

        hbox:
            spacing 30
            text _("Музыка в игре"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
            bar value Preference("music volume"):
                xsize 900
                ysize 50
                yalign 0.5

        hbox:
            spacing 30
            text _("Звуковые эффекты"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
            bar value Preference("sound volume"):
                xsize 900
                ysize 50
                yalign 0.5

        null height 30

        ## Скорость текста и режим окна.
        text _("ПРОЧЕЕ"):
            size 60
            color "#CE93D8"
            bold True

        hbox:
            spacing 30
            text _("Скорость текста"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
            bar value Preference("text speed"):
                xsize 900
                ysize 50
                yalign 0.5

    ## Кнопка возврата.
    textbutton _("НАЗАД"):
        xpos 1920 - 80
        ypos 1080 - 80
        xanchor 1.0
        yanchor 1.0
        text_size 56
        text_color "#ffffff"
        text_hover_color "#CE93D8"
        text_outlines [(3, "#000000", 0, 0)]
        text_bold True
        action Return()
