import pygame

WIDTH, HEIGHT = 800, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()

font_basic = pygame.font.Font(None, 50)
font_xo = pygame.font.Font(None, 150)


class Policko:
    list_of_policok = []
    def __init__(self, x, y, position, is_there_x, is_there_o,  color):
        self.x = x
        self.y = y
        self.position = position
        self.is_there_x = is_there_x
        self.is_there_o = is_there_o
        self.color = color

        self.list_of_policok.append(self)

    def draw_square(self, x, y, color, is_there_x, is_there_o):
        pygame.draw.rect(WIN, color, (x, y, 200, 200), 2)

        if is_there_x == True:

            x_help = font_xo.render("X", True, color)
            WIN.blit(x_help, (x + 60, y + 60))

        if is_there_o == True:

            o_help = font_xo.render("O", True, color)
            WIN.blit(o_help, (x + 60, y + 60))


def draw_window(pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, x_win, o_win, tie_counter, changing_turns):
    WIN.fill(WHITE)

    pole1.draw_square(pole1.x, pole1.y, pole1.position, pole1.is_there_x, pole1.is_there_o)
    pole2.draw_square(pole2.x, pole2.y, pole2.position, pole2.is_there_x, pole2.is_there_o)
    pole3.draw_square(pole3.x, pole3.y, pole3.position, pole3.is_there_x, pole3.is_there_o)
    pole4.draw_square(pole4.x, pole4.y, pole4.position, pole4.is_there_x, pole4.is_there_o)
    pole5.draw_square(pole5.x, pole5.y, pole5.position, pole5.is_there_x, pole5.is_there_o)
    pole6.draw_square(pole6.x, pole6.y, pole6.position, pole6.is_there_x, pole6.is_there_o)
    pole7.draw_square(pole7.x, pole7.y, pole7.position, pole7.is_there_x, pole7.is_there_o)
    pole8.draw_square(pole8.x, pole8.y, pole8.position, pole8.is_there_x, pole8.is_there_o)
    pole9.draw_square(pole9.x, pole9.y, pole9.position, pole9.is_there_x, pole9.is_there_o)


    if x_win:
        winner_help = font_basic.render("X is winner, wait 5 seconds to play again", True, BLACK)
        WIN.blit(winner_help, (50, 650))
    elif o_win:
        winner_help = font_basic.render("O is winner, wait 5 seconds to play again", True, BLACK)
        WIN.blit(winner_help, (50, 650))
    elif tie_counter == 9:
        winner_help = font_basic.render("Tie, wait 5 seconds to play again", True, BLACK)
        WIN.blit(winner_help, (120, 650))
    else:
        whose_turn(changing_turns)

    pygame.display.update()

def check_which_was_clicked(pos, pole1_bool, pole2_bool, pole3_bool, pole4_bool, pole5_bool, pole6_bool, pole7_bool,
                            pole8_bool, pole9_bool, pole1_bool_opposite, pole2_bool_opposite, pole3_bool_opposite,
                            pole4_bool_opposite, pole5_bool_opposite, pole6_bool_opposite, pole7_bool_opposite,
                            pole8_bool_opposite, pole9_bool_opposite):
    turn_done = False

    position_1 = pole1_bool
    if pos[0] > 100 and pos[0] < 300 and pos[1] > 10 and pos[1] < 210 and not pole1_bool_opposite:
        position_1 = True
        turn_done = True

    position_2 = pole2_bool
    if pos[0] > 300 and pos[0] < 500 and pos[1] > 10 and pos[1] < 210 and not pole2_bool_opposite:
        position_2 = True
        turn_done = True

    position_3 = pole3_bool
    if pos[0] > 500 and pos[0] < 700 and pos[1] > 10 and pos[1] < 210 and not pole3_bool_opposite:
        position_3 = True
        turn_done = True

    position_4 = pole4_bool
    if pos[0] > 100 and pos[0] < 300 and pos[1] > 210 and pos[1] < 410 and not pole4_bool_opposite:
        position_4 = True
        turn_done = True

    position_5 = pole5_bool
    if pos[0] > 300 and pos[0] < 500 and pos[1] > 210 and pos[1] < 410 and not pole5_bool_opposite:
        position_5 = True
        turn_done = True

    position_6 = pole6_bool
    if pos[0] > 500 and pos[0] < 700 and pos[1] > 210 and pos[1] < 410 and not pole6_bool_opposite:
        position_6 = True
        turn_done = True

    position_7 = pole7_bool
    if pos[0] > 100 and pos[0] < 300 and pos[1] > 410 and pos[1] < 610 and not pole7_bool_opposite:
        position_7 = True
        turn_done = True

    position_8 = pole8_bool
    if pos[0] > 300 and pos[0] < 500 and pos[1] > 410 and pos[1] < 610 and not pole8_bool_opposite:
        position_8 = True
        turn_done = True

    position_9 = pole9_bool
    if pos[0] > 500 and pos[0] < 700 and pos[1] > 410 and pos[1] < 610and not pole9_bool_opposite:
        position_9 = True
        turn_done = True

    return position_1, position_2, position_3, position_4, position_5, position_6, position_7, position_8, position_9, turn_done


