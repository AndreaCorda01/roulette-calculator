
import numpy as np
import matplotlib.pyplot as plt

class BaseStrategy:
    
    equity = 0
    number_games = 0
    number_wins = 0
    
    results = []
    simulated = False
    
    def __init__(self, equity=0):
        self.equity = equity
        
    def spin_roulette(self, n_spins):
        outcomes = np.random.choice(['red', 'black', 'green'], size=n_spins, p=[18/37, 18/37, 1/37])
        return outcomes
        
    def simulate(self):
        if self.simulated:
            print("This strategy is already being simulated!")
            raise Exception("This strategy is already being simulated!")
        self.simulated = True
        
    def render_results(self):
        plt.plot(self.results)
        plt.xlabel('Number of Spins')
        plt.ylabel('Balance')
        plt.title('Balance Over Time Using Fibonacci Betting Strategy')
        plt.savefig('output/fibonacci.png')

    def get_statistics(self):
        final_balance = self.results[-1]
        average_balance = np.mean(self.results)
        std_dev_balance = np.std(self.results)
        risk_of_ruin = sum(1 for balance in self.results if balance <= 0) / len(self.results)

        print(f'Final Balance: {final_balance}')
        print(f'Average Balance: {average_balance}')
        print(f'Standard Deviation: {std_dev_balance}')
        print(f'Risk of Ruin: {risk_of_ruin}')


class FibonacciStrategy(BaseStrategy):
    
    def __init__(self, equity=0):
        super().__init__(equity)
    
    def play(self):
        self.number_games += 1
        bet = self.fibonacci(self.number_games)
        if self.flip_coin(bet):
            self.equity += bet
            self.number_wins += 1
        else:
            self.equity -= bet
            

    def simulate(self, n_spins, base_bet=1):
        super().simulate()
        fibonacci_sequence = [1, 1]
        balance = self.equity
        bet_index = 0
        results = []

        spins = self.spin_roulette(n_spins)
        
        for spin in spins:
            if balance <= 0:
                break

            bet_amount = fibonacci_sequence[bet_index] * base_bet
            if bet_amount > balance:
                continue
            if spin == 'red': 
                balance += bet_amount
                if bet_index >= 2:
                    bet_index -= 2
                else:
                    bet_index = 0
            else:
                balance -= bet_amount
                bet_index += 1
                if bet_index >= len(fibonacci_sequence):
                    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

            results.append(balance)
        self.results = results
        self.balance = balance
        return results
