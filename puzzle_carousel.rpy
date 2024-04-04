init -996 python in PuzzleMinigameEngine:
    class PuzzleCarousel(renpy.Displayable):
        def __init__(self, puzzles_count, puzzle_size):
            super().__init__()
            self.puzzles_count = puzzles_count
            self.puzzles_offset = puzzles_count
            self.carousel_offset = 0
            self.puzzle_size = puzzle_size
        
        def render(self, width, height, st, at):
            render = renpy.Render(width, self.puzzle_size)


            render.blit(
                renpy.render(
                    Solid(CAROUSEL_MAIN_COLOR, ysize=CAROUSEL_SCROLLER_HEIGHT), width, height, st, at
                ),
                (0, height-CAROUSEL_HEIGHT-CAROUSEL_SPACE-CAROUSEL_SCROLLER_HEIGHT)
            )

            scroller_width = (self.puzzles_offset*self.puzzle_size)//width
            scroller_pos = 0#int(width*(1 - self.puzzles_offset/self.puzzles_count))

            render.blit(
                renpy.render(
                    Solid(CAROUSEL_SCROLLER_THUMB_COLOR, ysize=CAROUSEL_SCROLLER_HEIGHT, xsize=scroller_width), width, height, st, at
                ),
                (scroller_pos, height-CAROUSEL_HEIGHT-CAROUSEL_SPACE-CAROUSEL_SCROLLER_HEIGHT)
            )

            render.blit(
                renpy.render(
                    Solid(CAROUSEL_MAIN_COLOR, ysize=CAROUSEL_HEIGHT), width, height, st, at
                ),
                (0, height-CAROUSEL_HEIGHT)
            )
            return render