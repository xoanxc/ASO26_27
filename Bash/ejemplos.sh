#!/bin/bash

# --- Declaración de variables ---
variable=2
nombre="iago"
conjunto=$variable$nombre
conjunto2="$variable $nombre"

# --- Uso de variables --- 
echo $variable
echo $nombre
echo $conjunto
echo $conjunto2

# --- Variables de script ---
echo $0 # El nombre del script
echo $1 # El primer parámetro
echo $9 # El noveno parámetro
echo $# # Número de parámetros
echo $* # Todos los parámetros en forma de lista
echo $? # El estado de la ejecución de la última instrucción
ls ñ # Va a fallar
echo $? # Distinto de 0

# --- Variables de entorno ---
echo $USER # El usuario que ejecuta el script
echo $UID # El identificador de usuario que ejecuta el script
echo $HOME # Directorio personal del usuario que ejecuta el script
echo $PWD # Directorio desde donde se ejecuta el script

# --- Entrada de datos por consola ---

read -rep "Introduce un valor numérico: " valor_1 #Solicita valores y almacena en variable
echo "El valor escogido es $valor_1"

echo "Hola"
echo "¿Cómo estás?"
read -rep "" actitud

echo $valor_1 > log.txt # Crea fichero y redirige stdout a fichero
echo $valor_1 >> log.txt # Crea fichero, añade al final y redirige stdout a fichero
echo $valor_1 2> log.txt # Crea fichero y redirige stderr a fichero
echo $valor_1 &> log.txt # Crea fichero y redirige stdout y stderr al ficher


# --- Operadores aritméticos ---
# 1 - Crea un script que solicite dos valores y muestre por pantalla los resultados de las diferentes operaciones aritméticas

read -rep "Introduce el primer valor: " valor_1
read -rep "Introduce el segundo valor: " valor_2

let "resultado=$valor_1 + $valor_2"
echo "$valor_1 + $valor_2 = $resultado"

resultado=$(($valor_1 - $valor_2))
echo "$valor_1 - $valor_2 = $resultado"

let "resultado=$valor_1 * $valor_2"
echo "$valor_1 * $valor_2 = $resultado"

let "resultado=$valor_1 / $valor_2"
echo "$valor_1 / $valor_2 = $resultado"

let "resultado=$valor_1 % $valor_2"
echo "$valor_1 % $valor_2 = $resultado"


# 2 - Crea un programa que reciba por parámetro un valor numérico entero. Comprueba si es par o impar y muestralo por pantalla.

valor=$1

let "resto=$valor % 2"

if [ $resto -eq 0 ]
then
	echo "El valor es par"
else
	echo "El valor es impar"
fi

# 3 - Crea un programa que solicite un valor. Comprobar si es negativo, positivo o 0

read -rep "Introduce un valor entero: " entero

if [ $entero -gt 0 ]
then
	echo "El valor es positivo"
elif [ $entero -lt 0 ]
then
	echo "El valor es negativo"
else
	echo "El valor es 0"
fi


# 4 - Crea un programa que reciba por parámetro un código (es, gl o en) y muestre por pantalla el saludo en el idioma escogido.

codigo=$1
case $codigo in
	"es")
		echo "Hola buenas tardes"
	;;
	"gl")
		echo "Ola boas tardes"
	;;
	"en")
		echo "Hello good afternoon"
	;;
	*)
		echo "Opción no válida"
	;;
esac

# 5 - Crea un programa que muestre la tabla de multiplicar del valor solicitado al usuario


read -rep "Introduce un valor: " valor

while [ $valor -le 0 ]
do
	echo "Error, valor no válido"
	read -rep "Introduce un valor: " valor
done

contador=1

while [ $contador -lt 10 ]
do
	let "resultado=$valor * $contador"
	echo "$valor x $contador = $resultado"
	
	let "contador=$contador + 1"
done


for valor in {1..10}
do
	echo "El valor es $valor"
done

for valor in esto es un conjunto de valores arbitrario
do
	echo $valor
done

for valor in $*
do
	echo $valor
done


# 6 - Crea un programa que permita calcular los números primos entre el 1 y el 100

