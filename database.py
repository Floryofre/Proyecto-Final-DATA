import psycopg2

# Conexión a la base de datos
conn = psycopg2.connect(
    host="dpg-cf3enqun6mplnpe950v0-a.oregon-postgres.render.com",
    database="olist",
    user="olist",
    password="IHCRtcefMFbJIjUMXuUMtcIfpTAEo5d1"
)


# Creación del cursor
cur = conn.cursor()

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('closed_deals')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE closed_deals (
            mql_id VARCHAR(255) NOT NULL,
            seller_id VARCHAR(255) NOT NULL,
            sdr_id VARCHAR(255) NOT NULL,
            sr_id VARCHAR(255) NOT NULL,
            won_date DATE NOT NULL,
            business_segment VARCHAR(255),
            lead_type VARCHAR(255)
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")

cur.execute("""
    SELECT to_regclass('customers')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE customers (
            customer_id	 VARCHAR(255) NOT NULL,
            customer_unique_id VARCHAR(255) NOT NULL,
            customer_zip_code_prefix INTEGER NOT NULL,
            customer_city VARCHAR(255) NOT NULL,
            customer_state VARCHAR(255) NOT NULL

        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('geolocation')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE geolocation (
            geolocation_zip_code_prefix INTEGER NOT NULL,
            geolocation_lat DECIMAL NOT NULL,
            geolocation_lng DECIMAL NOT NULL,
            geolocation_city VARCHAR(255) NOT NULL,
            geolocation_state VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('marketing_qualified_leads')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE marketing_qualified_leads (
            mql_id VARCHAR(255) NOT NULL,
            first_contact_date DATE NOT NULL,
            landing_page_id	VARCHAR(255) NOT NULL,
            origin VARCHAR(255)
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('order_items')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE order_items (
            order_id VARCHAR(255) NOT NULL,
            order_item_id INTEGER NOT NULL,
            product_id VARCHAR(255) NOT NULL,
            seller_id VARCHAR(255) NOT NULL,
            shipping_limit_date DATE NOT NULL,
            price DECIMAL NOT NULL,
            freight_value DECIMAL NOT NULL
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('order_payments')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE order_payments (
            order_id VARCHAR(255) NOT NULL,
            payment_type VARCHAR(255) NOT NULL,
            payment_installments INTEGER NOT NULL,
            payment_value DECIMAL NOT NULL
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('order_reviews')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE order_reviews (
            review_id VARCHAR(255) NOT NULL,
            order_id VARCHAR(255) NOT NULL,
            review_score INTEGER NOT NULL,
            review_comment_title VARCHAR(255),
            review_comment_message VARCHAR(255),
            review_creation_date DATE NOT NULL,
            review_answer_timestamp DATE NOT NULL
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('orders')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE orders (
            order_id VARCHAR(255) NOT NULL,
            customer_id VARCHAR(255) NOT NULL,
            order_status VARCHAR(255) NOT NULL,
            order_purchase_timestamp DATE NOT NULL,
            order_approved_at DATE,
            order_delivered_carrier_date DATE,
            order_delivered_customer_date DATE,
            order_estimated_delivery_date DATE NOT NULL
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('olist_sellers')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE olist_sellers (
            seller_id VARCHAR(255) NOT NULL,
            seller_zip_code_prefix INTEGER NOT NULL,
            seller_city VARCHAR(255) NOT NULL,
            seller_state VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('products')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE products (
            product_id VARCHAR(255) NOT NULL,
            product_category_name VARCHAR(255),
            product_photos_qty FLOAT,
            product_weight_g FLOAT,
            product_length_cm FLOAT,
            product_height_cm FLOAT,
            product_width_cm FLOAT
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Verifica si la tabla existe
cur.execute("""
    SELECT to_regclass('product_category_name_translation')
""")

if cur.fetchone()[0] is None:
    # Creación de la tabla
    cur.execute("""
        CREATE TABLE product_category_name_translation (
            product_category_name VARCHAR(255) NOT NULL,
            product_category_name_english VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    print("Tabla creada con éxito")
else:
    print("La tabla ya existe")    

# Cierre de la conexión
cur.close()
conn.close()
