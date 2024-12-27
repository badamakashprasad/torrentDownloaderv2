from typing import Dict, List, Any, Optional
from common.Api import Api 
from common.ApiError import APIError

class EzTvClient:
    def __init__(self,limit:Optional[int],page:Optional[int]):
        self.site = "EZTV"
        self.api = Api(self.site)
        self.data = self.api.get_response(limit,page)
        

    def get_torrents(self) -> List[Dict[str, Any]]:
        if not self.data or "torrents" not in self.data:
            raise APIError("No torrent data available")
        return self.data["torrents"]


    def get_total(self) -> int:
        if not self.data or "torrents_count" not in self.data:
            raise APIError("Torrent count not available in response") 
        try:
            self.api.set_total(self.data["torrents_count"])
            return int(self.data["torrents_count"])
        except ValueError as e:
            raise APIError(f"Invalid torrent count in response: {str(e)}") from e

    def get_total_pages(self) -> int:
        if not self.api.total_pages:
            self.get_total()
        return self.api.total_pages