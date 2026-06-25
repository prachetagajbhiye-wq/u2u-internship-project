# API Documentation

## Overview

The AI-Powered Educational Learning Platform exposes REST API endpoints that allow the frontend interface to communicate with backend educational services.

The APIs are designed to support chatbot interactions, conversation history management, user information retrieval, feedback collection and system monitoring.

---

# API Endpoint Summary

| Endpoint | Method | Purpose |
|-----------|----------|----------|
| `/api/chat` | POST | Send prompts to the AI system |
| `/api/history` | GET | Retrieve conversation history |
| `/api/users` | GET | Retrieve user information |
| `/api/feedback` | POST | Store user feedback and ratings |
| `/api/health` | GET | Verify server availability |

---

# 1. Chat Endpoint

## Endpoint

`/api/chat`

## Method

`POST`

## Purpose

Accepts educational questions from users and returns AI-generated responses.

### Sample Request

```json
{
  "prompt": "What is CPU Scheduling?"
}
```

### Sample Response

```json
{
  "response": "CPU Scheduling is the process of selecting which process executes next."
}
```

---

# 2. History Endpoint

## Endpoint

`/api/history`

## Method

`GET`

## Purpose

Retrieves previous conversation records.

### Sample Response

```json
{
  "history": [
    {
      "question": "What is TCP?",
      "answer": "TCP is a connection-oriented protocol."
    }
  ]
}
```

---

# 3. Users Endpoint

## Endpoint

`/api/users`

## Method

`GET`

## Purpose

Retrieves user profile information.

### Sample Response

```json
{
  "user_id": 1,
  "name": "Student User"
}
```

---

# 4. Feedback Endpoint

## Endpoint

`/api/feedback`

## Method

`POST`

## Purpose

Stores user ratings and feedback.

### Sample Request

```json
{
  "rating": 5,
  "comment": "Helpful explanation."
}
```

### Sample Response

```json
{
  "status": "Feedback received"
}
```

---

# 5. Health Endpoint

## Endpoint

`/api/health`

## Method

`GET`

## Purpose

Checks whether the backend server is running correctly.

### Sample Response

```json
{
  "status": "healthy"
}
```

---

# Future Educational Endpoints

The following APIs are planned for future platform expansion:

| Endpoint | Method | Purpose |
|-----------|----------|----------|
| `/api/quiz` | POST | Generate quizzes |
| `/api/flashcards` | POST | Generate flashcards |
| `/api/study-plan` | POST | Generate personalized study plans |
| `/api/recommendations` | GET | Provide learning recommendations |

---

# API Design Principles

The APIs follow REST architecture principles and exchange data using JSON format.

## Benefits

- Simplicity
- Scalability
- Easy frontend integration
- Future AI model integration
- Support for educational analytics
- Support for adaptive learning systems

---

# Educational Platform API Workflow

```text
Student User
      │
      ▼
Frontend Interface (React)
      │
      ▼
Backend API Server (Flask)
      │
      ▼
Educational Services

├── Educational Chatbot
├── Quiz Generator
├── Flashcard Generator
├── Study Planner
├── Learning Analytics
└── Recommendation Engine

      │
      ▼
Data Sources

├── PDF Knowledge Base
├── CSV Datasets
├── JSON Datasets
└── Subject-Topic Mapping

      │
      ▼
AI & Retrieval Layer

├── Vector Database
├── Embeddings
├── RAG Pipeline
└── Large Language Model (LLM)
```

---

# Conclusion

The API layer serves as the communication bridge between the frontend application and backend educational services. The documented endpoints provide the foundation for chatbot interactions, analytics, feedback collection and future AI-powered educational features such as quiz generation, flashcard generation, personalized learning recommendations and Retrieval-Augmented Generation (RAG) capabilities.