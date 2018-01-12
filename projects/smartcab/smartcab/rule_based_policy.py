green_light = 'green'
red_light = 'red'
forward = 'forward'
left = 'left'
right = 'right'
no_action = None

def possible_going_left(light, oncoming_trafic, left_trafic):
    return light == green_light and oncoming_trafic == left

def possible_going_forward(light, oncoming_trafic, left_trafic):
    return light == green_light

def possible_going_right(light, oncoming_trafic, left_trafic):
    return (
        light == green_light
        ) or (
        light == red_light and not left_trafic == forward
        )

def ruled_based_policy(light, waypoint, oncoming_trafic, left_trafic):
    possible_to_move_towards_waypoint = {
        forward: possible_going_forward,
        left: possible_going_left,
        right: possible_going_right,
    }

    return waypoint if possible_to_move_towards_waypoint[waypoint](
            light,
            oncoming_trafic,
            left_trafic
        ) else no_action

def test_ruled_based_policy():
    from itertools import product

    lights = (red_light, green_light)
    waypoints = (left, right, forward)
    oncoming_trafics = (left, right, forward)
    left_trafics = (left, right, forward)

    for case in product(lights, waypoints, oncoming_trafics, left_trafics):
        print(case, ruled_based_policy(*case))
