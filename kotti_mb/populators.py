from kotti.resources import get_root

def populate():
    site = get_root()
    site.default_view = 'front-page'
