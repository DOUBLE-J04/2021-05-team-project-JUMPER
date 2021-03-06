import arcade
import json
import Menu
# Constants

screen_w = 1280
screen_h = 720
screen_t = "Platformer"

MOVEMENT_SPEED = 8

GRAVITY = 1
player_jump_speed = 18

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 100
RIGHT_VIEWPORT_MARGIN = 100
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

# Scaling
char_scaling = 0.25

def main():
    # Main method.
    window = arcade.Window(screen_w, screen_h, screen_t)
    start_view = Menu.MainView()
    start_view.setup()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()