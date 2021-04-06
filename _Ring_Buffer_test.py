from _Ring_Buffer import RingBufferList, RingBufferTwoPointer

for CircularQueue in [RingBufferList, RingBufferTwoPointer]:
    test_queue = CircularQueue(3)
    assert test_queue.enqueue(1) is True
    assert test_queue.enqueue(2) is True
    assert test_queue.enqueue(3) is True
    assert test_queue.enqueue(4) is False
    assert test_queue.rear() == 3
    assert test_queue.front() == 1
    assert test_queue.is_full() is True
    assert test_queue.dequeue() is True
    assert test_queue.enqueue(4)
    assert test_queue.rear() == 4
    assert test_queue.front() == 2
    assert test_queue.dequeue() is True
    assert test_queue.rear() == 4
    assert test_queue.front() == 3
    assert test_queue.dequeue() is True
    assert test_queue.rear() == 4
    assert test_queue.front() == 4
    assert test_queue.dequeue() is True
    assert test_queue.rear() == test_queue.NONE_VALUE
    assert test_queue.front() == test_queue.NONE_VALUE
    assert test_queue.dequeue() is False

for CircularQueue in [RingBufferList, RingBufferTwoPointer]:
    test_queue = CircularQueue(3)
    assert test_queue.enqueue('1') is True
    assert test_queue.enqueue('2') is True
    assert test_queue.enqueue(3) is True
    assert test_queue.enqueue('4') is False
    assert test_queue.rear() == 3
    assert test_queue.front() == '1'
    assert test_queue.is_full() is True
    assert test_queue.dequeue() is True
    assert test_queue.enqueue('4')
    assert test_queue.rear() == '4'
    assert test_queue.front() == '2'
    assert test_queue.dequeue() is True
    assert test_queue.rear() == '4'
    assert test_queue.front() == 3
    assert test_queue.dequeue() is True
    assert test_queue.rear() == '4'
    assert test_queue.front() == '4'
    assert test_queue.dequeue() is True
    assert test_queue.rear() == test_queue.NONE_VALUE
    assert test_queue.front() == test_queue.NONE_VALUE
    assert test_queue.dequeue() is False
