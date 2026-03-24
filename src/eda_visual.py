import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generar_analisis_visual():
    # 1. Cargar datos procesados
    ruta_input = os.path.join('data', 'processed', 'telemetria_final.csv')
    df = pd.read_csv(ruta_input)

    # Configuración de estilo
    sns.set_theme(style="whitegrid")
    
    # 2. Crear un gráfico de dispersión (Scatter Plot)
    # Este gráfico es clave: muestra Temperatura vs Vibración y colorea las fallas
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='temperatura_motor_c', y='vibracion_chasis_mms', hue='falla', palette='coolwarm')
    
    plt.title('Detección de Fallas: Temperatura vs Vibración (Flota CAT)')
    plt.xlabel('Temperatura del Motor (°C)')
    plt.ylabel('Vibración (mm/s)')
    plt.legend(title='Estado', labels=['Sano (0)', 'Falla (1)'])
    
    # 3. Guardar el gráfico
    ruta_grafico = os.path.join('models', 'analisis_fallas.png')
    plt.savefig(ruta_grafico)
    print(f"✅ Gráfico generado y guardado en: {ruta_grafico}")
    plt.show()

if __name__ == "__main__":
    generar_analisis_visual()