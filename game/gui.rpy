################################################################################
## Micro Zone - Настройки GUI (внешний вид интерфейса)
################################################################################
## Limbo: тут размеры шрифтов, цвета, кастомный шрифт, окно диалога.
## Если что-то выглядит криво — пиши, поправлю.
################################################################################

init offset = -2

init python:
    gui.init(1920, 1080)


################################################################################
## КАСТОМНЫЙ ШРИФТ
################################################################################

## Основной шрифт игры — Adventure Indiana. Лежит в game/fonts/adventure.ttf.
define gui.text_font = "fonts/adventure.ttf"
define gui.name_text_font = "fonts/adventure.ttf"
define gui.interface_text_font = "fonts/adventure.ttf"
define gui.button_text_font = "fonts/adventure.ttf"

## Принудительная замена дефолтного DejaVuSans на Adventure на уровне
## Ren'Py-движка. Без этого ряд встроенных стилей упорно лез к
## DejaVuSans, и шрифт в игре не менялся.
init python:
    config.font_replacement_map["DejaVuSans.ttf", False, False] = ("fonts/adventure.ttf", False, False)
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("fonts/adventure.ttf", False, True)
    config.font_replacement_map["DejaVuSans.ttf", True, False] = ("fonts/adventure.ttf", True, False)
    config.font_replacement_map["DejaVuSans.ttf", True, True] = ("fonts/adventure.ttf", True, True)

## Применить шрифт ко всем стилям через style default.
style default:
    font "fonts/adventure.ttf"


################################################################################
## ЦВЕТА
################################################################################

define gui.accent_color = "#CE93D8"
define gui.idle_color = "#cccccc"
define gui.idle_small_color = "#aaaaaa"
define gui.hover_color = "#CE93D8"
define gui.selected_color = "#ffffff"
define gui.insensitive_color = "#55555580"

define gui.muted_color = "#5a3766"
define gui.hover_muted_color = "#7a4f8c"

define gui.text_color = "#ffffff"
define gui.interface_text_color = "#ffffff"


################################################################################
## РАЗМЕРЫ ШРИФТОВ
################################################################################

define gui.text_size = 42
define gui.name_text_size = 56
define gui.interface_text_size = 38
define gui.label_text_size = 48
define gui.notify_text_size = 28
define gui.title_text_size = 90

define gui.button_text_size = 38
define gui.choice_button_text_size = 42


################################################################################
## ОКНО ДИАЛОГА
################################################################################

define gui.textbox_height = 320
define gui.textbox_yalign = 1.0

define gui.name_xpos = 80
define gui.name_ypos = 30
define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 80
define gui.dialogue_ypos = 110
define gui.dialogue_width = 1760
define gui.dialogue_text_xalign = 0.0


################################################################################
## КНОПКИ
################################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0


################################################################################
## КНОПКИ ВЫБОРА (menu choices)
################################################################################

define gui.choice_button_width = 1400
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#CE93D8"
define gui.choice_button_text_insensitive_color = "#666666"


################################################################################
## ПОЛЗУНКИ И ПОЛОСКИ
################################################################################

define gui.bar_size = 38
define gui.scrollbar_size = 14
define gui.slider_size = 38

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)


################################################################################
## РАМКИ
################################################################################

define gui.frame_borders = Borders(4, 4, 4, 4)
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.skip_frame_borders = Borders(16, 5, 50, 5)
define gui.notify_frame_borders = Borders(16, 5, 40, 5)
define gui.frame_tile = False


################################################################################
## ПРОЧЕЕ
################################################################################

define gui.choice_spacing = 22
define gui.navigation_spacing = 4
define gui.pref_spacing = 10
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 10

define gui.navigation_xpos = 40
define gui.skip_ypos = 10
define gui.notify_ypos = 45

define gui.unscrollable = "hide"
