import dataclasses,logging,re
from localstack.http import Request
from snowflake_local.engine.models import QueryState,Session
from snowflake_local.engine.transform_utils import get_canonical_name
from snowflake_local.server.models import QueryResponse
LOG=logging.getLogger(__name__)
@dataclasses.dataclass
class DBResources:file_formats:dict[str,dict]=dataclasses.field(default_factory=dict)
@dataclasses.dataclass
class ApplicationState:sessions:dict[str,Session]=dataclasses.field(default_factory=dict);queries:dict[str,QueryState]=dataclasses.field(default_factory=dict);db_resources:dict[str,DBResources]=dataclasses.field(default_factory=dict)
APP_STATE=ApplicationState()
def handle_use_query(query,result,session):
	F=result;E=query;A=session;C=re.match('^\\s*USE\\s+(\\S+)\\s+(\\S+)',E,flags=re.I)
	if not C:return F
	D=C.group(1).strip().lower();B=get_canonical_name(C.group(2),quoted=False)
	if D=='database':A.database=B;A.schema=None
	elif D=='warehouse':A.warehouse=B
	elif D=='schema':
		A.schema=B
		if'.'in B:A.database,A.schema=B.split('.')
	else:LOG.info("Unexpected 'USE ...' query: %s",E)
	return F
def get_auth_token_from_request(request):A=request.headers.get('Authorization')or'';A=A.removeprefix('Snowflake ').strip();A=A.split('Token=')[-1].strip('\'"');return A
def lookup_request_session(request):
	B=get_auth_token_from_request(request)
	for A in APP_STATE.sessions.values():
		if A.auth_token==B:return A