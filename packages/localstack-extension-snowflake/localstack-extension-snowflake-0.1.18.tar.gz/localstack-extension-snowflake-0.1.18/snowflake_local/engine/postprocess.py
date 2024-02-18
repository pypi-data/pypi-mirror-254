_U='already exists'
_T='status'
_S='VARCHAR'
_R='COLUMN_DEFAULT'
_Q='DATA_TYPE'
_P='COLUMN_NAME'
_O='TEXT'
_N='FUNCTION'
_M='default'
_L='TABLE'
_K='nullable'
_J='scale'
_I='precision'
_H='integer'
_G=True
_F='length'
_E='kind'
_D=None
_C='type'
_B='name'
_A='text'
import calendar,datetime,json,re
from sqlglot import exp,parse_one
from snowflake_local.engine.extension_functions import VARIANT_MARKER_PREFIX,_unwrap_variant_type
from snowflake_local.engine.models import Query
from snowflake_local.engine.postgres.db_state import State
from snowflake_local.engine.query_processors import QueryProcessor
from snowflake_local.server.conversions import to_pyarrow_table_bytes_b64
from snowflake_local.server.models import QueryResponse
class FixShowEntitiesResult(QueryProcessor):
	def should_apply(A,query):B=query;return A._is_show_tables(B)or A._is_show_schemas(B)or A._is_show_objects(B)or A._is_show_columns(B)or A._is_show_primary_keys(B)or A._is_show_procedures(B)or A._is_show_imported_keys(B)
	def _is_show_tables(B,query):A=query.original_query;return bool(re.match('^\\s*SHOW\\s+.*TABLES',A,flags=re.I)or re.search('\\s+FROM\\s+information_schema\\s*\\.\\s*tables\\s+',A,flags=re.I))
	def _is_show_schemas(B,query):A=query.original_query;return bool(re.match('^\\s*SHOW\\s+.*SCHEMAS',A,flags=re.I)or re.search('\\s+FROM\\s+information_schema\\s*\\.\\s*schemata\\s+',A,flags=re.I))
	def _is_show_objects(A,query):return bool(re.match('^\\s*SHOW\\s+.*OBJECTS',query.original_query,flags=re.I))
	def _is_show_columns(B,query):A=query.original_query;return bool(re.match('^\\s*SHOW\\s+.*COLUMNS',A,flags=re.I)or re.search('\\s+FROM\\s+information_schema\\s*\\.\\s*columns\\s+',A,flags=re.I))
	def _is_show_primary_keys(A,query):return bool(re.match('^\\s*SHOW\\s+.*PRIMARY\\s+KEYS',query.original_query,flags=re.I))
	def _is_show_imported_keys(A,query):return bool(re.match('^\\s*SHOW\\s+IMPORTED\\s+KEYS',query.original_query,flags=re.I))
	def _is_show_procedures(A,query):return bool(re.match('^\\s*SHOW\\s+PROCEDURES',query.original_query,flags=re.I))
	def postprocess_result(I,query,result):
		Y='rely';Z='key_sequence';a='options';b='catalog_name';c='TABLE_NAME';T='bytes';U='rows';V='cluster_by';M='budget';N='owner_role_type';O='retention_time';P='owner';Q='column_name';R='table_name';K='data_type';J='comment';F='created_on';G='timestamp_ltz';H=query;C='database_name';D='schema_name';B=result;from snowflake_local.engine.postgres.db_engine_postgres import State,convert_pg_to_snowflake_type as n;d=I._is_show_objects(H);e=I._is_show_tables(H);o=I._is_show_schemas(H);p=I._is_show_columns(H);q=I._is_show_procedures(H);r=I._is_show_primary_keys(H);s=I._is_show_imported_keys(H);t=re.match('.+\\sTERSE\\s',H.original_query,flags=re.I);_replace_dict_value(B.data.rowtype,_B,'TABLE_SCHEMA',D);_replace_dict_value(B.data.rowtype,_B,'SCHEMA_NAME',_B)
		if e or d:_replace_dict_value(B.data.rowtype,_B,c,_B)
		else:_replace_dict_value(B.data.rowtype,_B,c,R)
		_replace_dict_value(B.data.rowtype,_B,_P,Q);_replace_dict_value(B.data.rowtype,_B,'TABLE_TYPE',_E);_replace_dict_value(B.data.rowtype,_B,'TABLE_CATALOG',C);_replace_dict_value(B.data.rowtype,_B,'CATALOG_NAME',C);_replace_dict_value(B.data.rowtype,_B,_Q,K);_replace_dict_value(B.data.rowtype,_B,_R,_M);_replace_dict_value(B.data.rowtype,_B,'SPECIFIC_CATALOG',b);_replace_dict_value(B.data.rowtype,_B,'SPECIFIC_SCHEMA',D);_replace_dict_value(B.data.rowtype,_B,'SPECIFIC_NAME',_B);S=[];L=[A[_B]for A in B.data.rowtype]
		for W in B.data.rowset:A=dict(zip(L,W));S.append(A)
		def u(_name,_type):A=_type;return{_B:_name,_I:_D,_J:3 if A==G else _D,_C:A,_K:_G,_F:_D}
		v={F:G,_B:_A,_E:_A,C:_A,D:_A};w={F:G,_B:_A,C:_A,D:_A,_E:_A,J:_A,V:_A,U:_H,T:_H,P:_A,O:_A,N:_A,M:_A};x={F:G,_B:_A,C:_A,D:_A,_E:_A,J:_A,V:_A,U:_H,T:_H,P:_A,O:_A,'automatic_clustering':_A,'change_tracking':_A,'is_external':_A,'enable_schema_evolution':_A,N:_A,'is_event':_A,M:_A};y={F:G,_B:_A,'is_default':_A,'is_current':_A,C:_A,P:_A,J:_A,a:_A,O:_A,N:_A,M:_A};z={R:_A,D:_A,Q:_A,K:_A,'null?':_A,_M:_A,_E:_A,'expression':_A,J:_A,C:_A,'autoincrement':_A};A0={F:G,C:_A,D:_A,R:_A,Q:_A,Z:_A,'constraint_name':_A,Y:_A,J:_A};A1={F:G,'pk_database_name':_A,'pk_schema_name':_A,'pk_table_name':_A,'pk_column_name':_A,'fk_database_name':_A,'fk_schema_name':_A,'fk_table_name':_A,'fk_column_name':_A,Z:_A,'update_rule':_A,'delete_rule':_A,'fk_name':_A,'pk_name':_A,'deferrability':_A,Y:_A,J:_A};A2={F:G,_B:_A,D:_A,'is_builtin':_A,'is_aggregate':_A,'is_ansi':_A,'min_num_arguments':_H,'max_num_arguments':_H,'arguments':_A,'description':_A,b:_A,'is_table_function':_A,'valid_for_clustering':_A,'is_secure':_A};E=_D
		if r:E=A0
		elif t:E=v
		elif o:E=y
		elif d:E=w
		elif e:E=x
		elif p:E=z
		elif q:E=A2
		elif s:E=A1
		del B.data.rowtype[:];L=[A[_B]for A in B.data.rowtype]
		for(f,A3)in E.items():
			if f in L:continue
			B.data.rowtype.append(u(f,A3))
		for A in S:
			A.setdefault(V,'');A.setdefault(U,0);A.setdefault(T,0);A.setdefault(a,'')
			if A.get(_M)is _D:A[_M]=''
			if A.get(K):A4=n(A[K]);A[K]=json.dumps({_C:A4})
			A.setdefault(J,'');A.setdefault(P,'PUBLIC');A.setdefault(O,'1');A.setdefault(N,'ROLE');A.setdefault(M,_D)
			if A.get(_E)=='BASE TABLE':A[_E]=_L
			A.setdefault(F,'0')
		for A in S:
			for X in(_B,D,C,R,Q):
				if A.get(X):A[X]=A[X].upper()
			g=A.get(C);h=A.get(D);i=A.get(_B)
			if any((g,h,i)):
				j=State.identifier_overrides.find_match(g,schema=h,obj_name=i)
				if j:
					k,l,m=j
					if m:A[_B]=m
					elif l:A[D]=l
					elif k:A[C]=k
		L=[A[_B]for A in B.data.rowtype];B.data.rowset=[]
		for A in S:W=[A.get(B)for B in L];B.data.rowset.append(W)
