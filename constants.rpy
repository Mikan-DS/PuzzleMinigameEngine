init -999 python in PuzzleMinigameEngine:

    from store import Solid, Image

    PUZZLE_RIGHT_POS_OFFSET = 15
    PUZZLE_MASK_IMAGE = "plugins/PuzzleMinigameEngine/images/puzzle_mask.png"
    FREEZE_AFTER_CORRECT_PLACE = True
    PUZZLE_MASK_SHADOW = "plugins/PuzzleMinigameEngine/images/outer_mask_shadow.png"
    PUZZLE_SHADOW = "plugins/PuzzleMinigameEngine/images/puzzle_shadow.png"

    BOARD_PLACE = (.5, 0.0)
    RANDOM_INITIAL_PLACE_OFFSET = 230
    RANDOM_INITIAL_PLACE_BOTH_SIDES = True
    RANDOM_INITIAL_PLACE_DOWN_OFFSET = 250

    BOARD_BACKGROUND = "#4981C160"


init -997 python in PuzzleMinigameEngine:
    PUZZLE_MASK_SIZE = renpy.image_size(PUZZLE_MASK_IMAGE)
    BOARD_BACKGROUND = Solid(BOARD_BACKGROUND) if isinstance(BOARD_BACKGROUND, str) and BOARD_BACKGROUND.startswith("#") else BOARD_BACKGROUND
    BOARD_BACKGROUND = Image(BOARD_BACKGROUND) if isinstance(BOARD_BACKGROUND, str) else BOARD_BACKGROUND

