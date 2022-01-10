from nostr.event import Event


def test_event_id():
    e = Event("1q", "asd", created_at=1641819738)
    assert e.id == "bbe84e5f88993ad461f0ee82f746ed5f1aa023c53187185c54d95561deb2651f"
