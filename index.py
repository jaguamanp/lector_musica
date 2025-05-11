import pandas as pd
import time

COLOR = "\033[96m"  
RESET = "\033[0m"   

def convertir_a_segundos(tiempo_str):
    minutos, segundos = map(int, tiempo_str.split(":"))
    return minutos * 60 + segundos

def mostrar_letra_con_tiempo(nombre_archivo):
    df = pd.read_csv(nombre_archivo, delimiter=";")
    df["TiempoSegundos"] = df["Tiempo"].apply(convertir_a_segundos)

    for i in range(len(df)):
        fila = df.iloc[i]
        tiempo_actual = fila["TiempoSegundos"]
        
        if i < len(df) - 1:
            tiempo_siguiente = df.iloc[i + 1]["TiempoSegundos"]
        else:
            tiempo_siguiente = tiempo_actual + 3
        
        duracion_linea = tiempo_siguiente - tiempo_actual
        texto = str(fila["Letra"])
        num_letras = len(texto)
        
        if num_letras == 0:
            continue
        
        pausa_por_letra = duracion_linea / num_letras
        
        if texto != "#ESPACIO":
            for letra in texto:
                print(f"{COLOR}{letra}{RESET}", end="", flush=True)
                time.sleep(pausa_por_letra)
            print()
        else:
            time.sleep(duracion_linea)
            print()

mostrar_letra_con_tiempo("canciones/a_donde_vamos_morat.csv")