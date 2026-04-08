class Grader:
    def __init__(self):
        self.history = []

    def grade(self, action, target_code):
        """
        Deterministic scoring:
        - Exact match: 1.0
        - Partial match (same starting letter): 0.5
        - Wrong: 0.1
        - Penalty for repeated wrong answers: -0.1
        Final score is clipped between 0.0 and 1.0
        """

        score = 0.0

        # ✅ Exact match
        if action == target_code:
            score = 1.0

        # ✅ Partial match
        elif action and target_code and action[0] == target_code[0]:
            score = 0.5

        # ✅ Wrong but not zero (important for reward shaping)
        else:
            score = 0.1

        # 🔻 Penalize repeated wrong attempts
        if action in self.history and action != target_code:
            score -= 0.1

        # Save history
        self.history.append(action)

        # Keep score in range [0.0, 1.0]
        return max(min(score, 1.0), 0.0)

    def reset(self):
        self.history = []