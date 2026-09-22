[app]

# Nombre de la aplicación
title = Pulguita IA

# Nombre interno
package.name = pulguitaia

# Dominio de la aplicación
package.domain = org.pulguita

# Archivo principal
source.dir = .

# Archivos incluidos
source.include_exts = py,json,png,jpg,jpeg,wav,mp3

# Versión
version = 0.1

# Requisitos de Python
requirements = python3,kivy

# Orientación
orientation = portrait

# Pantalla completa
fullscreen = 0

# Permisos Android
android.permissions = INTERNET

# Icono
# Dejamos el icono para una versión posterior

# Configuración Android
android.api = 35
android.minapi = 23

# Arquitecturas
android.archs = arm64-v8a, armeabi-v7a

# Nombre del archivo APK
android.numeric_version = 1


[buildozer]

# Directorio de compilación
log_level = 2

# Advertencias
warn_on_root = 1


[app:android]

# Ventana Android
android.entrypoint = org.kivy.android.PythonActivity
