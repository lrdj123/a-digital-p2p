import random, time
    from dataclasses import dataclass
    from enum import Enum

    class EstadoEmocional(Enum):
      SEGURO     = "SEGURO"
      ALERTA     = "ALERTA"
      ESTRESSADO = "ESTRESSADO"
      COAGIDO    = "COAGIDO"

    @dataclass
    class ResultadoEmocional:
      estado: EstadoEmocional
      nivel_estresse: float
      alerta_sos: bool
      confianca: float
      descricao: str

    class AnalisadorEmocional:
      LIMIAR_SOS = 0.75

      def __init__(self):
          print("   [IA] Modelo emocional carregado (local)")

      def analisar(self, duracao_ms: int = 300) -> ResultadoEmocional:
          time.sleep(duracao_ms / 1000)
          nivel = random.uniform(0.05, 0.45)
          if nivel >= self.LIMIAR_SOS:
              return ResultadoEmocional(EstadoEmocional.COAGIDO,    nivel, True,  0.93, "Sinais de coacao detectados")
          if nivel >= 0.55:
              return ResultadoEmocional(EstadoEmocional.ESTRESSADO, nivel, False, 0.88, "Estresse elevado")
          if nivel >= 0.35:
              return ResultadoEmocional(EstadoEmocional.ALERTA,     nivel, False, 0.90, "Leve tensao")
          return     ResultadoEmocional(EstadoEmocional.SEGURO,     nivel, False, 0.95, "Usuario calmo e seguro")
    