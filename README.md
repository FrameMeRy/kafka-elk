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
Credit by https://github.com/sermilrod
