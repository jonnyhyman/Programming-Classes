# Super ultra simple wheel command solution
wheel_command = ((-50) - actual_position[1])*0.1 - actual_velocity[1]


# Better
cp = +0.1
cd = -1.0
error = (-50) - actual_position[1])
wheel_command = cp * error + cd * actual_velocity[1]
