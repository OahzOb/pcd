import time
import warnings


def time_this(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f"Func [{func.__name__}] cost {time_end - time_start:6f}s.")
        return result
    return wrapper

def deprecated(version: str = None, reason: str = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            message = f"Func [{func.__name__}] is deprecated. "
            if version:
                message += f"Since version {version}. "
            if reason:
                message += f"Reason: {reason}."
            warnings.warn(message, category=DeprecationWarning, stacklevel=2)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@deprecated(version='0.1', reason='test')
@time_this
def test_time_this(sleep_time: float = 1.0) -> None:
    time.sleep(sleep_time)
    return None


@time_this
def test_time_this_new(num_operations: int = 10000) -> None:
    temp = 0
    for _ in range(num_operations):
        temp += 1
    return None

if __name__ == '__main__':
    test_time_this()