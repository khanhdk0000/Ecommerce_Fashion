CREATE KEYSPACE IF NOT EXISTS ecommerce
   WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};

CREATE TABLE IF NOT EXISTS ecommerce.product(
    product_id int PRIMARY KEY,
    product_name text,
    product_gender text,
    product_quantity int,
    product_color text,
    product_type text,
    product_price decimal,
    image_link text,
    subcategory text,
    category text    
)WITH comment = 'Find information about a product';

CREATE TABLE IF NOT EXISTS ecommerce.order_detail(
    order_id int,
    product_id int,
    quantity int,
    price decimal,
    PRIMARY KEY(order_id, product_id)
)WITH comment = 'Find information about a order detail';

CREATE TABLE IF NOT EXISTS ecommerce.product_by_category(
    product_id int,
    product_name text,
    product_gender text,
    product_quantity int,
    product_color text,
    product_type text,
    product_price decimal,
    image_link text,
    category text,
	PRIMARY KEY ((category), product_id)
)WITH comment = 'Find information about a product by category';


CREATE TABLE IF NOT EXISTS ecommerce.product_by_subcategory(
    product_id int,
    product_name text,
    product_gender text,
    product_quantity int,
    product_color text,
    product_type text,
    product_price decimal,
    image_link text,
    subcategory text,
	PRIMARY KEY ((subcategory), product_id)
)WITH comment = 'Find information about a product by subcategory';

CREATE TABLE IF NOT EXISTS ecommerce.product_by_gender(
    product_id int,
    product_name text,
    product_gender text,
    product_quantity int,
    product_color text,
    product_type text,
    product_price decimal,
    image_link text,
	PRIMARY KEY ((product_gender), product_id)
)WITH comment = 'Find information about a product by gender';
