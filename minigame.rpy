init -995 python in PuzzleMinigameEngine:
    class PuzzleMinigame(renpy.Displayable):
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
                    if x:
                        if part.masks[0]:
                            part.outer_mask[0] = AlphaMask(
                                Crop((
                                        new_parts[x-1].width-new_parts[x-1].mask_height,
                                        0,
                                        new_parts[x-1].mask_height,
                                        new_parts[x-1].height),
                                    new_parts[x-1].original_image),
                                Transform(part.mask, rotate=-90, rotate_pad=False)
                                )
                        if new_parts[x-1].masks[2]:
                            print(x-1, y)
                            new_parts[x-1].outer_mask[2] = AlphaMask(
                                part.original_image,
                                Transform(new_parts[x-1].mask, rotate=90, rotate_pad=False)
                                )
                    if y:
                        if part.masks[1]:
                            part.outer_mask[1] = AlphaMask(
                                Crop((
                                        0,
                                        old_parts[x].height-old_parts[x].mask_height,
                                        old_parts[x].width,
                                        old_parts[x].mask_height),
                                    old_parts[x].original_image),
                                part.mask
                                )
                        if old_parts[x].masks[3]:
                            old_parts[x].outer_mask[3] = AlphaMask(
                                part.original_image,
                                Transform(old_parts[x].mask, rotate=180, rotate_pad=False)
                                )
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
                if part:
                    if FREEZE_AFTER_CORRECT_PLACE or not part.is_right_placed(align_pos((.5, .5), self.full_size)):
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
