### Organization - Application ###

##  Overview

This project is a FastAPI-based backend system designed using a **microservices architecture**.

The system is divided into two main services:

1. **Auth Service** → Handles authentication and user management
2. **Core Service** → Handles organization, teams, and members

## System Flow (Auth Service + Core Service)

This project follows a microservices architecture with two main services:

Auth Service → Handles authentication (who you are)
Core Service → Handles data (what you own)
JWT Token → Connects both services

---

## Overall Flow

Client (Frontend)
↓
Login / Register (Auth Service)
↓
JWT Token Generated
↓
Client stores token
↓
Client sends request with token
↓
Core Service verifies token
↓
Core Service processes request
↓
Response sent back to client

---

## Auth Service Flow

### 1. User Management

User sends name, email, password
Password is hashed
Data stored securely in database
Password is never returned

### 2. User Login

User provides email and password
Password is verified
Access Token is generated

### 3. Token Usage

Access token is used for API calls
Each request is verified:
Token validity checked
Expiry checked

### 4. Authorization (Permissions)

Users get permissions using:
Roles (admin, manager, user)
Types (organization, team)
Assignments (link user + role + resource)

### 5. Soft Delete

Data is not permanently deleted
deleted_at field is used
Only active records are used

---

## Core Service Flow

### 1. Authentication

Every request must include JWT token
Token is decoded to get user_id

### 2. Organization APIs

Create organization
Check duplicates
Store details

### 3. Team APIs

Teams belong to organizations
Organization must exist

### 4. Member APIs

Members are linked using:
team_id
auth_user_id (from Auth Service)

### 5. Data Handling

Only manages:
Organizations
Teams
Members

### 6. Soft Delete

Same as Auth Service
Records are hidden, not removed

---

## How Auth and Core Services Connect?

Auth Service → generates JWT token
Core Service → verifies token using same secret key
user_id from token is used for linking data

-----------------------------------------------------

## Request Flow (Detailed)

Client Request
↓
Middleware (CORS, Logging)
↓
Router (API endpoint)
↓
Token Verification
↓
Service Layer (Business Logic)
↓
Database Query
↓
Response to Client

---------------------------------

## Key Concepts

Users → Registered users
Roles → Define permissions
Types → Define level
Assignments → Link user + role + resource

--------------------------------------------
## Security Highlights 

Passwords are hashed → protects user passwords
JWT tokens verified → prevents unauthorized access
Access tokens expire → limits misuse
Sensitive data hidden → avoids data leaks

-------------------------------------------------------------

## Architecture Summary (How your system is designed)

Microservices-based design → split into Auth & Core
Separate services → independent scaling
JWT-based authentication → stateless system
Scalable system → can handle growth

-----------------------------------------------------------------
##  How to Run

1. Install dependencies
2. Run Auth Service:
   uvicorn main:app --reload --port 8001

3. Run Core Service:
   uvicorn main:app --reload --port 8002
-----------------------------------------------------------
## System Architecture

```mermaid
flowchart TD
    A[Client / Frontend] --> B[Auth Service]

    B --> C{Login / Register}
    C -->|Register| D[Store User (Hashed Password)]
    C -->|Login| E[Verify Credentials]
    E --> F[Generate JWT Token]

    F --> G[Client Stores Token]

    G --> H[Client Sends Request with JWT]
    H --> I[Core Service]

    I --> J[Verify JWT Token]
    J -->|Valid| K[Extract user_id]
    J -->|Invalid| X[Reject Request]

    K --> L{API Request Type}

    L -->|Organization| M[Create / Manage Organization]

    L -->|Team| N[Create / Manage Team]
    N --> O[Validate Organization Exists]

    L -->|Member| P[Add / Manage Members]
    P --> Q[Link team_id + auth_user_id]

    M --> R[(Database)]
    O --> R
    Q --> R

    R --> S[Return Response]
    S --> T[Client]
```



