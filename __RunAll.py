import concurrent.futures
import os
from sys import argv

files = os.listdir('.')


def execute_file(file_name: str) -> None:
    os.system("python " + file_name)


max_worker = 1
if len(argv) > 1:
    max_worker = min(int(argv[-1]), 5)
print("Running concurrent threads with %d workers" % max_worker)

with concurrent.futures.ThreadPoolExecutor(max_workers=max_worker) as executor:
    # Start the load operations and mark each future with its URL
    future_to_filename = {executor.submit(execute_file, file_name): file_name
                          for file_name in files
                          if file_name.endswith('.py') and
                          (not file_name.startswith("_") or file_name.endswith("_test.py"))}
    for future in concurrent.futures.as_completed(future_to_filename):
        print("Ran ", future_to_filename[future])
