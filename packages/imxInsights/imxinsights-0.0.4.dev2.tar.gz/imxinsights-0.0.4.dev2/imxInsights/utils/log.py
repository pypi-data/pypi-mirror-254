from loguru import logger

# possible log levels:
#   - TRACE (5): used to record fine-grained information about the program's execution path for diagnostic purposes.
#   - DEBUG (10): used by developers to record messages for debugging purposes.
#   - INFO (20): used to record informational messages that describe the normal operation of the program.
#   - SUCCESS (25): similar to INFO but used to indicate the success of an operation.
#   - WARNING (30): used to indicate an unusual event that may require further investigation.
#   - ERROR (40): used to record error conditions that affected a specific operation.
#   - CRITICAL (50): used to record error conditions that prevent a core function from working.

logger.add("log.log", level=0, catch=True, backtrace=True, diagnose=True)
logger.opt(record=True)
logger.level = 0


# jupyter notebook logging massive and slow logging solution: disable logging, if need log print it.


def run_from_notebook():  # pragma: no cover
    try:
        from IPython import get_ipython

        if "IPKernelApp" not in get_ipython().config:  # pragma: no cover
            return False
    except ImportError:
        return False
    except AttributeError:
        return False
    return True


# remove logger if jupyter notebook
if run_from_notebook():  # pragma: no cover
    logger.remove(0)


# hacky magic print methode
def print_log(from_row=0):  # pragma: no cover
    log_sink_path = logger._core.handlers[1]._sink._file_path
    with open(log_sink_path, "r") as f:
        x = f.readlines()
    print("".join(x[from_row:]))
