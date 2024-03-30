# PuzzleMinigameEngine

## Plugin for Ren'Py

This is a plugin for Renpy, it needs to be cloned/added as a submodule to the plugins folder in the game directory of your Ren'Py project.

---

## Плагин для Ren'Py

Это плагин для renpy, его необходимо склонировать/добавить как субмодуль в папку plugins в директорию game вашего проекта Ren'Py

---

Описание пока в разработке/Description in progress

## Документация

### Доступные параметры для настройки

- `PUZZLE_RIGHT_POS_OFFSET`
(По умолчанию 15)
Контроллирует дальность позиции паззла от правильной точки, когда оно может примагнититься на эту точку.
- `PUZZLE_MASK_IMAGE`
(по умолчанию путь "plugins/PuzzleMinigameEngine/images/puzzle_mask.png")
Это путь до картинки которая является маской для "отступов" паззлов.
- `FREEZE_AFTER_CORRECT_PLACE`
(По умолчанию True)
Этот флаг отвечает за возможность передвигать паззлы после того как они встали на правильное место
- `PUZZLE_MASK_SHADOW`
(по умолчанию путь "plugins/PuzzleMinigameEngine/images/outer_mask_shadow.png")
Это путь до картинки которая является тенью (или блеском) для "отступов" паззлов.
- `PUZZLE_SHADOW`
(по умолчанию путь "plugins/PuzzleMinigameEngine/images/puzzle_shadow.png")
Это путь до картинки которая является  тенью (или блеском) паззлов.