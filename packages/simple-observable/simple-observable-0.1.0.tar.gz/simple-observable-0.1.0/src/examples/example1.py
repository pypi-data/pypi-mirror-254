from simple_observable import Observable


observable = Observable()


def my_callback(event):
    print(f"Called with {event}")


observable.add_listener("mytopic", my_callback)

observable.notify("mytopic", {"event_details": "hello"})
