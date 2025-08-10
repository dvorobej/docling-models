import os


CONFIG = {
    "Elastic": {
        "host": os.getenv("ELASTIC_HOST", "http://172.30.56.91:9200"),
        "user": os.getenv("ELASTIC_USER", ""),
        "password": os.getenv("ELASTIC_PASSWORD", ""),
        "verify_certs": str(os.getenv("ELASTIC_VERIFY_CERTS", "false")).lower() == "true",
        "timeout_seconds": int(os.getenv("ELASTIC_TIMEOUT_SECONDS", 300)),
        "search": {
            "knn_num_neighbours": int(os.getenv("ELASTIC_SEARCH_KNN_NUM_NEIGHBOURS", 8)),
            "knn_num_candidates": int(os.getenv("ELASTIC_SEARCH_KNN_NUM_CANDIDATES", 100)) 
        },
        "index": {
            "CENSORE_UNCHECKED": int(os.getenv("ELASTIC_INDEX_CENSORE_UNCHECKED", 0)),
            "CENSORE_PASSED": int(os.getenv("ELASTIC_INDEX_CENSORE_PASSED", 1)),
            "CENSORE_FORBIDDEN": int(os.getenv("ELASTIC_INDEX_CENSORE_FORBIDDEN", 2)),
            "doc_index": os.getenv("ELASTIC_INDEX_DOC_INDEX", "llm_doc_index"),
            "dialogue_index": os.getenv("ELASTIC_INDEX_DIALOGUE_INDEX", "llm_dialogue_index"),
        }
    },
    "GigachatAPI": {
        "auth_url": os.getenv("GIGACHAT_AUTH_URL", "http://172.30.71.10:50510/api/v2/oauth"),
        "model_url": os.getenv("GIGACHAT_MODEL_URL", "http://172.30.71.10:50511/api/v1/chat/completions"),
        "embedding_url": os.getenv("GIGACHAT_EMBEDDING_URL", "http://172.30.71.10:50511/api/v1/embedding"),
        "proxy": os.getenv("GIGACHAT_PROXY", "172.30.71.80:3128"),
        "scope": os.getenv("GIGACHAT_SCOPE", "GIGACHAT_API_CORP"),
        "token_update_interval_minutes": int(os.getenv("TOKEN_UPDATE_INTERVAL_MINUTES"), 25),
        "auth_token": os.getenv("GIGACHAT_AUTH_TOKEN", ""),
        "model": {
            "temperature": float(os.getenv("GIGACHAT_MODEL_TEMPERATURE", 0.000001)),
            "max_tokens": int(os.getenv("GIGACHAT_MODEL_MAX_TOKENS", 512)),
            "name": os.getenv("GIGACHAT_MODEL_NAME", "GigaChat-2-Pro")
        }
    },
    "Service": {
        "timeout_seconds": int(os.getenv("SERVICE_TIMEOUT_SECONDS", 120)),
    },
    "Channel": {
        "retail": os.getenv("CHANNEL_RETAIL", ""),
        "corpo": os.getenv("CHANNEL_CORPO", ""),
        "retail_sales": os.getenv("CHANNEL_RETAIL_SALES", ""),
        "legal": os.getenv("CHANNEL_LEGAL", ""),
        "legal_gov": os.getenv("CHANNEL_LEGAL_GOV", "")
    }
}