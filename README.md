## API FastAPI com TDD

**Descrição**

Este repositório contém a implementação de uma API FastAPI com TDD para um projeto da DIO. A API é construída com Python e utiliza o framework FastAPI para fornecer uma interface RESTful para interagir com os dados do projeto.

**Pré-requisitos**

* **Poetry:** Gerenciador de dependências Python. Você pode instalá-lo seguindo as instruções em [https://python-poetry.org/docs/cli/](https://python-poetry.org/docs/cli/).
* **Python:** Versão 3.7 ou superior. Você pode verificar sua versão do Python executando o comando `python3 --version` no terminal.

**Instalação**

1. Clone este repositório no seu computador local.
2. Acesse o diretório do projeto.
3. Instale as dependências do projeto executando o seguinte comando no terminal:

```bash
make precommit-install
```

**Executando a API**

Para executar a API, basta executar o seguinte comando no terminal:

```bash
make run
```

Isso iniciará o servidor FastAPI e a API estará disponível na porta `8000`. Você pode testar a API usando ferramentas como Postman ou curl.

**Documentação da API**

A documentação da API está disponível em formato Swagger em [http://localhost:8000/docs](http://localhost:8000/docs). A documentação fornece informações detalhadas sobre os endpoints da API, seus métodos HTTP, parâmetros e respostas.

**Contribuindo**

Se você deseja contribuir para este projeto, siga estas etapas:

1. Crie um fork deste repositório.
2. Clone o fork para o seu computador local.
3. Crie uma nova branch para suas alterações.
4. Faça suas alterações no código.
5. Teste suas alterações completamente.
6. Envie um pull request para este repositório.

Agradecemos a sua contribuição!

**Observações**

* Este é um projeto em desenvolvimento e pode estar sujeito a alterações.
* Se você tiver alguma dúvida ou problema, por favor, envie um issue neste repositório.

**Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
