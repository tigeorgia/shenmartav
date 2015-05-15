# -*- coding: utf-8 -*-

from cms.models import monkeypatch_reverse
import haystack

monkeypatch_reverse()
haystack.autodiscover()
