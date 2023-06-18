CREATE DATABASE PROPERTY_MANAGEMENT;
CREATE TABLE OWNER (
    owner_id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    phone_no int NOT NULL,
    aadhaar_no int NOT NULL UNIQUE,
    address TEXT,
    city TEXT,
    state TEXT,
    pincode int
);
CREATE TABLE PROPERTIES (
    lease_id int PRIMARY KEY AUTO_INCREMENT,
    owner_id int,
    bhk int NOT NULL,
    washrooms int,
    status varchar(30) NOT NULL,
    address TEXT NOT NULL,
    city varchar(20),
    state varchar(20),
    pincode int,
    other_details varchar(100),
    FOREIGN KEY (owner_id) REFERENCES Owner(owner_id)
);
CREATE TABLE TENANTS (
    tenant_id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    aadhaar_no int UNIQUE NOT NULL,
    email varchar(20),
    phone_no int NOT NULL
);
CREATE TABLE LEASE (
    lease_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id int,
    lease_id int,
    tenant_id int,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    security_amount int,
    lease_amount int,
    rent_amount int,
    due_date int,
    FOREIGN KEY (owner_id) REFERENCES OWNER(owner_id),
    FOREIGN KEY (lease_id) REFERENCES PROPERTIES(lease_id),
    FOREIGN KEY (tenant_id) REFERENCES TENANTS(tenant_id)
);
CREATE TABLE VENDOR (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    work varchar(30),
    email varchar(30),
    address varchar(100),
    phone_id int NOT NULL
);
CREATE TABLE MAINTENANCE_REQUEST (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    lease_id INT,
    tenant_id INT,
    vendor_id INT,
    description varchar(100),
    status varchar(30),
    required_date DATE,
    amount int NOT NULL,
    payment_status INT,
    FOREIGN KEY (lease_id) REFERENCES PROPERTIES(lease_id),
    FOREIGN KEY (tenant_id) REFERENCES TENANTS(tenant_id),
    FOREIGN KEY (vendor_id) REFERENCES VENDOR(vendor_id)
);
CREATE TABLE PAYMENTS (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id INT,
    request_id INT,
    tenant_id INT,
    payment_date DATE NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES OWNER(owner_id),
    FOREIGN KEY (tenant_id) REFERENCES TENANTS(tenant_id),
    FOREIGN KEY (request_id) REFERENCES MAINTENANCE_REQUEST(request_id)
);