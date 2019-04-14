from math import sqrt
import matplotlib.pyplot as plt

no_of_steps = 278

measured_file = open("ekf_slam_output.txt",'r')
actual_file = open("robot4_reference.txt",'r')

measured_poses = []
actual_poses = []

# Store measured poses
for l in measured_file:
    pose = l.split()
    if pose[0] == 'F':
        measured_poses.append((float(pose[1]), float(pose[2])))

# Store actual poses
for l in actual_file:
    pose = l.split()
    actual_poses.append((float(pose[2]), float(pose[3])))

print(measured_poses[:5])
print('===============')
print(actual_poses[:5])

# Calculate error
overall_error = 0.0
error_at_each_step = []
for measured_pose, actual_pose in zip(measured_poses, actual_poses):
    error = sqrt((measured_pose[0] - actual_pose[0])**2 + (measured_pose[1] - actual_pose[1])**2)
    overall_error += error
    error_at_each_step.append(error)

overall_error = overall_error/no_of_steps

print('The overall error is: {}'.format(error))

plt.plot([i for i in range(no_of_steps)], error_at_each_step)
plt.show()