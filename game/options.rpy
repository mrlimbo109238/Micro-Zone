################################################################################
## Micro Zone - Настройки игры (Options)
################################################################################
## Это главный файл настроек. Здесь задаётся имя игры, разрешение,
## правила сборки и язык.
##
## Документация: https://www.renpy.org/doc/html/config.html
################################################################################

define config.name = _("Micro Zone")

define config.version = "0.1.0"

## Короткое описание игры (для магазинов приложений).
define gui.about = _("Визуальная новелла Micro Zone. Автор: Limbo.")

## Язык интерфейса (русский).
define config.language = "russian"

################################################################################
## Разрешение и окно
################################################################################

## Разрешение экрана. Фоны лучше рисовать в этом же размере (или кратном).
## Сейчас установлено 1920x1080 (Full HD, 16:9). Если твои сцены другого
## размера — поменяй эти две цифры, Ren'Py автоматически отмасштабирует.
define config.screen_width = 1920
define config.screen_height = 1080

################################################################################
## Звук
################################################################################

## Каналы для разных типов звука. Можно настраивать громкость в меню игры.
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Громкость по умолчанию (0.0 - тишина, 1.0 - максимум).
define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.8
define config.default_voice_volume = 1.0

## Отдельный канал для музыки в главном меню. Это позволяет иметь
## независимый ползунок "громкость музыки в меню" в настройках,
## независимо от громкости музыки внутри игры.
##
## Также регистрируем отдельные каналы для звуковых эффектов, чтобы
## несколько ambient-звуков (двигатель + печка + ветер + ...) могли
## звучать одновременно. По умолчанию у Ren'Py всего один `sound`
## канал, и новый звук просто перебивал предыдущий. Все эти каналы
## висят на миксере `sfx`, поэтому ползунок «Звуковые эффекты» в
## настройках управляет всеми ими сразу.
init python:
    renpy.music.register_channel("menu_music", mixer="menu_music", loop=True)

    # Зацикленные ambient-каналы (двигатель, печка, ветер, скрип пола,
    # сердце, уличный фонарь). Все на миксере sfx.
    renpy.music.register_channel("amb_engine",    mixer="sfx", loop=True)
    renpy.music.register_channel("amb_stove",     mixer="sfx", loop=True)
    renpy.music.register_channel("amb_wind",      mixer="sfx", loop=True)
    renpy.music.register_channel("amb_floor",     mixer="sfx", loop=True)
    renpy.music.register_channel("amb_heartbeat", mixer="sfx", loop=True)
    renpy.music.register_channel("amb_streetlamp", mixer="sfx", loop=True)

    # Однократные SFX. loop=False — звук играет один раз и сам
    # останавливается, когда файл кончится.
    renpy.music.register_channel("sfx_navigator", mixer="sfx", loop=False)
    renpy.music.register_channel("sfx_door",      mixer="sfx", loop=False)
    renpy.music.register_channel("sfx_noise",     mixer="sfx", loop=False)
    renpy.music.register_channel("sfx_scream",    mixer="sfx", loop=False)
    renpy.music.register_channel("sfx_surprise",  mixer="sfx", loop=False)
    renpy.music.register_channel("sfx_whisper",   mixer="sfx", loop=False)

################################################################################
## Автосохранение и переходы
################################################################################

define config.has_autosave = True

## Стандартные переходы между сценами.
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve

################################################################################
## Правила сборки (для APK / PC)
################################################################################

init python:
    build.name = "MicroZone"

    ## Классификация файлов по платформам.
    build.classify('game/audio/**.mp3', 'all')
    build.classify('game/audio/**.ogg', 'all')
    build.classify('game/audio/**.wav', 'all')
    build.classify('game/images/**.png', 'all')
    build.classify('game/images/**.jpg', 'all')
    build.classify('game/images/**.webp', 'all')
    build.classify('game/fonts/**.ttf', 'all')
    build.classify('game/fonts/**.otf', 'all')

    ## Не включать исходники в архив (только скомпилированный код).
    build.include_old_themes = False
