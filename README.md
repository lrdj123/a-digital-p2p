# 🖐️ A DIGITAL — Sistema P2P

    Sistema de segurança entre dispositivos **SEM servidor central**.
    A validação é feita diretamente entre as partes (P2P).

    > Não existe servidor para invadir. Não existe ponto único de falha.

    ## ✨ Funcionalidades

    | Módulo | Descrição |
    |---|---|
    | 🔐 **Criptografia E2E** | ECDH P-256 + AES-256-GCM |
    | 🧠 **IA Emocional** | Detecção de coação/estresse em tempo real |
    | 🚨 **SOS Invisível** | Alerta silencioso para contatos de confiança |
    | 🦠 **Contra-ataque** | Porta falsa que engana invasores |
    | 🔗 **Conexão P2P** | Sem intermediário, sem servidor central |

    ## 🚀 Como rodar

    ```bash
    pip install -r requirements.txt
    python main.py
    ```

    ## 📂 Estrutura

    ```
    a-digital-p2p/
    ├── main.py
    ├── requirements.txt
    └── modulos/
      ├── p2p/
      │   ├── conexao_direta.py    # MensagemP2P
      │   └── criptografia.py     # ECDH + AES-GCM
      ├── ia_emocional/
      │   └── analise_facial.py   # Detecção de coação
      ├── sos/
      │   └── sos_invisivel.py    # Alerta silencioso
      └── contra_ataque/
          └── porta_falsa.py      # Honeypot / trap
    ```

    ## 🛡️ Segurança

    - Chaves geradas localmente — nunca saem do dispositivo
    - Transações assinadas com ECDSA e verificadas pelo peer
    - SOS detecta coação via IA emocional facial
    - Porta falsa apresenta dados fictícios para invasores

    ---
    *Python 3.10+*
    