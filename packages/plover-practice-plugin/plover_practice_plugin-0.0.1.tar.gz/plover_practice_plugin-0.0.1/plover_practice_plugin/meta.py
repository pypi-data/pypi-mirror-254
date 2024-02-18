import random

def random_number(ctx, argument):
    low, high = [int(arg) for arg in argument.split(":")]
    number = random.randint(low, high)

    action = ctx.new_action()
    action.text = str(number)
    return action
