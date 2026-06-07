CREATE DATABASE RetailAnalytics;
USE RetailAnalytics;

/* ==========================
   CUSTOMERS
========================== */
CREATE TABLE dbo.Customers (
    CustomerID       NVARCHAR(20) PRIMARY KEY,
    CustomerName     NVARCHAR(100),
    Gender           NVARCHAR(20),
    Age              INT,
    City             NVARCHAR(100),
    State            NVARCHAR(100),
    Country          NVARCHAR(100),
    CustomerSegment  NVARCHAR(50),
    JoinDate         DATE
);


/* ==========================
   PRODUCTS
========================== */
CREATE TABLE dbo.Products (
    ProductID        NVARCHAR(20) PRIMARY KEY,
    ProductName      NVARCHAR(200),
    Category         NVARCHAR(100),
    SubCategory      NVARCHAR(100),
    Brand            NVARCHAR(100),
    UnitPrice        DECIMAL(18,2),
    UnitCost         DECIMAL(18,2)
);


/* ==========================
   SUPPLIERS
========================== */
CREATE TABLE dbo.Suppliers (
    SupplierID       NVARCHAR(20) PRIMARY KEY,
    SupplierName     NVARCHAR(200),
    SupplierType     NVARCHAR(100),
    City             NVARCHAR(100),
    State            NVARCHAR(100),
    Country          NVARCHAR(100),
    Rating           DECIMAL(3,1)
);

/* ==========================
   INVENTORY
========================== */
CREATE TABLE dbo.Inventory (
    ProductID        NVARCHAR(20) PRIMARY KEY,
    StockOnHand      INT,
    ReorderLevel     INT,
    Warehouse        NVARCHAR(50)
);


/* ==========================
   PURCHASES
========================== */
CREATE TABLE dbo.Purchases (
    PurchaseID       NVARCHAR(20) PRIMARY KEY,
    PurchaseDate     DATE,
    SupplierID       NVARCHAR(20),
    ProductID        NVARCHAR(20),
    Quantity         INT,
    UnitCost         DECIMAL(18,2),
    PurchaseAmount   DECIMAL(18,2)
);


/* ==========================
   SALES
========================== */
CREATE TABLE dbo.Sales (
    SalesID          NVARCHAR(20) PRIMARY KEY,
    OrderDate        DATE,
    CustomerID       NVARCHAR(20),
    ProductID        NVARCHAR(20),
    Quantity         INT,
    UnitPrice        DECIMAL(18,2),
    SalesAmount      DECIMAL(18,2),
    Discount         DECIMAL(10,2),
    Profit           DECIMAL(18,2)
);

SELECT COUNT(*) FROM Customers;
SELECT COUNT(*) FROM Products;
SELECT COUNT(*) FROM Suppliers;
SELECT COUNT(*) FROM Inventory;
SELECT COUNT(*) FROM Purchases;
SELECT COUNT(*) FROM Sales;

-----  Customers Cleaning ----
---- Check Missing Values
SELECT
COUNT(*) AS TotalRows,
SUM(CASE WHEN CustomerName IS NULL THEN 1 ELSE 0 END) AS MissingCustomerName,
SUM(CASE WHEN Gender IS NULL THEN 1 ELSE 0 END) AS MissingGender,
SUM(CASE WHEN City IS NULL THEN 1 ELSE 0 END) AS MissingCity
FROM Customers;
--- Remove Spaces
UPDATE Customers
SET
CustomerName = LTRIM(RTRIM(CustomerName)),
Gender = LTRIM(RTRIM(Gender)),
City = LTRIM(RTRIM(City)),
State = LTRIM(RTRIM(State)),
Country = LTRIM(RTRIM(Country)),
CustomerSegment = LTRIM(RTRIM(CustomerSegment));
--- Standardize Gender
UPDATE Customers
SET Gender =
CASE
WHEN LOWER(Gender)='male' THEN 'Male'
WHEN LOWER(Gender)='female' THEN 'Female'
ELSE 'Unknown'
END;
--  Check Duplicates
SELECT CustomerID,COUNT(*)
FROM Customers
GROUP BY CustomerID
HAVING COUNT(*)>1;

-----  Products Cleaning --- 
--- Missing Values
SELECT
SUM(CASE WHEN ProductName IS NULL THEN 1 ELSE 0 END) MissingProduct,
SUM(CASE WHEN Brand IS NULL THEN 1 ELSE 0 END) MissingBrand
FROM Products;
-- Remove Spaces
UPDATE Products
SET
ProductName = LTRIM(RTRIM(ProductName)),
Category = LTRIM(RTRIM(Category)),
SubCategory = LTRIM(RTRIM(SubCategory)),
Brand = LTRIM(RTRIM(Brand));
-- Check Cost > Price
SELECT *
FROM Products
WHERE UnitCost > UnitPrice;

-- Duplicates
SELECT ProductID,COUNT(*)
FROM Products
GROUP BY ProductID
HAVING COUNT(*)>1;

select * from Products

----- Suppliers Cleaning -----
--- Missing Values
SELECT
SUM(CASE WHEN SupplierName IS NULL THEN 1 ELSE 0 END) MissingSupplier,
SUM(CASE WHEN Rating IS NULL THEN 1 ELSE 0 END) MissingRating
FROM Suppliers;
-- Remove Spaces
UPDATE Suppliers
SET
SupplierName = LTRIM(RTRIM(SupplierName)),
SupplierType = LTRIM(RTRIM(SupplierType)),
City = LTRIM(RTRIM(City)),
State = LTRIM(RTRIM(State)),
Country = LTRIM(RTRIM(Country));
-- Fill Missing Rating

