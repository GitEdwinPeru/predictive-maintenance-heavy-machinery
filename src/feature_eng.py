import pandas as pd
import os

def procesar_caracteristicas():
    # 1. Cargar los datos crudos que generamos en la fase anterior
    ruta_raw = os.path.join('data', 'raw', 'telemetria_cat_raw.csv')
    
    if not os.path.exists(ruta_raw):
        print("❌ Error: No se encuentra el archivo raw. Ejecuta primero data_ingestion.py")
        return

    df = pd.read_csv(ruta_raw)

    # 2. Lógica de Ingeniería de Atributos (Reglas de Ferreyros)
    # Crearemos una columna 'falla' basada en condiciones críticas:
    # - Temperatura > 100°C
    # - Vibración > 10 mm/s
    # - Presión de aceite < 35 PSI
    
    df['falla'] = (
        (df['temperatura_motor_c'] > 100) | 
        (df['vibracion_chasis_mms'] > 10) | 
        (df['presion_aceite_psi'] < 35)
    ).astype(int)

    # 3. Crear una nueva característica: 'carga_termica'
    # Combinamos temperatura y vibración para ver el esfuerzo del motor
    df['carga_termica'] = df['temperatura_motor_c'] * df['vibracion_chasis_mms']

    # 4. Guardar los datos listos para la IA
    ruta_processed = os.path.join('data', 'processed', 'telemetria_final.csv')
    os.makedirs(os.path.dirname(ruta_processed), exist_ok=True)
    
    df.to_csv(ruta_processed, index=False)
    print(f"✅ Fase 2 completada. Datos procesados guardados en: {ruta_processed}")
    print(f"📊 Total de fallas detectadas para entrenamiento: {df['falla'].sum()}")

if __name__ == "__main__":
    procesar_caracteristicas()