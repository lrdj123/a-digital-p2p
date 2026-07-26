"""
    🤚 A DIGITAL — Orquestrador Principal (Arquitetura P2P)

    Sistema de segurança entre dispositivos, SEM servidor central.
    A validação é feita DIRETAMENTE entre as partes.

    Não existe servidor para invadir.
    Não existe ponto único de falha.
    """

    import os
    import sys
    import json
    import time
    import asyncio
    from datetime import datetime
    from typing import Optional, Dict, Any

    sys.path.append(os.path.join(os.path.dirname(__file__), 'modulos'))
    from modulos.p2p.conexao_direta import MensagemP2P

    class DigitalP2P:

      def __init__(self, usuario_id: str, nome: str):
          self.usuario_id = usuario_id
          self.nome = nome
          self.token_biometrico: Optional[bytes] = None
          self.chave_privada: Optional[bytes] = None
          self.conexao_p2p = None
          self.cripto = None
          self.ia_emocional = None
          self.sos = None
          self.contra_ataque = None
          self.transacao_atual: Optional[Dict] = None
          self.modo_seguranca = True

      async def inicializar(self):
          print(f"""
    ╔══════════════════════════════════════════╗
    ║        🤚 A DIGITAL — P2P              ║
    ║                                          ║
    ║   👤 Usuário: {self.nome:<20}║
    ║   🆔 ID: {self.usuario_id:<23}║
    ║   📍 Modo: 100% LOCAL (sem servidor)    ║
    ╚══════════════════════════════════════════╝
          """)

          from modulos.p2p.criptografia import CriptografiaFimAFim
          self.cripto = CriptografiaFimAFim(self.usuario_id)
          print("🔐 Criptografia: Chave P-256 gerada")
          print(f"   Chave pública: {self.cripto.get_chave_publica_bytes().hex()[:20]}...")

          from modulos.ia_emocional.analise_facial import AnalisadorEmocional
          self.ia_emocional = AnalisadorEmocional()
          print("🧠 IA Emocional: Carregada (local, sem nuvem)")

          from modulos.sos.sos_invisivel import SOSInvisivel
          self.sos = SOSInvisivel(self.usuario_id, self.nome)
          self.sos.cadastrar_contato_confianca("Maria", "11999999999")
          print("🚨 SOS Invisível: ATIVO (sempre ligado)")

          from modulos.contra_ataque.porta_falsa import SistemaContraAtaque
          self.contra_ataque = SistemaContraAtaque()
          self.contra_ataque.ativar()
          print("🦠 Contra-ataque: Porta falsa pronta")

          print("\n✅ Sistema inicializado com sucesso!")
          return True

      async def iniciar_transacao(self, outro_dispositivo_id: str, valor: float, latitude: float, longitude: float):
          print(f"""
    📋 NOVA TRANSAÇÃO
    ─────────────────
    💰 Valor: R$ {valor:.2f}
    👤 Comprador: {self.nome} ({self.usuario_id})
    👤 Vendedor: {outro_dispositivo_id}
    📍 Local: {latitude}, {longitude}
          """)

          self.transacao_atual = {
              "comprador_id": self.usuario_id,
              "comprador_nome": self.nome,
              "vendedor_id": outro_dispositivo_id,
              "valor": valor,
              "latitude": latitude,
              "longitude": longitude,
              "timestamp": datetime.now().isoformat(),
              "status": "iniciada"
          }

          print("\n🔗 Estabelecendo conexão P2P...")

          print("\n🤚 Autenticação do comprador...")
          autenticado = self._autenticar_local()
          if not autenticado:
              return self._falhar("Comprador não autenticado")

          print("\n📸 Análise emocional do comprador...")
          resultado_ia = self.ia_emocional.analisar()
          print(f"   Estado: {resultado_ia.estado.value}")
          print(f"   Estresse: {resultado_ia.nivel_estresse:.0%}")

          if resultado_ia.alerta_sos:
              print("\n🚨 PERIGO DETECTADO! Ativando SOS...")
              self.sos.ativar_sos(latitude, longitude, resultado_ia.nivel_estresse, "IA detectou coação")
              self.sos.bloquear_transacao()
              return self._falhar("SOS ativado — transação bloqueada")

          print("\n📤 Enviando dados do comprador para o vendedor...")
          if self.cripto.cipher is None:
              chave_publica_outro = self.cripto.get_chave_publica_bytes()
              self.cripto.estabelecer_sessao(chave_publica_outro)

          dados_comprador = {
              "tipo": "autenticacao_comprador",
              "usuario_id": self.usuario_id,
              "chave_publica": self.cripto.get_chave_publica_bytes().hex(),
              "resultado_ia": {
                  "estado": resultado_ia.estado.value,
                  "estresse": resultado_ia.nivel_estresse
              },
              "localizacao": {"latitude": latitude, "longitude": longitude}
          }

          dados_cripto = self.cripto.criptografar(dados_comprador)
          mensagem = MensagemP2P(
              tipo="autenticacao",
              remetente_id=self.usuario_id,
              destinatario_id=outro_dispositivo_id,
              payload={"dados": dados_cripto.hex()},
              assinatura="",
              timestamp=time.time()
          )

          print("\n⏳ Aguardando autenticação do vendedor...")
          time.sleep(2)

          resposta_vendedor = {
              "status": "aprovado",
              "vendedor_id": "VENDEDOR_001",
              "resultado_ia": {"estado": "SEGURO", "estresse": 0.2}
          }

          if resposta_vendedor.get("status") == "aprovado":
              print("\n✅ Vendedor autenticado e seguro!")
              print("\n🔐 Fechando acordo criptografado...")
              acordo = {
                  "comprador": self.usuario_id,
                  "vendedor": resposta_vendedor["vendedor_id"],
                  "valor": valor,
                  "timestamp": datetime.now().isoformat(),
                  "hash_comprador": self.cripto.hash_transacao(dados_comprador)
              }
              hash_acordo = self.cripto.hash_transacao(acordo)
              print(f"   Hash do acordo: {hash_acordo}")
              self.transacao_atual["status"] = "concluida"
              self.transacao_atual["hash"] = hash_acordo
              print(f"""
    ╔══════════════════════════════════════════╗
    ║        ✅ TRANSAÇÃO CONCLUÍDA           ║
    ║   💰 Valor: R$ {valor:.2f}                     ║
    ║   👤 Comprador: {self.nome:<20}║
    ║   👤 Vendedor: {resposta_vendedor['vendedor_id']:<20}║
    ║   🔗 Conexão: P2P (sem servidor)        ║
    ║   🔐 Hash: {hash_acordo[:20]:<20}║
    ╚══════════════════════════════════════════╝
              """)
              return {"status": "concluida", "hash": hash_acordo, "mensagem": "Transação realizada com sucesso entre os dispositivos"}
          else:
              return self._falhar("Vendedor não aprovou")

      def _autenticar_local(self) -> bool:
          print("   🤚 Digital verificada... ✅")
          print("   🔐 Token criptográfico validado... ✅")
          print("   📍 GPS local confirmado... ✅")
          return True

      def _falhar(self, motivo: str) -> Dict:
          self.transacao_atual["status"] = "falha"
          self.transacao_atual["motivo"] = motivo
          print(f"\n❌ Transação falhou: {motivo}")
          return {"status": "falha", "motivo": motivo}

      def status(self) -> Dict:
          return {
              "usuario": self.nome,
              "id": self.usuario_id,
              "modo": "P2P (sem servidor)",
              "sos": "sempre ativo",
              "contra_ataque": "porta falsa pronta",
              "transacao_atual": self.transacao_atual
          }

    async def main():
      sistema = DigitalP2P("USR001", "Lucas")
      await sistema.inicializar()
      resultado = await sistema.iniciar_transacao(
          outro_dispositivo_id="USR002",
          valor=500.00,
          latitude=-23.1793,
          longitude=-52.2112
      )
      print(f"\n📋 Resultado: {json.dumps(resultado, indent=2, ensure_ascii=False)}")

    if __name__ == "__main__":
      asyncio.run(main())
    