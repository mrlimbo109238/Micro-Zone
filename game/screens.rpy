################################################################################
## Micro Zone — Кастомные экраны интерфейса
################################################################################
## Главное меню, диалоговое окно, настройки, вступительные экраны.
################################################################################


## Объявление картинки меню — масштабируем под игру 1920x1080.
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
##
## Плашка прижата к нижнему краю (yalign 1.0) и автоматически растёт
## вверх под длину текста — длинные описания и стихи больше не вылезают
## за экран. ymaximum 600 ограничивает её половиной экрана, чтобы при
## совсем огромных абзацах не закрывала всю картинку.

screen say(who, what):

    style_prefix "say"

    window id "window":
        background Solid("#000000c8")
        yalign 1.0
        xfill True
        xpadding 90
        ypadding 24
        ymaximum 600

        vbox:
            spacing 10

            if who is not None:
                text who id "who":
                    size 48
                    color "#CE93D8"
                    bold True
                    outlines [(3, "#000000", 0, 0)]

            text what id "what":
                size 36
                color "#ffffff"
                outlines [(3, "#000000", 0, 0)]
                xmaximum 1740
                line_leading 4
                line_spacing 6


################################################################################
## QUICK MENU (rollback / skip / save / prefs)
################################################################################

## Quick-menu теперь сидит сверху экрана — раньше он стоял по нижнему
## краю и пересекался с длинными репликами / описаниями. Сверху картинку
## он почти не закрывает, а до плашки диалога никогда не дотягивается.

screen quick_menu():

    zorder 100

    if quick_menu:

        ## Полупрозрачная подложка, чтобы кнопки читались на любых фонах.
        frame:
            xalign 0.5
            yalign 0.0
            background Solid("#000000a0")
            xpadding 26
            ypadding 8

            hbox:
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
## ВСТУПИТЕЛЬНЫЕ ЭКРАНЫ (соо-креатор / дисклеймер / привет от Лимбы)
################################################################################
## Каждый экран — крупный центрированный текст на чёрном фоне.
## Тап в любом месте экрана продвигает к следующему экрану.

screen intro_message(message):

    modal True

    add Solid("#000000")

    text message:
        xalign 0.5
        yalign 0.5
        size 50
        color "#ffffff"
        outlines [(3, "#000000", 0, 0)]
        text_align 0.5
        layout "subtitle"
        xmaximum 1500

    text _("(нажмите, чтобы продолжить)"):
        xalign 0.5
        yalign 0.96
        size 24
        color "#888888"
        italic True

    ## Любой клик / тап / Enter / Space → дальше.
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    key "K_KP_ENTER" action Return()
    key "mouseup_1" action Return()


screen intro_age_question():

    modal True

    add Solid("#000000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        text _("Сколько тебе лет?"):
            xalign 0.5
            size 64
            color "#ffffff"
            outlines [(3, "#000000", 0, 0)]
            bold True

        text _("«Простите, мне это очень нужно, чтобы всё запрещённое стало разрушенным»"):
            xalign 0.5
            size 28
            color "#aaaaaa"
            italic True
            xmaximum 1500
            text_align 0.5
            layout "subtitle"

        null height 60

        textbutton _("Мне 16 или больше"):
            xalign 0.5
            text_size 48
            text_color "#ffffff"
            text_hover_color "#CE93D8"
            text_outlines [(3, "#000000", 0, 0)]
            action Return(False)

        textbutton _("Мне меньше 16"):
            xalign 0.5
            text_size 48
            text_color "#ffffff"
            text_hover_color "#CE93D8"
            text_outlines [(3, "#000000", 0, 0)]
            action Return(True)


################################################################################
## НАСТРОЙКИ
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
        ypos 200
        spacing 24

        text _("ГРОМКОСТЬ"):
            size 56
            color "#CE93D8"
            bold True
            outlines [(2, "#000000", 0, 0)]

        hbox:
            spacing 30
            text _("Музыка в меню"):
                size 38
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("menu_music volume"):
                xsize 900
                ysize 44
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

        hbox:
            spacing 30
            text _("Музыка в игре"):
                size 38
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("music volume"):
                xsize 900
                ysize 44
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

        hbox:
            spacing 30
            text _("Звуковые эффекты"):
                size 38
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("sound volume"):
                xsize 900
                ysize 44
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

        null height 18

        text _("ПРОЧЕЕ"):
            size 56
            color "#CE93D8"
            bold True
            outlines [(2, "#000000", 0, 0)]

        hbox:
            spacing 30
            text _("Скорость текста"):
                size 38
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            bar value Preference("text speed"):
                xsize 900
                ysize 44
                yalign 0.5
                left_bar Solid("#CE93D8")
                right_bar Solid("#444444")
                thumb None

        ## Тумблер вступительных экранов.
        hbox:
            spacing 30
            text _("Показывать вступление"):
                size 38
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            textbutton (_("ВКЛ") if persistent.show_intro else _("ВЫКЛ")):
                yalign 0.5
                text_size 38
                text_color ("#CE93D8" if persistent.show_intro else "#888888")
                text_hover_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                text_bold True
                action ToggleField(persistent, "show_intro")

        ## Тумблер цензуры матов.
        hbox:
            spacing 30
            text _("Цензура матов (для <16)"):
                size 38
                color "#ffffff"
                xsize 480
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            textbutton (_("ВКЛ") if persistent.profanity_censor else _("ВЫКЛ")):
                yalign 0.5
                text_size 38
                text_color ("#CE93D8" if persistent.profanity_censor else "#888888")
                text_hover_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                text_bold True
                action ToggleField(persistent, "profanity_censor")

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
## ОБЩИЕ СТИЛИ ПОЛЗУНКОВ
################################################################################

style bar:
    ysize 44
    left_bar Solid("#CE93D8")
    right_bar Solid("#444444")
    thumb None

style slider:
    ysize 44
    left_bar Solid("#CE93D8")
    right_bar Solid("#444444")
    thumb None

style vbar:
    xsize 44
    top_bar Solid("#CE93D8")
    bottom_bar Solid("#444444")
    thumb None

style vslider:
    xsize 44
    top_bar Solid("#CE93D8")
    bottom_bar Solid("#444444")
    thumb None


################################################################################
## ОТЛОЖЕННЫЙ ЗВУК СЕРДЦА (сцена 1.5)
################################################################################
## Limbo попросил, чтобы сердцебиение в сцене 5 включалось не сразу,
## а через 5 секунд после её начала. В Ren'Py нет встроенной команды
## «отложенный play», поэтому используем экран с timer'ом — он сидит
## на фоне 5 секунд, потом запускает звук и сам прячется.

screen sfx_heartbeat_delayed():

    zorder -100

    timer 5.0:
        action [
            Play("amb_heartbeat", "audio/sfx/heartbeat03.mp3", fadein=1.5),
            Hide("sfx_heartbeat_delayed"),
        ]
