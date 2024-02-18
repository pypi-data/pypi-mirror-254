from sym.sdk import hook, prefetch, reducer


@hook
def simple_hook():
    return "simple_hook"


@reducer
def simple_reducer():
    return "simple_reducer"


@prefetch("some_field")
def simple_prefetch(event):
    return "simple_prefetch"


class TestReducer:
    def test_all(self):
        assert simple_hook() == "simple_hook"
        assert simple_reducer() == "simple_reducer"
        assert simple_prefetch("event") == "simple_prefetch"
