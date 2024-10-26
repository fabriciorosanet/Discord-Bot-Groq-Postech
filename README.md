# Discord Bot Integração GroqCloud - POSTECH

Este projeto é um bot para Discord que utiliza a API do GroqCloud para gerar respostas automáticas a partir das mensagens recebidas.

O bot responde automaticamente quando mencionado, utilizando um modelo da GroqCloud para criar respostas baseadas no conteúdo enviado pelo usuário.

## Funcionalidades

- Respostas automáticas usando um modelo da GroqCloud (ex.: llama3-8b-8192).
- Ativação ao ser mencionado em mensagens.
- Integração com API da GroqCloud para geração de respostas inteligentes.

## Requisitos

- Python 3.9+
- Discord.py (`discord.py`)
- Groq (`groq`)
- Python-dotenv (`python-dotenv`)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt

3. Defina o token do bot do Discord e a URI do MongoDB no arquivo .env:

   ```bash
   DISCORD_TOKEN=seu_token
   GROQ_API_KEY=sua_chave_api_groqcloud

4. Execute o bot:

   ```bash
   python main.py

## Como usar

1. O bot será iniciado e ficará online, pronto para receber comandos.
2. Sempre que for mencionado em uma mensagem, o bot processará o conteúdo da mensagem e responderá automaticamente utilizando a API da GroqCloud e modelo de LLM adicionado. Nesse projeto o modelo é: llama3-8b-8192

## Funções importantes

- Função generate_groq_response(prompt): Conecta-se à API da GroqCloud e gera uma resposta para o prompt fornecido.
- Função on_message: Monitora as mensagens recebidas, e se o bot for mencionado, extrai o conteúdo e envia a resposta gerada para o canal.
- Função split_message: Divide a resposta em partes menores para respeitar o limite de 2000 caracteres imposto pelo Discord.

## Usabilidade

```bash
   @MentorIA Como posso melhorar minhas habilidades de programação?

   O bot responderá automaticamente com uma mensagem gerada pela GroqCloud.
````   

<h2 id="colab">🤝 Colaboradores</h2>

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQFhg6aT98EYyQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1697061290400?e=1735171200&v=beta&t=I7QymWDGwsoAsobMDPcCba6KiP3cvSA8LnWUF2G9nzU" width="100px;" alt="Fabricio Rosa"/><br>
        <sub>
          <b>Fabrício Rosa</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQE-5o3qpWIN9g/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1710954940792?e=1735171200&v=beta&t=7vLCKrr7DJio8MREsd9pBijdp8TjUFA5RdkCJpetsS0" width="100px;" alt="Eduardo Bortoli"/><br>
        <sub>
          <b>Eduardo Bortoli</b>
        </sub>
      </a>
    </td>
</table>