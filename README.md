# Z-API Message Sender

Aplicação Python para envio de mensagens WhatsApp em massa via Z-API, usando PostgreSQL via Supabase como banco de dados.

## Tecnologias usadas

- Python 3.7+
- [Z-API](https://www.z-api.io/)
- PostgreSQL via [Supabase](https://supabase.com/)
- Biblioteca `requests` para requisições
- Biblioteca `sqlalchemy` para ORM e conexão com banco
- Biblioteca  `python-dotenv` para variáveis de ambiente
- Biblioteca `logging` para facilitar depuração e monitoramento

## Instalação

1. Clone o projeto:

```bash
git clone https://github.com/capppp/zapi-message-sender.git
cd zapi-message-sender
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie e configure as variáveis de ambiente em um arquivo `.env` (exemplo abaixo):

```env
ENVIRONMENT=development (padrão) ou production (debug logger desativado)

DATABASE_CONNECTION_STRING=postgresql://usuario:senha@endereco_supabase:porta/nome_do_banco

ZAPI_INSTANCE_STRING=sua_instancia_zapi_aqui
ZAPI_CLIENT_TOKEN=seu_token_zapi_aqui
```

4. Configure o banco de dados PostgresSQL

No Supabase ou qualquer outro serviço compatível com PostgresSQL, crie a tabela `Contacts` com os campos:

- `id` do tipo `uuid`, sendo ele *primary key*
- `name` do tipo `texto`
- `phone` do tipo `texto`

## Uso

Você pode editar a mensagem padrão do envio em massa dentro do arquivo `main.py`:
```python
send_text(contact.phone, f"SUA MENSAGEM AQUI")
```

Depois, basta executar no terminal:

```bash
python main.py
```

# Licença

MIT License © Daniel (Cap) Endrell
