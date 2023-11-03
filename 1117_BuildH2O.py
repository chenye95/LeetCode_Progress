import time
from threading import Thread, Barrier, Semaphore, Lock, Condition


class H2O:
    def __init__(self, instruction_count: int):
        self.output_str: str = ''
        self.instruction_count = instruction_count

    def apply_function(self, instruction: chr, wait_time: float) -> None:
        time.sleep(wait_time)
        if instruction == 'H':
            self.hydrogen()
        else:
            self.oxygen()

    def _add_element(self, element: str) -> None:
        self.output_str += element

    def verify_output(self) -> bool:
        if len(self.output_str) != self.instruction_count:
            return False
        for i in range(self.instruction_count // 3):
            if sorted(self.output_str[i * 3: i * 3 + 3]) != sorted('HHO'):
                return False
        return True

    def hydrogen(self) -> None:
        pass

    def oxygen(self) -> None:
        pass


class H2O_Semaphore(H2O):
    def __init__(self, instruction_count: int):
        super().__init__(instruction_count)
        self.h_sem = Semaphore(2)
        self.o_sem = Semaphore(1)
        self.bar_assembling = Barrier(3)

    def hydrogen(self) -> None:
        with self.h_sem:
            self._add_element('H')
            self.bar_assembling.wait()

    def oxygen(self) -> None:
        with self.o_sem:
            self._add_element('O')
            self.bar_assembling.wait()


class H2O_Condition(H2O):
    def __init__(self, instruction_count: int):
        super().__init__(instruction_count)
        self.release_gate = Condition()
        self.count_h = 0

    def hydrogen(self) -> None:
        with self.release_gate:
            self.release_gate.wait_for(lambda: self.count_h < 2)
            self.count_h += 1
            self._add_element('H')
            self.release_gate.notify_all()

    def oxygen(self) -> None:
        with self.release_gate:
            self.release_gate.wait_for(lambda: self.count_h == 2)
            self._add_element('O')
            self.count_h = 0
            self.release_gate.notify_all()


class H2O_Lock(H2O):
    def __init__(self, instruction_count: int):
        super().__init__(instruction_count)
        self.h1_lock = Lock()
        self.h2_lock = Lock()
        self.o_lock = Lock()

        self.o_lock.acquire()
        self.h2_lock.acquire()

        self.odd_h_count = False

    def hydrogen(self) -> None:
        if self.odd_h_count:
            self.h2_lock.acquire()
        else:
            self.h1_lock.acquire()

        self._add_element('H')

        self.odd_h_count = not self.odd_h_count
        if not self.odd_h_count:
            self.o_lock.release()
        else:
            self.h2_lock.release()

    def oxygen(self) -> None:
        self.o_lock.acquire()
        self._add_element('O')
        self.h1_lock.release()


time_factor = .1

for object_class in [H2O_Semaphore, H2O_Condition, H2O_Lock, ]:
    print("Testing", object_class.__name__)
    for instruction_str in ["OOHHHH", "HOH", "HHHOOH", "HHOOHH", "HOHHOH", "HHHOHO", "HHHOOH"]:
        object_instance = object_class(len(instruction_str))
        thread_list = []
        for thread_id, instruction_id in enumerate(instruction_str):
            thread_no = Thread(target=object_instance.apply_function, args=(instruction_id, thread_id * time_factor))
            thread_no.start()
            thread_list.append(thread_no)

        for thread_no in thread_list:
            thread_no.join()

        assert object_instance.verify_output()
    print("Test Passed for", object_class.__name__)
