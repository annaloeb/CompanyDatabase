CREATE TABLE Suppliers (
SupplierID INT AUTO_INCREMENT PRIMARY KEY,
SupplierName VARCHAR(255) NOT NULL,
ContactName VARCHAR(255),
Address VARCHAR(255),
City VARCHAR(100),
PostalCode VARCHAR(20),
Country VARCHAR(100),
Phone VARCHAR(20)
);

CREATE TABLE Products (
ProductID INT AUTO_INCREMENT PRIMARY KEY,
ProductName VARCHAR(255) NOT NULL,
SupplierID INT,
Category VARCHAR(100),
UnitPrice DECIMAL(10, 2),
UnitsInStock INT,
FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);
CREATE TABLE Customers (
CustomerID INT AUTO_INCREMENT PRIMARY KEY,
CustomerName VARCHAR(255) NOT NULL,
ContactName VARCHAR(255),
Address VARCHAR(255),
City VARCHAR(100),
PostalCode VARCHAR(20),
Country VARCHAR(100)
);

CREATE TABLE Orders (
OrderID INT AUTO_INCREMENT PRIMARY KEY,
CustomerID INT,
OrderDate DATE,
ShipDate DATE,
ShipAddress VARCHAR(255),
ShipCity VARCHAR(100),
ShipPostalCode VARCHAR(20),
ShipCountry VARCHAR(100),
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
CREATE TABLE OrderDetails (
OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
OrderID INT,
ProductID INT,
Quantity INT,
UnitPrice DECIMAL(10, 2),
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Inserting data into Suppliers
INSERT INTO Suppliers (SupplierName, ContactName, Address, City, PostalCode,
Country, Phone) VALUES
('EcoFriendly Ltd', 'John Doe', '123 Green Road', 'EcoCity', 'EC123', 'Ecoland',
'123-456-7890'),
('NatureGoods Inc', 'Jane Smith', '456 Natural Way', 'GreenVille', 'GV456',
'Greenland', '987-654-3210');
-- Inserting data into Products
INSERT INTO Products (ProductName, SupplierID, Category, UnitPrice, UnitsInStock)
VALUES
('Bamboo Toothbrush', 1, 'Personal Care', 2.99, 100),
('Reusable Water Bottle', 1, 'Outdoor', 10.50, 200),
('Organic Cotton T-shirt', 2, 'Clothing', 15.99, 150);
-- Inserting data into Customers
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode,
Country) VALUES
('Eco Shopper', 'Alice Johnson', '789 Eco Ave', 'EcoTown', 'ET789', 'EcoCountry'),
('Green Buyer', 'Bob Brown', '321 Green St', 'EcoVille', 'EV321', 'EcoLand');
-- Inserting data into Orders
INSERT INTO Orders (CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity,
ShipPostalCode, ShipCountry) VALUES
(1, '2023-11-01', '2023-11-05', '789 Eco Ave', 'EcoTown', 'ET789', 'EcoCountry'),
(2, '2023-11-03', '2023-11-08', '321 Green St', 'EcoVille', 'EV321', 'EcoLand');
-- Inserting data into OrderDetails
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice) VALUES
(1, 1, 2, 2.99),
(1, 3, 1, 15.99),
(2, 2, 1, 10.50);

INSERT INTO Orders (CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity,
ShipPostalCode, ShipCountry) VALUES
(1, '2023-11-21', '2023-11-27', '789 Eco Ave', 'EcoTown', 'ET789', 'EcoCountry')
