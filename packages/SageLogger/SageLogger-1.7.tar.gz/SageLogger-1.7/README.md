# SageLogger: Python Logger Package

SageLogger is a versatile Python logger package that allows you to create loggers with both remote and local capabilities. The core module, "SageFactory.py," facilitates the creation of loggers with options for SageRemoteLogger (remote) and SageLogger (local). When using SageLogger, you have the flexibility to choose from 7 predefined log types for local logging: DEFAULT, POSITIVE, ONHOLD, NEGATIVE, FROZEN, INFORMATION, and MILD_EXCEPTION. Additionally, you can easily create custom log types to suit your specific needs using the `SageLogger.DynamicType` class.

## Features

### Local Logging Options
SageLogger offers 9 built-in log types for local logging:

1. DEFAULT: The default log type.
2. POSITIVE: For positive events and actions.
3. ONHOLD: To indicate events that are on hold or waiting for further action.
4. NEGATIVE: For negative events or errors.
5. FROZEN: To represent frozen states or events.
6. INFORMATION: For general information logging.
7. MILD_EXCEPTION: To log minor exceptions or errors.
8. DEBUG: To troubleshoot some things. (disabled by default)
9. .................................... (shh secret)

### Custom Local Log Types
Apart from the predefined log types, you can create custom log types using the `SageLogger.DynamicType.fromChar` method or the `SageLogger.DynamicType.fromColoredChar` method for colored logs.

### Remote Logging
SageLogger enables remote logging capabilities through the SageRemoteLogger class. You can load custom APIs for remote logging, and it also provides built-in support for Discord webhook integration.

## Example Code

To create a local logger with SageLogger, you can use the following code:

```python
from SageLogger import SageFactory, Logger
import colorama

sagelogs = SageFactory.create("tester", True)

sagelogs.log("Checking all types")

for x in sagelogs.Type.__iter__():
    sagelogs.log("Hello World! It's " + x.name, type=x)

sagelogs.log("It's dynamic!", type=sagelogs.DynamicType.fromChar(sagelogs, "XD"))

sagelogs.log("Doing the test again but with changed borders")

sagelogs.customization.set_border_style(colorama.Fore.GREEN, "()")

for x in sagelogs.Type.__iter__():
    sagelogs.log("Hello World! It's " + x.name, type=x)

sagelogs.log("It's dynamic!", type=sagelogs.DynamicType.fromColoredChar(sagelogs, colorama.Fore.LIGHTYELLOW_EX, "X"))

sagelogs.log("I'm ID 21", type=sagelogs.DynamicType.fromColoredChar(sagelogs, colorama.Fore.LIGHTYELLOW_EX, "N"), id=20)

sagelogs.log("I have time", type=sagelogs.DynamicType.fromColoredChar(sagelogs, colorama.Fore.LIGHTYELLOW_EX, "N"), date=True)
sagelogs.log("I have date", type=sagelogs.DynamicType.fromColoredChar(sagelogs, colorama.Fore.LIGHTYELLOW_EX, "N"), time=True)
sagelogs.log("I have time and date", type=sagelogs.DynamicType.fromColoredChar(sagelogs, colorama.Fore.LIGHTYELLOW_EX, "N"), time=True, date=True)
sagelogs.log("I have time and date", type=sagelogs.DynamicType.fromColoredChar(sagelogs, colorama.Fore.LIGHTYELLOW_EX, "N"), time=True, date=True, timecolor=colorama.Fore.YELLOW, datecolor=colorama.Fore.RED)

sageremotelog = SageFactory.create_discord_webhook_remote("<webhook>", savetofile=True)

sagelogs.log("Sent to discord", type=sagelogs.Type.INFORMATION)
sageremotelog.log("I sent to discord!")
```

IntelliSense should show you around!

### Big issue:
In log files it writes color codes.

### Version naming:
First number: Which major release
Second number: Which minor release
Third number: Which revision
No third number indicates that there was no revisions/the version will stay as it is.
If you catch a release that contains the third number, then you should remove and upgrade to the 2 number release - the 3 number are considered obsolete.

