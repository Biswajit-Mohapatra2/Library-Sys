# Library-Management System 

## Prerequisites: 

### Update the System Packages:

```shell
sudo apt update -y
```
### Install All Dependancies:

```python
pip install -r requirements.txt
```
### Install MYSQL Server And Start the Server:

```shell
sudo apt install mysql-server -y
```
```shell
sudo service mysql start
```
### To Enter Inside MYSQL Server:
```sql
sudo mysql -u root -p
# Then Enter your custom password
```
### Now Create Your DB, User and Grant Permission to User for Perform Action:

``` CREATE DATABASE library_db; ```

``` CREATE USER 'myapp'@'localhost' IDENTIFIED BY 'password'; ```

``` GRANT ALL PRIVILEGES ON library_db.* TO 'myapp'@'localhost'; ```

### Table Creation Inside DB:
```sql
USE library_db;
```
```sql
CREATE TABLE book (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(80) NOT NULL,
  author VARCHAR(120) NOT NULL,
  price FLOAT NOT NULL
);
```
### Now Exit from SQL Terminal:
```sql
Control + D
```
## Now Run the Python Server:
```python
python app.py
```

<p align="center">
  <img src="https://firebasestorage.googleapis.com/v0/b/mirror-webapp.appspot.com/o/myimages%2F515015ba5ac0-24d1-45ba-a9f5-b9941e6e4a76.gif?alt=media&token=eac99c1f-80e4-4bb2-b666-3f158f98b296&_gl=1*r0n8n6*_ga*OTQwMzkxNTQwLjE2OTc5MDU5NzQ.*_ga_CW55HF8NVT*MTY5NzkwNTk3NC4xLjEuMTY5NzkwNjQ4OS42MC4wLjA." alt="congrats"/>
</p>

