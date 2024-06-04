# Trabajo Práctico Algoritmia 2024
## Fundamentos de Informática/Introducción a la Algoritmia.

Una empresa de turismo desea lanzar una aplicación que permita a sus usuarios
planificar su viaje por distintos destinos de América Latina. Para ello, cuenta con una
lista de destinos que puede ofrecer a sus usuarios. El punto de origen es Buenos
Aires, Argentina y el usuario podrá decidir paso a paso qué otros destinos desea
visitar.

Desarrollar un programa que permita al usuario realizar el itinerario de su viaje. El mismo deberá mostrar a través de un menú los destinos disponibles para viajar con su distancia. La distancia a cada destino debe ser un número generado aleatoriamente que deberá ser mayor a 50km y nunca menor que 1000km. 
El usuario podrá elegir los destinos de su viaje hasta ingresar -1 para darlo por finalizado. No se podrán repetir destinos en el itinerario.

Una vez finalizada la entrada de datos el programa deberá informar la cantidad total de kilómetros recorridos, la cantidad de destinos visitados, la cantidad de kilómetros promedio por destino, la distancia más larga recorrida. Por último, mostrar un listado de los destinos visitados ordenado en forma ascendente según la distancia recorrida hasta cada uno.
### Ejemplo

```
Destinos disponibles
1) Lima, Peru - 200km
2) Brasilia, Brasil - 133km
3) Bogota, Colombia - 492km
4) Quito, Ecuador - 738 km.
5) Montevideo, Uruguay - 78km
-1) Finalizar viaje
Entrada usuario: 2

Destinos disponibles
1) Lima, Peru - 200km
2) Brasilia, Brasil - 133km
3) Bogota, Colombia - 492km
4) Quito, Ecuador - 738 km.
5) Montevideo, Uruguay - 78km
-1) Finalizar viaje
Entrada usuario: 4

Destinos disponibles
1) Lima, Peru - 200km
2) Brasilia, Brasil - 133km
3) Bogota, Colombia - 492km
4) Quito, Ecuador - 738 km.
5) Montevideo, Uruguay - 78km
-1) Finalizar viaje
Entrada usuario:5

Destinos disponibles
1) Lima, Peru - 200km
2) Brasilia, Brasil - 133km
3) Bogota, Colombia - 492km
4) Quito, Ecuador - 738 km.
5) Montevideo, Uruguay - 78km
-1) Finalizar viaje
Entrada usuario -1

Cantidad total de kilometros recorridos: 949km
Cantidad de destinos visitados: 3
Cantidad de kilometros promedio por destino: 316,3
Distancia mas larga recorrida: 738
Listado ordenado de tramos recorridos:
Destino 3: Montevideo, Uruguay - 78km
Destino 1: Brasilia, Brasil - 133km
Destino 2: Quito, Ecuador - 738 km.
```
