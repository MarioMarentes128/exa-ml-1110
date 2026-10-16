# Reporte de Análisis de Datos - Pandas

`Mario Yañez Machine Learning pandas, NC 1110`

## 1. DataFrame Convertido
```text
      Carniceria  Cortes  Kg_dia
0        El Toro      25     300
1         La Res      18     200
2  Don Carnicero      30     400
3     Meat House      22     250
4   Carnes Finas      28     350
5      El Rastro      20     180
```

## 2.1 Primeras Filas (head)
```text
  Carniceria  Cortes  Kg_dia
0    El Toro      25     300
1     La Res      18     200
```

## 2.2 Últimas Filas (tail)
```text
     Carniceria  Cortes  Kg_dia
4  Carnes Finas      28     350
5     El Rastro      20     180
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Carniceria      str
Cortes        int64
Kg_dia        int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Carniceria  6 non-null      str  
 1   Cortes      6 non-null      int64
 2   Kg_dia      6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Kg_dia'
```text
count      6.000000
mean     280.000000
std       86.023253
min      180.000000
25%      212.500000
50%      275.000000
75%      337.500000
max      400.000000
Name: Kg_dia, dtype: float64
```

## 4. Ordenar Ascendente por Kg_dia
```text
      Carniceria  Cortes  Kg_dia
5      El Rastro      20     180
1         La Res      18     200
3     Meat House      22     250
0        El Toro      25     300
4   Carnes Finas      28     350
2  Don Carnicero      30     400
```

## 5. Ordenar Descendente por Cortes
```text
      Carniceria  Cortes  Kg_dia
2  Don Carnicero      30     400
4   Carnes Finas      28     350
0        El Toro      25     300
3     Meat House      22     250
5      El Rastro      20     180
1         La Res      18     200
```
