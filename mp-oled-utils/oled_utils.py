def draw_wrapped_text(oled, text, x, y, max_width=96, line_height=10, font_width=6):
    """
    テキストを指定された最大幅で折り返してOLEDディスプレイに表示します。
    :param oled: OLEDディスプレイオブジェクト
    :param text: 表示するテキスト
    :param x: テキストの開始位置（x座標）
    :param y: テキストの開始位置（y座標）
    :param max_width: 1行あたりの最大幅（デフォルトは96）
    :param line_height: 各行の高さ（デフォルトは10）
    :param font_width: 1文字あたりの幅（デフォルトは6）
    """
    oled.fill(0)  # 画面をリセットして、前回の描画を消去
    
    words = text.split(' ')  # 単語ごとに分割
    current_line = ""  # 現在の行
    current_width = 0  # 現在の行の幅

    for word in words:
        word_width = len(word) * font_width  # 単語の幅を計算

        # 単語を追加しても幅を超えない場合
        if current_width + word_width + font_width <= max_width:  # スペースを含む幅計算
            current_line += word + " "
            current_width += word_width + font_width
        else:
            # 幅を超えた場合、現在の行を描画
            if current_line:
                oled.text(current_line.strip(), x, y)  # 現在の行を描画
                y += line_height  # 次の行に移動
            # 新しい行を開始
            current_line = word + " "
            current_width = word_width + font_width

    # 最後の行が残っていれば描画
    if current_line:
        oled.text(current_line.strip(), x, y)

    oled.show()  # 描画完了
