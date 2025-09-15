import ssd1306

class OLEDDisplay:
    def __init__(self, i2c, width=128, height=64):
        self.oled = ssd1306.SSD1306_I2C(width, height, i2c)

    # 画面を塗りつぶすメソッド
    def fill(self, color):
        self.oled.fill(color)

    # 画面をクリアするメソッド
    def clear(self):
        self.oled.fill(0)  # 0でクリア
        self.oled.show()

    # text() メソッドをラップ
    def text(self, text, x, y):
        self.oled.text(text, x, y)

    # 画面に描画を反映
    def show(self):
        self.oled.show()

    # 長方形を描画
    def draw_rect(self, x, y, w, h, color):
        self.oled.fill_rect(x, y, w, h, color)

    # line メソッドを追加
    def line(self, x1, y1, x2, y2, color):
        self.oled.line(x1, y1, x2, y2, color)
    
    # fill_rect メソッドを追加
    def fill_rect(self, x, y, w, h, color):
        self.oled.fill_rect(x, y, w, h, color)
