from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_mb')


def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_mb.views'
    settings['kotti.available_types'] += ' kotti_mb.resources.ContentType'
    settings['kotti.fanstatic.view_needed'] += ' kotti_mb.fanstatic.kotti_mb_group'
