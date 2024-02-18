import colorama
import datetime
import requests
from typing import Union
from enum import Enum
import os
from . import SageException, SageFactory
from colorama import init

thislogger = None

class DynamicType:
    @staticmethod
    def fromChar(logger, char) -> tuple[int, str, bool]:
        #if len(char) != 1:
            #MildError.throw(logger, "sagelogs.errors.TooLongChars", "Char in DynamicType is only allowed to have one character! If you need more characters, use \"custom\" method")
        return (-1, logger.customization.setup_custom_border(char[0]), True)
    
    @staticmethod
    def fromColoredChar(logger, color, char) -> tuple[int, str, bool]:
        #if len(char) != 1:
            #MildError.throw(logger, "sagelogs.errors.TooLongChars", "Char in DynamicType is only allowed to have one character! If you need more characters, use \"custom\" method")
        return (-1, logger.customization.setup_custom_border(color + char[0]), True)
    
    @staticmethod
    def custom(prefix) -> tuple[int, str]:
        return (-1, prefix)

class xxPartType:
    name : str = ""
    Id : int = 0
    customization : str = ""
    value : tuple[int, str, bool] = (-2, "", False)
    enabled = False
    lockedup = False
    def __init__(self, name, Id, customization, enabled, lockedup : bool = False) -> None:
        self.name = name
        self.Id = Id
        self.customization = customization
        self.value = (self.Id, self.customization, self.enabled)
        self.enabled = enabled
        self.lockedup = lockedup

class xxType:
    DEFAULT : xxPartType = xxPartType("DEFAULT", -2, "", True)
    POSITIVE : xxPartType = xxPartType("POSITIVE", -2, "", True)
    ONHOLD : xxPartType = xxPartType("ONHOLD", -2, "", True)
    NEGATIVE : xxPartType = xxPartType("NEGATIVE", -2, "", True)
    FROZEN : xxPartType = xxPartType("FROZEN", -2, "", True)
    INFORMATION : xxPartType = xxPartType("INFORMATION", -2, "", True)
    MILD_EXCEPTION : xxPartType = xxPartType("MILD_EXCEPTION", -2, "", True)
    DEBUG : xxPartType = xxPartType("DEBUG", -2, "", False)
    AMONGUS : xxPartType = xxPartType("AMONGUS", -2, "", True)
    SAGE_LOGGER_DEBUG : xxPartType = xxPartType("SAGE_LOGGER_DEBUG", -2, "", True)
    def refresh(self, customization):
        self.DEFAULT = xxPartType("DEFAULT", 0, "", self.DEFAULT.enabled)
        self.POSITIVE = xxPartType("POSITIVE", 1, customization.setup_custom_border(colorama.Fore.GREEN + "+"), self.POSITIVE.enabled)
        self.ONHOLD = xxPartType("ONHOLD", 2, customization.setup_custom_border(colorama.Fore.YELLOW + "/"), self.ONHOLD.enabled)
        self.NEGATIVE = xxPartType("NEGATIVE", 3, customization.setup_custom_border(colorama.Fore.RED + "-"), self.NEGATIVE.enabled)
        self.FROZEN = xxPartType("FROZEN", 4, customization.setup_custom_border(colorama.Fore.LIGHTBLUE_EX + "#"), self.FROZEN.enabled)
        self.INFORMATION = xxPartType("INFORMATION", 5, customization.setup_custom_border(colorama.Fore.CYAN + "i"), self.INFORMATION.enabled)
        self.MILD_EXCEPTION = xxPartType("MILD_EXCEPTION", 6, customization.setup_custom_border(colorama.Fore.LIGHTRED_EX + "X"), self.MILD_EXCEPTION.enabled)
        self.DEBUG = xxPartType("DEBUG", 7, customization.setup_custom_border(colorama.Fore.LIGHTMAGENTA_EX + "*"), self.DEBUG.enabled)
        self.AMONGUS = xxPartType("AMONGUS", 8, customization.setup_custom_border(colorama.Fore.RED + "ඞ"), self.AMONGUS.enabled)
        self.SAGE_LOGGER_DEBUG = xxPartType("SAGE_LOGGER_DEBUG", 9, customization.setup_custom_border(colorama.Fore.LIGHTGREEN_EX + "S" + colorama.Fore.GREEN + "L" + colorama.Fore.LIGHTMAGENTA_EX + "D"), self.SAGE_LOGGER_DEBUG.enabled and not self.SAGE_LOGGER_DEBUG.lockedup)
    
    def loggers_in_array(self):
        return [self.DEFAULT, self.POSITIVE, self.ONHOLD, self.NEGATIVE, self.FROZEN, self.INFORMATION, self.MILD_EXCEPTION, self.DEBUG, self.AMONGUS, self.SAGE_LOGGER_DEBUG]
    
    def __iter__(self):
        return self.loggers_in_array()
    
    def is_enabled_type(self, type):
        return self.loggers_in_array()[type.Id].enabled
    
    def toggle_type(self, type):
        if (type.lockedup):
            yield SageException.UhOhSomeoneTooCurious()
        self.loggers_in_array()[type.Id].enabled = not self.loggers_in_array()[type.Id].enabled
        
    def enable_type(self, type):
        if (self.loggers_in_array()[type.Id].lockedup):
            yield SageException.UhOhSomeoneTooCurious()
        self.loggers_in_array()[type.Id].enabled = True
        
    def disable_type(self, type):
        self.loggers_in_array()[type.Id].enabled = False
        
    def unlock_type_not_recommended_please_leave_it_alone_it_will_spam(self, type):
        customization = xxCustomization(None)
        customization.bordcol = colorama.Back.RED + colorama.Fore.WHITE
        SageFactory.create(name="SageLoggerImportant").log("Unlocked, it isn't recommended, remember. This message cannot be turned off." + colorama.Back.RESET, type=xxPartType("IMPORTANT_HARD_CODED", 1, customization.setup_custom_border(colorama.Fore.LIGHTRED_EX + "!"), True))
        self.loggers_in_array()[type.Id].lockedup = False
