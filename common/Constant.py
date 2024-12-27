from typing import Dict
from enum import Enum

class ResponseStatus(Enum):
    """Enum for API response status"""
    SUCCESS = "success"
    ERROR = "error"
    NO_DATA = "no_data"


class ApiSite(Enum):
    """Enum for Api site name"""
    EZTV = "EZTV"
    YTS = "YTS"

class ApiSiteEndpoints(Dict):
    """Dict for Api endpoints"""
    endpoints = {
        "eztv" : "api/get-torrents",
        "yts" : "api/v2/list_movies.json"
    }

class ScraperEndpoints(Dict):
    x1337 = {
        "prefix" : "popular",
        "delimiter" : "-",
        "categories": [
            "anime",
            "music",
            "games",
            "tv",
            "apps",
            "documentaries",
            "other",
            "xxx",
            "movies",
        ]
    }

    torlock = {
        "suffix" : "html",
        "delimiter" : ".",
        "categories": [
            "movies",
            "television",
            "games",
            "music",
            "software",
            "anime",
            "ebooks",
            "adult",
            "other"
        ]
    }