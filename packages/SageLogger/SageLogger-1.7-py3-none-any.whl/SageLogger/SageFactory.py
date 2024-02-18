from . import Logger
from typing import Union
from colorama import init

loggers = []

def getLoggerByName(name: str) -> Union[Logger.SageConsoleLogger, Logger.SageRemoteLogger]:
    """
    Returns a logger object by name.
    :param name: The name of the logger to retrieve.
    :type name: str
    :return: The logger object if found, otherwise None.
    :rtype: Logger
    """
    for l in loggers:
        if l.name == name:
            return l
        
    return Logger.SageConsoleLogger(name="NotFoundLogger", savetofile=False, logfile="log")

def create(name: str = "", savetofile: bool = False, logfile: str = "log"):
    """
    Creates a console logger and adds it to the list of loggers.
    :param name: The name of the logger. Default is an empty string.
    :type name: str
    :param savetofile: Whether to save logs to a file. Default is False.
    :type savetofile: bool
    :param logfile: The filename to save logs. Default is "log".
    :type logfile: str
    :return: The created console logger.
    :rtype: Logger
    """
    l = Logger.SageConsoleLogger(name, savetofile, logfile)
    loggers.append(l)
    return l

def create_remote(method, url, headers, body, name: str = "", savetofile: bool = False, logfile: str = "log"):
    """
    Creates a remote logger and adds it to the list of loggers.
    :param method: The HTTP method to use for the remote logger.
    :param url: The URL to send logs to.
    :param headers: The headers to be included in the request.
    :param body: The log payload.
    :param name: The name of the logger. Default is an empty string.
    :type name: str
    :param savetofile: Whether to save logs to a file. Default is False.
    :type savetofile: bool
    :param logfile: The filename to save logs. Default is "log".
    :type logfile: str
    :return: The created remote logger.
    :rtype: Logger
    """
    l = Logger.SageRemoteLogger(method, url, headers, body, name, savetofile, logfile)
    loggers.append(l)
    return l

def create_discord_webhook_remote(url, name: str = "", savetofile: bool = False, logfile: str = "log"):
    """
    Creates a Discord webhook logger and adds it to the list of loggers.
    :param url: The Discord webhook URL to send logs to.
    :param name: The name of the logger. Default is an empty string.
    :type name: str
    :param savetofile: Whether to save logs to a file. Default is False.
    :type savetofile: bool
    :param logfile: The filename to save logs. Default is "log".
    :type logfile: str
    :return: The created Discord webhook logger.
    :rtype: Logger
    """
    l = Logger.SageDiscordWebhookLogger.create(url, name, savetofile, logfile)
    loggers.append(l)
    return l

def create_temporary():
    """
    Creates a temporary logger and adds it to the list of loggers.
    :return: The created temporary logger.
    :rtype: Logger
    """
    l = create(name="temporary", savetofile=False)
    loggers.append(l)
    return l

# A pre-created console logger named "Errors" that doesn't save logs to a file.
errorlogger = create("Errors", False, "log")