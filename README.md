# Obsidian with Telegram Bot

텔레그램 봇을 통해 Obsidian 데일리 노트에 할 일(Todo)을 빠르고 간편하게 추가할 수 있는 도구입니다.

## ✨ 기능

- **간편한 할 일 추가**: 텔레그램 채팅방에서 명령어를 통해 Obsidian에 할 일을 바로 저장합니다.
- **데일리 노트 자동 연동**: 오늘 날짜의 데일리 노트(`YYYY-MM-DD.md`)를 자동으로 찾거나 생성합니다.
- **섹션 자동 관리**: `## 텔레그램에서 추가된 TODO` 섹션 아래에 할 일을 정리에 추가합니다. 섹션이 없으면 자동으로 생성합니다.

## 🚀 시작하기

### 1. 환경 설정

Python 3.8 이상이 필요합니다.

```bash
# 필요한 라이브러리 설치
pip install python-telegram-bot
```

### 1.1 텔레그램 봇 토큰 발급

1. 텔레그램에서 **[@BotFather](https://t.me/botfather)**를 검색하여 대화를 시작합니다.
2. `/newbot` 명령어를 입력하여 새로운 봇 생성을 시작합니다.
3. 봇의 이름(Name)을 입력합니다. (예: `My Todo Bot`)
4. 봇의 유저네임(Username)을 입력합니다. 이는 반드시 `bot`으로 끝나야 합니다. (예: `mytodo_bot`)
5. 생성이 완료되면 발급되는 **HTTP API Token**을 복사합니다. 이 토큰은 `config.py` 설정에 사용됩니다.

### 2. 설정 파일 구성

`config.example.py` 파일을 `config.py`로 복사하고, 자신의 환경에 맞게 수정합니다.

```python
# config.py
OBSIDIAN_VAULT_PATH = r"C:/Users/YourName/Documents/Obsidian Vault" # Obsidian 보관함 경로
DAILY_NOTE_FOLDER = "01. Daily" # 데일리 노트가 저장되는 폴더 (보관함 루트 기준)
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN" # BotFather로부터 받은 텔레그램 봇 토큰
```

### 3. 실행

```bash
python telegram_bot.py
```

## 💡 사용 방법

텔레그램 봇과의 채팅방에서 아래 명령어 중 하나를 사용하여 메시지를 보냅니다.

형식: `[명령어]: [할일 내용]`

- `ㅌㄷ: 우유 사기`
- `/todo 책 읽기`
- `td: 운동하기`

**예시:**
> 사용자: ㅌㄷ: 내일 회의 준비하기
>
> 봇: ✅ 추가됨: 내일 회의 준비하기

**Obsidian 결과:**
> <img width="519" height="142" alt="image" src="https://github.com/user-attachments/assets/82686177-3597-4fd3-918d-69378789ae9e" />

```markdown
# 2026-01-30

... (기존 내용)

## 텔레그램에서 추가된 TODO
- [ ] 내일 회의 준비하기
```

## ⚠️ 주의사항

- 이 프로그램은 로컬 환경에서 Obsidian 파일 시스템에 직접 접근합니다. 따라서 Obsidian이 설치된 PC에서 봇을 실행해야 합니다.
- `config.py` 파일에는 개인적인 경로와 토큰이 포함되므로 Git에 커밋되지 않도록 주의하세요 (`.gitignore`에 추가되어 있습니다).
