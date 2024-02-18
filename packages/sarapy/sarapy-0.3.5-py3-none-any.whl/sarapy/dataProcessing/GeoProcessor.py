###Documentación en https://github.com/lucasbaldezzari/sarapy/blob/main/docs/Docs.md

import numpy as np
from geopy.distance import geodesic
from sklearn.base import BaseEstimator, TransformerMixin
import warnings

class GeoProcessor(BaseEstimator, TransformerMixin):
    """La clase GeoProcessor se encarga de gestionar los datos de georreferenciación."""
    
    def __init__(self):
        """Inicializa la clase GeoProcessor."""
        
        self._points = None #np.array de tuplas con las coordenadas de latitud y longitud
        self.is_fitted = False

    @staticmethod
    def getDistance(point1: np.array, point2: np.array) ->float:
        """Calcula la distancia elipsoidal (en metros) entre los puntos p1 y p2 donde cada punto está representado como un array con un valor de latitud y otro de longitud. 

        Parametros
            point1 (np.array): array con los valores de latitud y longitud del punto 1
            point2 (np.array): array con los valores de latitud y longitud del punto 2

        Returns:
            float: np.array con las distancias entre los dos puntos
        """
        
        ##aplicamos la función geodesic
        return geodesic(point1, point2).meters
        
    def fit(self, X: np.array, y=None)-> np.array:
        """fittea el objeto
        
        - X: array con los puntos de latitud y longitud. Shape (n, 2)
        """
        ##asserteamos que X sea un np.array
        assert isinstance(X, np.ndarray), "X debe ser un np.array"
        ##asserteamos que X tenga dos columnas
        assert X.ndim == 2, "X debe ser de la forma (n, 2)"
        ##asserteamos que X no tenga valores nulos
        assert not np.isnan(X).any(), "X no debe tener valores nulos"
        ##chequeamos que X tenga una sola fila, si es así, enviamos un warning
        if X.shape[0] == 1:
            warnings.warn("X tiene una sola fila, se recomienda utilizar fit_transform")

        self._points = X
        self.is_fitted = True
        
    def transform(self, X, y=None):
        """Transforma los datos de X en distancias entre los puntos.
        
        - X: array con los puntos de latitud y longitud. Shape (n, 2)-
        
        Returns:
            np.array: np.array con las distancias entre los dos puntos
        """
        if not self.is_fitted:
            raise RuntimeError("El modelo no ha sido fitteado.")
        
        if self._points.shape[0] >= 2:
            ##calculamos la distancia entre los puntos de latitud y longitud dentro de X
            self._distances = np.array([self.getDistance(point1, point2) for point1, point2 in zip(self.points,self.points[1:])]).round(2)
            #agrego un cero al final del array
            self._distances = np.append(self._distances, 0)
        
        elif self._points.shape[0] == 1:
            self._distances = np.array([0])
        
        return self._distances

    def fit_transform(self, X, y=None):
        """Fit y transforma los datos de X en distancias entre los puntos.
        
        - X: datos de entrenamiento
        
        Returns:
            np.array: np.array con las distancias entre los dos puntos
        """
        self.fit(X)
        return self.transform(self.points)
        
    @property
    def points(self):
        """Devuelve los puntos de georreferenciación."""
        return self._points
    
    @property
    def distances(self):
        """Devuelve las distancias entre los puntos."""
        ##chqueamos que el modelo haya sido fitteado
        if not self.is_fitted:
            warnings.warn("El modelo no ha sido fitteado.")
            return None
        else:
            return self._distances
        
        
if __name__ == "__main__":
    ga = GeoProcessor()

    puntos = np.array([[-32.329910, -57.229061],
              [	-32.329895, -57.229061],
              [-32.329880, -57.229069],
              [-32.329865, -57.229069]])
    
    ga.fit(puntos)
    print(ga.transform(puntos))
    print(ga.fit_transform(puntos))
    print(ga.distances)
    punto_referencia = puntos[0]
    
    sample = np.array([[-32.329910, -57.229061]])
    
    ga2 = GeoProcessor()
    ga2.fit(sample)
    ga2.points
    print(ga2.fit_transform(sample))
    print(ga2.distances)