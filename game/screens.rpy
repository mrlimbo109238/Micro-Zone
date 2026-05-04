################################################################################
## Micro Zone — Кастомные экраны интерфейса
################################################################################
## Главное меню, диалоговое окно, настройки, вступительные экраны.
################################################################################


## Объявление картинки меню — масштабируем под игру 1920x1080.
image bg_main_menu = Transform("bg_menu_calm.jpg", size=(1920, 1080))

## Логотип, который показываем на сплеш-экране при запуске.
image splash_logo = "images/splash_logo.jpg"


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

    ## Соцсети-кнопки (Телеграм + поддержка автору) в правом верхнем углу.
    ## Нажатие открывает экран с подтверждением «вы уверены, что хотите
    ## перейти?» — иначе случайный тап увёл бы игрока в браузер.
    hbox:
        xanchor 1.0
        xpos 1920 - 50
        ypos 70
        spacing 20

        textbutton _("TELEGRAM"):
            text_size 44
            text_color "#5dadff"
            text_hover_color "#ff2f2f"
            text_outlines [(2, "#000000", 0, 0)]
            text_bold True
            activate_sound UICLICK_SOUND
            hover_sound UIHOVER_SOUND
            action Show("confirm_external_link",
                        url="https://t.me/+Ju8irSUWfHtiM2Zi",
                        title=_("Перейти в Telegram-канал автора?"),
                        subtitle=_("Откроется браузер / приложение Telegram"))

        textbutton _("ПОДДЕРЖАТЬ ♥"):
            text_size 44
            text_color "#ff7a7a"
            text_hover_color "#ff2f2f"
            text_outlines [(2, "#000000", 0, 0)]
            text_bold True
            activate_sound UICLICK_SOUND
            hover_sound UIHOVER_SOUND
            action Show("confirm_external_link",
                        url="https://dalink.to/wreezik900",
                        title=_("Поддержать автора?"),
                        subtitle=_("Откроется страница с вариантами доната"))

    vbox:
        xpos 70
        ypos 280
        spacing 35

        ## Все кнопки главного меню: при нажатии шрифт становится
        ## красным (text_selected_color/insensitive — не подходят, поэтому
        ## используем text_hover_color "#ff2f2f", чтобы при тапе на
        ## мобилке видно было красную подсветку, и activate_sound для
        ## приятного клика).

        textbutton _("ИГРАТЬ"):
            text_size 90
            text_color "#ffffff"
            text_hover_color "#ff2f2f"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            activate_sound UICLICK_SOUND
            hover_sound UIHOVER_SOUND
            action Start()

        textbutton _("НАСТРОЙКИ"):
            text_size 64
            text_color "#ffffff"
            text_hover_color "#ff2f2f"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            activate_sound UICLICK_SOUND
            hover_sound UIHOVER_SOUND
            action ShowMenu("preferences")

        textbutton _("ПРОДОЛЖИТЬ"):
            text_size 56
            text_color "#dddddd"
            text_hover_color "#ff2f2f"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            activate_sound UICLICK_SOUND
            hover_sound UIHOVER_SOUND
            action Continue()

        textbutton _("ВЫЙТИ"):
            text_size 56
            text_color "#dddddd"
            text_hover_color "#ff2f2f"
            text_outlines [(3, "#000000", 0, 0)]
            text_bold True
            activate_sound UICLICK_SOUND
            hover_sound UIHOVER_SOUND
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
## ПОДТВЕРЖДЕНИЕ ПЕРЕХОДА ПО ВНЕШНЕЙ ССЫЛКЕ
################################################################################
## Показывается, когда игрок тапает по [TG] или [♥ Поддержать] в меню.
## Спрашиваем «вы уверены», чтобы случайный тап не уводил человека в
## браузер / Telegram. «ДА» — открывает url через OpenURL, «НЕТ» —
## просто прячет окно.

