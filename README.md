---
encoding: utf-8
---

#Bling trading bot

🇻🇪 Un Bot que nace para que las personas con discapacidad visual (Ciegas) 🧑‍🦯 puedan tener acceso al precio del mercado y algunos indicadores. facilitándole la toma de decisión al invertir.

##¿Dónde lo consigo?

Si eres una persona que estás interesada en seguir el mercado y usar esta herramienta nos puedes conseguir en Telegram en el siguiente enlace:
https://t.me/BlindTrading_bot

##Desarrolladores

Si eres un programador y quieres clonar este repositorio lo puedes hacer, no olvides mejorarlo y sitar de donde salió la idea original.

Te dejo como instalar y hacer correr este pequeño proyecto.

##Instalación

1.	Al clonar el repositorio encontraras un archivo llamado requirements.txt, allí están todas las librerías y dependencias del proyecto así que solo ejecuta en tu terminal el siguiente comando:

pip install -r requirements.txt

Espera que termine la instalación.
Si al finalizar genera un error con la librería ta-lib sigue los siguientes pasos:

2.	Descarga ta-lib-0.4.0-src.tar.gz con el siguiente comando:

wget https://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

3.	comprueba que hallas descargado ta-lib-0.4.0-src.tar.gz y descomprímelo con el siguiente comando:

tar -xf ta-lib-0.4.0-src.tar.gz

4.	entra en la carpeta ta-lib con el siguiente comando:

cd ta-lib/

5.	inicia la configuración de tu entorno para la instalación de este modulo ejecutando el script configure con el siguiente comando:

./configure

6.	Al finalizar la ejecución de configure use el siguiente comando:

Make

7.	Ejecute ahora el siguiente comando:

Sudo make install

8.	Y por último instale la librería con:

Pip install ta-lib

###despliegue

Una vez preparado el entorno, configure su token en el archivo config.py
Y ejecute bot.py

Éxito ya puedes empezar aportar más funcionalidades ha este proyecto.

