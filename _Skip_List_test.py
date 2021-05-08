from datetime import datetime
from random import randint

from _Skip_List import SkipList


def test_case_1(n=10000):
    previous_time_stamp = datetime.now()
    test = SkipList()
    assert not test.search(n)
    print("Test Add Operations")
    for i in range(n):
        test.add(i)
        test.add(i)
        # print("Added %d" % i)
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Test Search Operations")
    for i in range(n):
        assert test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Test First Erase Operations")
    for i in range(n):
        assert test.erase(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Confirm First Erase Operations")
    for i in range(n):
        assert test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Test Second Erase Operations")
    for i in range(n):
        assert test.erase(i)
        assert not test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Confirm Second Erase Operations")
    for i in range(n):
        assert not test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    assert not test.search(n)


def test_case_2(n=100000):
    test_class = SkipList()
    action_list = [0, 0, 0]

    start_time = datetime.now()
    for _ in range(n):
        take_step, param = randint(0, 2), randint(0, 1000)
        if take_step == 0:
            test_class.add(param)
        elif take_step == 1:
            test_class.erase(param)
        else:
            test_class.search(param)
        action_list[take_step] += 1
    print("Test 2: %d Actions Total Duration" % n, datetime.now() - start_time)
    print(action_list)


if __name__ == '__main__':
    test_case_1()
    test_case_2()