class MildError:
    @staticmethod
    def throw(logger, name, args):
        logger.log(f"Mild {name} - {args}, you don't need to catch it, but you may fix it ;)", type=SageConsoleLogger.Type.MILD_EXCEPTION)
        
class xxCustomization:
    bordcol = colorama.Fore.LIGHTBLACK_EX
    borders = "[]"
    logger = None
    
    def __init__(self, logger):
        self.logger = logger

    def set_border_style(self, border_colorama, borders):
        self.bordcol = border_colorama
        if len(borders) != 2:
            MildError.throw(self.logger, "sagelogs.errors.TooLongChars", "Too much characters in border styling (max 2)")
        self.borders = borders
        self.logger.Type.refresh(self) # type: ignore

    def setup_custom_border(self, cos):
        return self.bordcol + self.borders[0] + colorama.Fore.RESET + cos + self.bordcol + self.borders[1] + " "
    
class SageConsoleLogger:
    customization : xxCustomization = None # type: ignore
    DynamicType = DynamicType()
    
    name = ""
    logfile = ""
    savetofile = True
    Type = xxType()

    def fix_ansi(self):
        init()

    def __init__(self, name : str = "", savetofile : bool = False, logfile : str = "log"):
        global thislogger
        if thislogger == None:
            thislogger = self
        self.customization = xxCustomization(logger=thislogger)
        self.Type.refresh(customization=self.customization)
        self.name = name
        self.logfile = logfile
        self.savetofile = savetofile
        if savetofile:
            with open(self.name + "." + self.logfile, "a") as wr:
                wr.write(("-" * 16) + " " + datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + " " + ("-" * 16) + "\n")
                wr.close()
    
    def log(self, message : str, type : Union[tuple[int, str, bool], xxPartType] = Type.DEFAULT.value, color = colorama.Fore.RESET, id : int = -2137, date : bool = False, time : bool = False, datecolor : str = colorama.Fore.RESET, timecolor : str = colorama.Fore.RESET, showname : bool = False, ending : str = "\n"):
        typefinish = None
        if(isinstance(type, xxPartType)):
            typefinish = (type.Id, type.customization, type.enabled)
        else:
            typefinish = type
        if not typefinish[2]:
            return
        t = ""
        if date or time:
            t = self.customization.setup_custom_border(datetime.datetime.now().strftime((datecolor + "%d/%m/%Y" if date else "") + colorama.Fore.RESET + (", " if date and time else "") + (timecolor + "%H:%M:%S" if time else "")))
        x = t + (self.customization.setup_custom_border(str(id)) if id != -2137 else "") + typefinish[1] + color + message
        c = (self.customization.setup_custom_border(self.name) + " " if showname else "")
        x = c + x
        print(x, end=ending)
        if self.savetofile:
            with open(self.name + "." + self.logfile, "a") as wr:
                wr.write(x.replace("ඞ", "AMONGUS") + ending)
                wr.close()
                
    def ask(self, message : str, type : Union[tuple[int, str, bool], xxPartType] = Type.DEFAULT.value, color = colorama.Fore.RESET, answercolor = colorama.Fore.RESET, id : int = -2137, date : bool = False, time : bool = False, datecolor : str = colorama.Fore.RESET, timecolor : str = colorama.Fore.RESET) -> str:
        typefinish = None
        if(isinstance(type, xxPartType)):
            typefinish = (type.Id, type.customization, type.enabled)
        else:
            typefinish = type
        t = ""
        if date or time:
            t = self.customization.setup_custom_border(datetime.datetime.now().strftime((datecolor + "%d/%m/%Y" if date else "") + (", " if date and time else "") + (timecolor + "%H:%M:%S" if time else "")))
        x = t + (self.customization.setup_custom_border(str(id)) if id != -2137 else "") + typefinish[1] + color + message + answercolor
        ans = input(x)
        if self.savetofile:
            with open(self.name + "." + self.logfile, "a") as wr:
                wr.write(x.replace("ඞ", "AMONGUS") + ">" + ans + "\n")
                wr.close()
        return ans

