# Projeto de API REST da Livraria com Django e DRF

Bem-vindo ao projeto de API REST da Livraria Render! Este repositório contém o código-fonte e recursos relacionados à criação de uma API REST utilizando Django e Django REST Framework. A API foi desenvolvida como parte das aulas de Desenvolvimento Web no IFC - Campus Araquari, por Marco Andre Lopes Mendes (marcoandre@gmail.com).

## Visão Geral

Este projeto tem como objetivo fornecer uma API completa para a gestão de livrarias. O uso do Django e do Django REST Framework oferece uma base sólida e robusta para a criação de APIs RESTful.

## Instalação e Configuração

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em seu sistema.

2. Clone este repositório usando o seguinte comando:

   ```
   git clone https://github.com/marrcandre/livraria_render.git
   ```

3. Navegue até o diretório da API:

   ```
   cd livraria_render/api
   ```

4. Crie um ambiente virtual usando o [PDM](https://pdm.fming.dev/):

   ```
   pdm install
   ```

5. Crie o superusuário do Django:

   ```
   pdm run python manage.py createsuperuser
   ```

6. Aplique as migrações do banco de dados:

   ```
    pdm run python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:

   ```
   pdm run python manage.py runserver
   ```

A API estará acessível em `http://localhost:8000`.

## Uso da API

A documentação completa dos endpoints da API e exemplos de uso estão disponíveis na [Documentação da API](http://localhost:8000/api/swagger)

## Contribuição

Se você deseja contribuir para a API Livraria Render, siga estas etapas:

1. Fork este repositório.

2. Crie uma nova branch para a sua contribuição:

   ```
   git checkout -b minha-contribuicao
   ```

3. Faça suas modificações e commit.

4. Envie as mudanças para o seu repositório fork:

   ```
   git push origin minha-contribuicao
   ```

5. Abra um Pull Request neste repositório.

## Licença

Este projeto está licenciado sob a [Licença GPL](https://www.gnu.org/licenses/gpl-3.0.html), uma licença de software livre.

---

Agradecemos por considerar a contribuição para a API Livraria Render! Para mais informações, entre em contato com Marco André Lopes Mendes em marcoandre@gmail.com. Estamos ansiosos para ver as suas contribuições!