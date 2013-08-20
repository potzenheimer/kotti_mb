from kotti.resources import Document
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer


from kotti_mb import _


class LandingPage(Document):
    """This is your content type."""

    # add your columns
    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)

    # change the type info to your needs
    type_info = Document.type_info.copy(
        name=u'LandingPage',
        title=_(u'Landing Page'),
        add_view=u'add_landing_page',
        addable_to=[u'Document'],
    )

    # adjust the __init__ method according to your columns
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
