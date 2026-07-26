import random, string, hashlib
    from datetime import datetime
    from typing import Dict, Any, List

    def _fake_cpf() -> str:
      n = [random.randint(0,9) for _ in range(9)]
      return f"{''.join(map(str,n[:3]))}.{''.join(map(str,n[3:6]))}.{''.join(map(str,n[6:]))}-XX"

    def _fake_key(n=64) -> str:
      return ''.join(random.choices(string.hexdigits.lower(), k=n))

    class SistemaContraAtaque:
      def __init__(self):
          self._ativo = False
          self._tentativas = 0
          self._dados: Dict[str, Any] = {}

      def ativar(self):
          self._ativo = True
          self._dados = {
              "usuarios": [{"id":f"USR{random.randint(1000,9999)}","nome":n,"cpf":_fake_cpf(),"saldo":round(random.uniform(10,500),2)}
                           for n in ["Ana Silva","Bruno Costa","Carla Mendes"]],
              "chave_mestra": _fake_key(128),
          }
          print(f"   [TRAP] Porta falsa gerada — {len(self._dados['usuarios'])} registros ficticios")

      def interceptar_requisicao(self, origem: str = "desconhecida") -> Dict:
          self._tentativas += 1
          print(f"   ⚠️  Invasao #{self._tentativas} de '{origem}' — dados falsos servidos")
          return self._dados
    