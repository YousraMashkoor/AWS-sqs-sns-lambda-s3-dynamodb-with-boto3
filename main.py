from get_secrets import get_db_secrets


secret = get_db_secrets('postgres')
print(secret)