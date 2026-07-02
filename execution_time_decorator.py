import time


def execution_timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        elapsed_time = time.perf_counter() - start_time

        print(f"{function.__name__} completed in {elapsed_time:.6f} seconds")

        return result

    return wrapper


@execution_timer
def calculate_average(values):
    return sum(values) / len(values)


average = calculate_average([84, 91, 77, 89, 95])

print(average)