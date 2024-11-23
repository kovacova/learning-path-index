# import os

# from chromadb.config import Settings

# # Define the folder for storing database
# PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY', 'vector_db')

# # Define the Chroma settings
# CHROMA_SETTINGS = Settings(
#     chroma_db_impl='duckdb+parquet',
#     persist_directory=PERSIST_DIRECTORY,
#     anonymized_telemetry=False,
# )

import os
from chromadb.config import Settings

# Define the folder for storing the database
PERSIST_DIRECTORY = os.environ.get("PERSIST_DIRECTORY", "vector_db")

# Define the Chroma settings with a supported configuration
CHROMA_SETTINGS = Settings(
    chroma_db_impl="duckdb+parquet",  # Local storage implementation
    persist_directory=PERSIST_DIRECTORY,  # Where the database will be stored
    anonymized_telemetry=False,  # Disable telemetry
)