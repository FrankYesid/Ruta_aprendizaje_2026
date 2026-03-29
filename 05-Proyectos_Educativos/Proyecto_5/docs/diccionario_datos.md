# Diccionario de Datos - Spaceship Titanic

Para ayudarte a hacer estas predicciones, se te proporciona un conjunto de registros recuperados del sistema informático dañado de la nave espacial Titanic.

## train.csv
Registros personales de aproximadamente dos tercios (~8700) de los pasajeros, para ser utilizados como datos de entrenamiento.

- `PassengerId`: Un Id único para cada pasajero. Cada Id toma la forma `gggg_pp` donde `gggg` indica un grupo con el que viaja el pasajero y `pp` es su número dentro del grupo. Las personas en un grupo suelen ser miembros de la familia, pero no siempre.
- `HomePlanet`: El planeta del que partió el pasajero, típicamente su planeta de residencia permanente.
- `CryoSleep`: Indica si el pasajero eligió ser puesto en animación suspendida durante la duración del viaje. Los pasajeros en criosueño están confinados en sus cabinas.
- `Cabin`: El número de cabina donde se hospeda el pasajero. Toma la forma `deck/num/side`, donde `side` puede ser `P` para Babor (Port) o `S` para Estribor (Starboard).
- `Destination`: El planeta al que el pasajero desembarcará.
- `Age`: La edad del pasajero.
- `VIP`: Si el pasajero ha pagado por servicio VIP especial durante el viaje.
- `RoomService`, `FoodCourt`, `ShoppingMall`, `Spa`, `VRDeck`: Monto que el pasajero ha facturado en cada una de las muchas comodidades de lujo de la nave espacial Titanic.
- `Name`: El nombre y apellido del pasajero.
- `Transported`: Si el pasajero fue transportado a otra dimensión. Este es el **objetivo**, la columna que intentas predecir.

## test.csv
Registros personales para el tercio restante (~4300) de los pasajeros, para ser utilizados como datos de prueba. Tu tarea es predecir el valor de `Transported` para los pasajeros en este conjunto.

## sample_submission.csv
Un archivo de envío en el formato correcto.
- `PassengerId`: Id para cada pasajero en el conjunto de prueba.
- `Transported`: El objetivo. Para cada pasajero, predice True o False.
