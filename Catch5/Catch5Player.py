import random
import Catch5
import numpy as np

ActionMap = {0: 3, 1: 2, 2: 1, 3: -1, 4: -2, 5: -3}
class TrainStats():
    def __init__(self):
        self.epoch  = 0
        self.nb_wins = 0
        self.nb_losses = 0
        self.p_wins = 0
        self.p_loss = 0


class Agent:
    def __init__(self):
        self.game = Catch5.Game()
        self.qtable ={}

    def ensure_qtable_entry(self, state):
        if state not in self.qtable:
            self.qtable[state] = np.zeros(6)  

    def get_action(self, state):
        return random.randint(0,5)

    # mapping actions (0..5) to answers (3..-3)
    def action_to_answer(self, action):
        return ActionMap[action]

    def train(self, state, action, reward, next_state, final):

        self.ensure_qtable_entry(state)
        self.ensure_qtable_entry(next_state)

        if final:
            q_value = reward
        else:
            next_state_actions = self.qtable[next_state]
            next_state_max = np.amax(next_state_actions)

            q_value = reward + 0.6 * next_state_max

        self.qtable[state][action] = q_value

    def print_epoch_stats(self, stats):
        print('Epoch: {stats.epoch} Wins: {stats.nb_wins} ({stats.p_wins:.2f}%) Losses: {stats.nb_losses} ({stats.p_loss:.2f}%)'.format(stats=stats))

    def play(self, num_times):

      for nb_game in range(1, num_times + 1):
        self.game.reset()
        print('Starting game #{nb_game}'.format(nb_game=nb_game))
        while (self.game.is_active()):
            print('Current number is {current_number}'.format(current_number=self.game.current_number))
            action = self.get_action(self.game.current_number)
            human_readable_answer = self.action_to_answer(action)
            
            print('Playing {answer}'.format(answer=human_readable_answer))
            self.game.play(human_readable_answer)

            if (self.game.has_won()):
                print('You won!')

            if (self.game.has_lost()):
                print('You lost')

        print('##############################################')

    def get_reward(self):
        if self.game.has_won():
            return 1
        elif self.game.has_lost():
            return -1
        else:
            return -0.1

    def play_and_train(self):
        stats = TrainStats()

        for epoch in range(1, 101):

            self.game.reset()
            stats.epoch = epoch

            while (self.game.is_active()):

                state = self.game.current_number

                action = self.get_action(state)
                human_readable_answer = self.action_to_answer(action)

                self.game.play(human_readable_answer)

                reward = self.get_reward()
                next_state = self.game.current_number
                final = not self.game.is_active()
                self.train(state, action, reward, next_state, final)

                if (self.game.has_won()):
                    stats.nb_wins += 1

                if (self.game.has_lost()):
                    stats.nb_losses += 1

                stats.p_wins = 100 / epoch * stats.nb_wins
                stats.p_loss = 100 / epoch * stats.nb_losses

            if (epoch  % 10==0):
                self.print_epoch_stats(stats)


Agent().play_and_train()