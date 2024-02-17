import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Timed out!")

def input_with_timeout(prompt, default=None, timeout=5):
    # Set up a signal handler for the alarm signal
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)  # Set the alarm to trigger after timeout

    try:
        user_input = input(prompt)
        return user_input
    except TimeoutError:
        print("Timeout reached. Default value will be used.")
        return default
    finally:
        # Reset the alarm to 0 to cancel any pending alarms
        signal.alarm(0)

