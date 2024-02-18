import re
from snowflake_local.engine.models import Query
class QueryHelpers:
	REGEX_UPDATE_QUERY=re.compile('^\\s*UPDATE\\s+',flags=re.I)
	@classmethod
	def is_update_query(A,query):return A._query_matches(query,A.REGEX_UPDATE_QUERY)
	@classmethod
	def _query_matches(B,query,regex):
		A=query
		if isinstance(A,Query):A=A.original_query
		return bool(regex.match(A))