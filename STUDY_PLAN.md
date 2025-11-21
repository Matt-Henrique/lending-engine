# 📘 Study Plan for LendAPI - Software Engineer (Remote)

This study plan is tailored for the **Software Engineer role at LendAPI**, focusing on Python (Django), React, scalable systems, financial compliance, and cloud/DevOps. It is structured into **4 sprints**, covering all essential skills required by the position.

---

## 🏁 Overview
**Total Duration:** 6–8 weeks  
**Goal:** Build strong proficiency in backend, frontend, cloud, and scalability concepts required for contributing to LendAPI’s large-scale fintech platform.

---

## 🧭 Sprint 1 — Core Backend Foundations (Python, Django, Celery)

### 🎯 Objectives
- Strengthen backend fundamentals with Python and Django.
- Learn how to design scalable REST APIs.
- Use Celery + Redis for asynchronous background tasks.
- Improve PostgreSQL querying and performance.

### 📚 Topics to Cover
- Advanced Python: type hints, async, design patterns
- Django & Django REST Framework (DRF): CBVs, ORM depth
- Celery workers and distributed task queues
- PostgreSQL: indexes, EXPLAIN ANALYZE, performance tuning
- Authentication: JWT, OAuth2

### 🛠️ Practice
- Build a REST API with authentication and permissions
- Implement Celery tasks for email notifications or async jobs
- Add caching and request throttling

---

## 🧭 Sprint 2 — Frontend (React) + System Architecture

### 🎯 Objectives
- Develop modular and scalable React applications.
- Understand modern system design and microservices.
- Explore performance techniques and observability.

### 📚 Topics to Cover
- React: hooks, context, state management, optimization
- System Design: Clean Architecture, Hexagonal Architecture
- Microservices: API gateways, communication patterns
- Caching strategies and load balancing
- Observability: logging, metrics, tracing (OpenTelemetry basics)

### 🛠️ Practice
- Build a React SPA integrated with your Django backend
- Simulate a microservices architecture using Docker
- Add structured logging and simple tracing

---

## 🧭 Sprint 3 — Cloud, DevOps & Security (AWS, Docker, Terraform)

### 🎯 Objectives
- Deploy scalable applications using cloud infrastructure.
- Learn Terraform and Infrastructure as Code.
- Understand fintech-grade security and compliance.

### 📚 Topics to Cover
- AWS: ECS, EC2, RDS, Lambda, IAM, SQS
- Docker: images, orchestration, multi-container setups
- Terraform: modules, variables, infra provisioning
- CI/CD: GitHub Actions pipelines
- Networking: VPCs, subnets, gateways
- Secrets management (AWS Secrets Manager, Vault)

### 🔐 Security & Compliance
- PCI-DSS fundamentals
- SOC 2 principles
- GDPR requirements
- Encryption (in transit and at rest), auditing, log retention

### 🛠️ Practice
- Deploy Django + React with Docker on AWS
- Build Terraform scripts for VPC, ECS, and RDS
- Create a CI/CD pipeline with linting, tests, and auto-deploy

---

## 🧭 Sprint 4 — High Scalability & Fintech Specialization

### 🎯 Objectives
- Understand how to scale services to 3000+ RPS.
- Optimize databases with billions of records.
- Explore event-driven and distributed architectures.

### 📚 Topics to Cover
- Horizontal scaling, sharding, replication
- PostgreSQL partitioning and optimizer internals
- Kafka / RabbitMQ event-driven communication
- Distributed tracing and debugging
- Optional: CQRS, Event Sourcing

### 🛠️ Practice
- Load test your API with Locust or K6
- Partition PostgreSQL tables for performance
- Process simulated financial transactions with events

### 📦 Deliverables
- Full-stack Django + React fintech project
- Celery async worker system
- Terraform infrastructure for AWS
- CI/CD pipeline
- Load test report
- Security & compliance documentation
