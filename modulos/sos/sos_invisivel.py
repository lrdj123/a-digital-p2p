from dataclasses import dataclass, field
    from datetime import datetime
    from typing import List

    @dataclass
    class ContatoConfianca:
      nome: str
      telefone: str
      notificado: bool = False

    @dataclass
    class AlertaSOS:
      latitude: float
      longitude: float
      nivel_estresse: float
      motivo: str
      timestamp: str
      contatos_notificados: List[str] = field(default_factory=list)

    class SOSInvisivel:
      def __init__(self, usuario_id: str, nome: str):
          self.usuario_id = usuario_id
          self.nome = nome
          self.contatos: List[ContatoConfianca] = []
          self._bloqueado = False

      def cadastrar_contato_confianca(self, nome: str, telefone: str):
          self.contatos.append(ContatoConfianca(nome, telefone))
          print(f"   [SOS] Contato cadastrado: {nome} ({telefone})")

      def ativar_sos(self, lat: float, lon: float, estresse: float, motivo: str) -> AlertaSOS:
          alerta = AlertaSOS(lat, lon, estresse, motivo, datetime.now().isoformat())
          print(f"\n🚨 SOS ATIVADO! Motivo: {motivo}")
          for c in self.contatos:
              print(f"   📱 Alerta enviado para {c.nome} ({c.telefone})")
              c.notificado = True
              alerta.contatos_notificados.append(c.nome)
          return alerta

      def bloquear_transacao(self):
          self._bloqueado = True
          print("   🔒 Transacao bloqueada pelo SOS")
    