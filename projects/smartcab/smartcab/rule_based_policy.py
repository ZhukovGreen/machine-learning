GREEN_LIGHT = 'green'
RED_LIGHT = 'red'
FORWARD = 'forward'
LEFT = 'left'
RIGHT = 'right'
NO_ACTION = None

def possible_going_left(light, oncoming_trafic, left_trafic):
    return light == GREEN_LIGHT and oncoming_trafic == LEFT

def possible_going_forward(light, oncoming_trafic, left_trafic):
    return light == GREEN_LIGHT

def possible_going_right(light, oncoming_trafic, left_trafic):
    return (
        light == GREEN_LIGHT
        ) or (
        light == RED_LIGHT and left_trafic != FORWARD
        )

POSSIBLE_TO_MOVE_TOWARD_WAYPOINT = {
    FORWARD: possible_going_forward,
    LEFT: possible_going_left,
    RIGHT: possible_going_right,
}

VALID_ACTIONS = {
    ('red', 'left', 'left', 'left'): None,
    ('red', 'left', 'left', 'right'): None,
    ('red', 'left', 'left', 'forward'): None,
    ('red', 'left', 'right', 'left'): None,
    ('red', 'left', 'right', 'right'): None,
    ('red', 'left', 'right', 'forward'): None,
    ('red', 'left', 'forward', 'left'): None,
    ('red', 'left', 'forward', 'right'): None,
    ('red', 'left', 'forward', 'forward'): None,
    ('red', 'right', 'left', 'left'): 'right',
    ('red', 'right', 'left', 'right'): 'right',
    ('red', 'right', 'left', 'forward'): None,
    ('red', 'right', 'right', 'left'): 'right',
    ('red', 'right', 'right', 'right'): 'right',
    ('red', 'right', 'right', 'forward'): None,
    ('red', 'right', 'forward', 'left'): 'right',
    ('red', 'right', 'forward', 'right'): 'right',
    ('red', 'right', 'forward', 'forward'): None,
    ('red', 'forward', 'left', 'left'): None,
    ('red', 'forward', 'left', 'right'): None,
    ('red', 'forward', 'left', 'forward'): None,
    ('red', 'forward', 'right', 'left'): None,
    ('red', 'forward', 'right', 'right'): None,
    ('red', 'forward', 'right', 'forward'): None,
    ('red', 'forward', 'forward', 'left'): None,
    ('red', 'forward', 'forward', 'right'): None,
    ('red', 'forward', 'forward', 'forward'): None,
    ('green', 'left', 'left', 'left'): 'left',
    ('green', 'left', 'left', 'right'): 'left',
    ('green', 'left', 'left', 'forward'): 'left',
    ('green', 'left', 'right', 'left'): None,
    ('green', 'left', 'right', 'right'): None,
    ('green', 'left', 'right', 'forward'): None,
    ('green', 'left', 'forward', 'left'): None,
    ('green', 'left', 'forward', 'right'): None,
    ('green', 'left', 'forward', 'forward'): None,
    ('green', 'right', 'left', 'left'): 'right',
    ('green', 'right', 'left', 'right'): 'right',
    ('green', 'right', 'left', 'forward'): 'right',
    ('green', 'right', 'right', 'left'): 'right',
    ('green', 'right', 'right', 'right'): 'right',
    ('green', 'right', 'right', 'forward'): 'right',
    ('green', 'right', 'forward', 'left'): 'right',
    ('green', 'right', 'forward', 'right'): 'right',
    ('green', 'right', 'forward', 'forward'): 'right',
    ('green', 'forward', 'left', 'left'): 'forward',
    ('green', 'forward', 'left', 'right'): 'forward',
    ('green', 'forward', 'left', 'forward'): 'forward',
    ('green', 'forward', 'right', 'left'): 'forward',
    ('green', 'forward', 'right', 'right'): 'forward',
    ('green', 'forward', 'right', 'forward'): 'forward',
    ('green', 'forward', 'forward', 'left'): 'forward',
    ('green', 'forward', 'forward', 'right'): 'forward',
    ('green', 'forward', 'forward', 'forward'): 'forward',
}

def rule_based_policy(light, waypoint, oncoming_trafic, left_trafic):

    return waypoint if POSSIBLE_TO_MOVE_TOWARD_WAYPOINT[waypoint](
            light,
            oncoming_trafic,
            left_trafic
        ) else NO_ACTION

def test_rule_based_policy():
    from itertools import product

    lights = (RED_LIGHT, GREEN_LIGHT)
    waypoints = (LEFT, RIGHT, FORWARD)
    oncoming_trafics = (LEFT, RIGHT, FORWARD)
    left_trafics = (LEFT, RIGHT, FORWARD)

    for case in product(lights, waypoints, oncoming_trafics, left_trafics):
        assert rule_based_policy(*case) == VALID_ACTIONS[case]
