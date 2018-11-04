import random
import Catch5

ActionMap = {0: 3, 1: 2, 2: 1, 3: -1, 4: -2, 5: -3}

# creating random actions


def get_action():
    return random.randrange(0, 6)

# mapping actions (0, 1, 2, 3, 4, 5) to answers (3, 2, 1, -1 , -2, -3)


def action_to_answer(action):

    return ActionMap[action]


def play(num_times):
    game = Catch5.Game()
    won = 0
    for nb_game in range(1, num_times + 1):

        game.reset()
        print('Starting game #{nb_game}'.format(nb_game=nb_game))
        while (game.is_active()):
            print('Current number is {current_number}'.format(
                current_number=game.current_number))
            action = get_action()
            human_readable_answer = action_to_answer(action)

            print('Playing {answer}'.format(answer=human_readable_answer))
            game.play(human_readable_answer)

            if (game.has_won()):
                print('You won!')
                won = won + 1

            if (game.has_lost()):
                print('You lost')

        print('##############################################')
        print("stats:")
        print("Won ",won)
        print("Won % ",won/num_times)


play(100)
