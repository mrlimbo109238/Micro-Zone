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

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            spacing 35
            xfill True

            hbox:
                box_wrap True
                spacing 60

                vbox:
                    style_prefix "radio"
                    label _("Окно")
                    textbutton _("Окно") action Preference("display", "window")
                    textbutton _("Полный экран") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Текст")
                    textbutton _("Пропуск непрочитанного") action Preference("skip", "toggle")
                    textbutton _("Пропускать после выбора") action Preference("after choices", "toggle")

            null height 30

            label _("Громкость") xalign 0.5

            grid 2 4:
                spacing 25
                xfill True

                label _("Музыка в меню")
                bar value Preference("menu_music volume")

                label _("Музыка в игре")
                bar value Preference("music volume")

                label _("Звуковые эффекты")
                bar value Preference("sound volume")

                label _("Скорость текста")
                bar value Preference("text speed")
