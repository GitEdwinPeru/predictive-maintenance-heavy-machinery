import pandas as pd
import numpy as np
import os

def generar_reporte_telemetria(num_registros=1000):
    # Configuramos una semilla para que los datos aleatorios sean consistentes
    np.random.seed(42)
    
    # Simulación de sensores de maquinaria pesada (estilo Caterpillar)
    datos = {
        'timestamp': pd.date_range(start='2026-01-01', periods=num_registros, freq='H'),
        'unidad_id': np.random.choice(['CAT-797F-01', 'CAT-797F-02', 'CAT-797F-03'], num_registros),
        'temp_motor_c': np.random.uniform(70, 115, num_registros),      # Grados Celsius
        'presion_aceite_psi': np.random.uniform(35, 75, num_registros), # PSI
        'vibracion_motor': np.random.uniform(2, 18, num_registros)      # mm/s
    }
    
    # Creamos el DataFrame (la tabla de datos)
    df = pd.DataFrame(datos)
    
    # Definimos la ruta de guardado profesional (data/raw)
    ruta_archivo = os.path.join('data', 'raw', 'telemetria_inicial.csv')
    
    # Guardamos el archivo
    df.to_csv(ruta_archivo, index=False)
    print(f"✅ Archivo generado exitosamente en: {ruta_archivo}")

if __name__ == "__main__":
    generar_reporte_telemetria()