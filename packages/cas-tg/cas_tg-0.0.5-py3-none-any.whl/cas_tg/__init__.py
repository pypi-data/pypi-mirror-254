import requests

def check(id: str|int) -> bool:
    """
    Check if a user banned by CAS (Combot Anti-Spam System).

    Args:
    id (str | int): The user ID to be checked.

    Returns:
    bool: True if the user is banned or False if the user is not banned.
    """
    r = requests.get(f"https://api.cas.chat/check?user_id={id}").json()
    return not r["ok"]

def get_messages(id) -> dict[str, list, str]:
    """
    Check information about user.
    
    Args:
        id (str | int): The user ID to be checked.
        
    Returns:
        Returns the number of spam messages, messages, and the time of the ban. If there is no user in ban, returns None.
    """
    r = requests.get(f"https://api.cas.chat/messages?check={id}").json()
    if check(id):
        return r["result"]
