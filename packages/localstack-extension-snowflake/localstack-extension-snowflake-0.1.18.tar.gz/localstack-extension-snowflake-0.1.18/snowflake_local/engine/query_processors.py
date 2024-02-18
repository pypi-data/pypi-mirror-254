import logging
from abc import ABC
from localstack.utils.objects import get_all_subclasses
from sqlglot import exp
from snowflake_local.engine.models import Query
from snowflake_local.server.models import QueryResponse
LOG=logging.getLogger(__name__)
class QueryProcessor(ABC):
	def initialize_db_resources(A,database):0
	def should_apply(A,query):return True
	def transform_query(A,expression,query):return expression
	def postprocess_result(A,query,result):0
	def get_priority(A):return 0
	@classmethod
	def get_instances(B):A=[A()for A in get_all_subclasses(QueryProcessor)];A=sorted([A for A in A],key=lambda item:item.get_priority(),reverse=True);return A