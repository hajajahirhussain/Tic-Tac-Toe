import pygame
import time
import os


def update_text(screen, font_type, font_name, text, size, color, antialias, pos, bold):
    """
    Renders and displays text on the screen.

    Args:
        screen (pygame.Surface): The display surface to draw the text on.
        font_type (str): The type of font to use ('sys' for system font, 'custom' for a specific font).
        font_name (str): The name of the system font or the path to the custom font.
        text (str): The text to be displayed.
        size (int): The size of the font.
        color (tuple): The color of the text as an RGB tuple.
        antialias (bool): Whether the font should be antialiased.
        pos (tuple): The position on the screen to display the text (x, y).
        bold (bool): Whether the font should be bold.
    """
    if font_type == "sys":
        font = pygame.font.SysFont(font_name, size, bold)
    elif font_type == "custom":
        font = pygame.font.Font(my_font_path, size)
    font_text = font.render(text, antialias, color)
    screen.blit(font_text, pos)


def draw_x_or_o(screen, val, o_pos, x_pox, color=False):
    """
    Draws an 'X' or 'O' on the screen based on the current player's turn.

    Args:
        screen (pygame.Surface): The display surface to draw on.
        val (int): The current turn value (even for 'X', odd for 'O').
        o_pos (tuple): The position and size for drawing 'O'.
        x_pos (list): The start and end points for drawing 'X'.
        color (bool): Whether to draw the shape in the winning color.

    Returns:
        str: 'X' if 'X' was drawn, 'O' if 'O' was drawn.
    """
    if val % 2 == 0:
        if not color:
            touch_sound.play()
            pygame.draw.line(screen, pygame.Color('red'), x_pox[0][0], x_pox[0][1], 3)
            pygame.draw.line(screen, pygame.Color('red'), x_pox[1][0], x_pox[1][1], 3)
        else:
            pygame.draw.line(screen, pygame.Color('green'), x_pox[0][0], x_pox[0][1], 3)
            pygame.draw.line(screen, pygame.Color('green'), x_pox[1][0], x_pox[1][1], 3)
        return 'X'
    else:
        if not color:
            touch_sound.play()
            pygame.draw.circle(screen, pygame.Color('blue'), (o_pos[0], o_pos[1]), o_pos[2], 3)
        else:
            pygame.draw.circle(screen, pygame.Color('green'), (o_pos[0], o_pos[1]), o_pos[2], 3)
        return 'O'


