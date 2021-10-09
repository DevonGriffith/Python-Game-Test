# Devon Griffith
# March 25, 2018
#
# THIS IS THE ARTIFICIALLY INTELLIGENT PLAYER

import math, sys, time, numpy

Class AI:

    def __init__(self, gamma, alpha):
        self.gamma = gamma
        self.alpha = alpha

    def __Q_Value(previous_q, gamma, temporal_difference):
        return previous_q + gamma * temporal_difference

    def __TemporalDifference(action, state, reward, gamma, next_q, previous_q):
        return reward + gamma * max() - previous_q

    def __Loss(Q_Target, Q_Value)
        return sum((Q_Target - Q_Value) ** 2)

    def __Softmax(x)
        e_x = exp(x - max(x))
        return e_x / e_x.sum()