class ConvertDescribeTableResultColumns(QueryProcessor):
	DESCRIBE_TABLE_COL_ATTRS={_B:_P,_C:_Q,_E:"'COLUMN'",'null?':'IS_NULLABLE',_M:_R}
	def should_apply(D,query):A=query.original_query;B=re.match('^DESC(RIBE)?\\s+(TABLE\\s+)?.+',A,flags=re.I);C=re.match('\\s+information_schema\\s*\\.\\s*columns\\s+',A,flags=re.I);return bool(B or C)
	def postprocess_result(E,query,result):
		A=result;G=[A[_B]for A in A.data.rowtype];F=list(E.DESCRIBE_TABLE_COL_ATTRS);A.data.rowtype=[]
		for H in F:A.data.rowtype.append({_B:H,_I:_D,_J:_D,_C:_S,_K:_G,_F:_D})
		for(I,J)in enumerate(A.data.rowset):
			C=[]
			for K in F:
				D=E.DESCRIBE_TABLE_COL_ATTRS[K]
				if D.startswith("'"):C.append(D.strip("'"))
				else:L=dict(zip(G,J));B=L[D];B={'YES':'Y','NO':'N'}.get(B)or B;C.append(B)
			A.data.rowset[I]=C
class FixCreateEntityResult(QueryProcessor):
	def should_apply(A,query):B=A._get_created_entity_type(query.original_query);return B in(_L,_N)
	def postprocess_result(E,query,result):
		D=result;B=query;C=E._get_created_entity_type(B.original_query);F={_L:'Table',_N:'Function'};G=F.get(C)
		if C==_L:A=_get_table_from_creation_query(B.original_query);A=A and A.upper()
		elif C==_N:H=_parse_snowflake_query(B.original_query);I=H.this;A=str(I.this).upper()
		else:A='test'
		D.data.rowset.append([f"{G} {A} successfully created."]);D.data.rowtype.append({_B:_T,_C:_A,_F:0,_I:0,_J:0,_K:_G})
	def _get_created_entity_type(B,query):
		A=_parse_snowflake_query(query)
		if isinstance(A,exp.Create):return A.args.get(_E)
