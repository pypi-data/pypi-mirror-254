class NoLogPlaceholder(Exception):
    """
    This exception is raised when there is an attempt to use a log placeholder that has not been defined.
    Usage example:
    try:
        # Some code that may raise the NoLogPlaceholder exception
        raise NoLogPlaceholder("Error: Log placeholder 'xyz' is not defined.")
    except NoLogPlaceholder as e:
        print(str(e))  # Output: "Error: Log placeholder 'xyz' is not defined."
    It should be used only in catching Errors
    """
    pass

class NotDiscordWebhook(Exception):
    """
    This exception is raised when there is an attempt to use a non-Discord webhook logger in a Discord webhook context.
    It should be used only in catching Errors
    """
    pass

class UhOhSomeoneTooCurious(Exception):
    """
    This exception is raised when a user is being too curious or attempting unauthorized actions.
    You can consider this an easter egg :)
    """
    pass

class TypeIsntLocked(Exception):
    """
    This exception is raised when you try to unlock an unlocked type.
    """
    pass