### Changelogs:
v1.0 - Initial version
v1.1 - Skipped as of a fail in version naming :(
v1.2 - Skipped as of a fail in version naming :(
v1.3 - Logger arrays in SageFactory and getLoggerByName(name), 3 more loggers (1 secret shh). More functions of enabling, changed class name from SageLogger.Logger.SageLogger to SageLogger.Logger.SageConsoleLogger
v1.4 - Forced release because I forgot to change sample code from README.md
v1.5 - Fixed logger.ask() method so it returns String object (which is the users answer)
v1.6 - Fixed ANSI coloring, removed auto name showing

# Common errors:
No colors just ANSI symbols? Use logger.fix_ansi()

# -------------------------
# SageLogger Documentation:
# -------------------------
#
# SageFactory.py

`SageFactory.py` is a Python module that provides logging functionalities through the `Logger` module.

## Functions

### getLoggerByName(name: str) -> Logger
- Description: Returns a logger object by name.
- Parameters:
  - `name` (str): The name of the logger to retrieve.
- Returns:
  - (Logger): The logger object if found, otherwise `None`.

### create(name: str = "", savetofile: bool = False, logfile: str = "log") -> Logger
- Description: Creates a console logger and adds it to the list of loggers.
- Parameters:
  - `name` (str, optional): The name of the logger. Default is an empty string.
  - `savetofile` (bool, optional): Whether to save logs to a file. Default is `False`.
  - `logfile` (str, optional): The filename to save logs. Default is "log".
- Returns:
  - (Logger): The created console logger.

### create_remote(method, url, headers, body, name: str = "", savetofile: bool = False, logfile: str = "log") -> Logger
- Description: Creates a remote logger and adds it to the list of loggers.
- Parameters:
  - `method`: The HTTP method to use for the remote logger.
  - `url`: The URL to send logs to.
  - `headers`: The headers to be included in the request.
  - `body`: The log payload.
  - `name` (str, optional): The name of the logger. Default is an empty string.
  - `savetofile` (bool, optional): Whether to save logs to a file. Default is `False`.
  - `logfile` (str, optional): The filename to save logs. Default is "log".
- Returns:
  - (Logger): The created remote logger.

### create_discord_webhook_remote(url, name: str = "", savetofile: bool = False, logfile: str = "log") -> Logger
- Description: Creates a Discord webhook logger and adds it to the list of loggers.
- Parameters:
  - `url`: The Discord webhook URL to send logs to.
  - `name` (str, optional): The name of the logger. Default is an empty string.
  - `savetofile` (bool, optional): Whether to save logs to a file. Default is `False`.
  - `logfile` (str, optional): The filename to save logs. Default is "log".
- Returns:
  - (Logger): The created Discord webhook logger.

### create_temporary() -> Logger
- Description: Creates a temporary logger and adds it to the list of loggers.
- Returns:
  - (Logger): The created temporary logger.

## Usage

Example usage:
```python
from SageFactory import create

# Create a console logger with name "MyLogger" and save logs to file "mylog.txt"
console_logger = create(name="MyLogger", savetofile=True, logfile="mylog.txt")

# Create a remote logger with custom HTTP method, URL, headers, and log payload
remote_logger = create_remote(method="POST", url="https://example.com/log", headers={"Authorization": "Bearer XXX"}, body={"message": "Log message"})

# Create a Discord webhook logger with the webhook URL
discord_logger = create_discord_webhook_remote(url="https://discord.com/api/webhooks/XXX")

# Create a temporary logger with default settings
temporary_logger = create_temporary()
```

# SageException.py

`SageException.py` is a Python module that defines custom exception classes used in the SageFactory module.

## Custom Exception Classes

### NoLogPlaceholder
- Description: This exception is raised when there is an attempt to use a log placeholder that has not been defined.

## NotDiscordWebhook
- Description: This exception is raised when there is an attempt to use a non-Discord webhook logger in a Discord webhook context.

## UhOhSomeoneTooCurious
- Description: This exception is raised when a user is being too curious or attempting unauthorized actions.

This file should be used to catch errors.

# Logger.py

`Logger.py` is a Python module that provides logging functionalities through custom logger classes.

## Classes

### SageConsoleLogger
- Description: Provides console logging capabilities.
- Methods:
  - `is_enabled_type(type)`: Checks if the given log type is enabled.
  - `log(message, type = Type.DEFAULT.value, color = colorama.Fore.RESET, id = -2137, date = False, time = False, datecolor = colorama.Fore.RESET, timecolor = colorama.Fore.RESET, showname = True, ending = "\n")`: Logs a message with the specified log type and customization options.
  - `ask(message, type = Type.DEFAULT.value, color = colorama.Fore.RESET, answercolor = colorama.Fore.RESET, id = -2137, date = False, time = False, datecolor = colorama.Fore.RESET, timecolor = colorama.Fore.RESET)`: Asks a question with the specified log type and customization options.

### SageRemoteLogger (Based on SageConsoleLogger)
- Description: Provides remote logging capabilities using HTTP requests.
- Methods:
  - `log(message, print_on_console = False, ending = "\n")`: Logs a message and sends it remotely using an HTTP request.

### SageDiscordWebhookLogger
- Description: Creates a Discord webhook logger using SageRemoteLogger.
- Methods:
  - `create(url, name = "", savetofile = False, logfile = "log")`: Creates a Discord webhook logger.

### SageConsoleLogger.customization
- Description: Customizes log message appearance.
- Methods:
  - `set_border_style(border_colorama, borders)`: Sets the border style for log messages.
  - `setup_custom_border(cos)`: Sets up a custom border for the log message.

### SageConsoleLogger.Type
- Description: Enumerates different log types with customizations.
- Properties: `DEFAULT`, `POSITIVE`, `ONHOLD`, `NEGATIVE`, `FROZEN`, `INFORMATION`, `MILD_EXCEPTION`, `DEBUG`, `AMONGUS`, `SAGE_LOGGER_DEBUG`
- Methods:
  - `toggle_type(type)`: Toggles the given log type on/off.
  - `enable_type(type)`: Enables the given log type.
  - `disable_type(type)`: Disables the given log type.

### SageConsoleLogger.Type.XYZ (PartType)
- Description: Defines a part of a log type with customization options.
- Properties: `name`, `Id`, `customization`, `value`, `enabled`, `lockedup`

### DynamicType
- Description: Represents dynamic log types.
- Methods:
  - `fromChar(logger, char)`: Creates a dynamic log type from a character.
  - `fromColoredChar(logger, color, char)`: Creates a dynamic log type from a colored character.
  - `custom(prefix)`: Creates a custom dynamic log type.

## Usage

Example usage (SageConsoleLogger):
```python
from Logger import SageConsoleLogger

# Create a console logger with name "MyLogger" and save logs to file "mylog.txt"
console_logger = SageConsoleLogger(name="MyLogger", savetofile=True, logfile="mylog.txt")

# Log a message with the default log type
console_logger.log("This is a log message.")

# Enable the "POSITIVE" log type and log a message with that type
console_logger.enable_type(SageConsoleLogger.Type.POSITIVE)
console_logger.log("This is a positive message.", type=SageConsoleLogger.Type.POSITIVE.value, color=colorama.Fore.GREEN)

# Disable the "DEFAULT" log type and log a message with that type
console_logger.disable_type(SageConsoleLogger.Type.DEFAULT)
console_logger.log("This message will not be displayed.", type=SageConsoleLogger.Type.DEFAULT.value)
```

Example usage (SageRemoteLogger):
```python
from Logger import SageRemoteLogger

# Create a remote logger with custom HTTP method, URL, headers, and log payload
remote_logger = SageRemoteLogger("POST", "https://example.com/log", {"Authorization": "Bearer XXX"}, {"message": "Log message"})

# Log a message and send it remotely
remote_logger.log("This is a remote log message.")
```

Example usage (SageDiscordWebhookLogger):
```python
from Logger import SageDiscordWebhookLogger

# Create a Discord webhook logger with the webhook URL
discord_logger = SageDiscordWebhookLogger.create(url="https://discord.com/api/webhooks/XXX")

# Log a message and send it to the Discord webhook
discord_logger.log("This is a log message sent via Discord webhook.")
```

## Note

Make sure to import the necessary modules (colorama, datetime, requests, etc.) before using the logger classes.
For Logger.py the docs in the file aren't available.