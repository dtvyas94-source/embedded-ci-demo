import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pid_controller import PIDController

def test_pid_zero_error():
    """When setpoint equals measurement, output should be zero"""
    pid = PIDController(kp=1.0, ki=0.0, kd=0.0)
    output = pid.compute(setpoint=10.0, measurement=10.0, dt=0.1)
    assert output == 0.0

def test_pid_positive_error():
    """When setpoint > measurement, output should be positive"""
    pid = PIDController(kp=1.0, ki=0.0, kd=0.0)
    output = pid.compute(setpoint=10.0, measurement=5.0, dt=0.1)
    assert output > 0

def test_pid_negative_error():
    """When setpoint < measurement, output should be negative"""
    pid = PIDController(kp=1.0, ki=0.0, kd=0.0)
    output = pid.compute(setpoint=5.0, measurement=10.0, dt=0.1)
    assert output < 0

def test_pid_proportional_gain():
    """Output should scale with proportional gain"""
    pid_low = PIDController(kp=1.0, ki=0.0, kd=0.0)
    pid_high = PIDController(kp=2.0, ki=0.0, kd=0.0)
    out_low = pid_low.compute(setpoint=10.0, measurement=5.0, dt=0.1)
    out_high = pid_high.compute(setpoint=10.0, measurement=5.0, dt=0.1)
    assert out_high > out_low