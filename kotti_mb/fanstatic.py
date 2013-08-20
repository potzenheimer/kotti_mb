from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

library = Library("kotti_mb", "static")
kotti_mb_css = Resource(library, "css/styles.css")
kotti_mb_js_holder = Resource(library, "assets/js/holder.js")
kotti_mb_js = Resource(library, "assets/js/bootstrap.min.js")
kotti_mb_group = Group([kotti_mb_css])
