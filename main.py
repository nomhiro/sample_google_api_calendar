from googleCalendar import GoogleCalendar

def main():
    gc = GoogleCalendar()
    events = gc.read()
    print(f"🚀 events: {events}")
    
    gc.regist(
        summary="新しいイベント",
        location="東京",
        description="これはテストイベントです。",
        start_time="2024-08-16T12:00:00",
        end_time="2024-08-16T18:00:00"
    )

# main関数を実行する
if __name__ == "__main__":
    main()