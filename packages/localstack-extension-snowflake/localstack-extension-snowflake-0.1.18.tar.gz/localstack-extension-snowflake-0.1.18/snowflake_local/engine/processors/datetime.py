import datetime,logging
from localstack.utils.time import timestamp
from sqlglot import exp
from snowflake_local.engine.query_processors import QueryProcessor
LOG=logging.getLogger(__name__)
class ConvertTimestampTypes(QueryProcessor):
	def transform_query(D,expression,**E):
		B='kind';A=expression
		if isinstance(A,exp.ColumnDef):
			C=str(A.args.get(B,'')).upper()
			if C=='TIMESTAMP':A.args[B]=exp.Identifier(this='TIMESTAMP WITHOUT TIME ZONE',quoted=False)
		return A
class CastParamsForToDate(QueryProcessor):
	def transform_query(C,expression,**D):
		A=expression
		if isinstance(A,exp.Func)and str(A.this).lower()=='to_date':
			A=A.copy();B=exp.Cast();B.args['this']=A.expressions[0];B.args['to']=exp.DataType.build('TEXT');A.expressions[0]=B
			if len(A.expressions)<=1:LOG.info('Auto-detection of date format in TO_DATE(..) not yet supported');A.expressions.append(exp.Literal(this='YYYY/MM/DD',is_string=True))
		return A
class ReplaceCurrentTime(QueryProcessor):
	def transform_query(D,expression,**E):
		A=expression
		if isinstance(A,(exp.CurrentTime,exp.CurrentTimestamp)):
			B=exp.Literal();C=timestamp()
			if isinstance(A,exp.CurrentTime):C=str(datetime.datetime.utcnow().time())
			B.args['this']=C;B.args['is_string']=True;return B
		return A