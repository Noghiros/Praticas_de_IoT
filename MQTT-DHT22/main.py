import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient

# Parametros do Cliente MQTT
MQTT_CLIENT_ID  = "teste.utfpr.edu.br"
MQTT_BROKER     = "broker.mqttdashboard.com"
MQTT_USER       = ""
MQTT_PASSWORD   = ""
MQTT_TOPIC      = "Stefano-Calheiros-Stringhini"

sensor = dht.DHT22(Pin(15))
print("Conectando ao Wifi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".",end="")
    time.sleep(0.1)
print(" Conectado!")

print("Conectando ao Broker MQTT...", end="")
Cliente = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
Cliente.connect()
print(" Conectado!")

anterior = ""
while True:
    print("Medindo...", end="")
    sensor.measure()
    mensagem = ujson.dumps({
        "temperatura": sensor.temperature(),
        "umidade": sensor.humidity(),
    })    
    if mensagem != anterior:
        print("Atualizando...")
        print("Reportando alterações ao topico MQTT {} : {}".format(MQTT_TOPIC, mensagem))
        Cliente.publish(MQTT_TOPIC, mensagem)
        anterior = mensagem
    else:
        print("Nenhuma mudança detectada")
    
    time.sleep(2)