from dinky_whatson import DinkyWhatsOnPlugin

def test_dinky_whatson_plugin_init():
    plugin = DinkyWhatsOnPlugin('suburb')
    assert plugin.suburb == 'suburb'
