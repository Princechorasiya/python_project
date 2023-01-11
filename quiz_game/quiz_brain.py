class CheckAns:
    def check_ans(self, user_input, answer):
        if user_input == answer:
            return True
        else:
            return False


class ScoreChecker:
    def __init__(self):

        self.score = 0

    def update_score(self, result):
        if result == True:
            self.score += 1
        else:
            self.score += 0

    def get_score(self):
        return self.score
