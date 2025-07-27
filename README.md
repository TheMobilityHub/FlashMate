# FlashMate

펌웨어 파일 추출 GUI 도구

## 🚀 빠른 시작

### 필수 요구사항
- Python 3.8 이상
- Windows 10 이상

### 설치 및 설정
```cmd
# 1. 프로젝트 클론
git clone [repository-url]
cd FlashMate

# 2. 환경 설정 (가상환경 생성 + 패키지 설치)
env_config.bat
```

### 개발
```cmd
# 환경 설정 (가상환경 활성화)
env_config.bat

# 통합 실행 관리자
python run.py
```

## 💡 사용법

`python run.py` 실행 후 다음 옵션 중 선택:

- **[1] Run Program**: 애플리케이션 실행
- **[2] Build**: 실행파일 빌드
- **[3] Clean**: 프로젝트 정리
- **[4] Exit**: 종료

## 📁 프로젝트 구조
```
FlashMate/
├── 📁 src/                          # 소스 코드
├── 📁 docs/                         # 문서
├── 📁 build/                        # 빌드 관련
├── 📁 scripts/                      # 관리 스크립트
├── 📁 sample_data/                  # 샘플 데이터
├── 📁 venv/                         # 가상환경 (자동 생성)
├── 📁 requirements.txt              # Python 의존성
├── 📁 env_config.bat               # 🚀 환경 설정
├── 📁 run.py                       # 🎯 통합 실행 관리자
└── 📁 README.md                    # 프로젝트 설명
```

## 🎯 팁
- `env_config.bat`을 처음 실행하면 가상환경을 생성하고 패키지를 설치합니다
- 두 번째 실행부터는 기존 가상환경을 활성화만 합니다
- 매일 개발 시작할 때 `env_config.bat` → `python run.py` 순서로 실행하세요

## 📋 기능
- ZIP 파일에서 펌웨어 파일 추출
- Car Variant 기반 파일 필터링
- Database 폴더 관리
- 단일 실행파일 빌드
