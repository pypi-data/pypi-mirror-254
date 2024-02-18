_L='UNKNOWN'
_K='FUNCTION'
_J='TABLE'
_I='nullable'
_H='scale'
_G='precision'
_F='name'
_E='kind'
_D=True
_C='length'
_B='TEXT'
_A='type'
import calendar,datetime,json,re
from sqlglot import exp
from snowflake_local.engine.models import VARIANT_MARKER_PREFIX,Query
from snowflake_local.engine.query_processors import QueryProcessor
from snowflake_local.engine.transform_utils import get_table_from_creation_query,parse_snowflake_query,unwrap_variant_type
from snowflake_local.server.conversions import to_pyarrow_table_bytes_b64
from snowflake_local.server.models import QueryResponse
TYPE_MAPPINGS={'VARIANT':_B,'OBJECT':_B,'STRING':_B,_L:_B,'ARRAY':_B}
class EncodeComplexTypesInResults(QueryProcessor):
	def postprocess_result(D,query,result):
		for A in result.data.rowset:
			for(C,B)in enumerate(A):
				if isinstance(B,(dict,list)):A[C]=json.dumps(B)
class ConvertTimestampResults(QueryProcessor):
	def postprocess_result(L,query,result):
		D=result
		for(E,C)in enumerate(D.data.rowtype):
			B=str(C.get(_A)).upper();F='TIMESTAMP','TIMESTAMP WITHOUT TIME ZONE';G='TIMESTAMP WITH TIME ZONE',;H='DATE',
			if B in F:C[_A]='TIMESTAMP_NTZ'
			if B in G:C[_A]='TIMESTAMP_TZ'
			I=B in H
			if B not in F+G+H:continue
			for J in D.data.rowset:
				A=J[E]
				if I:K=calendar.timegm(A.timetuple());A=datetime.datetime.utcfromtimestamp(K)
				if isinstance(A,datetime.datetime):A=A.replace(tzinfo=datetime.timezone.utc)
				if A is None:continue
				A=int(A.timestamp())
				if I:A=A/24/60/60
				J[E]=str(int(A))
class UnwrapVariantTypes(QueryProcessor):
	def postprocess_result(E,query,result):
		A=result
		for C in A.data.rowset:
			for(D,B)in enumerate(C):
				if isinstance(B,str)and B.startswith(VARIANT_MARKER_PREFIX):
					A=unwrap_variant_type(B)
					if isinstance(A,(list,dict)):A=B.removeprefix(VARIANT_MARKER_PREFIX)
					C[D]=A
class FixBooleanResultValues(QueryProcessor):
	def postprocess_result(F,query,result):
		A=result
		for(B,D)in enumerate(A.data.rowtype):
			E=D.get(_A,'')
			if E.upper()not in('BOOL','BOOLEAN'):continue
			for C in A.data.rowset:C[B]='TRUE'if str(C[B]).lower()=='true'else'FALSE'
class AdjustQueryResultFormat(QueryProcessor):
	def postprocess_result(C,query,result):
		A=result;B=re.match('.+FROM\\s+@',query.original_query,flags=re.I);A.data.queryResultFormat='arrow'if B else'json'
		if B:A.data.rowsetBase64=to_pyarrow_table_bytes_b64(A);A.data.rowset=[];A.data.rowtype=[]
class AdjustColumnTypes(QueryProcessor):
	TYPE_MAPPINGS={_L:_B,'VARCHAR':_B,'CHARACTER VARYING':_B}
	def postprocess_result(C,query,result):
		for A in result.data.rowtype:
			D=A.get(_A,'');B=C.TYPE_MAPPINGS.get(D)
			if B:A[_A]=B
			if A[_A].upper()==_B and A.get(_C)==-1:A[_C]=0
class FixInsertQueryResult(QueryProcessor):
	def should_apply(A,query):return bool(re.match('^\\s*INSERT\\s+.+',query.original_query,flags=re.I))
	def postprocess_result(B,query,result):A=result;A.data.rowset=[[len(A.data.rowset)]];A.data.rowtype=[{_F:'count',_A:'integer',_C:0,_G:0,_H:0,_I:_D}]
class FixCreateEntityResult(QueryProcessor):
	def should_apply(A,query):B=A._get_created_entity_type(query.original_query);return B in(_J,_K)
	def postprocess_result(E,query,result):
		D=result;B=query;C=E._get_created_entity_type(B.original_query);F={_J:'Table',_K:'Function'};G=F.get(C)
		if C==_J:A=get_table_from_creation_query(B.original_query);A=A and A.upper()
		elif C==_K:H=parse_snowflake_query(B.original_query);I=H.this;A=str(I.this).upper()
		else:A='test'
		D.data.rowset.append([f"{G} {A} successfully created."]);D.data.rowtype.append({_F:'status',_A:'text',_C:0,_G:0,_H:0,_I:_D})
	def _get_created_entity_type(B,query):
		A=parse_snowflake_query(query)
		if isinstance(A,exp.Create):return A.args.get(_E)
class AddDefaultResultIfEmpty(QueryProcessor):
	def should_apply(B,query):
		A=parse_snowflake_query(query.original_query)
		if isinstance(A,exp.AlterTable):return _D
		return isinstance(A,exp.Command)and str(A.this).upper()=='ALTER'
	def postprocess_result(B,query,result):
		A=result
		if not A.data.rowtype:A.data.rowtype=[{_F:'?column?',_A:'text',_C:0,_G:0,_H:0,_I:_D}]
		A.data.rowset=[('Statement executed successfully.',)]
class ReplaceUnknownTypes(QueryProcessor):
	def transform_query(F,expression,**G):
		A=expression
		for(C,D)in TYPE_MAPPINGS.items():
			E=getattr(exp.DataType.Type,D.upper());B=A
			if isinstance(B,exp.Alias):B=B.this
			if isinstance(B,exp.Cast)and B.to==exp.DataType.build(C):B.args['to']=exp.DataType.build(E)
			if isinstance(A,exp.ColumnDef):
				if A.args.get(_E)==exp.DataType.build(C):A.args[_E]=exp.DataType.build(E)
			if isinstance(A,exp.Identifier)and isinstance(A.parent,exp.Schema):
				if str(A.this).upper()==C.upper():A.args['this']=D.upper()
		return A
class AdjustAutoIncrementColumnTypes(QueryProcessor):
	def transform_query(D,expression,**E):
		A=expression
		if isinstance(A,exp.ColumnDef):
			B=exp.AutoIncrementColumnConstraint,exp.GeneratedAsIdentityColumnConstraint
			for C in A.constraints:
				if isinstance(C.kind,B):A.args[_E]=exp.Identifier(this='SERIAL',quoted=False)
			A.args['constraints']=[A for A in A.constraints if not isinstance(A.kind,B)]
		return A