<h2 align="center"><b>DATA GENERATION & SCHEMA DESIGN CODE</b></h2>

----


In this branch, we mainly focus on extracting the data from kaggle dataset [Fashion Product Images Dataset](https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset)


## **Files & Folder Structure**
----
### **Raw Data**

Raw data retrieved from kaggle's link are `images.csv`, `product.csv` and `styles.csv`

### **preprocessed-data**

This file contains of raw data combined and data after preprocessed in file `.ipynb` and ready for database insert

### **queries-code**

This file contains **structure schema code** of MySQL and Cassandra and theirs data imports code including:

- `category_insert.sql` : The insert queries for adding different type of main categories

- `subcategory_insert.sql` : The insert queries for adding different type of sub categories

- `product.sql` : The insert queries for adding different type of products

- ... Same thing apply for all `.cql` files inside cassandra folder

- `schema` folder contains of MySQL and Cassandra database structure.






