import ntptime
import time

class NTPTime:
    def __init__(self):
        self.synced_time = 0
        self.synced_millis = 0
        self.time_base_ms = 0
        self.ntp_server = "pool.ntp.org"  # 使用するNTPサーバーの指定
        self.max_retries = 3  # 最大リトライ回数
        self.retry_delay = 5  # リトライ間の待機時間（秒）

    def sync_time(self):
        attempt = 0
        while attempt < self.max_retries:
            try:
                # 明示的にNTPサーバーを指定
                ntptime.host = self.ntp_server
                ntptime.settime()  # NTPで時刻を設定

                # NTP同期後の基準時刻とミリ秒の設定
                self.synced_time = time.time()
                self.synced_millis = time.ticks_ms()
                self.time_base_ms = self.synced_millis  # 基準のミリ秒を設定

                print("NTP synced")
                return True
            except Exception as e:
                print(f"NTP sync failed: {e}")
                attempt += 1
                if attempt < self.max_retries:
                    print(f"Retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)  # 次のリトライまで待機
                else:
                    print("Max retries reached. NTP sync failed.")
                    return False

    def get_current_time(self):
        # 経過ミリ秒を基準時刻と比較して、現在時刻を取得
        elapsed_ms = time.ticks_diff(time.ticks_ms(), self.time_base_ms)
        current_unix = self.synced_time + elapsed_ms // 1000  # 経過時間を加算
        current_unix_jst = current_unix + 9 * 3600  # JSTに変換（UTC+9）
        return time.localtime(current_unix_jst)  # JSTのローカルタイムを返す
