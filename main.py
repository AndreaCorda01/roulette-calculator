
from strategies.strategies import FibonacciStrategy
from strategies.scaler import ScalerStrategy


print("RESULTS: Fibonacci Strategy")

scalerFibonacci =  ScalerStrategy(FibonacciStrategy)
print(scalerFibonacci.run(number_sessions=50, number_spins=100, equity=100))
scalerFibonacci.get_bar_chart()

