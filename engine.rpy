init -997 python in PuzzleMinigameEngine:

    from store import build, im, Text, Solid, Image, config, Transform, Composite, Crop, AlphaMask
    from math import sqrt

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
        def __init__(self, image, part_pos, initial_pos, width, height, masks):
            super().__init__()
            self.part_pos = part_pos
            self.x, self.y = initial_pos
            self.width, self.height = width, height
            self.masks = list(masks)
            mask_ratio = self.width/PUZZLE_MASK_SIZE[0]
            self.mask_height = int(PUZZLE_MASK_SIZE[1]*mask_ratio)
            self.mask = Transform(PUZZLE_MASK_IMAGE, zoom=mask_ratio)

            inner_mask = []
            self.outer_mask = [None, None, None, None]

            if self.masks[0] == -1:
                inner_mask.extend(
                    ((0, 0), Transform(self.mask, rotate=90, rotate_pad=False))
                )
                self.masks[0] = False


            if self.masks[1] == -1:
                inner_mask.extend(
                    ((0, 0), Transform(self.mask, rotate=180, rotate_pad=False))
                )
                self.masks[1] = False


            if self.masks[2] == -1:
                inner_mask.extend(
                    ((self.width-self.mask_height, 0), Transform(self.mask, rotate=-90, rotate_pad=False))
                )
                self.masks[2] = False


            if self.masks[3] == -1:
                inner_mask.extend(
                    ((0, self.height-self.mask_height), self.mask)
                )
                self.masks[3] = False


            self.image = AlphaMask(
                Crop((self.part_pos[0]*self.width, self.part_pos[1]*self.height, self.width, self.height), image),
                Composite((self.width, self.height), *inner_mask),
                invert=True
            )

        def set_outer_mask(self, masks):
            pass

        def render(self, width, height, st, at):

            render = renpy.Render(width, height)

            if self.masks[0]:
                render.blit(
                    renpy.render(
                        Transform(self.mask, rotate=-90, rotate_pad=False),
                        width,
                        height,
                        st, at
                    ),
                    (-self.mask_height, 0)
                )   
     

            if self.masks[1]:
                render.blit(
                    renpy.render(
                        self.mask,
                        width,
                        height,
                        st, at
                    ),
                    (0, -self.mask_height)
                ) 

            if self.masks[2]:
                render.blit(
                    renpy.render(
                        Transform(self.mask, rotate=90, rotate_pad=False),
                        width,
                        height,
                        st, at
                    ),
                    (self.width, 0)

                )   

            if self.masks[3]:
                render.blit(
                    renpy.render(
                        Transform(self.mask, rotate=180, rotate_pad=False),
                        width,
                        height,
                        st, at
                    ),
                    (0, self.height)
                )    

            render.blit(
                renpy.render(
                    self.image,
                    width,
                    height,
                    st, at
                ),
                (0, 0)
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

        @property
        def right_x(self):
            return self.part_pos[0]*self.width

        @property
        def right_y(self):
            return self.part_pos[1]*self.height

        def is_right_placed(self, pos):
            x, y = pos
            return abs(self.x-x-self.right_x) < PUZZLE_RIGHT_POS_OFFSET and abs(self.y-y-self.right_y) < PUZZLE_RIGHT_POS_OFFSET

        def place_right(self, pos):
            x, y = pos
            self.x = self.right_x+x
            self.y = self.right_y+y


    class PuzzleMinigameHandler(renpy.Displayable):
        def __init__(self, image):

            super().__init__()

            self.image = image

            self.full_size = list(renpy.image_size(self.image))

            
            self.parts = []

            parts_count = 50
            r = self.full_size[0]/self.full_size[1]


            self.segment_size = int(self.full_size[1]/sqrt(parts_count/r))

            self.segment_width = self.segment_size
            self.segment_height = self.segment_size

            self.full_size[0] -= int(self.full_size[0]%self.segment_width)
            self.full_size[1] -= int(self.full_size[1]%self.segment_height)


            qty = 1

            self.selected = False
            self.selected_offset = (0, 0)
            self.is_finished = False

            y_max = (self.full_size[1]//self.segment_height)-1
            x_max = (self.full_size[0]//self.segment_width)-1

            last_y_mask = [0]*(y_max+1)
            last_x_mask = 0
            old_parts = []

            for y in range(y_max+1):
                new_y_mask = [renpy.random.choice((-1, 1)) for _ in range(x_max+1)]
                new_parts = []
                for x in range(x_max+1):
                    qty += 1
                    new_x_mask = renpy.random.choice((-1, 1))
                    part = PuzzleElement(
                            self.image,
                            (x, y),
                            random_pos((self.segment_width, self.segment_height), (400, config.screen_height)),
                            self.segment_width, self.segment_height,
                            (-last_x_mask, -last_y_mask[x], (0 if x==x_max else new_x_mask), (0 if y==y_max else new_y_mask[x]))
                            )
                    self.parts.append(
                        part
                    )
                    new_parts.append(part)
                    last_x_mask = new_x_mask
                old_parts = new_parts
                last_y_mask = new_y_mask

                last_x_mask = 0

            renpy.random.shuffle(self.parts)
            CitrusPluginSupport.log("Create puzzle with %d elements (%dx%d)"%(qty, x_max, y_max), plugin_config["name"])


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


        @property
        def selected_part(self):
            if self.selected:
                return self.parts[-1]
            return None

        def event(self, ev, x, y, st):

            if renpy.map_event(ev, ["mousedown_1"]):
                part = self.find_hovered_part(x, y)
                if part:# and not part.is_right_placed(align_pos((.5, .5), self.full_size))
                    self.set_part_active(part)
                    self.selected_offset = x-part.x, y-part.y
                renpy.redraw(self, 0)
            elif renpy.map_event(ev, ["mouseup_1"]):
                board_offset = align_pos((.5, .5), self.full_size)

                if self.selected:
                    if self.selected_part.is_right_placed(board_offset):
                        self.selected_part.place_right(board_offset)
                    self.try_finish()
                
                self.selected = False
                renpy.redraw(self, 0)
            elif self.selected:
                self.selected_part.x = x-self.selected_offset[0]
                self.selected_part.y = y-self.selected_offset[1]
                renpy.redraw(self, 0)
            return

        def try_finish(self):
            board_offset = align_pos((.5, .5), self.full_size)
            for part in self.parts:
                if not part.is_right_placed(board_offset):
                    self.is_finished = False
                    renpy.restart_interaction()

                    return False
            for part in self.parts:
                part.place_right(board_offset)
            self.is_finished = True
            renpy.restart_interaction()
            return True

        def finish_all(self):
            board_offset = align_pos((.5, .5), self.full_size)
            for part in self.parts:
                part.place_right(board_offset) 


            