class RemoteWhereLog(Enum):
    NOWHERE = 0
    HEADERS = 1
    BODY = 2

class SageRemoteLogger(SageConsoleLogger):
    @staticmethod
    def search_for_placeholder(headers, body) -> RemoteWhereLog:
        for h in headers.keys():
            if len(headers[h].split("%LOG%")) != 1:
                return RemoteWhereLog.HEADERS
        for h in body.keys():
            if len(body[h].split("%LOG%")) != 1:
                return RemoteWhereLog.BODY
        return RemoteWhereLog.NOWHERE
    
    @staticmethod
    def replace_placeholder(message, whoami, rwl, headers, body):
        if rwl == RemoteWhereLog.HEADERS and whoami == RemoteWhereLog.HEADERS:
            for h in headers.keys():
                if len(headers[h].split("%LOG%")) != 1:
                    headers[h] = headers[h].replace("%LOG%", message)
            return headers
        elif rwl == RemoteWhereLog.HEADERS and whoami == RemoteWhereLog.BODY:
            return body
        if rwl == RemoteWhereLog.BODY and whoami == RemoteWhereLog.BODY:
            for h in body.keys():
                if len(body[h].split("%LOG%")) != 1:
                    body[h] = body[h].replace("%LOG%", message)
            return body
        elif rwl == RemoteWhereLog.BODY and whoami == RemoteWhereLog.HEADERS:
            return headers
    
    method = ""
    url = ""
    headers = {}
    body = {}
    remote = RemoteWhereLog.NOWHERE
    
    name = ""
    logfile = ""
    savetofile = ""
    def __init__(self, method, url, headers, body, name: str = "", savetofile: bool = False, logfile: str = "log"):
        SageFactory.errorlogger.log("Initializing remote logger...", type=SageConsoleLogger.Type.SAGE_LOGGER_DEBUG)
        global thislogger
        if thislogger is None:
            thislogger = self
        self.name = "remote" + ("-" if name != "" else "") + name
        self.logfile = logfile
        self.savetofile = savetofile
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body
        SageFactory.errorlogger.log("Searching for placeholder %LOG%", type=SageConsoleLogger.Type.SAGE_LOGGER_DEBUG)
        self.remote = SageRemoteLogger.search_for_placeholder(headers, body)
        if self.remote == RemoteWhereLog.NOWHERE:
            raise SageException.NoLogPlaceholder("Remember to somewhere put %LOG%, maybe in the body?")

        if savetofile:
            with open(self.name + "." + self.logfile, "a") as wr:
                wr.write(("-" * 16) + " " + datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + " " + ("-" * 16) + "\n")
                wr.close()
    
    def log(self, message : str, print_on_console : bool = False, ending : str = "\n"):
        if print_on_console:
            print(message, end=ending)
        
        a = requests.request(self.method, self.url, json=SageRemoteLogger.replace_placeholder(message, RemoteWhereLog.BODY, self.remote, self.headers, self.body), headers=SageRemoteLogger.replace_placeholder(message, RemoteWhereLog.HEADERS, self.remote, self.headers, self.body))
        SageFactory.errorlogger.log(a.text + " - " + str(a.status_code), type=SageConsoleLogger.Type.SAGE_LOGGER_DEBUG)
        if self.savetofile:
            with open(self.name + "." + self.logfile, "a") as wr:
                wr.write("(" + str(a.status_code) + ") " + message + ending)
                wr.write(a.text + ending)
                wr.close()
                
    def ask(self, its_unsupported_sadly):
        i = its_unsupported_sadly
        return i
    
class SageDiscordWebhookLogger:
    @staticmethod
    def create(url, name : str = "", savetofile : bool = False, logfile : str = "log") -> SageRemoteLogger:
        if len(url.split("discord.com")) >= 2 and len(url.split("webhook")) >= 2:
            esc = "\\"
            return SageRemoteLogger("POST", url, {"Content-Type": "application/json"},
                                    {
                                        "content": "%LOG%",
                                        "username": f"Sage Logger - {os.getcwd().split(esc)[-1]}"
                                    }, name, savetofile, logfile)
        else:
            MildError.throw(SageFactory.create_temporary(), "NotDiscordWebhook", "This url isn't a discord webhook, maybe try SageFactory.create_remote method")
            return SageRemoteLogger("", "", {"log":"%LOG%"}, {})