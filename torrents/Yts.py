from typing import Dict, List, Any
from common.Api import Api 
from common.ApiError import APIError

class YtsClient:
    def __init__(self):
        self.site = "YTS"
        self.api = Api(self.site)
        self.data = self.api.get_response()["data"]
        

    def get_torrents(self) -> List[Dict[str, Any]]:
        if not self.data or "movies" not in self.data:
            raise APIError("No torrent data available")
        return self.data["movies"]


    def get_total(self) -> int:
        if not self.data or "movie_count" not in self.data:
            raise APIError("Torrent count not available in response") 
        try:
            self.api.set_total(self.data["movie_count"])
            return int(self.data["movie_count"])
        except ValueError as e:
            raise APIError(f"Invalid torrent count in response: {str(e)}") from e

    def get_total_pages(self) -> int:
        if not self.api.total_pages:
            self.get_total()
        return self.api.total_pages