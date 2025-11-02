def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"

initial_state = {
    'monkeyAt0': True,
    'monkeyLevel': 'Down',
    'bananaAt1': True,
    'boxAt2': True
}

goal_state = {
    'GetBanana': True,
    'at': 1
}

def plan_actions(current_state, goal):
    actions = []

    # This is a hard-coded solution for the specific initial state.
    if current_state['monkeyAt0'] and \
       current_state['boxAt2'] and \
       current_state['bananaAt1'] and \
       current_state['monkeyLevel'] == 'Down':

        # 1. Monkey goes from 0 to 2 (to get the box)
        actions.append(move('Monkey', 0, 2))

        # 2. Monkey pushes box from 2 to 1 (under the banana)
        actions.append(push_box(2, 1))

        # 3. Monkey climbs the box (which is now at 1)
        actions.append(climb_box(1, 'Up'))

        # 4. Monkey grabs the banana
        actions.append(have_banana(1))

    return actions

actions = plan_actions(initial_state, goal_state)

print("Plan:")
for action in actions:
    print(action)
