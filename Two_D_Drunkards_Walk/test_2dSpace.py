# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:38:22 2024

@author: jim
"""
from datetime import datetime
import pandas as pd
from Two_D_Drunkards_Walk.TestRandomGenerator import TestRandomGenerator
from Two_D_Drunkards_Walk.Test_To_Get_Arrested_Generator import (
    Test_To_Get_Arrested_Generator,
)
from Two_D_Drunkards_Walk.production_random import production_random
from walk_space import two_d_space_walker


def test_space_gets_set_up_with_postion_at_centre():
    walker = two_d_space_walker(11, 400)
    assert walker.get_current_position() == 0


def test_random_walk_where_walker_not_arrested():
    print()
    # random function for testing
    # prepare the data frame to receive the results of the single iterations
    df = pd.DataFrame(columns=["Index", "Moves", "Arrested"])

    test_random_generator = TestRandomGenerator()
    for i in range(1):  # trying just one simulation
        walker = two_d_space_walker(
            11, 10
        )  # 11 means j=5` 400 is the number of steps to survive to be counted`
        simulation = walker.move_drunkard(
            10, test_random_generator.next
        )  # test 40 moves
        print(i, simulation)
    df.loc[i] = [i, simulation[1], simulation[0]]  # Adding a new row at the end
    print(df)
    # should survive
    assert simulation == (False, 10)


def test_random_walk_where_walker_is_arrested():
    print()
    # random function for testing
    # prepare the data frame to receive the results of the single iterations
    df = pd.DataFrame(columns=["Index", "Moves", "Arrested"])
    # this random generator produces 15 "left"s which force a death
    test_random_generator = Test_To_Get_Arrested_Generator()
    for i in range(1):  # trying just one simulation
        walker = two_d_space_walker(
            11, 10
        )  # 11 means j=5` 400 is the number of steps to survive to be counted`
        simulation = walker.move_drunkard(
            10, test_random_generator.next
        )  # test 40 moves
    df.loc[i] = [i, simulation[1], simulation[0]]  # Adding a new row at the end
    print(df)
    # should not survive
    assert simulation == (True, 5)


def test_correctly_identify_no_arrest_J_0():
    walker = two_d_space_walker(11, 400)
    arrested = walker.is_arrested(0)
    assert arrested == False


def test_correctly_identify_arrest_plus_J():
    walker = two_d_space_walker(11, 400)
    arrested = walker.is_arrested(5)
    assert arrested == True


def test_correctly_identify_arrest_minus_J():
    walker = two_d_space_walker(11, 400)
    arrested = walker.is_arrested(-5)
    assert arrested == True


def test_correctly_identify_arrest_plus_J_plus_1():
    walker = two_d_space_walker(11, 400)
    arrested = walker.is_arrested(6)
    assert arrested == True


def test_correctly_identify_arrest_minus_J_plus_1():
    walker = two_d_space_walker(11, 400)
    arrested = walker.is_arrested(-6)
    assert arrested == True


def test_non_random():
    test_random_generator = TestRandomGenerator()
    directions = []
    for i in range(15):
        direction = get_random_direction(test_random_generator.next)
        print(direction)
        directions.append(direction)
    print(directions)
    assert directions == [
        "left",
        "left",
        "right",
        "right",
        "left",
        "right",
        "right",
        "left",
        "right",
        "left",
        "right",
        "left",
        "left",
        "left",
        "left",
    ]


def test_random():
    directions = []
    for i in range(15):
        direction = get_random_direction(production_random)
        print(direction)
        directions.append(direction)
    print(directions)
    assert directions != [
        "left",
        "left",
        "right",
        "right",
        "left",
        "right",
        "right",
        "left",
        "right",
        "left",
        "right",
        "left",
        "left",
        "left",
        "left",
    ]


def get_random_direction(random_function):
    result = random_function()
    print(f"The result is {datetime.now()} {result}")
    return result
    # Further processing can be done here


# For production, you might use the random.choice() function to randomly select between "left" and "right"
# Initialize the test random generator with a starting seed


def test_production():
    # Using the functions in different contexts
    print("In production:")
    for _ in range(15):  # Example: Generate 5 test outputs
        result = get_random_direction(production_random)
        print(result)


def test_in_test():
    print("\nIn testing:")
    test_random_generator = TestRandomGenerator()
    # Use a loop or call the test_random_generator.next() multiple times based on your test cases
    for _ in range(15):  # Example: Generate 5 test outputs
        result = get_random_direction(test_random_generator.next)
        print(result)


def get_random_direction(random_function):
    result = random_function()
    print(f"The result is {datetime.now()} {result}")
    return result


def test_Get_Arrested_Generator():
    print("\nIn getting arrested testing:")
    test_random_generator = Test_To_Get_Arrested_Generator()
    for _ in range(15):  # Example: Generate 15 test outputs
        result = get_random_direction(test_random_generator.next)
        print(result)
