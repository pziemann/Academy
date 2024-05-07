import os
import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from google.cloud import storage
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

storage_client = None  # Initialize later after setting up credentials

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logger.info("Strona jest dostępna: %s", url)
        else:
            logger.error("Strona nie jest dostępna: %s", url)
        return response.status_code == 200
    except Exception as e:
        logger.error("Wystąpił błąd podczas sprawdzania dostępności strony: %s", e)
        return False

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        logger.info("Wiadomość e-mail została wysłana.")
    except Exception as e:
        logger.error("Wystąpił błąd podczas wysyłania e-maila: %s", e)

def write_log_to_file(log_message, file_path):
    try:
        with open(file_path, 'a') as log_file:
            log_file.write(log_message + '\n')
    except Exception as e:
        logger.error("Blad zapisywania logow do pliku: %s", e)

def upload_logs_to_bucket(bucket_name, file_path, destination_blob_name):
    global storage_client

    if not storage_client:
        logger.error("Storage client niedostępny")
        return

    try:
        # Get the bucket
        bucket = storage_client.bucket(bucket_name)

        # Upload the file to the bucket
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(file_path)

        logger.info("Logi prawidlowo przeniesione do bucketa.")
    except Exception as e:
        logger.error("Blad podczas przesylania logow do bucketa: %s", e)

def main():
    global storage_client  # Access the global storage_client variable

    # Access the credentials JSON from Kubernetes secret
    credentials_json = os.getenv('CREDENTIALS_JSON')

    # Initialize Google Cloud Storage client with explicit credentials
    try:
        credentials_info = json.loads(credentials_json)
        storage_client = storage.Client.from_service_account_info(credentials_info)
    except Exception as e:
        logger.error("Storage client niedostepny: %s", e)
        return

    #ENVY
    URL_TO_CHECK = os.getenv('URL_TO_CHECK')
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
    SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
    BUCKET_NAME = os.getenv('BUCKET_NAME')
    FILE_NAME = os.getenv('FILE_NAME')
    while True:
        if check_website(URL_TO_CHECK):
            logger.info("Strona dziala prawidlowo")
            write_log_to_file(f"Strona {URL_TO_CHECK} działa prawidłowo", "/var/log/web-checker.log")
        else:
            error_message = f"Blad dostepnosci strony {URL_TO_CHECK}"
            if SENDER_EMAIL and SENDER_PASSWORD and RECIPIENT_EMAIL:
                send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, "Błąd dostępności strony", error_message)
                write_log_to_file(error_message, "/var/log/web-checker.log")
            else:
                logger.error("Nie ustawiono wszystkich wymaganych zmiennych środowiskowych do wysyłania e-maili.")

        # Upload logs to Google Cloud Storage bucket
        upload_logs_to_bucket(BUCKET_NAME, "/var/log/web-checker.log", FILE_NAME)

        time.sleep(60)

if __name__ == '__main__':
    main()
