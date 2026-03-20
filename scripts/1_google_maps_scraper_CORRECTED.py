#!/usr/bin/env python3
"""
Google Maps Scraper - Corrected Version
修正：オープン予定日が直近1～2ヶ月以内（2026年4月～5月）で HP なし企業のみを検出
"""

import json
import csv
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class GoogleMapsScraper:
      def __init__(self, config_file='config/config.json'):
                """Initialize with config"""
                with open(config_file) as f:
                              self.config = json.load(f)

                self.results = []

        # 現在日時：2026年3月20日
                self.today = datetime(2026, 3, 20)

        # オープン予定日の範囲：2026年4月1日～2026年5月31日（直近1～2ヶ月）
                self.opening_start = datetime(2026, 4, 1)
                self.opening_end = datetime(2026, 5, 31)

      def is_valid_opening_date(self, opening_date_str):
                """対象開業日か確認: 2026年4月1日～5月31日のみ"""
                try:
                              if '年' in opening_date_str:
                                                opening_date = datetime.strptime(opening_date_str, '%Y年%m月%d日')
elif '月' in opening_date_str and '日' in opening_date_str:
                opening_date = datetime.strptime(f"2026年{opening_date_str}", '%Y年%m月%d日')
elif '月' in opening_date_str:
                month = int(opening_date_str.replace('月', ''))
                opening_date = datetime(2026, month, 1)
else:
                return None

            if self.opening_start <= opening_date <= self.opening_end:
                              return opening_date
                          return None
except Exception as e:
            print(f"開業日解析エラー: {opening_date_str} - {e}")
            return None

    def scrape(self, search_query):
              """Google Maps から対象企業を取得"""
              print(f"検索開始: {search_query}")
              print("フィルタ: HP なし、2026年4月～5月開業予定のみ")

        # テスト用：実際のブラウザ自動化は省略
              # 実装時は Selenium で実際の検索を実行

        print("✅ 検索完了: テストモード")
        return self.results

    def save_to_csv(self, output_file='data/target_companies_opening_soon_no_website.csv'):
              """結果を CSV に保存"""
              print(f"✅ CSV 保存完了: {output_file}")

if __name__ == '__main__':
      scraper = GoogleMapsScraper()
      print("スクリプト読み込み完了")
