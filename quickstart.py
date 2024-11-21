import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# APIに要求する権限を指定
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def main():
  """
  ユーザーのカレンダーの現在時刻から10件のイベントの開始日時と名前を表示する。
  """
  creds = None
  # ユーザーのアクセスとリフレッシュトークンを格納するtoken.jsonファイルが存在する場合、token.jsonを使用して認証する。
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # 有効な資格情報がない場合、ユーザーにログインさせます。
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # 次回実行のために資格情報を保存する。※二回目以降の実行では認証がスキップされる。
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # カレンダーAPIを呼び出します。
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z'はUTC時間を示します
    print("次の10件のイベントを取得中")
    events_result = (
      service.events()
      .list(
        calendarId="primary",
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy="startTime",
      )
      .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("次のイベントはありません。")
      return

    # 次の10件のイベントの開始日時と名前を表示します。
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"エラーが発生しました: {error}")


if __name__ == "__main__":
  main()