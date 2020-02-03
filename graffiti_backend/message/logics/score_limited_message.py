import random
from message.logics.abstract_message import AbstractMessage

class ScoreLimitedMessage(AbstractMessage):
    """ TODO: When user pickup this message, she can get the share of total scores.
    """
    def __init__(self, database_message_instance):
        super(self.__class__, self).__init__(database_message_instance)
        self.__total_scores = database_message_instance.total_scores
        self.__score_min_scale = database_message_instance.score_min_scale

    def set_total_scores(self, total_scores, scores_min_scale):
        self.__total_scores = total_scores
        self.__scores_min_scale = scores_min_scale

    def get_current_scores(self):
        return self.__score

    def get_random_scores(self):
        random_scores = random.randint(1, self.__total_scores)
        if random_scores < self.__score_min_scale:
            random_scores = self.__score_min_scale
        self.__total_scores = self.__total_scores - random_scores
        if self.__total_scores < self.__scores_min_scale:
            self.__total_scores = 0
        return random_scores