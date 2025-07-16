# strategy_lab.py — Strategy Core Lab

class StrategyLab:
    def __init__(self):
        self.active_strategies = []

    def register_strategy(self, name, logic_function):
        self.active_strategies.append((name, logic_function))

    def execute_all(self, market_data):
        for name, logic in self.active_strategies:
            print(f"Executing strategy: {name}")
            logic(market_data)
