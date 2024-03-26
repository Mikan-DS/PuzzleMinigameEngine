init -997 python in PuzzleMinigameEngine:

    from store import build, im, Text, Solid

    build.classify('game/plugins/PuzzleMinigameEngine/*.rpy', None)


    def align_pos(pos, element_size, container_size):
        return (0, 0)


    class PuzzleElement(renpy.Displayable):
        def __init__(self, image, part_pos, initial_pos, width, height):
            self.image = im.Crop(image, (x*width, y*height, width, height))
            self.part_pos = part_pos
            self.x, self.y = initial_pos

        def render(self, width, height, st, at):

            render = renpy.Render(width, height)

            return render


    class PuzzleMinigameHandler(renpy.Displayable):
        def __init__(self, image):

            super().__init__()

            self.image = image

            self.full_size = renpy.image_size(self.image)

            
            self.parts = []

            self.segment_width = 100
            self.segment_height = 100

            qty = 1


            for y in range(self.full_size[1]//self.segment_height-1):
                for x in range(self.full_size[0]//self.segment_width-1):
                    qty += 1
                    self.parts.append(
                        im.Crop(self.image, (x*self.segment_width, y*self.segment_height, self.segment_width, self.segment_height))
                    )

        def render(self, width, height, st, at):
            width = self.full_size[0]
            height = self.full_size[1]
            render = renpy.Render(width, height)

            render.blit(
                renpy.render(
                    Solid("550"), width, height, st, at
                ),
                (0, 0)
            )



            renpy.redraw(self, 2)

            return render


            