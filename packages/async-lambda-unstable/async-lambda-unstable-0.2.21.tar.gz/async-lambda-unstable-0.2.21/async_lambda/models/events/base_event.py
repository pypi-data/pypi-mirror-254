from typing import Any


class BaseEvent:
    """
    All Async-Lambda Invocation Event types inherit from this.
    """

    _event: dict
    _context: Any

    def __init__(self, event: dict, context: Any):
        self._event = event
        self._context = context
        self._hydrate_event()

    def _hydrate_event(self):
        """
        Overridden in sub-classes to implement event parsing/hydration.
        """
        pass

    def get_raw_event(self):
        """
        Returns the unmodified event object passed to the event handler.
        """
        return self._event

    def get_raw_context(self):
        """
        Returns the unmodified context object passed to the event handler.
        """
        return self._context
