import asyncio


async def maybe_coro(func, *args, **kwargs):
    """Call the given func, awaiting if required."""
    if asyncio.iscoroutinefunction(func):
        return await func(*args, **kwargs)

    return func(*args, **kwargs)
