
# ⁡⁢⁣⁢​‌‍‌‍tipado para variabls y funciones en python (es como en java) ​⁡, se usa en la industria para hacer un poco mas fuerte el programa

#⁡⁢⁣⁣​‌‌‍tipado para variables:

from inspect import _void


numero : int;

numero1 :float = 5.2;

stringss : str;

stringss2 : str = 'soy un crack'

boleanos : bool = True

boleanos2 : bool;

print(numero1)

#⁡⁣⁣⁢​‌‍‌tipado de funciones DESPUES DE -> SE PONE LO QUE RETORINARA LA FUNCION ​⁡,⁡⁣⁢⁣​‌‍‌ 𝗔𝗦𝗜 𝗡𝗢 𝗟𝗘 𝗣𝗔𝗦𝗘𝗠𝗢𝗦 𝗟𝗢𝗦 𝗗𝗔𝗧𝗢𝗦 𝗤𝗨𝗘 𝗘𝗦𝗧𝗔𝗠𝗢𝗦 𝗣𝗜𝗗𝗜𝗘𝗡𝗗𝗢 𝗡𝗢 𝗠𝗘 𝗚𝗘𝗡𝗘𝗥𝗔𝗥𝗔 𝗘𝗥𝗥𝗢𝗥 𝗬 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗔𝗥𝗔 𝗘𝗟 𝗣𝗥𝗢𝗚𝗥𝗔𝗠𝗔 𝗣𝗔𝗥𝗔 𝗘𝗩𝗜𝗧𝗔𝗥 𝗘𝗦𝗧𝗢 𝗨𝗦𝗔𝗠𝗢𝗦 𝗘𝗟 𝗠𝗢𝗗𝗨𝗟𝗢 𝗺𝘆𝗽𝘆​⁡

def sumar(numero2 : int , numero3 : int ) -> int:
    return numero2+numero3

def vacia(palabra : str , palabra2 : str ) -> _void:
    print(palabra+palabra2)

vacia("sergio ","el crack")

print(sumar(1,2))


print("si le paso cadenas no me generara error me dara = ",sumar('1','2') , " para que esto no ocurra usamos el modulo mypy para que marque errores")


#PARA TIPAR ESTRUCTURAS DE DATOS DESPUES DE TENER PYTHON 3.10 LO HACEMOS COMO SIEMPRE PONIENDO EL TIPO DE DATO  EJ
"""
positives: List [int] = [1,2,3,4,5]

users: Dict [str, int] = {
	"argentina": 1.
	"mexico": 34,
	"colombia": 45,
}

countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]
"""


#  ​‌‍‌⁡⁢⁣⁢P​ARA TIPAR ESTRUCTURAS TENDREMOS QUE IMPORTAR  from typing import Tuple, Dict, List SEGUN EL TIPO DE ESTRURCTURA
#  A USAR⁡​

from typing import Tuple, Dict, List

positivos : list [int];


CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
	{
		"coord1": (1,2),
		"coord2": (3,5)
	},
	{
		"coord1": (0,1),
		"coord2": (2,5)
	}
]

