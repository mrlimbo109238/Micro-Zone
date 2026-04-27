################################################################################
## Micro Zone — Кастомные экраны интерфейса
################################################################################
## Главное меню, диалоговое окно, настройки.
################################################################################


## Объявление картинки меню — масштабируем под игру 1920x1080.
## Исходник 5120x3413, без масштаба Ren'Py показывал бы только кусок.
image bg_main_menu = Transform("bg_menu_calm.jpg", size=(1920, 1080))


################################################################################
## ГЛАВНОЕ МЕНЮ
################################################################################

screen main_menu():

    tag menu

    add "bg_main_menu"

    ## Полупрозрачная виньетка слева, чтобы белые буквы кнопок читались.
    add Solid("#000000aa") xpos 0 ypos 0 xsize 720 ysize 1080

    ## Музыка в меню. Канал menu_music регистрируется в options.rpy.
    on "show" action Play("menu_music", "audio/music/menu_start.mp3", fadein=1.5, if_changed=True)
    on "replace" action Play("menu_music", "audio/music/menu_start.mp3", fadein=1.5, if_changed=True)
    on "hide" action Stop("menu_music", fadeout=1.0)

    text "MICRO ZONE":
        xpos 70
        ypos 70
        size 110
        bold True
        color "#ffffff"
        outlines [(4, "#000000", 0, 0)]

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
## ДИАЛОГОВОЕ ОКНО (screen say)
################################################################################
## Переопределяем стандартный say-screen. По умолчанию он использует
## gui/textbox.png (которого у нас нет), поэтому без override текст
## улетал в самый верх экрана без подложки. Мы рисуем своё окно
## с полупрозрачным фоном внизу экрана.

screen say(who, what):

    style_prefix "say"

    window id "window":
        background Solid("#000000c8")
        ysize 360
        yalign 1.0
        xfill True
        xpadding 90
        ypadding 35

        if who is not None:
            text who id "who":
                size 60
                color "#CE93D8"
                bold True
                outlines [(3, "#000000", 0, 0)]
                xpos 0
                ypos 0

        text what id "what":
            size 44
            color "#ffffff"
            outlines [(3, "#000000", 0, 0)]
            xpos 0
            ypos 80
            xmaximum 1740
            line_leading 4
            line_spacing 6

    ## Add the quick menu, like Ren'Py default.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


################################################################################
## QUICK MENU (snap save / skip / prefs)
################################################################################
## Маленькая панелька внизу экрана. Дефолтный quick_menu от Ren'Py
## использует picture-кнопки которых у нас нет, поэтому делаем свою.

screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            xalign 0.5
            yalign 0.98
            spacing 18

            textbutton _("Назад") action Rollback() text_size 26 text_color "#ffffffcc" text_hover_color "#CE93D8"
            textbutton _("История") action ShowMenu("history") text_size 26 text_color "#ffffffcc" text_hover_color "#CE93D8"
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True) text_size 26 text_color "#ffffffcc" text_hover_color "#CE93D8"
            textbutton _("Авто") action Preference("auto-forward", "toggle") text_size 26 text_color "#ffffffcc" text_hover_color "#CE93D8"
            textbutton _("Сохранить") action ShowMenu("save") text_size 26 text_color "#ffffffcc" text_hover_color "#CE93D8"
            textbutton _("Загрузить") action ShowMenu("load") text_size 26 text_color "#ffffffcc" text_hover_color "#CE93D8"
            textbutton _("Настройки") action ShowMenu("preferences") text_size 26 text_color "#ffffffcc" text_hover_color "#CE93D8"


init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True


################################################################################
## НАСТРОЙКИ (с тремя ползунками громкости)
################################################################################

screen preferences():

    tag menu

    add "bg_main_menu"
    add Solid("#000000d0")

    text _("НАСТРОЙКИ"):
        xpos 80
        ypos 60
        size 90
        bold True
        color "#ffffff"
        outlines [(3, "#000000", 0, 0)]

    vbox:
        xpos 80
        ypos 220
        spacing 28

        text _("ГРОМКОСТЬ"):
            size 60
            color "#CE93D8"
            bold True
            outlines [(2, "#000000", 0, 0)]

        hbox:
            spacing 30
            text _("Музыка в меню"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("menu_music volume"):
                xsize 900
                ysize 50
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

        hbox:
            spacing 30
            text _("Музыка в игре"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("music volume"):
                xsize 900
                ysize 50
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

        hbox:
            spacing 30
            text _("Звуковые эффекты"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("sound volume"):
                xsize 900
                ysize 50
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

        null height 30

        text _("ПРОЧЕЕ"):
            size 60
            color "#CE93D8"
            bold True
            outlines [(2, "#000000", 0, 0)]

        hbox:
            spacing 30
            text _("Скорость текста"):
                size 42
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("text speed"):
                xsize 900
                ysize 50
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

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


################################################################################
## ОБЩИЕ СТИЛИ ПОЛЗУНКОВ (на случай, если где-то ещё используются)
################################################################################

style bar:
    ysize 50
    left_bar Solid("#CE93D8")
    right_bar Solid("#444444")
    thumb None

style slider:
    ysize 50
    left_bar Solid("#CE93D8")
    right_bar Solid("#444444")
    thumb None

style vbar:
    xsize 50
    top_bar Solid("#CE93D8")
    bottom_bar Solid("#444444")
    thumb None

style vslider:
    xsize 50
    top_bar Solid("#CE93D8")
    bottom_bar Solid("#444444")
    thumb None
