###Documentación en https://github.com/lucasbaldezzari/sarapy/blob/main/docs/Docs.md

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import warnings
from sarapy.dataProcessing import TLMSensorDataExtractor, TimeSeriesProcessor, GeoProcessor
from sarapy.preprocessing import DistancesImputer

class PlantinFMCreator(BaseEstimator, TransformerMixin):
    """La clase FMCreator se encarga de crear la Feature Matrix (FM) a partir de los datos de telemetría. Se utilizan las clases TLMSensorDataExtractor, TimeSeriesProcessor y GeoProcessor para realizar las transformaciones necesarias.
    
    Versión 0.1.0
    
    En esta versión la matriz de características está formada por las siguientes variables
    
    - DST_PT: Distorsión de plantín
    - deltaO: delta operación
    - ratio_dCdP: Ratio entre el delta de caminata y delta de pico abierto
    - distances: Distancias entre operaciones
    """
    
    def __init__(self, imputeDistances = True, distanciaMedia:float = 1.8,
                 umbral_mismo_lugar:float = 0.3, dist_mismo_lugar = 0.0,
                 umbral_ratio_dCdP:float = 0.5, deltaO_medio = 4):
        """Inicializa la clase FMCreator.
        
        Args:
            - imputeDistances: Si es True, se imputan las distancias entre operaciones. Si es False, no se imputan las distancias.
            - distanciaMedia: Distancia media entre operaciones.
            - umbral_mismo_lugar: Umbral para considerar que dos operaciones son el mismo lugar.
            - umbral_ratio_dCdP: Umbral para el ratio entre el delta de caminata y el delta de pico abierto.
            - deltaO_medio: delta de operación medio entre operaciones.
        """
        
        self.is_fitted = False
        self.imputeDistances = imputeDistances
        self.distanciaMedia = distanciaMedia
        self.dist_mismo_lugar = dist_mismo_lugar
        self.umbral_mismo_lugar = umbral_mismo_lugar
        self.umbral_ratio_dCdP = umbral_ratio_dCdP
        self.deltaO_medio = deltaO_medio
        
        ##creamos un diccionario para saber la posición de cada dato dentro del array devuelto por transform()
        self._dataPositions = {"DST_PT": 0, "deltaO": 2, "ratio_dCdP": 3, "distances": 4}
        
    def fit(self, X: np.array, y=None)-> np.array:
        """Fittea el objeto
        
        Params:
            - X: Es un array con los datos provenientes (strings) de la base de datos histórica. La forma de X es (n,4)Las columnas de X son,
                - 0: tlm_spbb son los datos de telemetría.
                - 1: date_oprc son los datos de fecha y hora de operación.
                - 2: latitud de la operación
                - 3: longitud de la operación
                - 4: precision del GPS
        """
        
        ##agregar asserts y warnings
        
        tlm_spbb = X[:,0] #datos de telemería
        date_oprc = X[:,1].astype(int) #datos de fecha y hora de operación
        lats = X[:,2].astype(float) #latitudes de las operaciones
        longs = X[:,3].astype(float) #longitudes de las operaciones  
        precitions = X[:,4].astype(float) #precision del GPS      
        
        ##instanciamos los objetos
        tlmDataExtractor = TLMSensorDataExtractor()
        timeProcessor = TimeSeriesProcessor()
        geoprocessor = GeoProcessor()
        
        ##***** OBTENEMOS LOS DATOS PARA FITEAR LOS OBJETOS Y ASÍ PROCESAR LA FM *****
        ##obtengo las posiciones de los datos de tlmDataExtractor y timeProcessor
        self._tlmdeDP = tlmDataExtractor.dataPositions #posiciones de los datos transformados de tlmDataExtractor
        self._tpDP = timeProcessor.dataPositions #posiciones de los datos transformados de timeProcessor
        
        ##fitteamos tlmse con los datos de telemetría
        self._tlmExtracted = tlmDataExtractor.fit_transform(tlm_spbb)
        
        ##fitteamos timeProcessor con los datos de fecha y hora de operación y los TIMEAC
        timeData = np.hstack((date_oprc.reshape(-1,1),self._tlmExtracted[:,self._tlmdeDP["TIMEAC"]].reshape(-1, 1)))
        self._timeDeltas = timeProcessor.fit_transform(timeData)
        
        ##fitteamos geoprocessor con las latitudes y longitudes
        ##genero un array de puntos de la forma (n,2)
        points = np.hstack((lats.reshape(-1,1),longs.reshape(-1,1)))
        self._distances = geoprocessor.fit_transform(points)
        
        ####***** IMPUTAMOS DATOS SI ES LO REQUERIDO*****
        if self.imputeDistances:
            distanceimputer = DistancesImputer(distanciaMedia = self.distanciaMedia,
                                               umbral_mismo_lugar = self.umbral_mismo_lugar,
                                               dist_mismo_lugar = self.dist_mismo_lugar,
                                               umbral_ratio_dCdP = self.umbral_ratio_dCdP,
                                               deltaO_medio = self.deltaO_medio)
            
            X_distance_imputation = np.hstack((self._distances.reshape(-1, 1),
                                            precitions.reshape(-1, 1),
                                            self._tlmExtracted[:,self._tlmdeDP["GNSSFlag"]].reshape(-1, 1),
                                            self._tlmExtracted[:,self._tlmdeDP["FIX"]].reshape(-1, 1),
                                            self._timeDeltas[:,self._tpDP["deltaO"]].reshape(-1, 1),
                                            self._timeDeltas[:,self._tpDP["ratio_dCdP"]].reshape(-1, 1)))
            
            self._distances = distanceimputer.fit_transform(X_distance_imputation)
        
        self.is_fitted = True
        
    def transform(self, X: np.array, y = None):
        """Transforma los datos de X en la matriz de características.
        
        Params:
            - X: Es un array con los datos provenientes (strings) de la base de datos histórica. La forma de X es (n,4)Las columnas de X son,
                - 0: tlm_spbb son los datos de telemetría.
                - 1: date_oprc son los datos de fecha y hora de operación.
                - 2: latitud de la operación
                - 3: longitud de la operación
                
        Returns:
            - featureMatrix: Es un array con la matriz de características. La forma de featureMatrix es (n,5). Las columnas de featureMatrix son,
                - 0: DST_PT: Distorsión de plantín
                - 2: deltaO: delta operación
                - 3: ratio_dCdP: Ratio entre el delta de caminata y delta de pico abierto
                - 4: distances: Distancias entre operaciones
        """
        
        if not self.is_fitted:
            raise RuntimeError("El modelo no ha sido fitteado.")
        
        ##armamos la feature matrix
        featureMatrix = np.vstack((self._tlmExtracted[:,self._tlmdeDP["DSTRPT"]],
                                   self._timeDeltas[:,self._tpDP["deltaO"]],
                                   self._timeDeltas[:,self._tpDP["ratio_dCdP"]],
                                   self._distances)).T
        
        return featureMatrix

    def fit_transform(self, X: np.array, y=None):
        """Fittea y transforma los datos de X en la matriz de características.
        
        Params:
            - X: Es un array con los datos provenientes (strings) de la base de datos histórica. La forma de X es (n,4)Las columnas de X son,
                - 0: tlm_spbb son los datos de telemetría.
                - 1: date_oprc son los datos de fecha y hora de operación.
                - 2: latitud de la operación
                - 3: longitud de la operación
        
        Returns:
            - featureMatrix: Es un array con la matriz de características. La forma de featureMatrix es (n,5). Las columnas de featureMatrix son,
                - 0: DST_PT: Distorsión de plantín
                - 2: deltaO: delta operación
                - 3: ratio_dCdP: Ratio entre el delta de caminata y delta de pico abierto
                - 4: distances: Distancias entre operaciones
        """
        self.fit(X)
        return self.transform(X)
    
    @property
    def tlmExtracted(self):
        """Devuelve los datos de telemetría extraídos."""
        return self._tlmExtracted
    
    @property
    def timeDeltas(self):
        """Devuelve los datos de tiempo extraídos."""
        return self._timeDeltas
    
    @property
    def distances(self):
        """Devuelve las distancias entre operaciones."""
        return self._distances
    
    @property
    def dataPositions(self):
        """Devuelve el diccionario con la posición de los datos dentro del array devuelto por transform()."""
        return self._dataPositions
    
        
if __name__ == "__main__":
    ##genero objeto FMCreator
    fmcreator = PlantinFMCreator(imputeDistances=True)
    
    ##datos de ejemplo
    tlmsbp_sample = np.array(['0010001000010010110000011000000111111101001000000000000000000000',
                              '0010001000010100110000011000000111111101001000000000000000000000',
                              '0010001000010000110000011000000111111101001000000000000000000000',
                              '0010001000011010110000011000110111111101001000000000000000000000'])
    
    date_oprc = ["35235", "35240", "35244", "35248"]
    lats = ["-32.331093", "-32.331116", "-32.331131", "-32.331146"]
    lons = ["-57.229733", "-57.229733", "-57.229733", "-57.22974"]
    precitions = ["1", "0.12", "0.1", "1"]
    
    ##generamos matriz de datos X
    ##generamos matriz de datos X de tal forma que cada columna tenga los datos de tlmsbp_sample, date_oprc, lats y lons
    X = np.vstack((tlmsbp_sample, date_oprc, lats, lons,precitions)).T
    X = X.astype(str)
    fmcreator.fit(X)
    fm = fmcreator.fit_transform(X)
    print(fm)