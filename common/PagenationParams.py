from dataclasses import dataclass
from typing import Dict, Optional
from common.ValidationError import ValidationError


#@dataclass
class PaginationParams:
    """Data class to handle pagination parameters"""
    limit: int = 100
    page: int = 1
    total: Optional[int] = None
    total_pages: Optional[int] = None

    def __post_init__(self):
        self.validate_limit(self.limit)

#    @staticmethod
    def validate_limit(limit: int) -> None:
        """Validate that limit is within acceptable range"""
        if not 1 <= limit <= 100:
            raise ValidationError("Limit per page should be between 1 and 100")

    def set_limit(self, limit: int) -> None:
        """Set page limit with validation"""
        self.validate_limit(limit)
        self.limit = limit
        self._recalculate_total_pages()

    def set_page(self, page: int) -> None:
        """Set current page with validation"""
        if self.total_pages is None:
            raise ValidationError("Total pages not yet calculated")
        if page > self.total_pages:
            raise ValidationError(f"Page {page} exceeds total pages {self.total_pages}")
        self.page = page

    def set_total(self, total: int) -> None:
        """Set total items count with validation"""
        if total < 0:
            raise ValidationError("Total cannot be negative")
        self.total = total
        self._recalculate_total_pages()

    def _recalculate_total_pages(self) -> None:
        """Recalculate total pages based on current total and limit"""
        if self.total is not None:
            self.total_pages = (self.total + self.limit - 1) // self.limit

    def get_params(self) -> Dict[str, int]:
        """Get parameters for API request"""
        return {
            "limit": self.limit,
            "page": self.page
        }