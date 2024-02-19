from llm_party.model.session_models import Attendee
from typing import Callable, Any

def can_execute_action(attendee: Attendee, action_method: Callable[..., bool], default: bool = False) -> bool:

    """
    Check if the user has a certain permission by attempting to call the
    specified action method on the user object.

    :param attendee: The attendee object to check the permissions on.
    :param action_method: The method object that checks a specific permission.
    :param default: The default value to return if the method doesn't exist.
    :return: Boolean indicating if the action is permissible.
    """
    # Check if the method exists and is callable
    if callable(getattr(attendee, action_method.__name__, None)):
        # Call the method directly
        return action_method()
    else:
        return default