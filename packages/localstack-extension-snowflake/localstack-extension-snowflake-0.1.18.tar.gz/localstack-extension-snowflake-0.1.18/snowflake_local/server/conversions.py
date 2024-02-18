import base64,re
from localstack.utils.strings import to_str
from snowflake_local.server.models import QueryResponse
def to_pyarrow_table_bytes_b64(result):
	I='16777216';B=result;import pyarrow as C;J={'byteLength':I,'charLength':I,'logicalType':'VARIANT','precision':'38','scale':'0','finalType':'T'};D=[];E=[re.sub('_col','$',A['name'],flags=re.I)for A in B.data.rowtype]
	for K in range(len(E)):L=[A[K]for A in B.data.rowset];D.append(C.array(L))
	F=C.record_batch(D,names=E);G=C.BufferOutputStream();A=F.schema
	for H in range(len(A)):M=A.field(H);N=M.with_metadata(J);A=A.set(H,N)
	with C.ipc.new_stream(G,A)as O:O.write_batch(F)
	B=base64.b64encode(G.getvalue());return to_str(B)