def deep_flatten(maybe_iter):
    try:
        for k in maybe_iter:
            if isinstance(k, str):
                yield k
            else:
                yield from deep_flatten(k)
    except TypeError:
        yield maybe_iter