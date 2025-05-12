def dist_angles(a, b):
    diff = abs(a - b)
    return min(diff, 2 * math.pi - diff)

def get_end_effector(angles, lengths):
    x, y = 0, 0
    current_angle = 0
    for i in range(len(lengths)):
        current_angle += angles[i]
        x += lengths[i] * math.cos(current_angle)
        y += lengths[i] * math.sin(current_angle)
    return x, y