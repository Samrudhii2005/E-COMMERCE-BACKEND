# E-COMMERCE-BACKEND
COMPANY NAME: CODETECH IT SOLUTIONS

NAME: SAMRUDHI GHANATE

Intern ID :CT12DL761

DOMAIN: BACK END DEVELOPMENT

DURATION: 11 WEEKS

MENTOR: NEELA SANTHOSH

PROJECT DESCRIPTION: This project is a backend API for an e-commerce platform built using FastAPI and MySQL, with SQLAlchemy as the ORM and JWT-based authentication. The main aim of this project is to demonstrate a simple yet functional implementation of product management and user authentication using modern Python web development tools. It supports core e-commerce backend features like product CRUD (Create, Read, Update, Delete), user registration and login, and order placement. The structure of this backend is clean and modular, which makes it easy to scale or integrate with a frontend or mobile application later. The backend is built using FastAPI, which is known for its fast performance, automatic documentation through Swagger and Redoc, and ease of use for creating REST APIs.

The database used is MySQL, which stores the data for users, products, and orders. SQLAlchemy helps in interacting with the database using Python classes and methods instead of writing raw SQL queries. The database connection is securely handled using environment variables stored in a .env file, which includes credentials like database username, password, and JWT secret key. This allows for better security and flexibility when deploying the project to different environments.

Users can register using a username and password. Passwords are hashed using the PassLib library before being stored in the database, ensuring that sensitive data is not exposed. Once a user logs in, a JWT (JSON Web Token) is issued, which is then required to access protected routes like creating, updating, or deleting products. The authentication system is simple and efficient, making use of FastAPI’s dependency injection system to validate and authorize users for protected operations. The token-based authentication ensures that only registered users can perform certain actions, such as placing orders or modifying the product catalog.

Products are managed using RESTful routes that allow users to perform all CRUD operations. Users can create new products, view a list of all products, update product details, or delete products. These operations interact with the MySQL database, with SQLAlchemy handling the model definitions and queries. Each product includes basic fields like name, description, price, and stock, allowing for practical inventory control and display.

The order system lets authenticated users place orders for products. Orders are stored in the database with details such as the product ordered and the user who placed it. This provides a simple simulation of how a real e-commerce site would track customer purchases. The backend structure includes routers for clean separation of logic, schemas for request/response validation using Pydantic, and models that define how data is stored in the database.

This backend was tested using Postman for sending requests to the various API endpoints, including user registration, login, creating products, and placing orders. Token-based authorization was also tested through Postman to ensure that only authenticated users could access specific routes. The goal was to keep the project as minimal and understandable as possible while covering the core backend functionality required in an e-commerce platform. This makes it ideal for beginners who are looking to learn backend development using FastAPI and want to understand how to build a secure and functional API.

Overall, this project serves as a clean, beginner-friendly template for anyone who wants to build a backend system for an e-commerce application or learn how to work with FastAPI, MySQL, and JWT authentication.

<img width="1912" height="1199" alt="Image" src="https://github.com/user-attachments/assets/d8b40bcb-2774-44e6-9d01-ebfed0f6febd" />
<img width="1919" height="1198" alt="Image" src="https://github.com/user-attachments/assets/6d160024-9905-45dd-bd47-8a1a72c6bce3" />
<img width="1919" height="1199" alt="Image" src="https://github.com/user-attachments/assets/4b5e8174-594e-47c7-a259-1b38044065a7" />
<img width="1919" height="1199" alt="Image" src="https://github.com/user-attachments/assets/903baf20-47c2-4411-ba08-b75d1a5a118b" />
<img width="1919" height="1196" alt="Image" src="https://github.com/user-attachments/assets/2b69ad36-3d2d-46b2-9715-b62ae2bdfd0e" />
<img width="1919" height="1199" alt="Image" src="https://github.com/user-attachments/assets/e3656853-f534-4df7-ae68-f2b74f279f5f" />
<img width="1919" height="1197" alt="Image" src="https://github.com/user-attachments/assets/397be3da-4303-42bc-b02c-714ed6155903" />
<img width="1918" height="1198" alt="Image" src="https://github.com/user-attachments/assets/1a606e6f-d67c-4970-90fb-34b0291202fa" />
<img width="1919" height="1196" alt="Image" src="https://github.com/user-attachments/assets/14ec1584-b93b-487b-bda5-29419d75b3c7" />
<img width="1919" height="1196" alt="Image" src="https://github.com/user-attachments/assets/e195efee-d475-48e5-a4e8-f8cc7a7a7da0" />
