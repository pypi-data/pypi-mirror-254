from localstack.utils.strings import to_bytes
from sqlglot import exp
from snowflake_local.engine.query_processors import QueryProcessor
class FixFunctionCodeEscaping(QueryProcessor):
	def transform_query(C,expression,**D):
		A=expression
		if isinstance(A,exp.Create)and str(A.args.get('kind')).upper()=='FUNCTION'and isinstance(A.expression,exp.Literal):B=to_bytes(A.expression.this).decode('unicode_escape');A.expression.args['this']=B
		return A