isPrimo=0 # Si es 0, el valor es primo
contador=1 # Contador usado para el cálculo de valores
contador_aux=1 # Usado para el segundo bucle y calcular si el valor es primo o no

while [ $contador -lt 100 ]
do
	isPrimo=0
	contador_aux=1
	while [ $contador_aux -le $contador -a $isPrimo -eq 0 ]
	do
		let "resultado=$contador % $contador_aux"
		if [ $contador_aux -ne 1 -a $contador_aux -ne $contador ]
		then
			if [ $resultado -eq 0 ]
			then
				isPrimo=1
			fi
		fi
		let "contador_aux=$contador_aux + 1"
	done
	
	if [ $isPrimo -eq 0 ]
	then
		echo "El valor $contador es primo"
	fi
	
	let "contador=$contador + 1"
done


resultado_ls=$(ls /bin)

for valor in $resultado_ls
do
	echo $valor
done

resultado_pwd=$(cat /etc/passwd | cut -d: -f1)

for valor in $resultado_pwd
do
	echo $valor
done


# 7 - Crea un programa que solicite al usuario valores enteros hasta que decida detenerse (con -1, por ejemplo). Mostrar el número de valores introducidos (salvo el -1), el valor medio de los valores, el máximo y el mínimo

control=0

max=-99999999
min=99999999
cantidad=0
acumulado=0

while [ $control -eq 0 ]
do
	read -rep "Introduce un valor numérico entero, -1 para terminar: " valor
	if [ $valor -eq -1 ]
	then
		control=1
	else
		# Control de número de valores
		let "cantidad=$cantidad + 1"
		# Control de valor máximo
		if [ $valor -gt $max ]
		then
			max=$valor
		fi
		# Control de valor mínimo
		if [ $valor -lt $min ]
		then
			min=$valor
		fi
		let "acumulado=$acumulado+$valor"
	fi
done

let "media=$acumulado / $cantidad"

echo "Los valores son $cantidad"
echo "La media es $media"
echo "El máximo es $max"
echo "El mínimo es $min"


# 8 - Crea un programa que reciba por parámetro 2 valores enteros. Muestra el menor de ellos.

function comparar() {
	valor_1=$1
	valor_2=$2
	
	if [ $valor_1 -gt $valor_2 ]
	then
		echo "El primer valor es mayor que el segundo"
	elif [ $valor_1 -lt $valor_2 ]
	then
		echo "El segundo valor es mayor que el primero"
	else
		echo "Los valores son iguales"
	fi
}

param_1=$1
param_2=$2

resultado_comparar=$(comparar $param_1 $param_2)

echo "Resultado: $resultado_comparar"


# 9 - Crea un programa que permita seleccionar de una lista de formas geométricas y además se pueda decidir si calcular el área o el perímetro. 


function calculo_area() {
	forma=$1
	
	case $forma in
		1)
			read -rep "Introduce el lado del cuadrado: " lado
			let "resultado=$lado * $lado"
			echo $resultado
		;;
		2)
			read -rep "Introduce el radio del círculo: " radio
			let "resultado=3*($radio * $radio)"
			echo $resultado
		;;
		3)
			read -rep "Introduce la base del triángulo: " base
			read -rep "Introduce la altura del triángulo: " altura
			let "resultado=$base * $altura / 2"
			echo $resultado
		;;
		*)
			echo "Forma no válida"
		;;
	esac
}

function calculo_perimetro() {
	forma=$1
	case $forma in
		1)
			read -rep "Introduce el lado del cuadrado: " lado
			let "resultado=$lado * 4"
			echo $resultado
		;;
		2)
			read -rep "Introduce el radio del círculo: " radio
			let "resultado=2 * 3 * $radio"
			echo $resultado
		;;
		3)
			read -rep "Introduce el lado del triángulo: " lado
			let "resultado=$lado * 3"
			echo $resultado		
		;;
		*)
			echo "Forma no válida"
		;;
	esac
}

function calculo() {
	forma=$1
	echo "¿Qué cálculo quieres hacer?"
	echo "1. Área"
	echo "2. Perímetro"
	read -rep "" opcion
	
	if [ $opcion -eq 1 ]
	then
		calculo_area $forma
	elif [ $opcion -eq 2 ]
	then
		calculo_perimetro $forma
	fi

}

