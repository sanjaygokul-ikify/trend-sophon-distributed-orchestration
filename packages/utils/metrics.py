import time

last_call_time = time.time()
def get_elapsed_time():
    global last_call_time
    current_time = time.time()
    elapsed_time = current_time - last_call_time
    last_call_time = current_time
    return elapsed_time
