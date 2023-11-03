import time
from threading import Thread, Lock, Semaphore, Condition, Event, Barrier


class Foo:
    """
    Ensure that the order of execution is First, Second, Third, in threading situations
    """

    def __init__(self):
        self.output_list = []

    def update_list(self, i: int) -> None:
        self.output_list.append(i)

    def apply_function(self, id: int, wait_time: float) -> None:
        time.sleep(wait_time)
        if id == 0:
            self.first_implementation()
        elif id == 1:
            self.second_implementation()
        else:
            self.third_implementation()

    def first_implementation(self) -> None:
        pass

    def second_implementation(self) -> None:
        pass

    def third_implementation(self) -> None:
        pass


class Foo_Lock(Foo):
    def __init__(self):
        super().__init__()
        self.first_job_done = Lock()
        self.second_job_done = Lock()
        self.first_job_done.acquire()
        self.second_job_done.acquire()

    def first_implementation(self) -> None:
        self.update_list(1)
        self.first_job_done.release()

    def second_implementation(self) -> None:
        with self.first_job_done:
            self.update_list(2)
            self.second_job_done.release()

    def third_implementation(self) -> None:
        with self.second_job_done:
            self.update_list(3)


class Foo_Semaphore(Foo):
    def __init__(self):
        super().__init__()
        self.first_job_done = Semaphore(1)
        self.second_job_done = Semaphore(1)
        self.first_job_done.acquire()
        self.second_job_done.acquire()

    def first_implementation(self) -> None:
        self.update_list(1)
        self.first_job_done.release()

    def second_implementation(self) -> None:
        with self.first_job_done:
            self.update_list(2)
            self.second_job_done.release()

    def third_implementation(self) -> None:
        with self.second_job_done:
            self.update_list(3)


class Foo_Condition(Foo):
    def __init__(self):
        super().__init__()
        self.condition_channel = Condition()
        self.first_job_done = self.second_job_done = False

    def first_implementation(self) -> None:
        with self.condition_channel:
            self.update_list(1)
            self.first_job_done = True
            self.condition_channel.notify_all()

    def second_implementation(self) -> None:
        with self.condition_channel:
            self.condition_channel.wait_for(lambda: self.first_job_done)
            self.update_list(2)
            self.second_job_done = True
            self.condition_channel.notify_all()

    def third_implementation(self) -> None:
        with self.condition_channel:
            self.condition_channel.wait_for(lambda: self.second_job_done)
            self.update_list(3)


class Foo_Event(Foo):
    def __init__(self):
        super().__init__()
        self.first_job_done = Event()
        self.second_job_done = Event()

    def first_implementation(self) -> None:
        self.update_list(1)
        self.first_job_done.set()

    def second_implementation(self) -> None:
        self.first_job_done.wait()
        self.update_list(2)
        self.second_job_done.set()

    def third_implementation(self) -> None:
        self.second_job_done.wait()
        self.update_list(3)


class Foo_Barrier(Foo):
    def __init__(self):
        super().__init__()
        self.first_job_done = Barrier(2)
        self.second_job_done = Barrier(2)

    def first_implementation(self) -> None:
        self.update_list(1)
        self.first_job_done.wait()

    def second_implementation(self) -> None:
        self.first_job_done.wait()
        self.update_list(2)
        self.second_job_done.wait()

    def third_implementation(self) -> None:
        self.second_job_done.wait()
        self.update_list(3)


time_factor = .1

for object_class in [Foo_Lock, Foo_Semaphore, Foo_Condition, Foo_Event, Foo_Barrier, ]:
    print("Testing", object_class.__name__)
    for wait_permutation in [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1), ]:
        object_instance = object_class()
        thread_list = []
        for thread_id, permutation_id in enumerate(wait_permutation):
            thread_no = Thread(target=object_instance.apply_function, args=(thread_id,
                                                                            wait_permutation[thread_id] * time_factor))
            thread_no.start()
            thread_list.append(thread_no)

        for thread_no in thread_list:
            thread_no.join()

        assert object_instance.output_list == [1, 2, 3], object_instance.output_list
    print("Test Passed for", object_class.__name__)
