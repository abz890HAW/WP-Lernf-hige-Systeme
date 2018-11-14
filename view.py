#!/usr/bin/env python3.7

from tkinter import Tk, Canvas, font, CENTER
from game_core import Game

WIDTH = 400
HEIGHT = 400
PADDING = 10
CORNER_RADIUS = 10
FONT_SIZE = HEIGHT//4//4
# dinstance from center of rectangle to border
dx = (WIDTH/8-PADDING/2)
dy = (HEIGHT/8-PADDING/2)

COLOR_CODES = {
    "bg" : "#bbada0",
    None : "#cdc1b4",
    2    : "#eee4da",
    4    : "#ede0c8",
    8    : "#f2b179",
    16   : "#f59563",
    32   : "#f67c5f",
    64   : "#f65e3b",
    128  : "#edcf72",
    256  : "#edcc61",
    512  : "#edc850",
    1024 : "#edc53f",
    2048 : "#edc22e",
    -1   : "#3c3a32"
}

# Add rounded corner function to Canvas Class
Canvas.round_rectangle = lambda self, x1, y1, x2, y2, radius=25, **kwargs:\
    self.create_polygon((x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1), **kwargs, smooth=True)

def draw_grid(canvas, grid, font):
    for x in range(4):
        for y in range(4):
            # center position of rectangle
            pos = {'x': (x+0.5)*WIDTH/4, 'y': (y+0.5)*WIDTH/4}
            color = COLOR_CODES[grid[y][x]] if grid[y][x] in COLOR_CODES else COLOR_CODES[-1]
            canvas.round_rectangle(
                pos['x']-dx,
                pos['y']-dy,
                pos['x']+dx,
                pos['y']+dy,
                CORNER_RADIUS,
                fill=color)
            string = str(grid[y][x]) if grid[y][x] != None else ""
            canvas.create_text((pos['x'], pos['y']), text=string, justify=CENTER, font=font)
    canvas.pack()

def action(function, game, canvas, font):
    function()
    draw_grid(canvas, game.get_state(), font)


def main():
    # assignments
    game = Game()
    window = Tk()
    canvas = Canvas(window, width=400, height=400, bg=COLOR_CODES["bg"])
    FantasqueSansMono = font.Font(family="Fantasque Sans Mono", size=FONT_SIZE, weight='bold')
    KEY_BINDINGS = {
        "<w>"     : game.up,
        "<Up>"    : game.up,
        "<s>"     : game.down,
        "<Down>"  : game.down,
        "<a>"     : game.left,
        "<Left>"  : game.left,
        "<d>"     : game.right,
        "<Right>" : game.right
    }

    # initial rendering
    window.geometry("400x400")
    window.title("2048")
    draw_grid(canvas, game.get_state(), FantasqueSansMono)
    # key assignments
    for key, value in KEY_BINDINGS.items():
        window.bind(key, lambda e, value=value: action(value, game, canvas, FantasqueSansMono))

    window.mainloop()

if __name__ == "__main__":
    main()