def play_ttt():
    """
    Main function to play the Tic Tac Toe game.

    Handles the game loop, rendering, and input handling for the Tic Tac Toe game.
    Plays sound effects for winning and drawing, and restarts the game after completion.
    """
    winner_sound = pygame.mixer.Sound(my_path + r"\winner.wav")
    game_over_sound = pygame.mixer.Sound(my_path + r"\game_over_sound.wav")
    clock = pygame.time.Clock()
    ttt_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tic Tac Toe Game by Haja")
    ttt_screen.fill(pygame.Color('black'))
    won = False
    pos_gap = 50
    pos1 = 20
    pos2 = pos1 + pos_gap  # 70
    pos3 = pos2 + pos_gap  # 120
    pos4 = pos3 + pos_gap  # 170
    pos5 = pos4 + pos_gap  # 220
    pos6 = pos5 + pos_gap  # 270
    pos7 = pos6 + pos_gap  # 320
    pos8 = pos7 + pos_gap  # 370
    pos9 = pos8 + pos_gap  # 420
    pos10 = pos9 + pos_gap  # 470
    pos11 = pos10 + pos_gap  # 520
    pos12 = pos11 + pos_gap  # 570
    pos13 = pos12 + pos_gap  # 620

    xoro = 0
    fst_draw = scnd_draw = thrd_draw = frth_draw = ffth_draw = sxth_draw = svnth_draw = eth_draw = nth_draw = False
    fst_shape = scnd_shape = thrd_shape = frth_shape = ffth_shape = sxth_shape = svnth_shape = eth_shape = nth_shape = ''
    fst_pos = scnd_pos = thrd_pos = frth_pos = ffth_pos = sxth_pos = svnth_pos = eth_pos = nth_pos = ''
    pygame.draw.line(ttt_screen, pygame.Color('white'), (pos5, pos1), (pos5, pos13), 4)
    pygame.draw.line(ttt_screen, pygame.Color('white'), (pos9, pos1), (pos9, pos13), 4)
    pygame.draw.line(ttt_screen, pygame.Color('white'), (pos1, pos5), (pos13, pos5), 4)
    pygame.draw.line(ttt_screen, pygame.Color('white'), (pos1, pos9), (pos13, pos9), 4)
    is_running = True
    while is_running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if (mx <= pos5 - 2) and (my <= pos5 - 2):
                if fst_draw == False:
                    fst_draw = True
                    xoro += 1
                    fst_pos = ((pos3, pos3, 50), (((pos2, pos2), (pos4, pos4)), ((pos4, pos2), (pos2, pos4))))
                    fst_shape = draw_x_or_o(ttt_screen, xoro, fst_pos[0], fst_pos[1])
            elif (pos5 + 2 <= mx <= pos9 - 2) and (my <= pos5 - 2):
                if scnd_draw == False:
                    scnd_draw = True
                    xoro += 1
                    scnd_pos = ((pos7, pos3, 50), (((pos6, pos2), (pos8, pos4)), ((pos8, pos2), (pos6, pos4))))
                    scnd_shape = draw_x_or_o(ttt_screen, xoro, scnd_pos[0], scnd_pos[1])
            elif (mx >= pos9 + 2) and (my <= pos5 - 2):
                if thrd_draw == False:
                    thrd_draw = True
                    xoro += 1
                    thrd_pos = ((pos11, pos3, 50), (((pos10, pos2), (pos12, pos4)), ((pos12, pos2), (pos10, pos4))))
                    thrd_shape = draw_x_or_o(ttt_screen, xoro, thrd_pos[0], thrd_pos[1])
            elif (mx <= pos5 - 2) and (pos5 + 2 <= my <= pos9 - 2):
                if frth_draw == False:
                    frth_draw = True
                    xoro += 1
                    frth_pos = ((pos3, pos7, 50), (((pos2, pos6), (pos4, pos8)), ((pos4, pos6), (pos2, pos8))))
                    frth_shape = draw_x_or_o(ttt_screen, xoro, frth_pos[0], frth_pos[1])
            elif (pos5 + 2 <= mx <= pos9 - 2) and (pos5 + 2 <= my <= pos9 - 2):
                if ffth_draw == False:
                    ffth_draw = True
                    xoro += 1
                    ffth_pos = ((pos7, pos7, 50), (((pos6, pos6), (pos8, pos8)), ((pos8, pos6), (pos6, pos8))))
                    ffth_shape = draw_x_or_o(ttt_screen, xoro, ffth_pos[0], ffth_pos[1])
            elif (mx >= pos9 + 2) and (pos5 + 2 <= my <= pos9 - 2):
                if sxth_draw == False:
                    sxth_draw = True
                    xoro += 1
                    sxth_pos = ((pos11, pos7, 50), (((pos10, pos6), (pos12, pos8)), ((pos12, pos6), (pos10, pos8))))
                    sxth_shape = draw_x_or_o(ttt_screen, xoro, sxth_pos[0], sxth_pos[1])
            elif (mx <= pos5 - 2) and (my >= pos9 + 2):
                if svnth_draw == False:
                    svnth_draw = True
                    xoro += 1
                    svnth_pos = ((pos3, pos11, 50), (((pos2, pos10), (pos4, pos12)), ((pos4, pos10), (pos2, pos12))))
                    svnth_shape = draw_x_or_o(ttt_screen, xoro, svnth_pos[0], svnth_pos[1])
            elif (pos5 + 2 <= mx <= pos9 - 2) and (my >= pos9 + 2):
                if eth_draw == False:
                    eth_draw = True
                    xoro += 1
                    eth_pos = ((pos7, pos11, 50), (((pos6, pos10), (pos8, pos12)), ((pos8, pos10), (pos6, pos12))))
                    eth_shape = draw_x_or_o(ttt_screen, xoro, eth_pos[0], eth_pos[1])
            elif (mx >= pos9 + 2) and (my >= pos9 + 2):
                if nth_draw == False:
                    nth_draw = True
                    xoro += 1
                    nth_pos = ((pos11, pos11, 50), (((pos10, pos10), (pos12, pos12)), ((pos12, pos10), (pos10, pos12))))
                    nth_shape = draw_x_or_o(ttt_screen, xoro, nth_pos[0], nth_pos[1])

            shape_list = [fst_shape, scnd_shape, thrd_shape, frth_shape, ffth_shape, sxth_shape, svnth_shape, eth_shape,
                          nth_shape]
            if (shape_list.count("O") >= 3 or shape_list.count("X") >= 3) and won == False:
                for x in ("OOO", "XXX"):
                    val = 1
                    if x == "XXX":
                        val = 2
                    if fst_shape + scnd_shape + thrd_shape == x:
                        draw_x_or_o(ttt_screen, val, fst_pos[0], fst_pos[1], True)
                        draw_x_or_o(ttt_screen, val, scnd_pos[0], scnd_pos[1], True)
                        draw_x_or_o(ttt_screen, val, thrd_pos[0], thrd_pos[1], True)
                        won = True
                    elif frth_shape + ffth_shape + sxth_shape == x:
                        draw_x_or_o(ttt_screen, val, frth_pos[0], frth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, ffth_pos[0], ffth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, sxth_pos[0], sxth_pos[1], True)
                        won = True
                    elif svnth_shape + eth_shape + nth_shape == x:
                        draw_x_or_o(ttt_screen, val, svnth_pos[0], svnth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, eth_pos[0], eth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, nth_pos[0], nth_pos[1], True)
                        won = True
                    elif fst_shape + frth_shape + svnth_shape == x:
                        draw_x_or_o(ttt_screen, val, fst_pos[0], fst_pos[1], True)
                        draw_x_or_o(ttt_screen, val, frth_pos[0], frth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, svnth_pos[0], svnth_pos[1], True)
                        won = True
                    elif scnd_shape + ffth_shape + eth_shape == x:
                        draw_x_or_o(ttt_screen, val, scnd_pos[0], scnd_pos[1], True)
                        draw_x_or_o(ttt_screen, val, ffth_pos[0], ffth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, eth_pos[0], eth_pos[1], True)
                        won = True
                    elif thrd_shape + sxth_shape + nth_shape == x:
                        draw_x_or_o(ttt_screen, val, thrd_pos[0], thrd_pos[1], True)
                        draw_x_or_o(ttt_screen, val, sxth_pos[0], sxth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, nth_pos[0], nth_pos[1], True)
                        won = True
                    elif fst_shape + ffth_shape + nth_shape == x:
                        draw_x_or_o(ttt_screen, val, fst_pos[0], fst_pos[1], True)
                        draw_x_or_o(ttt_screen, val, ffth_pos[0], ffth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, nth_pos[0], nth_pos[1], True)
                        won = True
                    elif thrd_shape + ffth_shape + svnth_shape == x:
                        draw_x_or_o(ttt_screen, val, thrd_pos[0], thrd_pos[1], True)
                        draw_x_or_o(ttt_screen, val, ffth_pos[0], ffth_pos[1], True)
                        draw_x_or_o(ttt_screen, val, svnth_pos[0], svnth_pos[1], True)
                        won = True
                    if won:
                        break

                if won:
                    winner_sound.play()
                    pygame.display.update()
                    time.sleep(2)
                    winner = "O"
                    if val == 2:
                        winner = "X"
                    # print(val)
                    ttt_screen.fill((20, 100, 120))
                    # Game Over Text
                    update_text(ttt_screen, "custom", "", "GAME OVER", 200, pygame.Color('yellow'), True, (100, 200),
                                False)
                    # End Score Text
                    update_text(ttt_screen, "sys", "comicsansms", f"{winner} won the match ! ! !", 30,
                                pygame.Color('green'), True, (200, 300), False)
                    pygame.display.update()
                    time.sleep(2)
                    play_ttt()
                    is_running = False
                elif fst_draw and scnd_draw and thrd_draw and frth_draw and ffth_draw and sxth_draw and svnth_draw and eth_draw and nth_draw:
                    pygame.display.update()
                    time.sleep(1)
                    game_over_sound.play()
                    ttt_screen.fill((20, 100, 120))
                    # Game Over Text
                    update_text(ttt_screen, "custom", "", "GAME OVER", 200, pygame.Color('yellow'), True, (100, 200),
                                False)
                    # Winner Text
                    update_text(ttt_screen, "sys", "comicsansms", f"match draw", 30, pygame.Color('red'), True,
                                (230, 300), False)
                    pygame.display.update()
                    time.sleep(2)
                    play_ttt()
                    is_running = False

        pygame.display.update()  # update the entire screen


if __name__ == '__main__':
    print()
    screen_width = 640
    screen_height = 640
    my_path = os.path.dirname(os.path.abspath(__file__))
    my_font_path = my_path + r"\game_over.ttf"
    pygame.init()
    touch_sound = pygame.mixer.Sound(my_path + r"\ping.wav")
    play_ttt()
    pygame.quit()
    exit()
