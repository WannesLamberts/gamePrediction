import time
import calendar

def convert_to_epoch_time(time_string):
    """
    Converts a date-time string to epoch time (seconds since Unix epoch).

    Parameters:
    -----------
    time_string : str
        A date-time string representing the time to be converted. The string must be in the format '%Y-%m-%d %H:%M:%S'

    Returns:
    --------
    int
        The corresponding epoch time in seconds. This represents the number of seconds since the Unix epoch (January 1, 1970).

    """
    # Convert the time string to a struct_time object using strptime
    time_struct = time.strptime(time_string, '%Y-%m-%d %H:%M:%S')

    # Convert the struct_time object to epoch time using mktime
    epoch_time = calendar.timegm(time_struct)

    return epoch_time
