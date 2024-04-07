init -996 python in PuzzleMinigameEngine:
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
            self.mask_shadow = Transform(PUZZLE_MASK_SHADOW, zoom=mask_ratio)
            self.shadow = Transform(PUZZLE_SHADOW, zoom=mask_ratio)

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

            self.original_image = Crop((self.part_pos[0]*self.width, self.part_pos[1]*self.height, self.width, self.height), image)
            self.image = AlphaMask(
                self.original_image,
                Composite((self.width, self.height), *inner_mask),
                invert=True
            )

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            if self.masks[0]:
                render.blit(
                    renpy.render(
                        self.outer_mask[0],
                        width,
                        height,
                        st, at
                    ),
                    (-self.mask_height, 0)
                )
                render.blit(
                    renpy.render(
                        Transform(self.mask_shadow, rotate=-90, rotate_pad=False),
                        width,
                        height,
                        st, at
                    ),
                    (-self.mask_height, 0)
                )
     
            if self.masks[1]:
                render.blit(
                    renpy.render(
                        self.outer_mask[1],
                        width,
                        height,
                        st, at
                    ),
                    (0, -self.mask_height)
                )
                render.blit(
                    renpy.render(
                        self.mask_shadow,
                        width,
                        height,
                        st, at
                    ),
                    (0, -self.mask_height)
                )
            if self.masks[2]:
                render.blit(
                    renpy.render(
                        self.outer_mask[2],
                        width,
                        height,
                        st, at
                    ),
                    (self.width, 0)
                )
                render.blit(
                    renpy.render(
                        Transform(self.mask_shadow, rotate=90, rotate_pad=False),
                        width,
                        height,
                        st, at
                    ),
                    (self.width, 0)
                )
            if self.masks[3]:
                render.blit(
                    renpy.render(
                        self.outer_mask[3],
                        width,
                        height,
                        st, at
                    ),
                    (0, self.height)
                )
                render.blit(
                    renpy.render(
                        Transform(self.mask_shadow, rotate=180, rotate_pad=False),
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

            render.blit(
                renpy.render(
                    self.shadow,
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
