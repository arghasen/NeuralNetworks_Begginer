ActionMap = {0: 3, 1: 2, 2: 1, 3: -1, 4: -2, 5: -3}


class TrainStats():
    def __init__(self):
        self.epoch = 0
        self.nb_wins = 0
        self.nb_losses = 0
        self.p_wins = 0
        self.p_loss = 0


class AgentConfig():
    def __init__(self):
        self.nb_epoch = 10000
        self.print_every_n_epoch = 1
        self.plot_charts = True
        self.discount_factor = 0.99
        self.initial_randomness_rate = 1