# SARAPY

Library for processing SARAPICO project metadata of _AMG_.

#### Version 0.3.5

- Se implementa clase _DistanceImputer_.

#### Version 0.3.4

- Se actializa _dataPositions_ de PlantinFMCreator.

#### Version 0.3.3

- Se cambia el nombre de la clase FMCreator a PlantinFMCreator. Se modifica la matriz transformada quitando el dato de distorsión de Fertilizante.

#### Version 0.3.2

- Se agrega property en FMCreator para acceder a \_dataPosition. Se cambia la forma de los diccionarios de _dataPosition_ de FMCreator, TimeSeriesProcesor y TLMSensorDataExtractor. Además, ahora este atributo se crea en init().
- Se corrige bug por división por cero en el cálculo de _ratio_dCdP_ de TimeSeriesProcessor.

#### Version 0.3.1

- Se corrige forma de acceder a los datos de X en FMCreator.fit().

#### Version 0.3.0

- Se implementa clase FMCreator.
- Se quita método TLMSensorDataExtractor.getMetadataRevisionNumber().
- Se agrega cálculo de ratio_dCdP en TimeSeriesProcessor
- Se cambia nombre de clase _GeoAnalyzer_ por _GeoProcessor_
- Se agrega atritubo dataPositions en _TLMSensorDataExtractor_ para poder saber qué representa cada columna dentro del array devuelto por tranform.
- Se agrega dataPositions a TimeSeriesProcessor

#### Version 0.2.6

- Se cambia la forma de computar los deltaO de TimeSeriesProcessor. Ahora se hace deltaO*i = T_i - T*(i-1)

#### Version 0.2.5

- Se corrige GeoAnalyzer.transform() para que entregue el array con un cero adicional al final ya que estaba entregando _(n-1,2)_ datos cuando X es de shape (n,2).

#### Version 0.2.4

- Se corrige nombre de atributos de TLMSensorDataExtractor

#### Version 0.2.3

- Se modifican métodos _TLMSensorDataExtractor.fit()_ y _TLMSensorDataExtractor.transofmr()_ ya que no se habían considerado los datos de FIX y SIV de la metadata.

#### Version 0.2.2

- Se quita el chequeo de valores nulos en TimeSeriesProcessor.fit()
- Si la cantidad de filas de X que se pasa a TimeSeriesProcessor.fit() es igual a uno, los tiempos de operación y de caminata se hacen cero. El método transform devolverá un array de (1,3) donde el único valor diferente de cero será el deltaC.

#### Version 0.2.1

- Se corrige _init.py_ de dataProcessing.

#### Version 0.2.0

- Transforming some attributs to private attributes. Adding @property for getters.
- Created GNSSDataProcessor class.
- Created TimeSeriesProcessor class.

#### Version 0.1.4

Setting an **init**.py file for TLMSensorDataExtractor module.

#### Version 0.1.3

Setting version.py file.

#### Version 0.1.1 and Version 0.1.0

Just for testing.

### Docs

Documentation [here](https://github.com/lucasbaldezzari/sarapy/blob/main/docs/Docs.md).
