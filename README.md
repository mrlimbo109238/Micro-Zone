# Micro Zone

Визуальная новелла от **Limbo**. Разработка на движке [Ren'Py](https://www.renpy.org/).

---

## Как это работает

Ты пишешь код и добавляешь сцены / звуки на телефоне (через Acode или любой редактор), пушишь в GitHub — и **GitHub Actions сам собирает APK** в облаке. Локальный ПК не нужен.

```
Телефон (редактируешь .rpy + закидываешь картинки)
          │  git push
          ▼
       GitHub
          │  (автоматически)
          ▼
 GitHub Actions  →  собирает APK
          │
          ▼
   Скачиваешь APK  →  устанавливаешь на телефон
```

---

## Что установить на телефон

| Приложение | Зачем | Где взять |
|---|---|---|
| **Acode** | Редактор кода с подсветкой | [Play Store](https://play.google.com/store/apps/details?id=com.foxdebug.acode) |
| **Termux** | Терминал Linux (для git) | [F-Droid](https://f-droid.org/packages/com.termux/) (версия из Play Market устарела) |
| **GitHub app** (опционально) | Смотреть статус сборок, скачивать APK | Play Store |

### Первая настройка Termux
```bash
pkg update && pkg upgrade
pkg install git openssh
git config --global user.name "Limbo"
git config --global user.email "твой-email@example.com"
```

Дальше клонируешь свой репозиторий:
```bash
cd ~
git clone https://github.com/ТВОЙ_USERNAME/Micro-Zone.git
cd Micro-Zone
```

---

## Структура проекта

```
Micro-Zone/
├── game/
│   ├── script.rpy          ← ГЛАВНЫЙ ФАЙЛ: диалоги, сцены, выборы
│   ├── characters.rpy      ← описания персонажей
│   ├── options.rpy         ← настройки (имя игры, разрешение, язык)
│   ├── gui.rpy             ← цвета и шрифты интерфейса
│   ├── images/             ← сюда кидаешь все PNG/JPG сцены
│   │   ├── bg_room.png
│   │   ├── bg_street.png
│   │   └── ...
│   └── audio/
│       ├── music/          ← фоновая музыка (mp3/ogg)
│       │   └── main_theme.mp3
│       └── sfx/            ← короткие звуки (mp3/ogg/wav)
│           └── door_open.mp3
├── .android.json           ← настройки Android-сборки (package name, версия)
├── .github/workflows/
│   └── build-android.yml   ← автосборка APK
└── README.md
```

---

## Правила именования файлов

**ВАЖНО:** чтобы код работал везде (телефон, эмулятор, сборка):
- Только **латиница**: `scene_01.png`, не `сцена1.png`
- **Без пробелов**: используй `_` — `main_menu_bg.png`
- **Маленькие буквы**: `limbo.png`, не `Limbo.png`
- Фоны (сцены): префикс `bg_` → `bg_school.png`, `bg_forest.png`
- Спрайты: `имя_эмоция.png` → `limbo_happy.png`, `limbo_sad.png`
- Музыка/звук: `.mp3` или `.ogg` (ogg лучше, меньше весит)

---

## Как писать диалоги

Открой `game/script.rpy` — там уже есть шаблон. Основные команды:

```renpy
label start:

    scene bg_room              # показать фон game/images/bg_room.png
    with fade                  # плавный переход

    play music "main_theme.mp3"  # включить музыку

    limbo "Привет, я Limbo!"     # реплика персонажа
    "Просто текст от автора."     # реплика рассказчика

    play sound "door_open.mp3"   # короткий звук

    # Выбор игрока:
    menu:
        "Пойти налево":
            jump left_path
        "Пойти направо":
            jump right_path
```

Полная документация (на английском): <https://www.renpy.org/doc/html/quickstart.html>
Перевод на русский: <https://ru.renpy.org/wiki/renpy/doc/tutorials/Быстрый_старт>

---

## Как собрать APK

### Автоматически (после каждого push)
1. Закинь изменения: `git add . && git commit -m "my changes" && git push`
2. Зайди в GitHub → вкладка **Actions** → дождись зелёной галочки (5–10 мин)
3. Кликни на успешный прогон → внизу скачай **micro-zone-android-apk.zip**
4. Распакуй — там будет `.apk` файл → установи на телефон (разреши "Установка из неизвестных источников")

### Вручную (запустить сборку без push)
GitHub → Actions → "Build Android APK" → **Run workflow** → Run

---

## Версия движка

Используется **Ren'Py 8.3.7** (стабильная, от марта 2025). Если нужно обновить — поменяй переменную `RENPY_VERSION` в `.github/workflows/build-android.yml`.

---

## Автор

**Limbo** (mrlimbo109238)

Сюжет, сцены, музыка — всё от автора. Код на Ren'Py — собирается пошагово вместе с Devin.
