# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para um catálogo de livros usando FastAPI. Pratique rotas HTTP, parâmetros de caminho, corpos JSON e validação de dados.

## 📝 Tarefas

### 🛠️ Executar a API e criar uma rota de saúde

#### Descrição
Na pasta que contém `starter-code.py`, instale `fastapi` e `uvicorn` com `python -m pip install fastapi uvicorn`. Inicie o servidor com `python starter-code.py` e implemente a rota `GET /health` para confirmar que a API está disponível.

#### Requisitos
O programa concluído deve:

- Iniciar sem erros usando `python starter-code.py`.
- Responder a `GET /health` com status HTTP 200 e o JSON `{ "status": "ok" }`.
- Exibir a documentação interativa do FastAPI em `http://127.0.0.1:8000/docs`.

### 🛠️ Consultar o catálogo de livros

#### Descrição
Implemente rotas para listar os livros do catálogo e consultar um livro pelo seu identificador numérico. Use os dados iniciais fornecidos no starter code.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books` com a lista de livros em JSON.
- Responder a `GET /books/{book_id}` com o livro correspondente ao identificador.
- Retornar status HTTP 404 quando o identificador não existir.
- Aceitar `book_id` como parâmetro inteiro de caminho.

### 🛠️ Adicionar e remover livros

#### Descrição
Implemente a criação de livros a partir de um corpo JSON e a remoção de livros pelo identificador. Use a documentação em `/docs` para enviar requisições e observar as respostas.

Exemplo de corpo para criar um livro:

```json
{
  "title": "Dune",
  "author": "Frank Herbert"
}
```

#### Requisitos
O programa concluído deve:

- Responder a `POST /books` usando os campos `title` e `author` e retornar o livro criado com um identificador único e status HTTP 201.
- Usar o modelo Pydantic fornecido para validar o corpo; campos obrigatórios ausentes devem resultar em status HTTP 422.
- Responder a `DELETE /books/{book_id}` removendo o livro solicitado.
- Retornar status HTTP 404 ao tentar consultar ou remover um livro inexistente.
- Informar que os dados ficam apenas em memória e são reiniciados quando o servidor é encerrado.
