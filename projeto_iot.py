import machine
import time
import dht
import conexao_wifi as wifi
import urequests

r = machine.Pin(2,machine.Pin.OUT)

while True:
	r.value(1)
    time.sleep(1)
	r.value(0)
	time.sleep(1)
 


d = dht.DHT11(machine.Pin(4))
while True:
d.measure()
print("Temperatura={}Umidade={}".format(d.temperature(),d.humidity()))
time.sleep(3)

if (d.temperature() > 31 or d.humidity() > 70) and r.value() == 0:
      r.value(1)
time.sleep(1)
      if d.temperature() > 31:
          print("A temperatura está acima de 31°C. Relé ligado")
      else:
          print("A umidade está acima de 70%. Relé ligado")

def conecta(ssid, senha):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

ssid = input("Rede: ")
senha = input("Senha: ")
print("Conectando...")
station = conecta(ssid, senha)
