CREATE DATABASE BankingAnalytics;
USE BankingAnalytics;

CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    City VARCHAR(50),
    Occupation VARCHAR(50),
    Income DECIMAL(12,2),
    Credit_Score INT,
    Customer_Tenure INT,
    Risk_Category VARCHAR(20),
    Online_Banking_Status VARCHAR(20)
);

CREATE TABLE Accounts (
    Account_ID INT PRIMARY KEY,
    Customer_ID INT,
    Branch_Name VARCHAR(100),
    Account_Type VARCHAR(50),
    Account_Balance DECIMAL(15,2),
    Credit_Card_Usage DECIMAL(12,2),

    FOREIGN KEY (Customer_ID)
    REFERENCES Customers(Customer_ID)
);

CREATE TABLE Transactions (
    Transaction_ID BIGINT PRIMARY KEY,
    Account_ID INT,
    Transaction_Date DATE,
    Transaction_Amount DECIMAL(12,2),
    Transaction_Type VARCHAR(20),

    FOREIGN KEY (Account_ID)
    REFERENCES Accounts(Account_ID)
);

CREATE TABLE Loans (
    Loan_ID INT PRIMARY KEY,
    Customer_ID INT,
    Loan_Amount DECIMAL(15,2),
    Loan_Status VARCHAR(20),

    FOREIGN KEY (Customer_ID)
    REFERENCES Customers(Customer_ID)
);
select * from customers
select * from accounts
select * from loans
select * from transactions
DESCRIBE accounts;

-- CLEAN THE DATA,CHECK NULL VALUES
SELECT *FROM Customers WHERE Customer_Name IS NULL;
SELECT *FROM accounts WHERE account_balance IS NULL;
SELECT *FROM loans WHERE loan_amount IS NULL;
SELECT *FROM transactions WHERE transaction_amount IS NULL;

-- Check Duplicate Records
SELECT customer_id,
       COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT account_id,
       COUNT(*) AS duplicate_count
FROM accounts
GROUP BY account_id
HAVING COUNT(*) > 1;

-- Total Customers
SELECT COUNT(*) AS total_customers FROM customers;

-- Average Income
SELECT AVG(income) AS average_income FROM customers;

-- Average Customer Age
SELECT AVG(age) AS avg_age
FROM customers;

-- Top 10 Highest Income Customers
SELECT customer_name,income
FROM customers
ORDER BY income DESC
LIMIT 10;

-- Customers by City
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;

-- Customers by Gender
SELECT gender,
       COUNT(*) AS total_customers
FROM customers
GROUP BY gender;

-- Total Bank Balance
SELECT SUM(account_balance) AS total_balance
FROM accounts;

-- Balance by Account Type
SELECT account_type,
       SUM(account_balance) AS total_balance
FROM accounts
GROUP BY account_type;

-- Branch-wise Balance
SELECT branch_name,
       SUM(account_balance) AS total_balance
FROM accounts
GROUP BY branch_name
ORDER BY total_balance DESC;

-- Total Loan Amount
SELECT SUM(loan_amount) AS total_loan
FROM loans;

-- Loan Status Distribution
SELECT loan_status, COUNT(*) AS total
FROM loans
GROUP BY loan_status;

-- 1. Customer + Account summary
CREATE VIEW vw_customer_account_summary AS
SELECT c.customer_id, c.customer_name, c.age, c.city, c.gender,
       a.account_type, a.account_balance,
       COUNT(t.transaction_id) AS total_txn,
       SUM(t.transaction_amount) AS total_amount
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
LEFT JOIN transactions t ON a.account_id = t.account_id
GROUP BY c.customer_id, c.customer_name, c.age, c.city,
         c.gender, a.account_type, a.account_balance
         
select * from vw_customer_account_summary

-- 2. Loan portfolio view
CREATE VIEW vw_loan_summary AS
SELECT c.customer_id, c.customer_name, c.city,
	   l.loan_amount,l.loan_id,
       l.loan_status 
FROM customers c JOIN loans l ON c.customer_id = l.customer_id;

select * from vw_loan_summary

-- 3. Transaction trend
CREATE VIEW vw_transaction_trends AS
SELECT account_id, transaction_type,
       YEAR(transaction_date) AS yr,
       MONTH(transaction_date) AS mo,
       COUNT(*) AS txn_count,
       SUM(transaction_amount) AS total_amount,
       AVG(transaction_amount) AS avg_amount
FROM transactions
GROUP BY account_id, transaction_type,
         YEAR(transaction_date), MONTH(transaction_date);
         
select * from vw_transaction_trends

CREATE VIEW vw_transaction_trends1 AS
SELECT 
    t.account_id,
    a.account_type,
    t.transaction_type,
    YEAR(t.transaction_date) AS yr,
    MONTH(t.transaction_date) AS mo,
    COUNT(*) AS txn_count,
    SUM(t.transaction_amount) AS total_amount,
    AVG(t.transaction_amount) AS avg_amount
FROM transactions t
INNER JOIN accounts a
    ON t.account_id = a.account_id
GROUP BY 
    t.account_id,
    a.account_type,
    t.transaction_type,
    YEAR(t.transaction_date),
    MONTH(t.transaction_date);



