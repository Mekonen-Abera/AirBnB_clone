#!/usr/bin/python3
"""Initialization script for the models directory"""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
file_storage_instance = FileStorage()

# Reload the data from the storage
file_storage_instance.reload()
