#DATA
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
#OBTENER NOMBRES DE LOS QUE SOLO CONOCEN PYTHON UNA FUE USANDO LSO BUCLES FOR Y LA OTRA USANDO FILTER QUE ES MEJOR

# list_python=[] 
# for personas in DATA:
    
#     if personas['language']=='python':
#         list_python.append(personas)

# print(list_python)

list_filter_python=list(filter(lambda x: x['language']=='python',DATA))

print(list_filter_python)

#pero como esto me tira todos los argumentos y yo solo quiero el nombre usare map para que me imprima como quierp
print()
print("ahora lista con solo el nombre del anteriror filtro que pusimos")

list_map_python_nombre=list(map(lambda trabajadores_python: trabajadores_python['name'],list_filter_python))

print(list_map_python_nombre)

print()

print("PERSONAS QUE TRABAJAN EN PLATZI")

list_filter_platzi=list(filter(lambda x: x['organization']=='Platzi',DATA))
print(list_filter_platzi)

#AHORA CON LIST COMPREHENSION GUARDAREMOS SOLO EL NOMBRE
print("estos son los trabajadores que saben java")
list_compre_nombre_java=[trabajador['name'] for trabajador in DATA if trabajador['language']=='java']

print(list_compre_nombre_java)

