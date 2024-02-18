def test_import():
    from cacheline._mux import create_mux
    from cacheline._web_console import start_web_console

    return create_mux, start_web_console
