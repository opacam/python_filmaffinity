"""Config."""
# -*- coding: utf-8 -*-
from cachetools import LRUCache

cache = LRUCache(maxsize=100)
FIELDS_MOVIE = ['title', 'id']
FIELDS_TYPE = ['title', 'director', 'cast']


FIELDS_PAGE_MOVIES = ['id', 'title', 'rating', 'directors', 'poster']
FIELDS_DETAIL = ['description', 'votes', 'year', 'country', 'duration',
                 'genre', 'awards', 'reviews', 'actors']
FIELDS_PAGE_DETAIL = FIELDS_PAGE_MOVIES + FIELDS_DETAIL
