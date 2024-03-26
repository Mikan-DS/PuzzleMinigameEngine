init python in PuzzleMinigameEngine:
    build.classify('plugins/PuzzleMinigameEngine/demo.rpyc', None)


screen PuzzleMinigameEngineDemo:

    default puzzles = PuzzleMinigameEngine.PuzzleMinigameHandler("plugins/PuzzleMinigameEngine/demo/demo_2b.png")

    add puzzles


label PuzzleMinigameEngineDemo:

    call screen PuzzleMinigameEngineDemo

    pause

    return