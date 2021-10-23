# Back End

## Setup

1. Create folder secret

2. Create file admin.txt

3. Add your database's name, username and password for MySQL

Example:

```
ecommerce
admin
123456
```

4. Migrate to MySQL

Runs:

```
python manage.py makemigrates

python manage.py migrate
```