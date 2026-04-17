import pandas as pd
import requests
import os.path

pd.DataFrame.to_jsonl("users.jsonl")

requests.get_async("https://api.example.com/users")

os.path.joinpath("/etc", "myapp", "config.yml")
