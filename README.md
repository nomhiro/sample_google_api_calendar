
# Google Calendar API
https://developers.google.com/calendar/api/quickstart/python?hl=ja

## プロジェクト作成
![alt text](images/image-11.png)

## Google Calendar API有効化
![alt text](images/image-12.png)

![alt text](images/image-13.png)

## OAuth認証同意画面の構成
![alt text](images/image.png)

アプリ登録
![alt text](images/image-3.png)

![alt text](images/image-2.png)

スコープは設定せずに
テストユーザもそのまま
![alt text](images/image-4.png)

作成完
![alt text](images/image-5.png)

## 認証設定
![alt text](images/image-6.png)

![alt text](images/image-7.png)

Jsonをダウンロード
![alt text](images/image-8.png)

ダウンロードした JSON ファイルを credentials.json として保存

## テストユーザ作成
![alt text](images/image-15.png)

![alt text](images/image-16.png)

## 実行
main.pyを実行します。
※googleAPIへのアクセスは、googleCalendar.py内のクラスメソッドで行っています。


![alt text](images/image-9.png)

![alt text](images/image-10.png)

![alt text](images/image-14.png)

続行
![alt text](images/image-17.png)

続行
![alt text](images/image-18.png)

Completeとなるので、VSCodeに戻る
![alt text](images/image-19.png)

GoogleCalendarに登録しているイベント10件が取得できた。
![alt text](images/image-20.png)