class FixDropTableResult(QueryProcessor):
	def should_apply(A,query):return bool(_get_table_from_drop_query(query.original_query))
	def postprocess_result(C,query,result):A=result;B=_get_table_from_drop_query(query.original_query);A.data.rowset.append([f"{B} successfully dropped."]);A.data.rowtype.append({_B:_T,_C:_A,_F:0,_I:0,_J:0,_K:_G})
class HandleDropDatabase(QueryProcessor):
	def should_apply(A,query):return bool(_get_database_from_drop_query(query.original_query))
	def postprocess_result(C,query,result):A=query;B=_get_database_from_drop_query(A.original_query);State.initialized_dbs=[A for A in State.initialized_dbs if A.lower()!=B.lower()];A.session.database=_D;A.session.schema=_D
class FixAlreadyExistsErrorResponse(QueryProcessor):
	def postprocess_result(C,query,result):
		A=result
		if A.success or _U not in(A.message or''):return
		def B(match):return f"SQL compilation error:\nObject '{match.group(1).upper()}' already exists."
		A.message=re.sub('.*database \\"(\\S+)\\".+',B,A.message);A.message=re.sub('.*relation \\"(\\S+)\\".+',B,A.message);A.message=re.sub('.*function \\"(\\S+)\\".+',B,A.message)
class FixInsertQueryResult(QueryProcessor):
	def should_apply(A,query):return bool(re.match('^\\s*INSERT\\s+.+',query.original_query,flags=re.I))
	def postprocess_result(B,query,result):A=result;A.data.rowset=[[len(A.data.rowset)]];A.data.rowtype=[{_B:'count',_C:_H,_F:0,_I:0,_J:0,_K:_G}]
class UpdateSessionAfterCreatingDatabase(QueryProcessor):
	REGEX=re.compile('^\\s*CREATE.*\\s+DATABASE(\\s+IF\\s+NOT\\s+EXISTS)?\\s+(\\S+)',flags=re.I)
	def should_apply(A,query):return bool(A.REGEX.match(query.original_query))
	def postprocess_result(B,query,result):A=query;C=B.REGEX.match(A.original_query);A.session.database=C.group(2);A.session.schema=_D
class UpdateSessionAfterCreatingSchema(QueryProcessor):
	REGEX=re.compile('^\\s*CREATE.*\\s+SCHEMA(\\s+IF\\s+NOT\\s+EXISTS)?\\s+(\\S+)',flags=re.I)
	def should_apply(A,query):return bool(A.REGEX.match(query.original_query))
	def postprocess_result(B,query,result):A=query;C=B.REGEX.match(A.original_query);A.session.schema=C.group(2)
class AdjustQueryResultFormat(QueryProcessor):
	def postprocess_result(C,query,result):
		A=result;B=re.match('.+FROM\\s+@',query.original_query,flags=re.I);A.data.queryResultFormat='arrow'if B else'json'
		if B:A.data.rowsetBase64=to_pyarrow_table_bytes_b64(A);A.data.rowset=[];A.data.rowtype=[]
class AdjustColumnTypes(QueryProcessor):
	TYPE_MAPPINGS={'UNKNOWN':_O,_S:_O}
	def postprocess_result(C,query,result):
		for A in result.data.rowtype:
			D=A.get(_C,'');B=C.TYPE_MAPPINGS.get(D)
			if B:A[_C]=B
			if A[_C].upper()==_O and A.get(_F)==-1:A[_F]=0
