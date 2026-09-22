[app]

title = Pulguita IA
package.name = pulguitaia
package.domain = org.pulguita

source.dir = .
source.include_exts = py,json,png,jpg,jpeg,wav,mp3

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23

android.archs = arm64-v8a, armeabi-v7a

android.numeric_version = 1


[buildozer]

log_level = 2
warn_on_root = 1
