
init python in PuzzleMinigameEngine:
    build.classify('plugins/PuzzleMinigameEngine/demo/*', None)

screen PuzzleMinigameEngineDemo:

    tag menu

    default puzzles = PuzzleMinigameEngine.PuzzleMinigame("plugins/PuzzleMinigameEngine/demo/demo_nier.png")

    add puzzles

    if puzzles.is_finished:
        textbutton "Готово":
            if main_menu:
                action ShowMenu("main_menu")
            else:
                action Return()
    else:
        textbutton "Собрать пазл (для тестов)":
            action [Function(puzzles.finish_all), Function(renpy.restart_interaction)]


label PuzzleMinigameEngineDemo:

    call screen PuzzleMinigameEngineDemo

    pause

    return