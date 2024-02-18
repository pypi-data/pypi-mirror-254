import base64,io,logging,struct
from hashlib import sha256
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from localstack.utils.strings import to_bytes
LOG=logging.getLogger(__name__)
def decrypt_blob(blob,key,blob_path):B=struct.pack('q',0)+struct.pack('q',0);C=base64.b64decode(to_bytes(key));D=C+to_bytes(blob_path);E=sha256(D).digest();F=Cipher(algorithms.AES(E),modes.CTR(B));A=F.decryptor();G=A.update(blob)+A.finalize();return G
def get_parquet_from_blob(blob,key,blob_path):
	from pyarrow import parquet as B;A=decrypt_blob(blob,key=key,blob_path=blob_path)
	while A[-1]==0:A=A[:-1]
	try:C=io.BytesIO(A);D=B.read_table(C)
	except Exception as E:LOG.warning('Unable to parse parquet from decrypted data: %s... - %s',A[:300],E);raise
	return D.to_pylist()