# GigaChat RAG Service
## File structure

* configs - directory with .env files
* docker - directory with files for creating docker image
* data - directory to store .docx files for RAG
* models - directory with model weights
* modules - directory with business logic
    * utils - helping functions
    * schemas - pydantic schemas for endpoints
    * database - connection to database and its operations
    * prompts - collection of prompts for llm
    * gigachat - GigaChat API functionality

## Start up
1. Clone repository
> git clone http://gitlab.sigma-belpsb.by/datascience/gigachat_rag_service.git
2. Create virtual environment and switch to it
> python -m venv venv
3. Install requirements
> pip install -r docker/requirements.txt
4. Run app
> uvicorn main:app --port 7110 --host 0.0.0.0