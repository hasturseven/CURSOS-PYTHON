def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
	return funcion_entrante("David")
""""Las primeras dos funciones son obvias en su resultado, donde nos mostrarán un mensaje con el valor de la variable nombre. La tercera función puede ser más compleja de predecir, ya que toma otra función como entrada. Veamos que pasa cuando colocamos una función como atributo:"""
print(consume_funciones(presentarse))
print(consume_funciones(estudiemos_juntos))
""""Pongamos atención en cómo la función consume_funciones() se escribe con paréntesis para ser ejecutada, mientras que la función presentarse y estudiemos_juntos solo hace referencia a estas."""


print()
print()

"""LAS FUNCONCES DECORADORAS USO"""

def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

# def zumbido():
# 	print("Buzzzzzz")

# zumbido = funcion_decoradora(zumbido)

#zumbido()
"""COMO EN VERDAD SE IMPLEMENTAN LAS FUNCIONES DECORADAS SIEMPRE SE PONE ESE ARROBA ENCIMA Y SE AHORRA UNO LO DE ZUMBIDO=FUNCION_DECORADORA(ZUMBIDO) Y SIEMPRE QUE LLAME A ZUMBIDO SE EJECUTARA LA FUNCION QUE LLAME FUNCION_DECORADORA(FUNCION) ESTO SIRRVE PARA De esta manera obtendremos funciones dinámicas (que pueden cambiar) sin tener nosotros que cambiar su código fuente!"""
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")
zumbido()








print()
print()
#oEJEMPLO DE ANIDAMIENTO DE FUNCIONES
def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()

funcion_mayor()
