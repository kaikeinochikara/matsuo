import json
import os
import webbrowser
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# 認証情報
creds_path = r"C:\Users\kaike\AppData\Roaming\gcloud\legacy_credentials\kaikei.no.chikara@gmail.com\adc.json"
with open(creds_path) as f:
    creds_data = json.load(f)

creds = Credentials(
    token=None,
    refresh_token=creds_data["refresh_token"],
    token_uri="https://oauth2.googleapis.com/token",
    client_id=creds_data["client_id"],
    client_secret=creds_data["client_secret"],
    scopes=["https://www.googleapis.com/auth/drive"]
)

drive = build("drive", "v3", credentials=creds)

# アップロードするファイル
file_path = r"C:\Users\kaike\Documents\matsuo\ローンチ動画\【新版B】ローンチ動画台本_ゼロから新規_個別相談会誘導.docx"
file_name = "【新版B】ローンチ動画台本_ゼロから新規_個別相談会誘導"

# Googleドキュメントとしてアップロード（変換）
file_metadata = {
    "name": file_name,
    "mimeType": "application/vnd.google-apps.document"
}
media = MediaFileUpload(
    file_path,
    mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)

print("アップロード中...")
file = drive.files().create(
    body=file_metadata,
    media_body=media,
    fields="id,name,webViewLink"
).execute()

file_id = file.get("id")
url = f"https://docs.google.com/document/d/{file_id}/edit"
print(f"作成完了: {file.get('name')}")
print(f"URL: {url}")

webbrowser.open(url)
