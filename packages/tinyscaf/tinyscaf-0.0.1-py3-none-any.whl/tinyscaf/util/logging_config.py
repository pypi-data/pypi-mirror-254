import logging
import sys
from logging.handlers import RotatingFileHandler


import colorama

logger = logging.getLogger(__name__)


def configure_logging(log_format=None, log_level=False, log_location=None) -> None:
    """
    Configures colorama logging, log level output and log location.

    Parameters
    ----------
    log_format
    log_level
    log_location

    Returns
    -------
    None

    """
    # enable cross-platform colored output
    colorama.init()

    # get the root logger and make it verbose
    logger = logging.getLogger()
    if log_level:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # this allows us to set an upper threshold for the log levels since the
    # setLevel method only sets a lower one
    class UpperThresholdFilter(logging.Filter):
        def __init__(self, threshold, *args, **kwargs):
            self._threshold = threshold
            super(UpperThresholdFilter, self).__init__(*args, **kwargs)

        def filter(self, rec):
            return rec.levelno <= self._threshold

    # use colored output and use different colors for different levels
    class ColorFormatter(logging.Formatter):
        def __init__(self, colorfmt, *args, **kwargs):
            self._colorfmt = colorfmt
            super(ColorFormatter, self).__init__(*args, **kwargs)

        def format(self, record):
            if record.levelno == logging.INFO:
                color = colorama.Fore.GREEN
            elif record.levelno == logging.WARNING:
                color = colorama.Fore.YELLOW
            elif record.levelno == logging.ERROR:
                color = colorama.Fore.RED
            elif record.levelno == logging.DEBUG:
                color = colorama.Fore.CYAN
            else:
                color = ""
            self._style._fmt = self._colorfmt.format(color, colorama.Style.RESET_ALL)
            return logging.Formatter.format(self, record)

    # configure formatter
    if not log_format:
        logfmt = "{}%(asctime)s [%(levelname)s] [%(module)s:%(lineno)d] - %(message)s"
    else:
        logfmt = log_format
    formatter = ColorFormatter(logfmt)

    # configure stdout handler
    std_out_handler = logging.StreamHandler(sys.stdout)
    std_out_handler.setLevel(logging.DEBUG)
    std_out_handler.addFilter(UpperThresholdFilter(logging.INFO))
    std_out_handler.setFormatter(formatter)
    logger.addHandler(std_out_handler)

    # configure stderr handler
    std_err_handler = logging.StreamHandler(sys.stderr)
    std_err_handler.setLevel(logging.WARNING)
    std_err_handler.setFormatter(formatter)
    logger.addHandler(std_err_handler)

    if log_location:
        # configure file handler (no colored messages here)
        filehandler = RotatingFileHandler(
            f"{log_location}", maxBytes=1024 * 1024 * 100, backupCount=5
        )
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(logging.Formatter(logfmt.format("", "")))
        logger.addHandler(filehandler)
