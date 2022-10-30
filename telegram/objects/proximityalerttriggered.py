from .base import BaseObject

class ProximityAlertTriggered(BaseObject):
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    Args:
        traveler (telegram.objects.user.User): User that triggered the alert
        watcher (telegram.objects.user.User): User that set the alert
        distance (int): The distance between the users
    """
    
    
    def __init__(self, traveler, watcher, distance):
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance
