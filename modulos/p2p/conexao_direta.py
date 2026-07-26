from dataclasses import dataclass
    from typing import Any, Dict

    @dataclass
    class MensagemP2P:
      tipo: str
      remetente_id: str
      destinatario_id: str
      payload: Dict[str, Any]
      assinatura: str
      timestamp: float

      def to_dict(self) -> Dict:
          return self.__dict__

      @classmethod
      def from_dict(cls, d: Dict) -> "MensagemP2P":
          return cls(**d)
    