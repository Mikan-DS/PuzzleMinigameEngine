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
- `BOARD_PLACE`
(по умолчанию (.5, 0.0))
Этот параметр контролирует положение доски в процентах.
- `RANDOM_INITIAL_PLACE_OFFSET`
(по умолчанию 230)
Этот параметр контролирует начальное случайное положение пазлов на экране.
- `RANDOM_INITIAL_PLACE_BOTH_SIDES`
(по умолчанию True)
Если установлено значение True, пазлы будут размещаться с обеих сторон.
- `RANDOM_INITIAL_PLACE_DOWN_OFFSET`
(по умолчанию 250)
Если значение не равно 0, пазлы будут располагаться по всей ширине с нижней полосы.
- `BOARD_BACKGROUND`
(по умолчанию "#4981C160")
Фон игрового поля паззлов. Это может быть как цветом (строка с # в начале), путем к файлу или `Displayable`
