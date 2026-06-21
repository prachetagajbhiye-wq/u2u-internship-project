# Data Directory

## Overview

This directory contains all datasets collected, organized, and documented during Week 2 of the AI Internship project.

The data supports the development of an AI-Powered Educational Learning Platform that integrates:

- Large Language Models (LLMs)
- Retrieval Augmented Generation (RAG)
- Vector Databases
- Adaptive Learning
- Learning Analytics
- Educational Content Generation

---

# Directory Structure

data/

├── raw/

├── cleaned/

├── documentation/

├── schema/

├── README.md

├── data_strategy.md

---

# Raw Data

The raw folder contains original datasets collected from various educational sources.

## PDF Documents

Location:

data/raw/pdfs/

Files:

- operating_systems_notes.pdf
- dbms_notes.pdf
- computer_networks_notes.pdf
- dsa_notes.pdf

Purpose:

These documents form the primary knowledge base for the RAG pipeline.

Usage:

PDF Upload
→ Parsing
→ Chunking
→ Embedding Generation
→ Vector Database Storage
→ Semantic Retrieval
→ AI Response Generation

Supports Features:

- Chat with Documents
- Source Citations
- Explain Mode
- AI Learning Companion

---

## CSV Datasets

Location:

data/raw/csv/

### educational_qa.csv

Purpose:

Educational question-answer dataset used for evaluation and testing.

Supports:

- QA Validation
- Response Evaluation
- Educational Assistance

### student_performance.csv

Purpose:

Student performance analysis and educational analytics.

Supports:

- Weakness Detection Engine
- Learning Analytics
- Personalized Recommendations

---

## JSON Datasets

Location:

data/raw/json/

### flashcards.json

Purpose:

Structured flashcard content.

Supports:

- Flashcard Generator
- Revision Assistance

### quiz_questions.json

Purpose:

Structured quiz dataset.

Supports:

- Quiz Generator
- Adaptive Quiz System

---

## Excel Dataset

Location:

data/raw/excel/

### subjects_topics.xlsx

Purpose:

Subject-topic hierarchy and difficulty mapping.

Supports:

- Study Planner
- Topic Recommendations
- Learning Path Generation

---

# Cleaned Data

Location:

data/cleaned/

Purpose:

Contains processed and validated datasets prepared for future AI model development.

Cleaning activities include:

- Duplicate Removal
- Missing Value Handling
- Data Standardization
- Format Validation

---

# Documentation

Location:

data/documentation/

Purpose:

Contains information about dataset origins, usage, and collection strategy.

Files:

- data_sources.md

---

# Storage Schema

Location:

data/schema/

Purpose:

Defines storage architecture and future database organization.

Files:

- storage_schema.md

---

# Feature-to-Data Mapping

| Feature | Dataset |
|----------|----------|
| Chat with Documents | PDFs |
| RAG Pipeline | PDFs |
| Source Citations | PDFs |
| Flashcard Generator | flashcards.json |
| Quiz Generator | quiz_questions.json |
| Adaptive Quiz System | quiz_questions.json |
| Weakness Detection | student_performance.csv |
| Learning Analytics | student_performance.csv |
| Study Planner | subjects_topics.xlsx |
| AI Learning Companion | PDFs + CSVs |

---

# Data Flow Architecture

PDF Documents
↓
Document Parsing
↓
Text Cleaning
↓
Chunking
↓
Embedding Generation
↓
Vector Database
↓
Semantic Search
↓
LLM Response Generation

Structured Datasets (CSV / JSON / Excel)
↓
Analytics Processing
↓
Quiz Generation
↓
Flashcard Generation
↓
Study Planning
↓
Personalized Learning Support

---

# Data Collection Summary

| Data Type | File Count | Purpose |
|------------|------------|----------|
| PDF | 4 | RAG Knowledge Base |
| CSV | 2 | Analytics and Evaluation |
| JSON | 2 | Flashcards and Quizzes |
| Excel | 1 | Subject-Topic Mapping |

Total Datasets Collected: 9

---

# Data Processing and Validation

The collected datasets are validated before being used...

Implementation:

scripts/data_cleaning.py

Generated Outputs:

- cleaned_student_performance.csv
- cleaned_educational_qa.csv

---

# Future Scope

Future versions of the platform may include:

- Previous Year Question Banks
- Multi-language Educational Resources
- Student Interaction Logs
- Personalized Learning Histories
- Evaluation Datasets

