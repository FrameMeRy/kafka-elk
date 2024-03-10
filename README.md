# Kafka-ELK for Education in ITD62-332
## Update&Upgrade you software 
ใช้คำสั่งด้านล่างที่ให้ไปเพื่อทำการ Update และ Upgrade ตัวซอฟแวร์ หรือระบบต่างๆ ภายในเครื่อง

```bash
sudo apt update
```
```bash
sudo apt upgrade
```
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

## Dowload Docker-compose
ทำการติดตั้งตัว Docker-compose 
```bash
sudo apt install docker-compose
```
เมื่อทำการติดตั้งเสร็จให้อัปเดด ด้วยคำสั่ง
```bash
sudo apt update
```
## Install system
ทำการสร้าง Folder สำหรับในการเก็บตัวระบบด้วยคำสั่ง
```bash
mkdir <ชื่อ folder>
```
จากนั้นทำการใช้คำสั่ง cd เข้าไปที่ folder นั้น
```bash
cd <ชื่อ folder>
```

Credit by https://github.com/sermilrod
