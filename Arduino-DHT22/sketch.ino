#include <DHT.h>

//Definição do sensor DHT
#define DHTPIN 2
#define DHTTYPE DHT22 

DHT dht(DHTPIN,DHTTYPE);

void setup() {
Serial.begin(9600);
dht.begin();
}

void loop() {
 float temperatura = dht.readTemperature();
 float umidade = dht.readHumidity();

//Impressão na tela
 Serial.print("Temperatura:");
 Serial.print(temperatura);
 Serial.print("ºC");
 Serial.print(" -- Umidade:");
 Serial.print(umidade);
 Serial.println("%");

delay(5000);
}
