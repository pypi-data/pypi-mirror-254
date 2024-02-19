import logging
import multiprocessing
import pickle
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from hyperfunc.config import CPUS, THREADS_PER_CPU
from hyperfunc.core import FUNC_MAPPING, HyperFunc
from hyperfunc.core.mq import task_queue, delay_queue


def get_retry_delay(task: dict, func: HyperFunc) -> float | int:
    retries = task.get("retries") - 1
    retry_delay = func.retry_delay
    retry_backoff = 2 if func.retry_backoff else 1
    return retry_backoff**retries * retry_delay


def should_retry(task: dict, func: HyperFunc):
    return task["retries"] < func.max_retries


def consumer_thread():
    while 1:
        message = task_queue.get()
        task = pickle.loads(message)

        try:
            hyper_func: HyperFunc = FUNC_MAPPING[task["func"]]
        except KeyError:
            logging.error(f"No such function: {task['func']}")
            task_queue.ack(message)
            continue

        try:
            hyper_func.task_call(task)
        except:
            if should_retry(task, hyper_func):
                task["retries"] += 1
                delay_queue.put(pickle.dumps(task), run_at=time.time() + get_retry_delay(task, hyper_func))
        finally:
            task_queue.ack(message)


def consumer_process():
    with ThreadPoolExecutor(max_workers=THREADS_PER_CPU) as pool:
        futures = [pool.submit(consumer_thread) for _ in range(THREADS_PER_CPU)]
        for future in as_completed(futures):
            future.result()  # 获取线程的结果或异常


def delay_process():
    while 1:
        messages = next(delay_queue.get())
        for message in messages:
            task_queue.rput(message)
        delay_queue.ack(messages=messages)
        time.sleep(0.1)


def consume():
    print("Starting ...")
    for func in FUNC_MAPPING.values():
        print("Registered function: ", func)

    task_queue.load_processing()

    processes = []

    for _ in range(CPUS):
        p = multiprocessing.Process(target=consumer_process)
        processes.append(p)
        p.start()

    d_p = multiprocessing.Process(target=delay_process)
    processes.append(d_p)
    d_p.start()

    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("Shutting down ...")
        for p in processes:
            p.terminate()
            p.join()
