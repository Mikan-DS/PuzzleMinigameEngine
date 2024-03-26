init -997 python in PuzzleMinigameEngine:

    from store import build, im, Text, Solid, Image, config

    build.classify('game/plugins/PuzzleMinigameEngine/*.rpy', None)


    def align_pos(pos, element_size, container_size=None):
        if not container_size:
            container_size = (config.screen_width, config.screen_height)
        return (int((container_size[0]-element_size[0])*pos[0]), int((container_size[1]-element_size[1])*pos[1]))

    def random_pos(element_size, container_size=None):
        if not container_size:
            container_size = (config.screen_width, config.screen_height)
        return renpy.random.randint(0, container_size[0]-element_size[0]), renpy.random.randint(0, container_size[1]-element_size[1])


    class PuzzleElement(renpy.Displayable):
        def __init__(self, image, part_pos, initial_pos, width, height):
            super().__init__()
            self.part_pos = part_pos
            self.x, self.y = initial_pos
            self.width, self.height = width, height
            self.image = im.Crop(image, (part_pos[0]*self.width, part_pos[1]*self.height, self.width, self.height))


        def render(self, width, height, st, at):

            render = renpy.Render(width, height)

            render.blit(
                renpy.render(
                    self.image,
                    width,
                    height,
                    st, at
                ),
                (0, 9)
            )

            return render

        @property
        def pos(self):
            return self.x, self.y

        @property
        def size(self):
            return self.width, self.height

        def in_box(self, x, y):
            return self.x <= x <= self.x+self.width and self.y <= y <= self.y+self.height


    class PuzzleMinigameHandler(renpy.Displayable):
        def __init__(self, image):

            super().__init__()

            self.image = image

            self.full_size = renpy.image_size(self.image)

            
            self.parts = []

            self.segment_width = 100
            self.segment_height = 100

            qty = 1

            self.selected = True
            self.selected_offset = (0, 0)


            for y in range(self.full_size[1]//self.segment_height-1):
                for x in range(self.full_size[0]//self.segment_width-1):
                    qty += 1
                    self.parts.append(
                        PuzzleElement(
                            self.image,
                            (x, y),
                            random_pos((self.segment_width, self.segment_height)),
                            self.segment_width, self.segment_height)
                    )

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            render.blit(
                renpy.render(
                    Solid("550", xysize=self.full_size), width, height, st, at
                ),
                align_pos((.5, .5), self.full_size)
            )

            for part in self.parts:
                render.blit(
                    renpy.render(
                        part,
                        self.segment_width,
                        self.segment_height,
                        st, at
                    ),
                    part.pos
                )

            return render

        def find_hovered_part(self, x, y):
            for part in reversed(self.parts):
                if part.in_box(x, y):
                    return part
            return None


        def set_part_active(self, part):
            self.parts.remove(part)
            self.parts.append(part)
            self.selected = True

        def event(self, ev, x, y, st):

            if renpy.map_event(ev, ["mousedown_1"]):
                part = self.find_hovered_part(x, y)
                if part:
                    self.set_part_active(part)
                    self.selected_offset = x-part.x, y-part.y
                renpy.redraw(self, 0)
            elif renpy.map_event(ev, ["mouseup_1"]):
                self.selected = False
            elif self.selected:
                self.parts[-1].x = x-self.selected_offset[0]
                self.parts[-1].y = y-self.selected_offset[1]
                renpy.redraw(self, 0)
            return


            