screen confirm_external_link(url, title, subtitle):

    modal True
    zorder 300

    add Solid("#000000d8")

    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#1a1a1aee")
        xpadding 60
        ypadding 50
        xsize 1100

        vbox:
            spacing 22

            text title:
                xalign 0.5
                size 48
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]
                text_align 0.5
                layout "subtitle"

            text subtitle:
                xalign 0.5
                size 30
                color "#bbbbbb"
                italic True
                text_align 0.5
                layout "subtitle"

            null height 14

            text url:
                xalign 0.5
                size 24
                color "#888888"
                text_align 0.5
                layout "subtitle"

            null height 16

            hbox:
                xalign 0.5
                spacing 60

                textbutton _("ДА"):
                    text_size 56
                    text_color "#ffffff"
                    text_hover_color "#ff2f2f"
                    text_outlines [(2, "#000000", 0, 0)]
                    text_bold True
                    activate_sound UICLICK_SOUND
                    action [
                        Hide("confirm_external_link"),
                        OpenURL(url),
                    ]

                textbutton _("НЕТ"):
                    text_size 56
                    text_color "#dddddd"
                    text_hover_color "#ff2f2f"
                    text_outlines [(2, "#000000", 0, 0)]
                    text_bold True
                    activate_sound UICLICK_SOUND
                    action Hide("confirm_external_link")


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
## ПЛАШКА ГОЛОСОВОЙ ОЗВУЧКИ (TTS / Self-Voicing)
################################################################################
## Limbo попросил «плашку с сообщением, которая по голосу активируется».
## Используем встроенную self-voicing-фичу Ren'Py — она через системный
## TTS Android (или espeak на Linux) озвучивает все реплики, описания и
## всю речь от лица персонажей.
##
## Плашка живёт в верхнем левом углу прямо над quick_menu. Когда голос
## выключен — внутри иконка-микрофон с диагональной полосой, фон серый.
## Когда включён — иконка пульсирует красным, сама плашка тоже краснеет.
## Текст внутри обычной (не жирной) толщины, чтобы хорошо читался.

screen voice_panel():

    zorder 90

    if not main_menu:

        ## Включён ли голос — берём из стандартных настроек preferences
        ## (Ren'Py хранит self_voicing=True/False/"clipboard"/"debug").
        $ _voice_on = bool(_preferences.self_voicing)

        frame:
            xalign 0.0
            yalign 0.0
            xoffset 26
            yoffset 84
            background Solid("#0d0d0deb" if not _voice_on else "#1a0606ee")
            xpadding 16
            ypadding 12

            hbox:
                spacing 12

                ## Левая часть — индикатор-«микрофон». При включённом
                ## голосе анимируется красная пульсация (alpha 0.4↔1.0).
                if _voice_on:
                    text "{font=fonts/adventure.ttf}●{/font}":
                        size 32
                        color "#ff2f2f"
                        outlines [(2, "#000000", 0, 0)]
                        yalign 0.5
                        at _voice_pulse
                else:
                    text "{font=fonts/adventure.ttf}○{/font}":
                        size 32
                        color "#666666"
                        outlines [(2, "#000000", 0, 0)]
                        yalign 0.5

                vbox:
                    spacing 0

                    ## Заголовок плашки.
                    text _("ОЗВУЧКА"):
                        size 22
                        color ("#ffffff" if _voice_on else "#aaaaaa")
                        outlines [(1, "#000000", 0, 0)]

                    ## Маленький подзаголовок-подсказка.
                    text (_("Голос диктора активен") if _voice_on
                          else _("Тап — включить чтение вслух")):
                        size 16
                        color ("#ff7a7a" if _voice_on else "#666666")
                        italic True

                ## Тумблер ВКЛ / ВЫКЛ.
                textbutton (_("ВКЛ") if _voice_on else _("ВЫКЛ")):
                    yalign 0.5
                    text_size 22
                    text_color ("#ff2f2f" if _voice_on else "#888888")
                    text_hover_color "#ffffff"
                    text_outlines [(1, "#000000", 0, 0)]
                    text_bold True
                    activate_sound UICLICK_SOUND
                    action Preference("self voicing", "toggle")