function forma() {
	echo "Selecciona la forma de la que quieres realizar cálculos:"
	echo "1. Cuadrado"
	echo "2. Círculo"
	echo "3. Triángulo"
	echo "4. Salir"
	read -rep "" forma
	
	if [ $forma -eq 4 ]
	then
		echo "Hasta luego"
		exit 0
	else
		calculo $forma
	fi
}

forma


# 10 - Utilizando el programa anterior, realiza las siguientes tareas:
# a. Prevención de errores: si el usuario introduce un valor que no debería, se mostrará un mensaje de ayuda.
# b. El mensaje del resultado debe almacenarse como un resultado de la función y mostrar un mensaje más detallado del resultado 



function ayuda(){
	echo "Valor no válido"
	echo "Debe introducirse uno de los valores indicados (1,2 o 3) en las formas"
	echo "Debe introducirse uno de los valores indicados (1 o 2) en el cálculo" 
}

function calculo_area() {
	forma=$1
	
	case $forma in
		1)
			read -rep "Introduce el lado del cuadrado: " lado
			let "resultado=$lado * $lado"
			echo "Área = $lado x $lado = $resultado"
			
			echo $resultado
		;;
		2)
			read -rep "Introduce el radio del círculo: " radio
			let "resultado=3*($radio * $radio)"
			echo "Área = PI * $radio^2 = $resultado" 
			echo $resultado
		;;
		3)
			read -rep "Introduce la base del triángulo: " base
			read -rep "Introduce la altura del triángulo: " altura
			let "resultado=$base * $altura / 2"
			echo "Área = $base X $altura / 2 = $resultado"
			echo $resultado
		;;
		*)
			ayuda
		;;
	esac
}

function calculo_perimetro() {
	forma=$1
	case $forma in
		1)
			read -rep "Introduce el lado del cuadrado: " lado
			let "resultado=$lado * 4"
			echo "Perímetro = $lado * 4 = $resultado"
			echo $resultado
		;;
		2)
			read -rep "Introduce el radio del círculo: " radio
			let "resultado=2 * 3 * $radio"
			echo "Perímetro = 2 X PI X $radio = $resultado"
			echo $resultado
		;;
		3)
			read -rep "Introduce el lado del triángulo: " lado
			let "resultado=$lado * 3"
			echo "Perímetro = $lado * 3 = $resultado"
			echo $resultado		
		;;
		*)
			ayuda
		;;
	esac
}

function calculo() {
	forma=$1
	echo "¿Qué cálculo quieres hacer?"
	echo "1. Área"
	echo "2. Perímetro"
	read -rep "" opcion
	
	resultado=0
	
	if [ $opcion -eq 1 ]
	then
		resultado=$(calculo_area $forma)
		
	elif [ $opcion -eq 2 ]
	then
		resultado=$(calculo_perimetro $forma)
	else
		ayuda
	fi
	
	
	echo $resultado

}

function forma() {
	echo "Selecciona la forma de la que quieres realizar cálculos:"
	echo "1. Cuadrado"
	echo "2. Círculo"
	echo "3. Triángulo"
	echo "4. Salir"
	read -rep "" forma
	
	if [ $forma -eq 4 ]
	then
		echo "Hasta luego"
		exit 0
	elif [ $forma -ge 1 -a $forma -le 3 ]
	then
		resultado=$(calculo $forma)
	else 
		ayuda
	fi
	
	if [ $forma -eq 1 ]
	then
		echo "El resultado del cálculo del cuadrado es $resultado"
	elif [ $forma -eq 2 ]
	then
		echo "El resultado del cálculo del círculo es $resultado"
	elif [ $forma -eq 3 ]
	then
		echo "El resultado del cálculo del triángulo es $resultado"
	fi
	
}

forma


numeros=(1 2 3 4 5)

echo ${numeros[@]}

numeros=(${numeros[@]} 6)

echo ${numeros[@]}

numeros=(0 ${numeros[@]})

echo ${numeros[@]}

pares=(2 4 6 8 10)
impares=(1 3 5 7 9)

enteros=(${impares[@]} ${pares[@]})

echo ${enteros[@]}




















