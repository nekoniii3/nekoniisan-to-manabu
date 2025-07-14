import os
import tweepy
import datetime
from zoneinfo import ZoneInfo

# X APIKEYを設定（環境変数に設定推奨）
BEARER_TOKEN = "ここに取得したキーをセット"
API_KEY = "ここに取得したキーをセット"
API_SECRET = "ここに取得したキーをセット"
ACCESS_TOKEN = "ここに取得したキーをセット"
ACCESS_SECRET = "ここに取得したキーをセット"

def main():

    # 今日の日付を取得（日本時間）
    dt = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))

    month = dt.month
    day = dt.day

    tweet_text = f"今日は{month}月{day}日です。"

    Client = tweepy.Client(BEARER_TOKEN,API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    # ポスト実行
    Client.create_tweet(text = tweet_text)

    return

if __name__ == "__main__":
      main()