import serial
import requests
from time import time_ns
#from urllib.parse import urlencode, quote_plus

## not needed if sending post request directly
#from influxdb import InfluxDBClient
#client = InfluxDBClient(host='192.168.29.171', port=8086)
#client.switch_database('espresso')

# consts
# TODO: move to env variables / script params?
SERIAL_PORT = '/dev/ttyUSB0'
INFLUX_URL = 'http://192.168.29.171'
INFLUX_PORT = 8086
INFLUX_DB_NAME = 'mydb'
MEASUREMENT = 'temperature'

def main():
   ser = serial.Serial(SERIAL_PORT)
   influx_post_url = create_influx_url(INFLUX_URL, INFLUX_PORT, INFLUX_DB_NAME)

   while(True):
      # example line: 'C1.22,036,140,033,1190,1'
      line = ser.readline().decode('utf-8').strip()
      parsed_line = parse_line(line)

      # 'temperature priority="Coffee",steam_temp_actual=122,steam_temp_target=114,hx_temp_actual=95,fast_heating=False,heating=True 1605418074971404678'
      data = create_influx_data(MEASUREMENT, parsed_line)
      x = requests.post(influx_post_url, data=data)
      print(str(x.status_code) + ': ' + x.content.decode('utf-8'))


def parse_line(line):
   parts = line.split(',')
   priority = 'Coffee' if (parts[0][0] == 'C') else 'Steam'
   steam_temp_actual = int(parts[1])
   steam_temp_target = int(parts[2])
   hx_temp_actual = int(parts[3])
   fast_heating = (int(parts[4]) > 0)
   heating = (int(parts[5]) > 0)
   result = {
      "priority": priority,
      "steam_temp_actual": steam_temp_actual,
      "steam_temp_target": steam_temp_target,
      "hx_temp_actual": hx_temp_actual,
      "fast_heating": fast_heating,
      "heating": heating
   }
   return result

def create_influx_url(url, port, db):
   #'http://192.168.29.171:8086/write?db=mydb'
   post_url = url + ':' + str(port) + '/write?db=' + db
   return post_url

def create_influx_data(measurement, fieldset):
   data = measurement + ' '
   for field in fieldset:
      data += field + '='
      data += ('"' + fieldset[field] + '"') if isinstance(fieldset[field],str) else str(fieldset[field])
      data += ','
   data = data[:-1] + ' ' + str(time_ns())
   return data

main()
