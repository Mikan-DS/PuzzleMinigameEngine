init python in PuzzleMinigameEngine:
    build.classify('plugins/PuzzleMinigameEngine/demo.rpyc', None)


screen PuzzleMinigameEngineDemo:

    default puzzles = PuzzleMinigameEngine.PuzzleMinigameHandler("plugins/PuzzleMinigameEngine/demo/demo_2b.png")


    # add puzzles.image

    # hbox:
    #     xmaximum 800
    #     spacing 2

    #     box_wrap True
    #     box_wrap_spacing 2

    #     for part in puzzles.parts:
    #         add part

    add puzzles align (0.5, 0.5)


label PuzzleMinigameEngineDemo:

    call screen PuzzleMinigameEngineDemo

    pause

    return