## Анимация пульсации индикатора при активной озвучке. Меняем alpha
## плавно вверх-вниз, чтобы получить эффект «говорит».
transform _voice_pulse:
    alpha 0.4
    block:
        ease 0.6 alpha 1.0
        ease 0.6 alpha 0.4
        repeat


init python:
    config.overlay_screens.append("voice_panel")


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


################################################################################
## ОТЛОЖЕННЫЙ ЗВУК ФОНАРЯ (сцена 2.6)
################################################################################
## В сцене 6 главы 2 (разговор с Валентином на улице) уличный фонарь
## должен включиться не сразу, а через 5 секунд после начала сцены.
## Та же логика, что и у сердца, только звук другой.

screen sfx_streetlamp_delayed():

    zorder -100

    timer 5.0:
        action [
            Play("amb_streetlamp", "audio/music/street_lamp.mp3", fadein=1.5),
            Hide("sfx_streetlamp_delayed"),
        ]


################################################################################
## ОГРАНИЧИТЕЛЬ СЕРДЦЕБИЕНИЯ — 8 СЕКУНД (сцены 2.4 и 2.6)
################################################################################
## Limbo попросил, чтобы heartbeat03 в сценах 2.4 и 2.6 играл максимум
## 8 секунд, а потом плавно затихал. В скрипте мы делаем `play
## amb_heartbeat ... fadein 1.0`, а параллельно показываем этот экран —
## он через 8 секунд от своего показа гасит звук на канале и сам прячется.

screen sfx_heartbeat_8s_stopper():

    zorder -100

    timer 8.0:
        action [
            Stop("amb_heartbeat", fadeout=1.5),
            Hide("sfx_heartbeat_8s_stopper"),
        ]


################################################################################
## ОГРАНИЧИТЕЛЬ СЕРДЦЕБИЕНИЯ — 20 СЕКУНД (сцена 3.13)
################################################################################
## В сцене 3.13 («Тихон мёртв») сердцебиение должно длиться ровно
## 20 секунд, потом плавно затихать. Тот же приём, что и у 8-секундного
## ограничителя.

screen sfx_heartbeat_20s_stopper():

    zorder -100

    timer 20.0:
        action [
            Stop("amb_heartbeat", fadeout=1.5),
            Hide("sfx_heartbeat_20s_stopper"),
        ]


################################################################################
## ЭФФЕКТ МЕРЦАНИЯ ЭКРАНА (сцены 3.2, 3.3 — приступы Ани)
################################################################################
## Limbo попросил добавить мерцание при приступах. Полупрозрачный белый
## слой пульсирует с разной интенсивностью — выглядит как короткие
## вспышки/глитч сознания. Применяется к сцене целиком (zorder 200,
## поверх всех картинок). Включается через `show screen seizure_flicker`,
## выключается через `hide screen seizure_flicker`.

transform _seizure_flicker_anim:
    alpha 0.0
    block:
        ease 0.04 alpha 0.35
        ease 0.04 alpha 0.0
        pause 0.18
        ease 0.04 alpha 0.55
        ease 0.04 alpha 0.0
        pause 0.42
        ease 0.04 alpha 0.25
        ease 0.04 alpha 0.0
        pause 0.6
        repeat


screen seizure_flicker():

    zorder 200

    add Solid("#ffffff") size (config.screen_width, config.screen_height) at _seizure_flicker_anim


################################################################################
## ЗВУК НАЖАТИЯ КНОПКИ В МЕНЮ
################################################################################
## Один общий play-action, который вешается на activate_sound у кнопок
## главного меню. Файл лежит в audio/sfx/ui_click.mp3 — короткий
## приятный «тап». Канал sfx_uiclick зарегистрирован в options.rpy.

define UICLICK_SOUND = "audio/sfx/ui_click.mp3"
define UIHOVER_SOUND = "audio/sfx/ui_click.mp3"
