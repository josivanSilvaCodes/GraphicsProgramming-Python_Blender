
# MyFisrtCube.py
# Code write by Prof. Josivan Pereira da Silva, 2019
# Used in Graphics Programming classes at University
# To facilitate the learning by the students all the comments are in Portuguese
# Everyone can use it, but maintain the credits, please
# e-mail: josivan.engenharia@gmail.com


import bpy
 
#Definindo 4 vertices e 1 face
#Um array em Python com x,y,z de cada vertice/ponto 3D

# x = frente/tras, y = esquerda/direita, z = cima/baixo

verts = [(0,0,0), (0,0,5), (0, 5, 5), (0, 5, 0),
         (0,0,5), (-5,0,5), (-5,5,5), (0,5,5),
         (0,0,0), (-5,0,0), (-5,5,0), (0,5,0)] 
#verts = [(0,0,0),(0,0,2),(0,-2,2),(0,-2,0)] # Com normal para frente
 
# O Array de faces contém uma face em formato Quad
# A sequencia numerica se refere aos item do array de vertices
# A ordem define como a face será contruida
faces = [(0,1,2,3), (4,5,6,7), (8,9,10,11)]

edges = []

#Define a malha e o objeto "Plane"
mymesh = bpy.data.meshes.new("Plane")
 
#Relaciona a malha ao objeto
myobject = bpy.data.objects.new("Plane", mymesh)

#Define a posição do objeto no espaço
myobject.location = bpy.context.scene.cursor_location # Posição do cursor
bpy.context.scene.objects.link(myobject) # Liga o objeto ao contexto da cena

# Criação da malha
# Esse método tem um atributo opcional para as edges, que pode ser vazio
mymesh.from_pydata(verts,edges,faces) 
mymesh.update(calc_edges=True) #Calcula as edges

edges = myobject.data.edges # pega as edges e coloca na variavel

print("")
print("===========================================================")
print('Verts: ', verts) # imprime a lista/array de vertices

print('Edges: ') 
for e in edges:
    print('{}.  {} {}'.format(e.index, e.vertices[0], e.vertices[1]))
	
print('Faces: ', faces)
print("===========================================================")
print("")
