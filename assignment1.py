import numpy as np
from sim.sim1d import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8,8]
options['CONSTANT_SPEED'] = False

class KalmanFilterToy:
    def __init__(self):
        self.v = 0
        self.prev_x = 0
        self.prev_t = 0
    def predict(self,t):
        dt = t - self.prev_t
        prediction = self.prev_x + self.v * dt
        return prediction
    def measure_and_update(self,x,t):
        measured_v = (x - self.prev_x) / (t - self.prev_t)
        self.v += (measured_v - self.v) * 0.6
        self.prev_t = t
        self.prev_x = x
        return


sim_run(options,KalmanFilterToy)
