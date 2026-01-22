name: Build EXE

on:
  workflow_dispatch: # 讓你手動點擊按鈕才開始打包

jobs:
  build:
    runs-on: windows-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4  # 已更新至 v4

      - name: Set up Python
        uses: actions/setup-python@v5 # 已更新至 v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install requests websocket-client pynacl pyinstaller

      - name: Build EXE with PyInstaller
        run: |
          pyinstaller --onefile --console --name StandX_Bot main.py

      - name: Upload Artifact
        uses: actions/upload-artifact@v4 # 已更新至 v4 (關鍵點)
        with:
          name: ProcyonsBot-EXE
          path: dist/StandX_Bot.exe
