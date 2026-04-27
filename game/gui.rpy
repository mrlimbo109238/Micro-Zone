################################################################################
## Micro Zone - Настройки GUI (внешний вид интерфейса)
################################################################################
## Минимальный набор настроек. Полный gui.rpy с темами и кастомизацией
## создаётся Ren'Py автоматически при первом запуске launcher'а.
## Если захочешь кастомный стиль — замени этот файл на сгенерированный
## из Ren'Py SDK (через кнопку "Change/Update GUI" в launcher'е).
################################################################################

## Инициализация GUI. Без этого вызова Ren'Py не подключает современную
## систему экранов (screen main_menu, screen preferences и т.д.) и
## откатывается на старое compat-меню — из-за этого наше кастомное
## меню с грозой раньше не показывалось.
init offset = -2
init python:
    gui.init(1920, 1080)

## Размер шрифтов.
define gui.text_size = 38
define gui.name_text_size = 50
define gui.interface_text_size = 40
define gui.label_text_size = 46
define gui.notify_text_size = 32
define gui.button_text_size = 38
define gui.choice_button_text_size = 40

## Основной шрифт. Стандартный DejaVuSans поддерживает кириллицу.
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

## Цвета текста.
define gui.text_color = '#ffffff'
define gui.idle_color = '#aaaaaa'
define gui.hover_color = '#4FC3F7'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#555555'

## Основные цвета интерфейса (кнопок, рамок).
define gui.accent_color = '#4FC3F7'
define gui.selected_color = '#ffffff'

## Размер окна диалога (доля экрана).
define gui.textbox_height = 278
