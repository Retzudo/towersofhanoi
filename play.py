#!/usr/bin/env python3
import os
from towers import create_tower, TowerError
from towersvisualizer import Visualizer

def ask_for_init():
    """Ask for initial values and return them as a tuple."""
    while True:
        try:
            input_string = input('How many rods should the tower have? > ')
            rods = int(input_string)
        except ValueError:
            print('Invalid value {}'.format(input_string))
            continue
        else:
            break

    while True:
        try:
            input_string = input('How many pieces do you want to start with? > ')
            pieces = int(input_string)
        except ValueError:
            print('Invalid value {}'.format(input_string))
            continue
        else:
            break

    return rods, pieces

def game_loop():
    """Main game loop."""
    rods, pieces = ask_for_init()
    tower = create_tower(num_of_rods=rods, num_of_pieces=pieces)
    visualizer = Visualizer(tower)

    os.system('clear')
    print(visualizer.visualize())
    while True:
        while True:
            try:
                input_string = input('Move piece from rod #')
                from_rod = int(input_string)
                if not len(tower.rods) >= from_rod > 0:
                    print('There is no such rod #{}'.format(from_rod))
                    continue
            except ValueError:
                print('Invalid value'.format(input_string))
            else:
                os.system('clear')
                print(visualizer.visualize())
                break

        while True:
            try:
                input_string = input('Move piece from rod #{} to rod #'.format(from_rod))
                to_rod = int(input_string)
                if not len(tower.rods) >= to_rod > 0:
                    print('There is no such rod #{}'.format(to_rod))
                    continue
            except ValueError:
                print('Invalid value'.format(input_string))
            else:
                os.system('clear')
                print(visualizer.visualize())
                break

        try:
            tower.move_piece(from_rod-1, to_rod-1)
        except TowerError:
            print('Invalid move')
        else:
            os.system('clear')
            print(visualizer.visualize())


def main():
    """Run the game loop and exit on Ctrl+C."""
    try:
        game_loop()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
