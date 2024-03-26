init -998 python in PuzzleMinigameEngine:
    import store
    plugin_config = {
        "version": "0.24.03.26.0",
        "name": "PuzzleMinigameEngine",
        "order": 0
    }


init -997 python in PuzzleMinigameEngine:

    try:
        from store import CitrusPluginSupport
        CitrusPluginSupport.init_plugin(plugin_config)
    except Exception as e:
        raise Exception("[-] This project don't have plugin support. Contact Mikan_DS.")

