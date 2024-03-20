# Kafka-ELK for Education in ITD62-332
เป็นตัวระบบ Monitoring เพื่อใช้สำหรับในการตรวจสอบข้อมูลที่ผ่านเข้ามาใน Traffic
##

## GROK Debugger
https://grokdebugger.com/
##
## Update&Upgrade you software 
ใช้คำสั่งด้านล่างที่ให้ไปเพื่อทำการ Update และ Upgrade ตัวซอฟแวร์ หรือระบบต่างๆ ภายในเครื่อง

```bash
sudo apt update
```
```bash
sudo apt upgrade
```
##
## Dowload Docker & enable Docker
ใช้คำสั่งด้านล่างในการติดตั้งตัว Docker
```bash
sudo apt install docker.io
```
ใช้คำสั่งด้านล่างในการเปิดใช้งาน Docker
```bash
sudo systemctl enable docker
```
ทำการเช็คสถานะของ Docker ว่าเปิดใช้งานอยู่หรือไม่
```bash
sudo systemctl status docker
```
ถ้าขิ้นว่า enable ให้ทำการใช้คำสั่ง
```bash
sudo systemctl start docker
```
เพื่อเริ่มต้นการทำงานของตัว Docker และเมื่อเริ่มต้นการทำงานแล้วให้ใช้คำสั่ง
```bash
sudo docker run hello-world
```
เพื่อดูว่า Docker ทำงานแล้วหรือยัง
##
## Dowload Docker-compose
ทำการติดตั้งตัว Docker-compose 
```bash
sudo apt install docker-compose
```
เมื่อทำการติดตั้งเสร็จให้อัปเดด ด้วยคำสั่ง
```bash
sudo apt update
```
##
## Install system
ทำการสร้าง Folder สำหรับในการเก็บตัวระบบด้วยคำสั่ง
```bash
mkdir <ชื่อ folder>
```
จากนั้นทำการใช้คำสั่ง cd เข้าไปที่ folder นั้น
```bash
cd <ชื่อ folder>
```
ทำการ clone ตัวระบบมาที่ folder ที่เราได้สร้างไว้ด้วยคำสั่ง
```bash
git clone https://github.com/FrameMeRy/kafka-elk
```

ทำการเพื่ม Memory ในการทำงานของโปรแกรมก่อน ด้วยการเข้าไปที่ file sysctl.conf
```bash
sudo nano /etc/sysctl.conf
```
และนำข้อตวามด้านล่างไปใส่ใน file นั้นจากนั้นทำการ save และออกจาก file นั้น 
```bash
vm.max_map_count=262144
```
และทำการเริ่มการทำงานของ sysctl ใหม่ด้วย
```bash
sudo sysctl -p /etc/sysctl.conf
```
ทำการเข้าไปที่ folder kafka-elk-docker-compose-master ด้วยคำสั่ง
```bash
cd kafka-elk-docker-compose-master
```
เมื่อเข้าไปที่ folder ตัวระบบแล้วให้ทำการสร้าง folder ที่ใช้สำหรับในการจัดเก็บข้อมูลของ Elasticsearch ด้วยคำสั่ง
```bash
mkdir esdata && mkdir apache-logs
```
และทำการเปลี่ยนแปลงสิทธิ์การเข้าถึงไฟล์ filebeat.yaml ด้วยคำสั่ง
```bash
chmod go-w filebeat.yml
```
จากนั้นนำระบบที่ติดตั้งมาไปใช้การ Docker-compose ด้วยคำสั่ง
```bash
sudo docker-compose up -d
```
ระหว่างติดตั้งจะมีคำสั่ง  docker-compose build ในข้อความระหว่างติดตั้ง เมื่อทำการติดตั้งเสร็จ ให้ทำการ
```bash
sudo docker-compose build -d
```
##
## การใช้งาน

ทำการติดตั้งตัว curl ซึ่งเป็นเครื่องมือที่ใช้ในการโอนย้ายข้อมูลผ่านโปรโตคอล ด้วย
```bash
sudo apt install curl
```

โดยให้ตั้งค่าเริ่มต้น container ของ apache ที่สร้าง log จะแสดงผ่านพอร์ต 8888 
```bash
sudo curl http://localhost:8888/
```
ทำการเช็คตัวระบบ ELK ด้วยการใช้ 
```bash
sudo docker-compose ps
```
##
Credit by https://github.com/sermilrod
