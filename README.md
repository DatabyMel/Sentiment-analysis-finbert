# 📰 Análisis de Sentimiento Financiero Modular

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![APIs](https://img.shields.io/badge/Datos-NewsAPI%20%7C%20Yahoo%20Finance%20RSS-informational)
![Modelo](https://img.shields.io/badge/Sentimiento-FinBERT-orange)
![Licencia](https://img.shields.io/badge/License-MIT-green)

---

## 💡 Descripción General

Este proyecto demuestra dos métodos independientes para realizar un **análisis de sentimiento financiero** utilizando diferentes fuentes de datos y el modelo **FinBERT** (`ProsusAI/finbert`). El objetivo es obtener una puntuación agregada (positiva, negativa o neutral) para un activo o palabra clave específica.

### Módulos Incluidos

| Archivo | Fuente de Datos | Método | Requisito de API Key |
| :--- | :--- | :--- | :--- |
| `newsapi_script.py` | NewsAPI | Solicitud HTTP (JSON) | **Sí** |
| `yahoo_rss_script.py` | Yahoo Finance | Feed RSS | **No** |

---

## 🛠️ Requisitos e Instalación

### 1. Instalación de Dependencias

Instala las librerías necesarias utilizando `pip`:

```bash
pip install requests transformers feedparser
```

### 2. Configuración de API Key (Solo `newsapi_script.py`)

Para usar el script basado en NewsAPI, debes crear un archivo llamado `API_KEY` en el directorio raíz y pegar tu clave de NewsAPI dentro.

⚠️ **IMPORTANTE:** Este archivo está listado en el `.gitignore` y no debe ser subido al repositorio público por razones de seguridad.

---

## 🚀 Uso de los Scripts

### 1. Script con NewsAPI (`main2.py`)

Busca noticias por palabra clave, fecha e idioma.

1. Abre `main2.py` y ajusta las variables `keyword`, `date` y `language`.  
2. Ejecuta desde la terminal:

```bash
python newsapi_script.py
```

### 2. Script con Yahoo RSS (`main.py`)

Obtiene los titulares más recientes de Yahoo Finance para un símbolo de cotización (ticker).

1. Abre `main.py` y ajusta las variables `ticker` y `keyword`.  
2. Ejecuta desde la terminal:

```bash
python yahoo_rss_script.py
```

---

## 🚨 Advertencia sobre el Idioma

El modelo **FinBERT** está entrenado exclusivamente en un corpus de texto financiero en **inglés**.

Para obtener la máxima precisión y fiabilidad, se recomienda enfocar la búsqueda de noticias a artículos en inglés (`language = 'en'` en el script de NewsAPI).

El uso de noticias en español u otros idiomas puede generar clasificaciones de sentimiento **inexactas**.

---

## 🤝 Contribuciones y Mejoras

Las contribuciones son bienvenidas, especialmente para abordar las limitaciones del idioma o añadir visualizaciones.  
Si deseas contribuir:

1. Haz un **Fork** del repositorio.  
2. Crea una rama nueva:  
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Abre un **Pull Request**.

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**.

Autor: [Melissa Peñaloza Torrado]
