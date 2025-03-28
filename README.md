🌐 Rede Social
Este é um projeto web desenvolvido com Flask que simula uma pequena rede social voltada para uma comunidade de estudos. Nele, os usuários podem criar contas, editar seus perfis, publicar postagens, visualizar o conteúdo de outros membros e interagir com um painel de administração de perfis.

🚀 Funcionalidades
Autenticação de Usuários

Cadastro, login e logout de usuários

Validação de e-mail e senha com segurança (hash com Bcrypt)

Login com opção "Lembrar-me"

Gerenciamento de Perfil

Upload e redimensionamento de foto de perfil

Atualização de nome, e-mail e cursos realizados

Cursos salvos como string separada por ponto e vírgula

Sistema de Postagens

Criação, edição e exclusão de posts

Edição permitida apenas para o autor da postagem

Visualização dinâmica de posts na página inicial

Painel de Usuários

Listagem de todos os usuários cadastrados (requer login)

Contador de posts por usuário

🧰 Tecnologias Utilizadas
Backend: Python, Flask

Banco de Dados: SQLAlchemy (ORM), SQLite (padrão)

Front-end: Jinja2, HTML5, CSS, Bootstrap

Forms & Validação: Flask-WTF, WTForms

Autenticação: Flask-Login, Bcrypt

Imagens: PIL (Pillow) para manipulação de fotos de perfil

Gerenciamento de Sessão: Cookies via Flask

🔒 Segurança
Senhas são armazenadas de forma segura usando hash Bcrypt

Ações restritas por login com @login_required

Proteção contra CSRF com Flask-WTF
