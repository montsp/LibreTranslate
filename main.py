import sys
from libretranslate import main

def start_server():
    # Renderの環境変数からポートとCORS設定を取得
    import os
    port = os.environ.get("PORT", "5000")
    cors_origin = os.environ.get("LT_CORS_ALLOW_ORIGIN", "*")
    load_only = os.environ.get("LT_LOAD_ONLY", "en,ja") # 必要に応じて言語を追加

    # コマンドライン引数を構築
    sys.argv = [
        'libretranslate',
        '--host', '0.0.0.0',
        '--port', port,
        '--cors-allow-origin', cors_origin,
        '--load-only', load_only
    ]

    main()

if __name__ == '__main__':
    start_server()
