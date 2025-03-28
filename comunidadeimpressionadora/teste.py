from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post


#with app.app_context(): #É necessario para tudo que tem que ser feito no BD
#Criar o BD
'''
with app.app_context(): 
    database.create_all()
'''

#Adicionar Usuarios

with app.app_context():
    
    usuario = Usuario(username="Paulo", email="paulo@gmail.com", senha="123456")
    usuario2 = Usuario(username="Ricardo", email="ricardo@gmail.com", senha="123456")

    database.session.add(usuario)
    database.session.add(usuario2)

    database.session.commit()


#Pesquisar todos os usuarios e imprimir oque quiser pela posição
'''
with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios[1].username)
'''

#Pesquisar o usuario com o filtro, no caso encontrou o usarname do email 
'''
with app.app_context():
    usuario_teste =  Usuario.query.filter_by(email='paulo@gmail.com').first()
    print(usuario_teste)
    print(usuario_teste.username)
'''

#Realizando o primeiro post
'''
with app.app_context():
    meu_post = Post(id_usuario = 1, titulo = "Primeiro Post do Paulo", corpo = "Ai caliquinha, Raja Ram vem ai")
    database.session.add(meu_post)
    database.session.commit()
'''

#Mostrando o username do autor do post
'''
with app.app_context():
    post =  Post.query.first()
    print(post.autor.username)
'''  

#Limpando BD
'''
with app.app_context(): 
    database.drop_all()
'''
with app.app_context():
    Usuario.query.all()