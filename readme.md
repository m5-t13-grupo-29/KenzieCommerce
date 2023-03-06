# Python

# Instruções de uso:

1. Após clonar o repositório, crie seu ambiente virtual:
```bash
python -m venv venv
```
2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```
3. Faça a instalação dos pacotes utilizados no projeto:

```bash
pip install -r requirements.txt
```

4. Preencha as variáveis de ambiente seguindo o exemplo de `.env.example`:

#### SECRET_KEY= " Secret key da aplicação "
#### DB_NAME= " Nome do db"
#### DB_USER= " Nome do usuário db"
#### DB_PASSWORD= " Senha do usuário db"

5. Rode a aplicação para visualizar se ocorreu tudo certo:

```bash
python manage.py runserver
```
