from typing import Dict, List, Optional, Any
import requests
from urllib.parse import urljoin
from dotenv import load_dotenv
import os
from enum import Enum
from common.PagenationParams import PaginationParams
from common.ValidationError import ValidationError
from common.ApiError import APIError
from common.Constant import ApiSite, ApiSiteEndpoints




class Api(PaginationParams):
    """Client for interacting with API"""
    
    def __init__(self, site: str):
        load_dotenv()
        self.base_url = os.getenv(site.upper())
        if not self.base_url:
            raise ValueError("${} base URL not found in environment variables".format(site.upper()))
        self.endpoints = ApiSiteEndpoints().endpoints[site.lower()]
        self.params = super().get_params()
        self.data: Optional[Dict[str, Any]] = None
        self._session = requests.Session()


    def get_url(self) -> str:
        """Get the complete API URL"""
        return urljoin(self.base_url, self.endpoints)


    def get_response(self,limit:Optional[int],page:Optional[int]) -> Dict[str, Any]:
        """
        Fetch data from the API
        
        Returns:
            Dict containing API response data
            
        Raises:
            APIError: If the API request fails
        """
        if limit:
            self.set_limit(limit)
        if page:
            self.set_page(page)    
        try:
            url = self.get_url()
            response = self._session.get(url, params=self.params)
            response.raise_for_status()            
            self.data = response.json()
            return self.data            
        except requests.RequestException as e:
            raise APIError(f"API request failed: {str(e)}") from e
        except ValueError as e:
            raise APIError(f"Invalid JSON response: {str(e)}") from e