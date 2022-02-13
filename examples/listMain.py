import demoLists

def main():
    dice_list = make_list()
    display_list(dice_list)

    for item in dice_list:
        item.roll_dice(6)
    
    display_list(dice_list)


def display_list(a_list):
    for item in (a_list):
            print(item)
    print()

def make_list():
    dice_list = []
    for count in range(1,5):
        new_phone= demoLists.Dice()
        dice_list.append(new_phone)
    return dice_list

main()