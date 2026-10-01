class Goal:
    def __init__(self, description: str, target_amount: float):
        self.description = description
        self.target_amount = target_amount
        self.current_amount = 0.0
