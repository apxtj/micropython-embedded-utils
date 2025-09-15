# wifi_icon.py

def draw_wifi_icon(oled, status):
    """
    Wi-Fi接続状態に応じたアイコンを表示します。
    :param oled: OLEDディスプレイオブジェクト
    :param status: 'connected' または 'disconnected'
    """
    oled.fill_rect(0, 0, 20, 12, 0)  # アイコンエリアをクリア
    
    if status == 'connected':
        # Wi-Fi 接続アイコン
        oled.line(3, 11, 7, 7, 1)
        oled.line(7, 7, 13, 7, 1)
        oled.line(13, 7, 17, 11, 1)
        oled.line(5, 11, 7, 9, 1)
        oled.line(7, 9, 13, 9, 1)
        oled.line(13, 9, 15, 11, 1)
        oled.fill_rect(9, 11, 2, 2, 1)
    else:
        # Wi-Fi 切断アイコン（X）
        oled.text("X", 0, 0)

def clear_wifi_icon(oled):
    """
    Wi-Fiアイコンの表示エリアをクリアします。
    :param oled: OLEDディスプレイオブジェクト
    """
    oled.fill_rect(0, 0, 20, 12, 0)  # アイコンエリアをクリア