def check_if_win_x(pole1_bool, pole2_bool, pole3_bool, pole4_bool, pole5_bool, pole6_bool, pole7_bool, pole8_bool, pole9_bool):

    if pole1_bool and pole2_bool and pole3_bool:
        return True
    if pole4_bool and pole5_bool and pole6_bool:
        return True
    if pole7_bool and pole8_bool and pole9_bool:
        return True
    if pole1_bool and pole4_bool and pole7_bool:
        return True
    if pole2_bool and pole5_bool and pole8_bool:
        return True
    if pole3_bool and pole6_bool and pole9_bool:
        return True
    if pole1_bool and pole5_bool and pole9_bool:
        return True
    if pole3_bool and pole5_bool and pole7_bool:
        return True
    return  False

def check_if_win_o(pole1_bool, pole2_bool, pole3_bool, pole4_bool, pole5_bool, pole6_bool, pole7_bool, pole8_bool, pole9_bool):

    if pole1_bool and pole2_bool and pole3_bool:
        return True
    if pole4_bool and pole5_bool and pole6_bool:
        return True
    if pole7_bool and pole8_bool and pole9_bool:
        return True
    if pole1_bool and pole4_bool and pole7_bool:
        return True
    if pole2_bool and pole5_bool and pole8_bool:
        return True
    if pole3_bool and pole6_bool and pole9_bool:
        return True
    if pole1_bool and pole5_bool and pole9_bool:
        return True
    if pole3_bool and pole5_bool and pole7_bool:
        return True
    return  False

def whose_turn(changing_turns):
    if changing_turns:
        winner_help = font_basic.render("Now playing X", True, BLACK)
        WIN.blit(winner_help, (50, 650))
    else:
        winner_help = font_basic.render("Now playing O", True, BLACK)
        WIN.blit(winner_help, (50, 650))

def main():

    pole1 = Policko(100, 10, 1, False, False, BLACK)
    pole2 = Policko(300, 10, 2, False, False, BLACK)
    pole3 = Policko(500, 10, 3, False, False, BLACK)
    pole4 = Policko(100, 210, 4, False, False, BLACK)
    pole5 = Policko(300, 210, 5, False, False, BLACK)
    pole6 = Policko(500, 210, 6, False, False, BLACK)
    pole7 = Policko(100, 410, 7, False, False, BLACK)
    pole8 = Policko(300, 410, 8, False, False, BLACK)
    pole9 = Policko(500, 410, 9, False, False, BLACK)

    run = True

    changing_turns = True
    x_win = False
    o_win = False
    tie_counter = 0

    while run:

        draw_window(pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, x_win, o_win, tie_counter, changing_turns)

        if o_win or x_win or tie_counter == 9:
            pygame.time.wait(5000)
            x_win = False
            o_win = False
            main()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if changing_turns == True:
                    pole1.is_there_x, pole2.is_there_x, pole3.is_there_x, pole4.is_there_x, pole5.is_there_x,\
                    pole6.is_there_x, pole7.is_there_x, pole8.is_there_x,\
                    pole9.is_there_x, turn_done = check_which_was_clicked(pos, pole1.is_there_x, pole2.is_there_x, pole3.is_there_x,
                                                               pole4.is_there_x, pole5.is_there_x, pole6.is_there_x,
                                                               pole7.is_there_x, pole8.is_there_x, pole9.is_there_x,
                                                               pole1.is_there_o, pole2.is_there_o, pole3.is_there_o,
                                                               pole4.is_there_o, pole5.is_there_o,pole6.is_there_o,
                                                               pole7.is_there_o, pole8.is_there_o,pole9.is_there_o)

                    x_win = check_if_win_x(pole1.is_there_x, pole2.is_there_x, pole3.is_there_x, pole4.is_there_x,
                                           pole5.is_there_x, pole6.is_there_x, pole7.is_there_x, pole8.is_there_x,
                                           pole9.is_there_x)


                else:
                    pole1.is_there_o, pole2.is_there_o, pole3.is_there_o, pole4.is_there_o, pole5.is_there_o,\
                    pole6.is_there_o, pole7.is_there_o, pole8.is_there_o,\
                    pole9.is_there_o, turn_done = check_which_was_clicked(pos, pole1.is_there_o, pole2.is_there_o, pole3.is_there_o,
                                                               pole4.is_there_o, pole5.is_there_o, pole6.is_there_o,
                                                               pole7.is_there_o, pole8.is_there_o, pole9.is_there_o,
                                                               pole1.is_there_x, pole2.is_there_x, pole3.is_there_x,
                                                               pole4.is_there_x, pole5.is_there_x, pole6.is_there_x,
                                                               pole7.is_there_x, pole8.is_there_x, pole9.is_there_x)

                    o_win = check_if_win_o(pole1.is_there_o, pole2.is_there_o, pole3.is_there_o, pole4.is_there_o,
                                           pole5.is_there_o, pole6.is_there_o, pole7.is_there_o, pole8.is_there_o,
                                           pole9.is_there_o)

                if turn_done:
                    if changing_turns:
                        tie_counter += 1
                        changing_turns = False
                    elif not changing_turns:
                        tie_counter += 1
                        changing_turns = True


if __name__ == '__main__':
    main()






