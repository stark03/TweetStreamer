from rest_framework.pagination import LimitOffsetPagination


class TweetLimitOffsetPagination(LimitOffsetPagination):
	
	"""Inherits the standard Limit Offset Pagination Class with a default limit on each page as 4 and max no. of pages as 100"""
	
	default_limit = 4
	max_limit = 100
	
class UserLimitOffsetPagination(LimitOffsetPagination):
		
	"""Inherits the standard Limit Offset Pagination Class with a default limit on each page as 4 and max no. of pages as 100"""

	default_limit = 4
	max_limit = 100
