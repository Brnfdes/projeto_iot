import machine
import time
import dht
from conexao_wifi import conecta

r = machine.Pin(2,machine.Pin.OUT)
d = dht.DHT11(machine.Pin(4))

ssid = input("Rede: ")
senha = input("Senha: ")
print("Conectando...")
station = conecta(ssid, senha)

while True:
    # Lê o sensor DHT11
    d.measure()
    print("Temperatura={} Umidade={}".format(d.temperature(), d.humidity()))
    time.sleep(3)
    
    resposta = urequests.get("https://api.thingspeak.com/update?api_key=XGV138262JB85X8X&field1={}&field2={}".format(d.temperature(), d.humidity()))
    
    # Pisca o relé
    r.value(1)
    time.sleep(1)
    r.value(0)
    time.sleep(1)
    
    # Verifica temperatura e umidade
    if (d.temperature() > 31 or d.humidity() > 70) and r.value() == 0:
        r.value(1)
        time.sleep(1)
        if d.temperature() > 31:
            print("A temperatura está acima de 31°C. Relé ligado")
        else:
            print("A umidade está acima de 70%. Relé ligado")
