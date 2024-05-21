init -998 python in PuzzleMinigameEngine:
    import store
    plugin_config = {
        "version": "1.24.05.17.2",
        "name": "PuzzleMinigameEngine",
        "order": 0
    }


init -997 python in PuzzleMinigameEngine:

    try:
        from store import CitrusPluginSupport
    except Exception as e:
        raise Exception("[-] This project don't have plugin support. Run in plugins folder `git submodule add https://github.com/Mikan-DS/CitrusPluginCore.git` to add this submodule, or contact Mikan_DS.")
    CitrusPluginSupport.init_plugin(plugin_config)