SELECT DISTINCT Rating
FROM Suppliers
WHERE TRY_CAST(Rating AS DECIMAL(10,2)) IS NULL
  AND Rating IS NOT NULL;

  SELECT *
FROM Suppliers
WHERE Rating IS NULL
   OR LTRIM(RTRIM(Rating)) = '';

   UPDATE Suppliers
SET Rating = NULL
WHERE LTRIM(RTRIM(Rating)) = '';

UPDATE Suppliers
SET Rating = (
    SELECT AVG(TRY_CAST(Rating AS DECIMAL(10,2)))
    FROM Suppliers
    WHERE TRY_CAST(Rating AS DECIMAL(10,2)) IS NOT NULL
)
WHERE Rating IS NULL;

SELECT *
FROM Suppliers
WHERE TRY_CAST(Rating AS DECIMAL(3,1)) IS NULL
  AND Rating IS NOT NULL;

  ALTER TABLE Suppliers
ALTER COLUMN Rating DECIMAL(3,1);

-- Duplicates 
SELECT SupplierID,COUNT(*)
FROM Suppliers
GROUP BY SupplierID
HAVING COUNT(*)>1;

---- Inventory Cleaning -----
--- Negative Stock
SELECT count(*)
FROM Inventory
WHERE StockOnHand < 0

UPDATE Inventory
SET StockOnHand = 0
WHERE StockOnHand < 0;
--- Remove Spaces
UPDATE Inventory
SET Warehouse = UPPER(LTRIM(RTRIM(Warehouse)));
--- Duplicates
SELECT ProductID,COUNT(*)
FROM Inventory
GROUP BY ProductID
HAVING COUNT(*)>1;

select * from Inventory

------ Purchases Cleaning  ------
--- Missing Values
SELECT *
FROM Purchases
WHERE SupplierID IS NULL
OR ProductID IS NULL;
---- Negative Values
SELECT count(*)
FROM Purchases
WHERE Quantity < 0
OR UnitCost < 0
OR PurchaseAmount < 0;

SELECT
COLUMN_NAME,
DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Purchases';

ALTER TABLE Purchases
ALTER COLUMN Quantity INT;

ALTER TABLE Purchases
ALTER COLUMN UnitCost DECIMAL(18,2);

ALTER TABLE Purchases
ALTER COLUMN PurchaseAmount DECIMAL(18,2);

---- Duplicates
SELECT PurchaseID,COUNT(*)
FROM Purchases
GROUP BY PurchaseID
HAVING COUNT(*)>1;

----- Sales Cleaning ------
---- Missing Values
SELECT *
FROM Sales
WHERE CustomerID IS NULL
OR ProductID IS NULL;

--- Negative Values
SELECT *
FROM Sales
WHERE Quantity < 0
OR SalesAmount < 0;




ALTER TABLE Sales
ALTER COLUMN Quantity INT;

ALTER TABLE Sales
ALTER COLUMN UnitPrice DECIMAL(18,2);

ALTER TABLE Sales
ALTER COLUMN SalesAmount DECIMAL(18,2);

ALTER TABLE Sales
ALTER COLUMN Discount DECIMAL(18,2);

ALTER TABLE Sales
ALTER COLUMN Profit DECIMAL(18,2);

--- Check Profit
SELECT COUNT(*)
FROM Sales
WHERE Profit < 0;
--- Duplicates
SELECT SalesID,COUNT(*)
FROM Sales
GROUP BY SalesID
HAVING COUNT(*)>1;

--- add foreign key 
ALTER TABLE Inventory
ADD CONSTRAINT FK_Inventory_Products
FOREIGN KEY (ProductID)
REFERENCES Products(ProductID);

ALTER TABLE Purchases
ADD CONSTRAINT FK_Purchases_Products
FOREIGN KEY (ProductID)
REFERENCES Products(ProductID);

ALTER TABLE Purchases
ADD CONSTRAINT FK_Purchases_Suppliers
FOREIGN KEY (SupplierID)
REFERENCES Suppliers(SupplierID);

ALTER TABLE Sales
ADD CONSTRAINT FK_Sales_Customers
FOREIGN KEY (CustomerID)
REFERENCES Customers(CustomerID);

ALTER TABLE Sales
ADD CONSTRAINT FK_Sales_Products
FOREIGN KEY (ProductID)
REFERENCES Products(ProductID);


CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY,
    FullDate DATE,
    Year INT,
    Quarter INT,
    MonthNumber INT,
    MonthName VARCHAR(20)
);

SELECT
    CustomerID,
    CustomerName,
    Gender,
    Age,
    City,
    State,
    Country,
    CustomerSegment
INTO DimCustomers
FROM Customers;

SELECT
    ProductID,
    ProductName,
    Category,
    SubCategory,
    Brand
INTO DimProducts
FROM Products;

SELECT
    SupplierID,
    SupplierName,
    SupplierType,
    City,
    State,
    Country,
    Rating
INTO DimSuppliers
FROM Suppliers;

SELECT
    SalesID,
    OrderDate,
    CustomerID,
    ProductID,
    Quantity,
    UnitPrice,
    SalesAmount,
    Discount,
    Profit
INTO FactSales
FROM Sales;

SELECT
    PurchaseID,
    PurchaseDate,
    SupplierID,
    ProductID,
    Quantity,
    UnitCost,
    PurchaseAmount
INTO FactPurchases
FROM Purchases;

