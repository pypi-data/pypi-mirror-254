import math
import logging


def round_half_up(n: float,
                  decimals: int = 0) -> float:
    """This function rounds to the nearest integer number (e.g 2.4 becomes 2.0 and 2.6 becomes 3);
     in case of tie, it rounds up (e.g. 1.5 becomes 2.0 and not 1.0)
    Args:
        n: number to round
        decimals: number of decimal figures that we want to keep; defaults to zero
    Returns:
        rounded_number: input number rounded with the desired decimals
    """
    multiplier = 10 ** decimals

    rounded_number = math.floor(n * multiplier + 0.5) / multiplier

    return rounded_number


def print_running_time(start_time: float,
                       end_time: float,
                       process_name: str) -> None:
    """This function takes as input the start and the end time of a process and prints to console the time elapsed for this process
    Args:
        start_time: instant when the timer was started
        end_time: instant when the timer was stopped
        process_name: name of the process
    """
    sentence = str(process_name)  # convert to string whatever the user inputs as third argument
    temp = end_time - start_time  # compute time difference
    hours = temp // 3600  # compute hours
    temp = temp - 3600 * hours  # if hours is not zero, remove equivalent amount of seconds
    minutes = temp // 60  # compute minutes
    seconds = temp - 60 * minutes  # compute minutes
    print(f'\n{sentence} time: {hours:.0f} hh {minutes:.0f} mm {seconds:.0f} ss')


def print_running_time_with_logger(start_time: float,
                                   end_time: float,
                                   process_name: str,
                                   logger: logging.Logger) -> None:
    """This function takes as input the start and the end time of a process and prints to console the time elapsed for this process
    Args:
        start_time: instant when the timer was started
        end_time: instant when the timer was stopped
        process_name: name of the process
        logger: logger object
    """
    sentence = str(process_name)  # convert to string whatever the user inputs as third argument
    temp = end_time - start_time  # compute time difference
    hours = temp // 3600  # compute hours
    temp = temp - 3600 * hours  # if hours is not zero, remove equivalent amount of seconds
    minutes = temp // 60  # compute minutes
    seconds = temp - 60 * minutes  # compute minutes
    logger.info(f'\n{sentence} time: {hours:.0f} hh {minutes:.0f} mm {seconds:.0f} ss')
