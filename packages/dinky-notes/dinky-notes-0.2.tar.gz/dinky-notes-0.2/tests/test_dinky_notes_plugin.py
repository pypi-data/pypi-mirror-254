from dinky_notes import DinkyNotesPlugin

def test_dinky_notes_plugin_init():
    plugin = DinkyNotesPlugin('url')
    assert plugin.url == 'url'
