# Reporte de Análisis de Datos - Supermercados (Pandas)

`Daniel Nieves Machine Learning pandas, NC 1343`

## 1. DataFrame Convertido
```text
  Supermercado  Sucursales  Empleados
0      Walmart        2500     230000
1      Soriana         900     120000
2     Chedraui         350      45000
3       Costco          70      30000
4     La Comer          80      15000
5          HEB          50      10000
```

## 2.1 Primeras Filas (head)
```text
  Supermercado  Sucursales  Empleados
0      Walmart        2500     230000
1      Soriana         900     120000
```

## 2.2 Últimas Filas (tail)
```text
  Supermercado  Sucursales  Empleados
4     La Comer          80      15000
5          HEB          50      10000
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Supermercado      str
Sucursales      int64
Empleados       int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   Supermercado  6 non-null      str  
 1   Sucursales    6 non-null      int64
 2   Empleados     6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de 'Sucursales'
```text
count       6.000000
mean      658.333333
std       958.737016
min        50.000000
25%        72.500000
50%       215.000000
75%       762.500000
max      2500.000000
Name: Sucursales, dtype: float64
```

## 3.1 Estadísticas Generales de 'Empleados'
```text
count         6.000000
mean      75000.000000
std       85790.442358
min       10000.000000
25%       18750.000000
50%       37500.000000
75%      101250.000000
max      230000.000000
Name: Empleados, dtype: float64
```

## 4. Ordenar Ascendente por Sucursales
```text
  Supermercado  Sucursales  Empleados
5          HEB          50      10000
3       Costco          70      30000
4     La Comer          80      15000
2     Chedraui         350      45000
1      Soriana         900     120000
0      Walmart        2500     230000
```

## 5. Ordenar Descendente por Empleados
```text
  Supermercado  Sucursales  Empleados
0      Walmart        2500     230000
1      Soriana         900     120000
2     Chedraui         350      45000
3       Costco          70      30000
4     La Comer          80      15000
5          HEB          50      10000
```

`Daniel Nieves Machine Learning pandas, NC 1343`