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
        return [renpy.random.randint(0, container_size[0]-element_size[0]), renpy.random.randint(0, container_size[1]-element_size[1])]




            