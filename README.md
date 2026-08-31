# Track 1: Customer-Facing AI Agent ☕🤖

[![Deployed on Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?logo=render&logoColor=white)](https://track-1-customer-agent.onrender.com/)
[![Challenge](https://img.shields.io/badge/Challenge-AccelerateAIwithCloudRun-orange)](#)

This repository contains the Track 1 submission for the **Google Cloud Gen AI Academy Challenge**. It delivers an interactive, customer-facing AI agent grounded on business data to handle inquiries, dietary preferences, and order recommendations.

## 🌟 Overview
This application serves as an intelligent customer touchpoint (designed as a coffee shop AI barista) that leverages Retrieval-Augmented Generation (RAG) to ground the Gemini model's responses in specific business data, preventing hallucinations and ensuring accurate order recommendations.

## 🚀 Live Demo
**[https://track-1-customer-agent.onrender.com/](https://track-1-customer-agent.onrender.com/)**

[View Track 1 Demo pdf](track-1-demo.pdf)

*(Note: Hosted on a free Render instance. Please allow ~30–50 seconds for the initial load if the server is waking up from sleep mode.)*

## 🚀 Key Architectural Highlights
* **Grounding & RAG:** Real-time retrieval augmentation using structured knowledge bases (`knowledge_base.json`) to prevent hallucinations.
* **Model Engine:** Powered by `gemini-3.6-flash` for low latency and deterministic answers.
* **Serverless Deployment:** Fully containerized and hosted on **Render** (originally built for Google Cloud Run).

## 📁 Repository Structure
* `app.py`: Flask web application and Gemini API orchestration.
* `knowledge_base.json`: Grounding dataset for menu items, pricing, and allergen details.
* `Dockerfile`: Container configuration optimized for cloud deployment.
* `requirements.txt`: Python package dependencies.

## 🛠️ Local Development
1. Clone the repository:
   ```bash
   git clone [https://github.com/dharanimahazy/track-1-customer-agent.git](https://github.com/dharanimahazy/track-1-customer-agent.git)
   cd track-1-customer-agent
