init -998 python in PuzzleMinigameEngine:
    import store
    plugin_config = {
        "version": "0.24.03.30.3",
        "name": "PuzzleMinigameEngine",
        "order": 0
    }


init -997 python in PuzzleMinigameEngine:

    try:
        from store import CitrusPluginSupport
        CitrusPluginSupport.init_plugin(plugin_config)
    except Exception as e:
        raise Exception("[-] This project don't have plugin support. Run in plugins folder `git submodule add https://github.com/Mikan-DS/CitrusPluginCore.git` to add this submodule, or contact Mikan_DS.")


