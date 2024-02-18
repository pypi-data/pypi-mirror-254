_D='array_cat'
_C='TABLE'
_B=None
_A='kind'
import json,logging
from enum import Enum
from typing import Any
from localstack.utils.collections import ensure_list
from localstack.utils.numbers import is_number
from sqlglot import exp,parse_one
from snowflake_local import config
from snowflake_local.engine.models import VARIANT,VARIANT_MARKER_PREFIX
LOG=logging.getLogger(__name__)
INTERNAL_IDENTIFIERS={'attname','attnum','atttypid','atttypmod','attrelid','arg_min','arg_max','array_agg',_D,'array_join','array_size','array_sort','array_union_agg','current_database','current_schema','current_task_graphs','format_type','get_path','indisprimary','indkey','indrelid','is_array','lead','oid','parse_json','pg_class','pg_index','pg_attribute','plpython3u','plv8','relname','sum','to_char','to_date'}
class NameType(Enum):DATABASE=0;SCHEMA=1;RESOURCE=2
def convert_function_args_to_variant(expression,function,**F):
	D='to_variant';A=expression
	if not isinstance(A,exp.Func):return A
	C=str(A.this).lower()
	if isinstance(A,exp.ArrayConcat):C=_D
	if C!=function:return A
	for(E,B)in enumerate(A.expressions):A.expressions[E]=exp.Anonymous(this=D,expressions=ensure_list(B))
	if isinstance(A,exp.ArrayConcat):B=A.this;A.args['this']=exp.Anonymous(this=D,expressions=ensure_list(B))
	return A
def is_create_table_expression(expression):A=expression;return isinstance(A,exp.Create)and(B:=A.args.get(_A))and isinstance(B,str)and B.upper()==_C
def get_canonical_name(name,type=_B,quoted=True):
	E='public';C=quoted;B='"';A=name;A=A.strip()
	if not config.CONVERT_NAME_CASING:
		if type==NameType.DATABASE and not C:return A.lower()
		if'$'in A:return f'"{A}"'
		return A
	if A.startswith(B)and A.endswith(B):return A
	if'.'in A:LOG.info('Found dot in resource name, could hint at a potential name parsing issue: %s',A)
	if A.lower()in INTERNAL_IDENTIFIERS:return A
	if A.startswith(B)and A.endswith(B):return A
	if type in[_B,NameType.SCHEMA]and A.lower()==E:return E
	D=A.upper()
	if C:return f'"{D}"'
	return D
def get_table_from_creation_query(query):
	A=parse_snowflake_query(query)
	if not isinstance(A,exp.Create)or A.args.get(_A)!=_C:return
	B=A.this;C=B.this;D=C.this;E=getattr(D,'this',_B);return E
def get_table_from_drop_query(query):
	A=parse_snowflake_query(query)
	if not isinstance(A,exp.Drop)or A.args.get(_A)!=_C:return
	B=A.this;C=B.this;D=C.this;return D
def get_database_from_drop_query(query):
	A=parse_snowflake_query(query)
	if not isinstance(A,exp.Drop)or A.args.get(_A)!='DATABASE':return
	B=A.this;C=B.this;D=C.this;return D
def parse_snowflake_query(query):
	try:return parse_one(query,read='snowflake')
	except Exception:return
def unwrap_potential_variant_type(obj):
	A=obj
	if isinstance(A,str)and A.startswith(VARIANT_MARKER_PREFIX):return unwrap_variant_type(A)
	return A
def unwrap_variant_type(variant_obj_str,expected_type=_B):
	C=expected_type;B=variant_obj_str;B=B.removeprefix(VARIANT_MARKER_PREFIX);A=json.loads(B)
	if C:
		if not isinstance(A,C)and isinstance(A,str):
			try:
				D=json.loads(A)
				if isinstance(D,C):A=D
			except Exception:pass
	return A
def to_variant(obj):
	A=obj
	if isinstance(A,str)and A.startswith(VARIANT_MARKER_PREFIX):return A
	if not isinstance(A,bool)and is_number(A)and int(A)==A:A=int(A)
	try:B=json.dumps(A);return f"{VARIANT_MARKER_PREFIX}{B}"
	except Exception:return str(A)