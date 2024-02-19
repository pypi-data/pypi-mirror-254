class AttendeeRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, attendee_class):
        self._registry[attendee_class.__name__] = attendee_class

    def get(self, attendee_type):
        return self._registry.get(attendee_type)

# Create a global instance of the registry
attendee_registry = AttendeeRegistry()