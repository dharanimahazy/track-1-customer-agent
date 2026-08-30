# Track 1: Customer-Facing AI Agent ☕🤖

[![Deployed on Cloud Run](https://img.shields.io/badge/Deployed_on-Google_Cloud_Run-blue?logo=googlecloud)](https://coffee-barista-agent-965225441717.us-central1.run.app/)
[![Challenge](https://img.shields.io/badge/Challenge-AccelerateAIwithCloudRun-orange)](#)

This repository contains the Track 1 submission for the **Google Cloud Gen AI Academy Challenge**. It delivers an interactive, customer-facing AI agent grounded on business data to handle inquiries, dietary preferences, and order recommendations.

## 🌟 Overview
This application serves as an intelligent customer touchpoint (designed as a coffee shop AI barista) that leverages Retrieval-Augmented Generation (RAG) to ground the Gemini model's responses in specific business data, preventing hallucinations and ensuring accurate order recommendations.

## 🚀 Live Demo
**[https://coffee-barista-agent-965225441717.us-central1.run.app/](https://coffee-barista-agent-965225441717.us-central1.run.app/)**
[View Track 1 Demo pdf](track-1-demo.pdf)
*(Note: This application was deployed using temporary Google Cloud trial credits. The live server has automatically spun down to prevent billing, but the complete source code, RAG data, and deployment configurations are available in this repository.)*

## 🚀 Key Architectural Highlights
* **Grounding & RAG:** Real-time retrieval augmentation using structured knowledge bases (`knowledge_base.json`) to prevent hallucinations.
* **Model Engine:** Powered by `gemini-2.5-flash` for low latency and deterministic answers.
* **Serverless Deployment:** Fully containerized and hosted on **Google Cloud Run**.

## 📁 Repository Structure
* `app.py`: Flask web application and Gemini API orchestration.
* `knowledge_base.json`: Grounding dataset for menu items, pricing, and allergen details.
* `Dockerfile`: Container configuration optimized for Cloud Run.
* `requirements.txt`: Python package dependencies.

## 🛠️ Local Development
1. Clone the repository:
   ```bash
   git clone [https://github.com/dharanimahazy/track-1-customer-agent.git](https://github.com/dharanimahazy/track-1-customer-agent.git)
   cd track-1-customer-agent
