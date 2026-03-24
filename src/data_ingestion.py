import pandas as pd
import numpy as np
import os

def generar_datos_telemetria(n_filas=1000):
    """
    Simula datos de sensores de camiones mineros CAT.
    """
    np.random.seed(42)
    
    # 1. Definimos los componentes del dataset
    timestamps = pd.date_range(start='2026-01-01', periods=n_filas, freq='H')
    equipos = ['CAT-797F-001', 'CAT-797F-002', 'CAT-797F-003', 'CAT-797F-004']
    
    # 2. Generamos datos aleatorios realistas para maquinaria pesada
    data = {
        'fecha_hora': timestamps,
        'id_unidad': np.random.choice(equipos, n_filas),
        'temperatura_motor_c': np.random.uniform(65, 110, n_filas),   # Normal: 80-95°C
        'presion_aceite_psi': np.random.uniform(30, 75, n_filas),     # Normal: 45-60 PSI
        'vibracion_chasis_mms': np.random.uniform(1.5, 12.0, n_filas) # Normal: < 5.0 mm/s
    }
    
    return pd.DataFrame(data)

def guardar_datos(df, nombre_archivo):
    """
    Guarda el DataFrame en la carpeta de datos crudos (raw).
    """
    # Creamos la ruta de forma segura para cualquier sistema operativo
    ruta_directorio = os.path.join('data', 'raw')
    
    # Nos aseguramos de que la carpeta exista (por si acaso)
    os.makedirs(ruta_directorio, exist_ok=True)
    
    ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
    
    # Guardamos sin el índice de pandas para que sea un CSV limpio
    df.to_csv(ruta_completa, index=False)
    print(f"Proceso exitoso: Se han generado {len(df)} registros en {ruta_completa}")

if __name__ == "__main__":
    # Ejecutamos la lógica principal
    df_telemetria = generar_datos_telemetria(1200) # Generamos 1200 horas de datos
    guardar_datos(df_telemetria, 'telemetria_cat_raw.csv')