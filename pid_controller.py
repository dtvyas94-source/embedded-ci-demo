class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp  # Proportional gain
        self.ki = ki  # Integral gain
        self.kd = kd  # Derivative gain
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measurement, dt):
        error = setpoint - measurement
        self.integral +  error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        output = (self.kp  error) + (self.ki  self.integral) + (self.kd  derivative)
        return output
    
    def compute(self, setpoint, measurement, dt):
    error = setpoint - measurement
    self.integral += error * dt
    derivative = (error - self.prev_error) / dt
    self.prev_error = error
    output = (self.kp * error) + \
             (self.ki * self.integral) + \
             (self.kd * derivative)
    return output