# -*- coding: utf-8 -*-

"""
Resources common
"""
__docformat__ = 'epytext en'


from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource, Resource
from tastypie.throttle import CacheThrottle


ALLOWED_METHODS =[ 'get' ]
CACHE = SimpleCache()
THROTTLE = CacheThrottle(throttle_at=150, timeframe=3600)
DEFAULT_FORMAT = 'application/json'



class CommonModelResource (ModelResource):
    class Meta:
        allowed_methods = ALLOWED_METHODS
        cache = CACHE
        throttle = THROTTLE
        default_format = DEFAULT_FORMAT



class CommonResource (Resource):
    class Meta:
        allowed_methods = ALLOWED_METHODS
        cache = CACHE
        throttle = THROTTLE
        default_format = DEFAULT_FORMAT
