from dataclasses import dataclass
import typing as t


class Observable:

    LIFECYCLE_EVENTS = "__OBSERVABLE_LIFECYCLE__"
    TOPIC_ADDED_EVENT = "topic_added"
    TOPIC_REMOVED_EVENT = "topic_removed"

    @dataclass
    class Listeners:
        id: int
        topic: str
        callback: t.Callable

    listeners: dict[int, Listeners]
    ids_by_topic: dict[str, set]

    _last_id: int

    def __init__(self) -> None:
        self._last_id = -1

        self.listeners = {}
        self.ids_by_topic = {}

        self.add_topic(self.LIFECYCLE_EVENTS)

    def _get_next_id(self):
        self._last_id += 1
        return self._last_id

    def add_topic(self, topic: str) -> bool:
        if topic in self.ids_by_topic:
            return False
        self.ids_by_topic[topic] = set()
        return True

    def remove_topic(self, topic: str) -> bool:
        if topic not in self.ids_by_topic:
            return False
        del self.ids_by_topic[topic]
        return True

    def add_listener(self, topic: str, callback: t.Callable) -> int:
        listener_id = self._get_next_id()
        self.listeners[listener_id] = self.Listeners(listener_id, topic, callback)
        added_new_topic = self.add_topic(topic)
        self.ids_by_topic[topic].add(listener_id)

        if added_new_topic:
            self.notify(
                self.LIFECYCLE_EVENTS,
                {"event_type": self.TOPIC_ADDED_EVENT, "topic": topic},
            )

        return listener_id

    def remove_listener(self, listener_id: int) -> bool:

        def is_empty(_set: set) -> bool:
            return _set == set()

        if not listener_id in self.listeners:
            return False
        topic = self.listeners[listener_id].topic

        if topic not in self.ids_by_topic:
            msg = f"Topic '{topic}' does not exist. Listener {listener_id}"
            raise RuntimeError(msg)

        if listener_id in self.ids_by_topic[topic]:
            self.ids_by_topic[topic].remove(listener_id)
        del self.listeners[listener_id]

        if topic != self.LIFECYCLE_EVENTS and is_empty(self.ids_by_topic[topic]):
            del self.ids_by_topic[topic]
            self.notify(
                self.LIFECYCLE_EVENTS,
                {"event_type": self.TOPIC_REMOVED_EVENT, "topic": topic},
            )
        return True

    def notify(self, topic: str, event: t.Any) -> None:
        if topic not in self.ids_by_topic:
            return
        for listener_id in self.ids_by_topic[topic]:
            self.listeners[listener_id].callback(event)

    def get_state(self) -> dict:
        topics = dict(
            (topic, list(listeners)) for topic, listeners in self.ids_by_topic.items()
        )
        listeners = [
            {"id": listener.id, "topic": listener.topic}
            for listener in self.listeners.values()
        ]
        return {"topics": topics, "listeners": listeners}
