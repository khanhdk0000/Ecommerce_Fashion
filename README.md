<h2 align="center"><b>Ecommerce Project</b></h2>

This is the frontend and backend branch. To learn more about our database setup, switch to branch `mysql` and `cassandra`

## **Setup**
----

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

**Note:**
- If you already have the database schema on the device, you should not run those 2 lines. Instead runs

```
python manage.py migrate --fake
```

## **Files & Folder Structure**
----
### **backend**

- `backend` folder contains of initial setups for the django backend to connect to MySQL database.

- `checkout` folder contains models of Registered User, Order and Order's Detail

- `favorite` folder contains models of Favorite and Contains

- `product` folder contains models of Product, Category and Subcategory

#### Compiles the server
```
python manage.py runserver
```

### **Frontend**

#### Project setup
```
cd frontend
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
