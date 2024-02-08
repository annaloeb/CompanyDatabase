import mysql.connector

# Running through a docker container
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='change-me',
            database='loeb_db',
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Populate rest of tables
def populate_Tables(conn):
    cursor = conn.cursor()
    sample_customers = [
        ('Nature Lover', 'Charlie Green', '456 Nature St', 'GreenCity', 'GC456', 'GreenLand'),
        ('Organic Market', 'David Davis', '987 Organic Ave', 'OrganicTown', 'OT987', 'OrganicLand'),
        ('Sustainable Goods', 'Eva White', '123 Eco Lane', 'EcoCity', 'EC123', 'EcoNation'),
        ('Earthly Treasures', 'Frank Green', '555 Earth St', 'GreenVille', 'GV555', 'GreenLand'),
        ('Green Living', 'Helen Brown', '789 Green Blvd', 'EcoMetropolis', 'EM789', 'EcoNation'),
        ('Enviro Emporium', 'Ian Johnson', '456 Eco Road', 'EcoVillage', 'EV456', 'EcoCountry'),
        ('Eco Essentials', 'Karen Green', '111 Nature Ave', 'GreenTown', 'GT111', 'GreenNation'),
        ('Green Harmony', 'Luke White', '222 Organic St', 'OrganicVille', 'OV222', 'OrganicLand')
    ]
    insert_statement = "INSERT INTO Customers(CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_statement, sample_customers)

    sample_Orders = [
        (3, '2023-11-05', '2023-11-11', '456 Nature St', 'GreenCity', 'GC456', 'GreenLand'),
        (4, '2023-11-07', '2023-11-13', '987 Organic Ave', 'OrganicTown', 'OT987', 'OrganicLand'),
        (5, '2023-11-09', '2023-11-15', '123 Eco Lane', 'EcoCity', 'EC123', 'EcoNation'),
        (6, '2023-11-11', '2023-11-17', '555 Earth St', 'GreenVille', 'GV555', 'GreenLand'),
        (7, '2023-11-13', '2023-11-19', '789 Green Blvd', 'EcoMetropolis', 'EM789', 'EcoNation'),
        (8, '2023-11-15', '2023-11-21', '456 Eco Road', 'EcoVillage', 'EV456', 'EcoCountry'),
        (9, '2023-11-17', '2023-11-23', '111 Nature Ave', 'GreenTown', 'GT111', 'GreenNation'),
        (10, '2023-11-19', '2023-11-25', '222 Organic St', 'OrganicVille', 'OV222', 'OrganicLand'),
        (1, '2023-11-21', '2023-11-27', '789 Eco Ave', 'EcoTown', 'ET789', 'EcoCountry')
    ]
    insert_Orders = "INSERT INTO Orders(CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity, ShipPostalCode, ShipCountry) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_Orders, sample_Orders)

    sample_Suppliers = [
        ('EcoFriendly Ltd', 'John Doe', '123 Green Road', 'EcoCity', 'EC123', 'Ecoland', '123-456-7890'),
        ('NatureGoods Inc', 'Jane Smith', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210'),
        ('GreenSource Co', 'Mike Green', '789 Eco Blvd', 'EcoTown', 'ET789', 'Ecoland', '555-123-4567'),
        ('OrganicHarvest Ltd', 'Emily White', '234 Organic Lane', 'OrganicVille', 'OV234', 'Organicland', '789-321-6540'),
        ('SustainableSupply Inc', 'Alex Green', '567 Earth St', 'GreenCity', 'GC567', 'Greenland', '234-876-9012'),
        ('GreenTech Solutions', 'David Brown', '890 Green Ave', 'EcoMetropolis', 'EM890', 'EcoNation', '876-234-5670'),
        ('EnviroProducts Co', 'Laura Green', '321 Eco Road', 'EcoVillage', 'EV321', 'EcoCountry', '432-109-8765'),
        ('NaturalLiving Ltd', 'Mark White', '432 Nature Blvd', 'GreenTown', 'GT432', 'GreenNation', '321-678-5432')
    ]
    insert_Suppliers = "INSERT INTO Suppliers(SupplierName, ContactName, Address, City, PostalCode, Country, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_Suppliers, sample_Suppliers)

    sample_Products = [
        ('Eco-friendly Backpack', 3, 'Outdoor', 29.99, 50),
        ('Solar-powered Flashlight', 4, 'Electronics', 14.95, 75),
        ('Recycled Paper Notebook', 5, 'Office Supplies', 5.99, 120),
        ('Vegetarian Cookbook', 6, 'Books', 19.99, 80),
        ('Fair Trade Coffee Beans', 7, 'Food & Beverages', 8.50, 180),
        ('Biodegradable Dish Soap', 3, 'Household', 4.99, 120),
        ('Solar-powered Phone Charger', 4, 'Electronics', 24.99, 0),
    ]
    insert_Products = "INSERT INTO Products(ProductName, SupplierID, Category, UnitPrice, UnitsInStock) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_Products, sample_Products)

    sample_OrderDetails = [
        (3, 4, 1, 29.99),
        (4, 5, 3, 14.95),
        (5, 6, 6, 5.99),
        (6, 8, 2, 8.50),
        (7, 9, 1, 4.99),
        (8, 4, 3, 29.99),
        (9, 6, 1, 5.99),
        (10, 2, 1, 10.50),
        (11, 8, 3, 8.50),
        (11, 2, 1, 10.50)
    ]
    insert_OrderDetails = "INSERT INTO OrderDetails(OrderID, ProductID, Quantity, UnitPrice) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_OrderDetails, sample_OrderDetails)
    print("Data inserted successfully")
    conn.commit()

def getOption():
    print("\nOptions:")
    print("1. List all products that are out of stock")
    print("2. Find the total number of orders placed by each customer")
    print("3. Display the details of the most expensive product ordered in each order")
    print("4. Retrieve a list of products that have never been ordered")
    print('5. Show the total revenue (price * quantity) generated by each supplier')
    print('6. Place an order')
    print('7. Exit')
    option = input("Enter the option number: ")
    # make sure input is a valid menu option
    while option not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid option. Please enter a number between 1 and 7.")
        option = input("Enter the option number: ")
    return option

def list_OutOfStock(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT ProductName FROM Products WHERE UnitsInStock = 0"
        cursor.execute(query)
        print("\nProducts currently out of stock:")
        # show results of query
        for row in cursor:
            product_name = row[0]
            print(f"Product Name: {product_name}")
    #error handling
    except mysql.connector.Error as e:
        print(f"Error fetching records: {e}")

def total_num_orders_by_cust(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT c.CustomerID, c.ContactName, COUNT(o.OrderID) 
        FROM Customers c, Orders o 
        WHERE c.CustomerID = o.CustomerID 
        GROUP BY CustomerID"""
        cursor.execute(query)
        print("\nTotal number of orders placed by each customer:")
        for row in cursor:
            customerID = row[0]
            customerName = row[1]
            numOrders = row[2]
            print(f"Customer ID: {customerID}, Customer Name: {customerName}, Number of Orders Placed: {numOrders}")
    except mysql.connector.Error as e:
        print(f"Error fetching records: {e}")

def display_details(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT od.OrderID, p.* 
        FROM OrderDetails od 
        JOIN Products p ON od.ProductID = p.ProductID 
        JOIN (SELECT OrderID, MAX(UnitPrice) AS MaxUnitPrice FROM OrderDetails GROUP BY OrderID) max_prices 
        ON od.OrderID = max_prices.OrderID AND od.UnitPrice = max_prices.MaxUnitPrice"""
        cursor.execute(query)
        print("\nDetails of the most expensive product ordered in each order:")
        for row in cursor:
            orderID = row[0]
            productID = row[1]
            productName = row[2]
            supplierID = row[3]
            category = row[4]
            UnitPrice = row[5]
            unitsInStock = row[6]
            print(f"Order ID: {orderID}, Product ID: {productID}, Product Name: {productName}, Supplier ID: {supplierID}, Category: {category}, Unit Price: {UnitPrice}, Units left in stock: {unitsInStock}")
    except mysql.connector.Error as e:
        print(f"Error fetching records: {e}")

def products_not_ordered(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT p.ProductName, p.ProductID 
        FROM Products p 
        LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID 
        WHERE od.ProductID IS NULL"""
        cursor.execute(query)
        print("\nProducts that have not been ordered:")
        for row in cursor:
            productName = row[0]
            productID = row[1]
            print(f"Product ID: {productID}, Product Name: {productName}")
    except mysql.connector.Error as e:
        print(f"Error fetching records: {e}")

def supplier_revenue(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT s.SupplierID, s.SupplierName, SUM(od.Quantity * p.UnitPrice) AS TotalRevenue
        FROM Suppliers s
        LEFT JOIN Products p ON s.SupplierID = p.SupplierID
        LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID
        GROUP BY s.SupplierID, s.SupplierName"""
        cursor.execute(query)
        print("\nTotal revenue generated by each supplier:")
        for row in cursor:
            supplierID = row[0]
            supplierName = row[1]
            totalRevenue = row[2]
            print(f"Supplier ID: {supplierID}, Supplier Name: {supplierName}, Total Revenue: ${totalRevenue}")
    except mysql.connector.Error as e:
        print(f"Error fetching records: {e}")

def add_order(conn):
    try:
        cursor = conn.cursor()

        # Stored procedure to add an order
        addOrder = """
        CREATE PROCEDURE IF NOT EXISTS addOrder(
        IN p_customerID INT, 
        IN p_productID INT, 
        IN p_quantity INT, 
        IN p_address VARCHAR(100), 
        IN p_city VARCHAR(100), 
        IN p_zip VARCHAR(10), 
        IN p_country VARCHAR(100))
        BEGIN         
            INSERT INTO Orders(CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity, ShipPostalCode, ShipCountry)
            VALUES (p_customerID, NOW(), NOW() + INTERVAL 7 DAY, p_address, p_city, p_zip, p_country);
            
            SET @last_order_id = LAST_INSERT_ID();

            INSERT INTO OrderDetails(OrderID, ProductID, Quantity, UnitPrice)
            SELECT @last_order_id, p_productID, p_quantity, UnitPrice
            FROM Products
            WHERE ProductID = p_productID;

            UPDATE Products
            SET UnitsInStock = UnitsInStock - p_quantity
            WHERE ProductID = p_productID;
        END;"""

        updateStock = """
                CREATE PROCEDURE IF NOT EXISTS updateStockQuantity(
                IN p_productID INT,
                IN p_quantity INT)
                BEGIN
                    UPDATE Products
                    SET QuantityInStock = QuantityInStock - p_quantity
                    WHERE ProductID = p_productID;
                END;"""

        cursor.execute(addOrder)
        cursor.execute(updateStock)

        # User input of order information
        while True:
            try:
                cID = input("Enter Customer ID: ")
                pID = input("Enter Product ID: ")
                quantity = int(input("Enter Quantity: "))
                address = input("Enter address: ")
                city = input("Enter city: ")
                zip = input("Enter postal code: ")
                country = input("Enter country: ")
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Call the stored procedure
        procedure_call = "CALL addOrder(%s, %s, %s, %s, %s, %s, %s)"
        cursor.callproc("addOrder", (cID, pID, quantity, address, city, zip, country))

        conn.commit()
        print("Order added successfully.")
    except mysql.connector.Error as e:
        print(f"Error adding order: {e}")


def main():
    conn = connect_to_database()
    if conn:
        exit = False
        # used in the first run of the program, then commented after tables have been populated
        #populate_Tables(conn)
        while not exit:
            option = getOption()
            if option == "1":
                list_OutOfStock(conn)
            elif option == "2":
                total_num_orders_by_cust(conn)
            elif option == "3":
                display_details(conn)
            elif option == "4":
                products_not_ordered(conn)
            elif option == "5":
                supplier_revenue(conn)
            elif option == "6":
                add_order(conn)
            elif option == "7":
                exit = True
        conn.close()


main()
