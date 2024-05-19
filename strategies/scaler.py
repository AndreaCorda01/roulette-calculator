from strategies.strategies import BaseStrategy
import matplotlib.pyplot as plt


class ScalerStrategy():
    
    strategy_class = None
    equity = 0
    results = []
    spins = 0
    def __init__(self, strategy_class):
        if issubclass(strategy_class, BaseStrategy):
            self.strategy_class = strategy_class
        else:
            raise ValueError('Invalid strategy')

    def run(self, number_sessions, number_spins, equity=100):
        self.equity = equity
        self.spins = number_spins
        session_results = []
        for session in range(number_sessions):
            strategy = self.strategy_class(equity)
            strategy.simulate(number_spins)
            strategy.get_statistics()
            session_results.append(strategy.results[-1])
        self.results = session_results
        return session_results
    
    def get_bar_chart(self):
        plt.xlabel('Session')
        plt.ylabel('Net Balance')
        plt.bar(range(len(self.results)), list(map(lambda x: x - self.equity, self.results)))
        plt.title("Plays using " + self.strategy_class.__name__ + " with " + str(self.spins) + " spins and equity of " + str(self.equity))
        plt.savefig('output/' + self.strategy_class.__name__ + '-times-' + str(len(self.results)) + '.png')