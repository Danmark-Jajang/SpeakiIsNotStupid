# Speaki - 메뉴바 애니메이션 앱 🧹

macOS 메뉴바에 귀여운 스핔이를 구경하세요

## 기능

- 메뉴바에서 6프레임 애니메이션 재생
- 백그라운드에서 실행 (Dock에 표시 안 됨)
- 이외에 없음

## 요구사항

- macOS
- Python 3.x
- rumps 라이브러리

## 설치 1 (직접 빌드하기)
```bash
# 저장소 클론
git clone https://github.com/Danmark-Jajang/SpeakiIsNotStupid.git
cd SpeakiIsNotStupid

# 필요한 패키지 설치
pip3 install rumps py2app
```

# 개발 모드 실행(테스트용)
```bash
python3 speaki_push.py
```

## 앱 빌드
```bash
# 기존 빌드 삭제
rm -rf build dist

# 앱 빌드
python3 py2appSetup.py py2app

# 빌드된 앱 실행
open dist/speaki_push.app
```

빌드된 앱은 `dist/speaki_push.app`에 생성되며, Applications 폴더로 복사해서 사용할 수 있습니다.
일반 -> 로그인 항목 및 확장 프로그램에서 빌드한 앱을 넣으면 꺼지더라도 귀여운 스핔이를 다시 볼 수 있습니다

## 설치 2 (zip받기)
같이 올라가있는 `speaki_push.zip`파일을 풀어 안에 있는 app파일을 실행시키면 됩니다.
이 파일 또한 일반 -> 로그인 항목 및 확장 프로그램에서 빌드한 앱을 넣으면 꺼지더라도 귀여운 스핔이를 다시 볼 수 있습니다

## 파일 구조
```
SpeakyIsNotStupid/
├── speaki_push.py          # 메인 앱 코드
├── py2appSetup.py          # py2app 설정 파일
├── speaki_1.png ~ 6.png    # 애니메이션 프레임
└── README.md
```

## 사용 방법

1. 앱을 실행하면 메뉴바에 애니메이션이 표시됩니다
2. 종료하려면 메뉴바 아이콘을 클릭하고 "Quit" 선택

## 라이선스

MIT License