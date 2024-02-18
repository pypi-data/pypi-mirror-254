import asyncio
from copy import deepcopy
from datetime import timedelta

import pytest

from commons.caching import ExistingEntry, NonExistentEntry, TimedCache


def test_cache_add(create_timed_cache):
    assert not create_timed_cache.cache

    create_timed_cache.add_entry("key", "value")
    assert create_timed_cache.cache

    with pytest.raises(ExistingEntry):
        create_timed_cache.add_entry("key", "different value")

    create_timed_cache.add_entry("key", "A third value", override=True)


def test_delete_entry(create_timed_cache):
    create_timed_cache.add_entry("key", "value")
    assert "key" in create_timed_cache.cache

    create_timed_cache.delete_entry("key")
    assert "key" not in create_timed_cache.cache

    # Idempotent
    create_timed_cache.delete_entry("key")


def test_get_entry(create_timed_cache):
    create_timed_cache.add_entry("key", "value")
    assert "key" in create_timed_cache.cache

    r_1 = create_timed_cache.get_entry("key")
    assert r_1 == "value"

    with pytest.raises(NonExistentEntry):
        create_timed_cache.get_entry("key_2")


def test_contains(create_timed_cache):
    assert "key" not in create_timed_cache

    create_timed_cache.add_entry("key", "value")

    assert "key" in create_timed_cache


async def test_eviction(create_timed_cache):
    create_timed_cache.add_entry("key", "value", ttl=timedelta(seconds=1))
    assert "key" in create_timed_cache
    assert create_timed_cache.cache
    await asyncio.sleep(1.25)
    assert "key" not in create_timed_cache
    assert not create_timed_cache.cache


async def test_force_clean(create_timed_cache):
    create_timed_cache.add_entry("key", "value", ttl=timedelta(seconds=1))
    create_timed_cache.add_entry(
        "key_2",
        "value",
    )
    assert "key" in create_timed_cache
    assert "key_2" in create_timed_cache

    await asyncio.sleep(1.25)

    create_timed_cache.force_clean()
    assert "key" not in create_timed_cache
    assert "key_2" in create_timed_cache


async def test_ttl_from_last_access():
    with pytest.raises(ValueError):
        TimedCache(ttl_from_last_access=True)

    tc = TimedCache(global_ttl=timedelta(minutes=1), ttl_from_last_access=True)

    tc.add_entry("key", "value")
    r_1 = deepcopy(tc.cache["key"])

    await asyncio.sleep(0.5)

    # no-op to update
    tc.get_entry("key")

    r_2 = tc.cache["key"]
    assert r_1 != r_2
    assert r_1.expiry_time != r_2.expiry_time
