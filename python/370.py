# -------------------------------
# Author: Tuan Nguyen
# Date created: 20200518
#!370.py
# -------------------------------
"""
The “active time” of a courier is the time between the pickup and dropoff of a delivery. 
Given a set of data formatted like the following:
```
(delivery id, timestamp, pickup/dropoff)
```

Calculate the total active time in seconds. 
A courier can pick up multiple orders before dropping them off. The timestamp is in unix epoch seconds.

For example, if the input is the following:
```
(1, 1573280047, 'pickup')
(1, 1570320725, 'dropoff')
(2, 1570321092, 'pickup')
(3, 1570321212, 'pickup')
(3, 1570322352, 'dropoff')
(2, 1570323012, 'dropoff')
```

The total active time would be 1260 seconds.
"""


class Delivery:
    def __init__(self):
        self.id = None
        self.pickup_timestamp = None
        self.dropoff_timestamp = None

    def set_id(self, id):
        self.id = id

    def set_pickup(self, pickup_timestamp):
        self.pickup_timestamp = pickup_timestamp

    def set_dropoff(self, dropoff_timestamp):
        self.dropoff_timestamp = dropoff_timestamp

    def active_time(self):
        if self.pickup_timestamp == None:
            raise Exception("Pickup time is null")
        if self.dropoff_timestamp == None:
            raise Exception("Dropoff time is null")
        active_time = self.dropoff_timestamp - self.pickup_timestamp
        if active_time < 0:
            raise Exception("Dropoff time is before pickup time")
        return active_time


def courier_active_time(orders):
    deliveries = create_deliveries(orders)
    active_time = total_active_time_from_deliveries(deliveries)
    return active_time


def create_deliveries(orders):
    deliveries = dict()
    for order in orders:
        id, timestamp, state = order[0], order[1], order[2]
        if state == "pickup":
            d = create_new_delivery(id, timestamp)
            deliveries[id] = d
        else:  # "dropoff"
            d = deliveries.get(id)
            d.set_dropoff(timestamp)
    return deliveries.values()  # list of all complete deliveries


def create_new_delivery(id, pickup_timestamp):
    d = Delivery()
    d.set_id(id)
    d.set_pickup(pickup_timestamp)
    return d


def total_active_time_from_deliveries(deliveries):
    total_active_time = 0
    for delivery in deliveries:
        total_active_time += delivery.active_time()
    return total_active_time


def test1():
    orders = [(3, 1570321212, "pickup"), (3, 1570322352, "dropoff")]
    assert courier_active_time(orders) == 1140


def test2():
    orders = [(2, 1570321092, "pickup"), (2, 1570323012, "dropoff")]
    assert courier_active_time(orders) == 1920


def test3():
    orders = [
        (2, 1570321092, "pickup"),
        (3, 1570321212, "pickup"),
        (3, 1570322352, "dropoff"),
        (2, 1570323012, "dropoff"),
    ]
    assert courier_active_time(orders) == 3060


if __name__ == "__main__":
    test1()
    test2()
    test3()
