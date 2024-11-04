# Realm_of_Answers-GOT_Q-A_Bot

Realm_of_Answers-GOT_Q-A_Bot is a question-answering bot built to respond to queries about the *Game of Thrones* series using a synopsis PDF as its primary knowledge source. It combines Retrieval-Augmented Generation (RAG) with a fine-tuned BERT model to deliver accurate answers based on the content of the synopsis.

## Overview

- **Project Name**: Realm_of_Answers-GOT_Q-A_Bot
- **Purpose**: Provides answers to user questions about the *Game of Thrones* series by processing information directly from a comprehensive synopsis.
- **Core Technologies**:
  - **Data Retrieval**: Retrieval-Augmented Generation (RAG) to locate relevant information within the GOT synopsis.
  - **Question Answering**: `BertForQuestionAnswering` model (from the Hugging Face model `bert-large-uncased-whole-word-masking-finetuned-squad`) for precise and context-aware answers.

## How It Works

1. **Data Retrieval with RAG**: The bot first scans the *Game of Thrones* synopsis PDF using RAG, focusing on sections most relevant to the user's question.
2. **Answer Generation with BERT**: After locating the pertinent information, the bot uses the `BertForQuestionAnswering` model to generate a clear and accurate answer based on the extracted context.

## Key Components

- **PDF Knowledge Base**: The project utilizes a *Game of Thrones* series synopsis PDF (`GOT_synopsis.pdf`) as the main reference document.
- **FIAAS for PDF Handling**: The File Input Asynchronous Access System (FIAAS) efficiently manages PDF data retrieval.
- **BERT QA Model**: Leveraging Hugging Face's `bert-large-uncased-whole-word-masking-finetuned-squad`, fine-tuned for question answering tasks.

## Example Query

*User Query*: "Who killed the Night King?"

*Answer Generated*: "Arya Stark"

---

This README outlines the basic structure and functions of Realm_of_Answers-GOT_Q-A_Bot, providing an introduction to its purpose and methods used for question answering on *Game of Thrones* content.
