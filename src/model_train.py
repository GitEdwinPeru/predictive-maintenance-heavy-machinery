import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def entrenar_modelo():
    # 1. Cargar los datos procesados de la Fase 2
    ruta_input = os.path.join('data', 'processed', 'telemetria_final.csv')
    df = pd.read_csv(ruta_input)

    # 2. Seleccionar características (X) y objetivo (y)
    # Usamos las columnas de sensores para predecir la columna 'falla'
    X = df[['temperatura_motor_c', 'presion_aceite_psi', 'vibracion_chasis_mms', 'carga_termica']]
    y = df['falla']

    # 3. División Train/Test (80% para aprender, 20% para evaluar)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Crear y entrenar el modelo (Random Forest)
    print(" Entrenando el cerebro de la IA...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # 5. Evaluación
    predicciones = modelo.predict(X_test)
    print("\n Evaluación del Modelo:")
    print(classification_report(y_test, predicciones))

    # 6. Guardar el modelo entrenado en la carpeta 'models/'
    # Esto permite usarlo después sin volver a entrenar
    ruta_modelo = os.path.join('models', 'modelo_predictivo_cat.pkl')
    joblib.dump(modelo, ruta_modelo)
    print(f"\n Modelo guardado profesionalmente en: {ruta_modelo}")

if __name__ == "__main__":
    entrenar_modelo()