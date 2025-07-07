#!/usr/bin/env python3
"""
Generate a secure secret key for Flask application
"""
import secrets

if __name__ == "__main__":
    secret_key = secrets.token_hex(16)
    print(f"Generated SECRET_KEY: {secret_key}")
    print("\nCopy this value and use it as your SECRET_KEY environment variable in Render.") 