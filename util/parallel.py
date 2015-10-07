from multiprocessing.pool import ThreadPool
import multiprocessing

def process_map(func, itr, num_process=multiprocessing.cpu_count()):
    pool = multiprocessing.Pool(num_process)
    return pool.map(func, itr)
    
def thread_map(func, itr, num_process=multiprocessing.cpu_count()):
    pool = ThreadPool(num_process)
    return pool.map(func, itr)