class FixBooleanResultValues(QueryProcessor):
	def postprocess_result(F,query,result):
		A=result
		for(B,D)in enumerate(A.data.rowtype):
			E=D.get(_C,'')
			if E.upper()not in('BOOL','BOOLEAN'):continue
			for C in A.data.rowset:C[B]='TRUE'if str(C[B]).lower()=='true'else'FALSE'
class ReturnDescribeTableError(QueryProcessor):
	def postprocess_result(C,query,result):
		A=result;B=re.match('desc(?:ribe)?\\s+.+',query.original_query,flags=re.I)
		if B and not A.data.rowset:A.success=False
class IgnoreErrorForExistingEntity(QueryProcessor):
	REGEX=re.compile('^\\s*CREATE.*\\s+(\\S+)(\\s+IF\\s+NOT\\s+EXISTS)\\s+(\\S+)',flags=re.I)
	def should_apply(A,query):return bool(A.REGEX.match(query.original_query))
	def postprocess_result(B,query,result):
		A=result
		if not A.success and _U in(A.message or''):A.success=_G;A.data.rowtype=[];A.data.rowset=[]
class AddDefaultResultIfEmpty(QueryProcessor):
	def should_apply(B,query):
		A=_parse_snowflake_query(query.original_query)
		if isinstance(A,exp.AlterTable):return _G
		return isinstance(A,exp.Command)and str(A.this).upper()=='ALTER'
	def postprocess_result(B,query,result):
		A=result
		if not A.data.rowtype:A.data.rowtype=[{_B:'?column?',_C:_A,_F:0,_I:0,_J:0,_K:_G}]
		A.data.rowset=[('Statement executed successfully.',)]
class EncodeComplexTypesInResults(QueryProcessor):
	def postprocess_result(D,query,result):
		for A in result.data.rowset:
			for(C,B)in enumerate(A):
				if isinstance(B,(dict,list)):A[C]=json.dumps(B)
class ConvertTimestampResults(QueryProcessor):
	def postprocess_result(L,query,result):
		D=result
		for(E,C)in enumerate(D.data.rowtype):
			B=str(C.get(_C)).upper();F='TIMESTAMP','TIMESTAMP WITHOUT TIME ZONE';G='TIMESTAMP WITH TIME ZONE',;H='DATE',
			if B in F:C[_C]='TIMESTAMP_NTZ'
			if B in G:C[_C]='TIMESTAMP_TZ'
			I=B in H
			if B not in F+G+H:continue
			for J in D.data.rowset:
				A=J[E]
				if I:K=calendar.timegm(A.timetuple());A=datetime.datetime.utcfromtimestamp(K)
				if isinstance(A,datetime.datetime):A=A.replace(tzinfo=datetime.timezone.utc)
				if A is _D:continue
				A=int(A.timestamp())
				if I:A=A/24/60/60
				J[E]=str(int(A))
class UnwrapVariantTypes(QueryProcessor):
	def postprocess_result(E,query,result):
		A=result
		for C in A.data.rowset:
			for(D,B)in enumerate(C):
				if isinstance(B,str)and B.startswith(VARIANT_MARKER_PREFIX):
					A=_unwrap_variant_type(B)
					if isinstance(A,(list,dict)):A=B.removeprefix(VARIANT_MARKER_PREFIX)
					C[D]=A
def apply_post_processors(query,result):
	A=query
	for B in QueryProcessor.get_instances():
		if B.should_apply(A):B.postprocess_result(A,result=result)
def _replace_dict_value(values,attr_key,attr_value,attr_value_replace):
	A=attr_key;B=[B for B in values if B[A]==attr_value]
	if B:B[0][A]=attr_value_replace
def _get_table_from_creation_query(query):
	A=_parse_snowflake_query(query)
	if not isinstance(A,exp.Create)or A.args.get(_E)!=_L:return
	B=A.this;C=B.this;D=C.this;E=getattr(D,'this',_D);return E
def _get_table_from_drop_query(query):
	A=_parse_snowflake_query(query)
	if not isinstance(A,exp.Drop)or A.args.get(_E)!=_L:return
	B=A.this;C=B.this;D=C.this;return D
def _get_database_from_drop_query(query):
	A=_parse_snowflake_query(query)
	if not isinstance(A,exp.Drop)or A.args.get(_E)!='DATABASE':return
	B=A.this;C=B.this;D=C.this;return D
def _parse_snowflake_query(query):
	try:return parse_one(query,read='snowflake')
	except Exception:return