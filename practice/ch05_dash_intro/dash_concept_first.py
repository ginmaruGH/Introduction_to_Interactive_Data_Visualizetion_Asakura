# HTML 見出し（H1 タグ）に「Hello Dash」を表示する
from dash import Dash, html, dcc

# Dash インスタンスを生成する
app = Dash(__name__)

# コンポーネントを layout 属性に渡す
app.layout = html.H1(children="Hello Dash")

if __name__ == "__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)

