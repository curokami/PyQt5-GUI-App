import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout,QFileDialog
from PyQt5.QtCore import Qt

def generate_markdown(cond1, cond2, cond3, question):
    # Markdown生成処理io、
    markdown_text = f"# 生成されたMarkdown\n\n条件1: {cond1}\n条件2: {cond2}\n条件3: {cond3}\n質問: {question}"
    return markdown_text

def save_to_file(text):
    # ファイル保存ダイアログを表示
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_name, _ = QFileDialog.getSaveFileName(None, "ファイル保存", "", "Markdown (*.md);;All Files (*)", options=options)

    if file_name:
        with open(file_name, 'w') as f:
            f.write(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("生成AIプロンプト生成ツール")

    # レイアウト設定
    main_layout = QVBoxLayout()
    form_layout = QFormLayout()
    main_layout.addLayout(form_layout)
    window.setLayout(main_layout)

    # 入力フィールド
    cond1_label = QLabel("条件1:", window)
    cond1_input = QLineEdit(window)
    cond1_input.setFixedWidth(400)
    cond2_label = QLabel("条件2:", window)
    cond2_input = QLineEdit(window)
    cond2_input.setFixedWidth(400)    
    cond3_label = QLabel("条件3:", window)
    cond3_input = QLineEdit(window)
    cond3_input.setFixedWidth(400)
    
    question_label = QLabel("質問:", window)
    question_input = QLineEdit(window)
    question_input.setFixedWidth(400)

    # フォームに要素を追加
    form_layout.addRow(cond1_label, cond1_input)
    form_layout.addRow(cond2_label, cond2_input)
    form_layout.addRow(cond3_label, cond3_input)
    form_layout.addRow(question_label, question_input)

    # 生成ボタン
    generate_button = QPushButton("生成", window)
    main_layout.addWidget(generate_button, alignment=Qt.AlignCenter)

    # ボタンクリック時の処理
    generate_button.clicked.connect(lambda: save_to_file(
        generate_markdown(cond1_input.text(), cond2_input.text(), cond3_input.text(), question_input.text())
    ))

    window.show()
    sys.exit(app.exec_())