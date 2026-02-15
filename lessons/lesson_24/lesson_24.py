import random
from importlib.metadata import entry_points

def_choice = 8
menu = [' spam','egg','sausages','bacon']
menu_multi = menu +['egg', 'sausages']
joints = [' and ', ',', ' and ',' with ', ' and double portion of ']
prefered = menu[0]
forbidden = {'not', 'without', 'no'}

song = ','.join([prefered.capitalize()]+[prefered] * def_choice) + '!'
d_welcome = "Welcome to the Vikings restauant!.\n what would you like to eat?"
d_choise = '> '
d_promote = "We hightly recommend {dishes}" + f',and{prefered}...'
d_good = "That's a perfect choice. Let's have more {dishes}!"+ f',and{prefered}, of course!'
d_bad = "Disgusting. who eats {dishes}?"
d_unavailable = "That's not on our menu. We only serve {dishes}."

def get_dishes(number):
    sel = list(menu)
    res = []
    for i in range(number):
        rnd = random.choice(sel)
        res.append(rnd)
        sel.append(random.choice(joints))
    res = res[:-1]
    # print(res)
    return ' '.join(res)


def dialog(num_choice = def_choice):
    """User dialog simulation"""
    print(d_welcome)
    # print(d_promote.format(dishes=get_dishes(3)))

    entry = input(d_choise).strip()
    word = entry.lower().split()
    print(word)
    def promote():
        print(d_promote.format (dishes=get_dishes(num_choice)))
    if set(word) & set(menu_multi):
        if set(word) & set(forbidden):
            print(d_bad.format(dishes=entry))
            promote()
        else:
            print(d_good.format(dishes=entry))
            print(f"Viking's song:{song}")
        return 'done'
# entry = input(d_choise).strip()
#     word = entry.lower().split()
#     print(word)
#
#     def promote():
#         print(d_promote.format(dishes=get_dishes(num_choice)))
#
#     if set(word) and set(menu_multi):
#         if set(word) and set(forbidden):
#             print(d_bad.format(dishes=entry))
#             promote()
#


dialog()


print(get_dishes(5))