# simple-observable

A simple observer pattern implementation.

### Usage example

```python
from simple_observable import Observable


observable = Observable()


def my_callback(event):
    print(f"Called with {event}")


observable.add_listener("mytopic", my_callback)

observable.notify("mytopic", {"event_details": "hello"})

```

### Topic lifecycle events

The special topic `Observable.LIFECYCLE_EVENTS` can be used to perform an actions when new topics are added and existing ones are removed. 

```python
from simple_observable import Observable


observable = Observable()


def on_lifecycle_event(event):
    if event["event_type"] == observable.TOPIC_ADDED_EVENT:
        topic = event["topic"]
        print(f"topic lifecycle: added '{topic}'")
    if event["event_type"] == observable.TOPIC_REMOVED_EVENT:
        topic = event["topic"]
        print(f"topic lifecycle: removed '{topic}'")


observable.add_listener(observable.LIFECYCLE_EVENTS, on_lifecycle_event)


def my_callback(event):
    print(f"Called with {event}")


# the next line triggers a lifecycle event {"event_type": observable.TOPIC_ADDED_EVENT, "topic": "mytopic"}
listener_id = observable.add_listener("mytopic", my_callback)

observable.notify("mytopic", {"key": "value"})

# and the last line triggers a lifecycle event {"event_type": observable.TOPIC_REMOVED_EVENT, "topic": "mytopic"}
observable.remove_listener(listener_id)


```