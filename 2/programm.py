import random
import string
import multiprocessing
import time

def generate_random_text(length=1000):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for _ in range(length))

def create_text_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def create_text_files_in_multiprocesses(num_processes, num_files_per_process):
    start = time.time()

    def worker(process_id):
        for i in range(num_files_per_process):
            text = generate_random_text()
            filename = f'file_process_{process_id}_{i}.txt'
            create_text_file(filename, text)

    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end = time.time()
    return end - start

if __name__ == "__main__":
    num_files = 100
    num_processes = 3
    num_files_per_process = num_files // num_processes

    time_multiprocesses = create_text_files_in_multiprocesses(num_processes, num_files_per_process)
    print(f"Time taken in {num_processes} processes: {time_multiprocesses} seconds")
