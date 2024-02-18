#!/usr/bin/env python
# coding: utf-8

import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("PORT", "6006")
RIPPLED_ENV = os.environ.get("RIPPLED_ENV", "standalone")
server_url = f"ws://{HOST}:{PORT}"
if RIPPLED_ENV == "testnet" or RIPPLED_ENV == "mainnet":
    server_url = f"wss://{HOST}"
