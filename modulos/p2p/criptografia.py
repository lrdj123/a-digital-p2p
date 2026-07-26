import os, json, hashlib
    from typing import Optional
    from cryptography.hazmat.primitives.asymmetric.ec import SECP256R1, generate_private_key, ECDH, EllipticCurvePublicKey
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_der_public_key
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    class CriptografiaFimAFim:
      def __init__(self, usuario_id: str):
          self.usuario_id = usuario_id
          self._priv = generate_private_key(SECP256R1())
          self._pub  = self._priv.public_key()
          self.cipher: Optional[AESGCM] = None

      def get_chave_publica_bytes(self) -> bytes:
          return self._pub.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

      def estabelecer_sessao(self, pub_peer_bytes: bytes) -> None:
          peer_pub = load_der_public_key(pub_peer_bytes)
          shared   = self._priv.exchange(ECDH(), peer_pub)
          key = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"a-digital").derive(shared)
          self.cipher = AESGCM(key)

      def criptografar(self, dados: dict) -> bytes:
          if not self.cipher: raise RuntimeError("Sessao nao estabelecida")
          nonce = os.urandom(12)
          return nonce + self.cipher.encrypt(nonce, json.dumps(dados).encode(), None)

      def descriptografar(self, blob: bytes) -> dict:
          if not self.cipher: raise RuntimeError("Sessao nao estabelecida")
          return json.loads(self.cipher.decrypt(blob[:12], blob[12:], None))

      def hash_transacao(self, dados: dict) -> str:
          return hashlib.sha256(json.dumps(dados, sort_keys=True).encode()).hexdigest()
    