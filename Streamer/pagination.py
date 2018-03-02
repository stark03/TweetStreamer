from rest_framework.pagination import LimitOffsetPagination


class TweetLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 4
	max_limit = 100
