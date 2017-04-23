#!/usr/bin/env python

##########################################################################
##                                                                      ## 
##	Autor: Marti Puig Colome                                            ##
##	Fecha: 23/04/2017                                                   ##
##	Script: Sensor de movimiento y camara                               ##
##	Descripcion: El sensor cuando capta cualquier tipo de movimiento    ##
##  a su alrededor envia una senya a la camara para que tome una foto.  ##
##	Esta se almacena a una ruta que se especifica                       ##
##                                                                      ##
##########################################################################
import RPi.GPIO as GPIO    			#Importamos la libreria GPIO
import time                			#Importamos time
import os
from time import strftime  			#importamos gmtime y strftime
GPIO.setmode(GPIO.BCM)             	#Configuramos los pines GPIO como BCM
PIR_PIN = 23                        #Usaremos el pin GPIO n16 real
GPIO.setup(PIR_PIN, GPIO.IN)       	#Lo configuramos como entrada
RUTA='RUTA_DONDE_ALMACENAR_IMAGENES'


try:
    while True: 	 							#Iniciamos un bucle infinito
        if GPIO.input(PIR_PIN): 				#Si hay senyal en el pin GPIO n23
            data = (time.strftime("%d_%m_%y"))
            hora = (time.strftime("%H:%M:%S"))
            nom= hora+data
            time.sleep(1)        				#Pausa de 1 segundo
            
            print data +" "+hora + " MOVIMIENTO DETECTADO"  #La sacamos por pantalla
            time.sleep(1)  						#Pausa de 1 segundo
            os.chdir(RUTA)
            os.system('mkdir -p Images')
            os.chdir(RUTA+'/Images')
            os.system('mkdir -p '+data)
            os.chdir(RUTA+'/Images/'+data)
            os.system('raspistill -vf -hf -o ' +hora+'.jpg')
            time.sleep(5)

        time.sleep(1)              				#Pausa de 1 segundo y vuelta a empezar
except KeyboardInterrupt:   					#Si el usuario pulsa CONTROL + C...
    print "quit"            					#Anunciamos que finalizamos el script
    GPIO.cleanup()          					#Limpiamos los pines GPIO y salimos
