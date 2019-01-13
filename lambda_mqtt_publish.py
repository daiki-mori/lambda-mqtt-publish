# coding: UTF-8
"""
MQTT Publish

Folder Structure
/
┗ mqtt_publish.py
┗ cert/
  ┗　AmazonRootCA1.Pem
  ┗ <id>-certificatie.pem.crt
  ┗ <id>-private.pem.key

Requeired Library
- paho-mqtt
"""
import os
import ssl
import subprocess

from time import sleep

import paho.mqtt.client as mqtt

#####変更が必要な値#####
# AWS IoT settings
ENDPOINT = ""
CERT_ID = ""
## AWS IoTで利用するトピック名
TOPIC = ""
#####変更が必要な値#####

## マネージメントコンソール→AWS IoT→設定→カスタムエンドポイント にあるエンドポイント名をコピー
HOST = ENDPOINT + ".iot.ap-northeast-1.amazonaws.com"
## ポート番号は以下、固定
PORT = 8883  # port

B_PATH = os.getcwd()
## AWS IoTで作成した証明書
ROOT_CA = "./cert/AmazonRootCA1.pem"
CLIENT_CERT = "./cert/" + CERT_ID + "-certificate.pem.crt"
PRIVATE_KEY = "./cert/" + CERT_ID + "-private.pem.key"

CLIENT = None

def on_connect(client, userdata, flags, respons_code):
    """
    callback on_connect
    """
    print("Connected")
    print("res_code:" + str(respons_code))

def on_message(client, userdata, msg):
    """
    callback on_message
    """
    print("message")

def publish(mqtt_client):
    """
    publish
    """
    print("publish")
    sleep(2)
    pub_data = "publish_data"
    print("TOPIC:" + TOPIC)
    mqtt_client.publish(TOPIC, pub_data, qos=0)
    print("send publish")

def create_connection():
    """
    Create connection
    """
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    # callback
    client.on_connect = on_connect
    client.on_message = on_message
    # certifications
    client.tls_set(ROOT_CA, certfile=CLIENT_CERT, keyfile=PRIVATE_KEY,
                   cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    # port, keepalive
    client.connect(HOST, port=PORT, keepalive=60)
    return client

#if __name__ == '__main__':
def main(event, context):
    client_connection = create_connection()
    publish(client_connection)
