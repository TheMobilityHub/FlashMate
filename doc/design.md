# 🏗️ FlashMate Design Document

## 📋 설계 단계 진행 체크리스트

### 🔍 1. 아키텍처 설계 (Architecture Design)
- [x] **1.1 시스템 아키텍처 정의**
  - 전체 시스템 구조 (GUI + Core Logic)
  - 레이어 분리 (Presentation, Business, Data)
  - 모듈 간 의존성 정의

#### 1.1.1 전체 시스템 구조

```
┌─────────────────────────────────────────────────────────────┐
│                    FlashMate Application                    │
├─────────────────────────────────────────────────────────────┤
│  Presentation Layer (GUI)                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   File Input    │  │  Car Variant    │  │   Action     │ │
│  │   (Drag & Drop) │  │   Input Field   │  │   Buttons    │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │              Log & Status Display Area                  │ │
│  └─────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  Business Logic Layer (Core)                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │  ZIP Processor  │  │  File Filter    │  │  Folder      │ │
│  │  & Validator    │  │  (Car Variant)  │  │  Manager     │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  Data Layer (File System)                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │  Input ZIP      │  │  Database       │  │  Temp        │ │
│  │  Files          │  │  Folder         │  │  Directory   │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

#### 1.1.2 레이어 분리 (Layered Architecture)

| Layer | Components | Responsibilities | Dependencies |
|-------|------------|------------------|--------------|
| **Presentation** | MainWindow, FileInputWidget, LogWidget | UI rendering, user interaction, event handling | Business Logic Layer |
| **Business Logic** | ZipProcessor, FileFilter, FolderManager | Core processing logic, validation, business rules | Data Layer |
| **Data** | FileSystem, ConfigManager | File I/O, configuration management | None (External) |

#### 1.1.3 모듈 간 의존성 정의

```
MainWindow
├── FileInputWidget (ZIP file selection)
├── VariantInputWidget (Car Variant input)
├── ActionButtons (Start, New Task, Open Folder)
├── LogWidget (Status display)
└── CoreController (Business logic coordinator)

CoreController
├── ZipProcessor (ZIP file handling)
├── FileFilter (Firmware file filtering)
├── FolderManager (Output folder management)
└── LogManager (Logging and status)

ZipProcessor
├── FileValidator (ZIP validation)
├── ZipExtractor (File extraction)
└── TempFileManager (Temporary file handling)

FileFilter
├── VariantRuleEngine (Car Variant based rules)
├── FileTypeDetector (Firmware file detection)
└── FilterConfig (Filtering configuration)

FolderManager
├── DuplicateDetector (Folder duplication check)
├── PathBuilder (Output path construction)
└── SafeOverwriter (Safe folder overwrite)
```

#### 1.1.4 데이터 흐름 (Data Flow)

1. **Input Phase**: User selects ZIP files → FileInputWidget → ZipProcessor
2. **Processing Phase**: ZipProcessor → FileFilter → FolderManager
3. **Output Phase**: FolderManager → FileSystem → LogWidget
4. **Feedback Phase**: All components → LogManager → LogWidget

#### 1.1.5 에러 처리 아키텍처

- **Validation Errors**: Presentation Layer에서 즉시 처리
- **Processing Errors**: Business Logic Layer에서 로깅 후 Presentation Layer로 전달
- **System Errors**: Data Layer에서 발생 시 Business Logic Layer로 에스컬레이션

#### 1.2.1 Python 버전 및 필수 라이브러리

| Category | Library | Version | Purpose | Alternative |
|----------|---------|---------|---------|-------------|
| **GUI Framework** | PySide6 | 6.5+ | Main GUI framework | PyQt6, tkinter |
| **Core Python** | Python | 3.9+ | Base language | - |
| **File Processing** | zipfile | Built-in | ZIP file handling | - |
| **File Processing** | pathlib | Built-in | Path operations | os.path |
| **File Processing** | shutil | Built-in | File operations | - |
| **Configuration** | configparser | Built-in | Settings management | json, yaml |
| **Logging** | logging | Built-in | Application logging | - |
| **Threading** | threading | Built-in | Background processing | asyncio |
| **Testing** | pytest | 7.0+ | Unit testing | unittest |
| **Packaging** | PyInstaller | 5.0+ | Executable creation | cx_Freeze |

#### 1.2.2 PySide6 위젯 구조

```
QApplication
└── MainWindow (QMainWindow)
    ├── CentralWidget (QWidget)
    │   ├── FileInputSection (QGroupBox)
    │   │   ├── DragDropArea (QLabel with custom styling)
    │   │   └── FileListWidget (QListWidget)
    │   ├── VariantInputSection (QGroupBox)
    │   │   ├── VariantLabel (QLabel)
    │   │   └── VariantLineEdit (QLineEdit)
    │   ├── ActionSection (QHBoxLayout)
    │   │   ├── StartButton (QPushButton)
    │   │   ├── NewTaskButton (QPushButton)
    │   │   └── OpenFolderButton (QPushButton)
    │   └── LogSection (QGroupBox)
    │       └── LogTextEdit (QTextEdit with custom formatting)
    └── StatusBar (QStatusBar)
```

#### 1.2.3 파일 처리 라이브러리 상세

| Library | Module | Usage | Error Handling |
|---------|--------|-------|----------------|
| **zipfile** | `ZipFile` | ZIP 파일 읽기/검증 | `BadZipFile`, `LargeZipFile` |
| **zipfile** | `ZipInfo` | 파일 메타데이터 | - |
| **pathlib** | `Path` | 경로 조작 및 검증 | `PathError` |
| **shutil** | `copy2` | 파일 복사 (메타데이터 포함) | `OSError` |
| **shutil** | `rmtree` | 디렉토리 삭제 | `OSError` |
| **tempfile** | `TemporaryDirectory` | 임시 디렉토리 생성 | `OSError` |
| **os** | `makedirs` | 디렉토리 생성 | `OSError` |

#### 1.2.4 개발 도구 및 환경

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Git** | Version control | `.gitignore` for Python/PySide6 |
| **VSCode** | IDE | Python, PySide6 extensions |
| **Black** | Code formatting | 88 character line length |
| **Flake8** | Linting | PEP 8 compliance |
| **MyPy** | Type checking | Strict mode for core modules |
| **Docker** | Environment isolation | Python 3.9+ container |

#### 1.2.5 의존성 관리

**requirements.txt**:
```
PySide6>=6.5.0
pytest>=7.0.0
PyInstaller>=5.0.0
```

**pyproject.toml** (Optional):
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py39']

[tool.mypy]
python_version = "3.9"
strict = true
```

#### 1.2.6 성능 최적화 라이브러리

| Library | Purpose | When to Use |
|---------|---------|-------------|
| **concurrent.futures** | ThreadPoolExecutor | ZIP 파일 병렬 처리 |
| **mmap** | Memory mapping | 대용량 파일 처리 |
| **lzma** | LZMA compression | 압축 파일 최적화 |

#### 1.2.7 성능 목표 (Performance Targets)

| File Size | Target Processing Time | Optimization Strategy |
|-----------|----------------------|---------------------|
| **< 100MB** | < 2 seconds | Basic processing |
| **100MB - 500MB** | < 5 seconds | ThreadPoolExecutor |
| **500MB - 1GB** | < 10 seconds | Memory mapping |
| **> 1GB** | < 20 seconds | Chunked processing |

**성능 측정 기준**:
- ZIP 파일 압축 해제: 50% of total time
- 파일 필터링: 20% of total time  
- 폴더 생성 및 복사: 30% of total time

#### 1.3.1 프로젝트 디렉토리 구조

```
FlashMate/
├── 📁 src/                          # 소스 코드
│   ├── 📁 core/                     # 핵심 비즈니스 로직
│   │   ├── __init__.py
│   │   ├── zip_processor.py         # ZIP 파일 처리
│   │   ├── file_filter.py           # 펌웨어 파일 필터링
│   │   ├── folder_manager.py        # 폴더 관리
│   │   └── log_manager.py           # 로깅 관리
│   ├── 📁 gui/                      # GUI 관련 모듈
│   │   ├── __init__.py
│   │   ├── main_window.py           # 메인 윈도우
│   │   ├── widgets/                 # 커스텀 위젯
│   │   │   ├── __init__.py
│   │   │   ├── file_input_widget.py # 파일 입력 위젯
│   │   │   ├── variant_input_widget.py # Car Variant 입력
│   │   │   ├── log_widget.py        # 로그 표시 위젯
│   │   │   └── action_buttons.py    # 액션 버튼들
│   │   └── styles/                  # 스타일시트
│   │       ├── __init__.py
│   │       └── main_style.qss       # Qt 스타일시트
│   ├── 📁 utils/                    # 유틸리티 모듈
│   │   ├── __init__.py
│   │   ├── config_manager.py        # 설정 관리
│   │   ├── file_utils.py            # 파일 유틸리티
│   │   ├── validators.py            # 검증 로직
│   │   └── database_manager.py      # Database 폴더 관리
│   └── main.py                      # 애플리케이션 진입점
├── 📁 tests/                        # 테스트 코드
│   ├── __init__.py
│   ├── 📁 unit/                     # 단위 테스트
│   │   ├── test_zip_processor.py
│   │   ├── test_file_filter.py
│   │   └── test_folder_manager.py
│   ├── 📁 integration/              # 통합 테스트
│   │   ├── test_workflow.py
│   │   └── test_error_scenarios.py
│   └── 📁 fixtures/                 # 테스트 데이터
│       ├── sample_zips/
│       └── expected_outputs/
├── 📁 resources/                    # 리소스 파일
│   ├── 📁 icons/                    # 아이콘 파일
│   │   ├── app_icon.ico
│   │   ├── folder_icon.png
│   │   └── file_icon.png
│   ├── 📁 config/                   # 설정 파일
│   │   ├── default_config.ini
│   │   └── logging_config.ini
│   └── 📁 docs/                     # 문서
│       ├── user_manual.md
│       └── api_documentation.md
├── 📁 build/                        # 빌드 출력
│   ├── 📁 dist/                     # 배포 파일
│   └── 📁 temp/                     # 임시 빌드 파일
├── 📁 Database/                     # 사용자 생성 출력물 저장소
│   ├── 📄 database_index.json       # 폴더 인덱스 및 메타데이터
│   ├── 📁 CarVariant_A/             # Car Variant별 분류 폴더
│   │   └── 📁 2024-01-15_14-30-25/  # 생성된 폴더 (예시)
│   └── 📁 CarVariant_B/             # 다른 Car Variant
├── 📁 scripts/                      # 빌드/배포 스크립트
│   ├── build.py                     # PyInstaller 빌드 스크립트
│   ├── install.py                   # 설치 스크립트
│   └── package.py                   # 패키징 스크립트
├── 📄 requirements.txt              # Python 의존성
├── 📄 pyproject.toml               # 프로젝트 설정
├── 📄 setup.py                     # 설치 설정
├── 📄 .gitignore                   # Git 무시 파일
├── 📄 README.md                    # 프로젝트 설명
└── 📄 LICENSE                      # 라이선스
```

#### 1.3.2 소스 코드 모듈 분리

| Module | Path | Responsibility | Dependencies |
|--------|------|----------------|--------------|
| **Main Application** | `src/main.py` | 애플리케이션 진입점, QApplication 설정 | gui.main_window |
| **Core Controller** | `src/core/__init__.py` | 비즈니스 로직 조정자 | All core modules |
| **ZIP Processor** | `src/core/zip_processor.py` | ZIP 파일 검증 및 처리 | utils.validators |
| **File Filter** | `src/core/file_filter.py` | Car Variant 기반 필터링 | utils.config_manager |
| **Folder Manager** | `src/core/folder_manager.py` | 출력 폴더 관리, 중복 감지, 덮어쓰기 | utils.file_utils, utils.config_manager |
| **Log Manager** | `src/core/log_manager.py` | 로깅 및 상태 관리 | utils.config_manager |
| **Main Window** | `src/gui/main_window.py` | 메인 GUI 윈도우 | All widgets |
| **File Input Widget** | `src/gui/widgets/file_input_widget.py` | 파일 선택 UI | core.zip_processor |
| **Variant Input Widget** | `src/gui/widgets/variant_input_widget.py` | Car Variant 입력 UI | utils.validators |
| **Log Widget** | `src/gui/widgets/log_widget.py` | 로그 표시 UI | core.log_manager |
| **Action Buttons** | `src/gui/widgets/action_buttons.py` | 액션 버튼 UI | core.folder_manager |
| **Config Manager** | `src/utils/config_manager.py` | 설정 파일 관리 | None |
| **File Utils** | `src/utils/file_utils.py` | 파일 시스템 유틸리티 | None |
| **Validators** | `src/utils/validators.py` | 입력 검증 로직 | None |
| **Database Manager** | `src/utils/database_manager.py` | Database 폴더 관리, 생성 기록 | None |

#### 1.3.3 리소스 파일 관리

| Resource Type | Location | Purpose | Format |
|---------------|----------|---------|--------|
| **Icons** | `resources/icons/` | 애플리케이션 아이콘, UI 아이콘 | .ico, .png |
| **Configuration** | `resources/config/` | 기본 설정 파일 | .ini |
| **Documentation** | `resources/docs/` | 사용자 매뉴얼, API 문서 | .md |
| **Styles** | `src/gui/styles/` | Qt 스타일시트 | .qss |
| **Test Data** | `tests/fixtures/` | 테스트용 샘플 파일 | .zip, .hex, .s19 |

#### 1.3.4 모듈 임포트 구조

```python
# src/main.py
from gui.main_window import MainWindow
from core.log_manager import LogManager

# src/gui/main_window.py
from gui.widgets.file_input_widget import FileInputWidget
from gui.widgets.variant_input_widget import VariantInputWidget
from gui.widgets.log_widget import LogWidget
from gui.widgets.action_buttons import ActionButtons
from core.zip_processor import ZipProcessor
from core.file_filter import FileFilter
from core.folder_manager import FolderManager

# src/core/zip_processor.py
from utils.validators import validate_zip_file
from utils.file_utils import create_temp_directory

# src/gui/widgets/file_input_widget.py
from PySide6.QtWidgets import QWidget, QLabel, QListWidget
from PySide6.QtCore import Signal
from core.zip_processor import ZipProcessor
```

#### 1.3.5 빌드 및 배포 구조

```
build/
├── dist/                           # 최종 배포 파일
│   ├── FlashMate.exe              # Windows 실행 파일
│   ├── FlashMate/                 # 폴더 구조 (PyInstaller)
│   │   ├── FlashMate.exe
│   │   ├── resources/             # 포함된 리소스
│   │   ├── lib/                   # Python 라이브러리
│   │   └── Database/              # 사용자 출력물 저장소 (초기 빈 폴더)
│   │       └── 📄 database_index.json  # 초기 인덱스 파일
│   └── FlashMate_Setup.exe        # 인스톨러
└── temp/                          # 임시 빌드 파일
    ├── build/                     # PyInstaller 빌드 파일
    └── spec/                      # PyInstaller 스펙 파일
```


### 🎨 2. UI/UX 설계 (User Interface Design)
- [x] **2.1 와이어프레임 작성**
  - 메인 화면 레이아웃
  - 파일 입력 영역 (드래그 앤 드롭)
  - Car Variant 입력 필드
  - 버튼 배치 및 액션 영역

#### 2.1.1 메인 화면 레이아웃 (Main Window Layout - Z Pattern)

```
┌──────────────────────────────────────────────────────────────┐
│  [FlashMate Logo/Title]         [Status/Settings]           │
├──────────────────────────────────────────────────────────────┤
│  [File Input / Drag & Drop]   [Car Variant Input]           │
│                                                              │
│  [Selected Files]             [Action Buttons]               │
│                                                              │
│  [Log / Status Area]    [Output Path / Result]               │
└──────────────────────────────────────────────────────────────┘
```

- **좌상단**: 파일 입력(Drag & Drop)
- **우상단**: Car Variant 입력
- **중앙**: 선택된 파일, 액션 버튼(처리, 리셋, 폴더 열기)
- **하단**: 로그/상태, 결과 경로(좌→우로 시선 이동)

**Z-패턴 흐름**
1. 파일 입력 → 2. Car Variant 입력 → 3. 액션 버튼 → 4. 결과/로그

#### 2.1.1.1 주요 컴포넌트 배치

| 위치      | 컴포넌트                | 설명                                  |
|-----------|------------------------|---------------------------------------|
| 좌상단    | File Input             | Drag & Drop, 파일 선택, 실시간 검증   |
| 우상단    | Car Variant Input      | Car Variant 입력, 실시간 검증         |
| 중앙좌    | Selected Files         | 선택된 파일 목록, 용량, 상태          |
| 중앙우    | Action Buttons         | Start, New Task, Open Output Folder   |
| 하단좌    | Log / Status Area      | 실시간 로그, 상태 메시지, 색상코딩    |
| 하단우    | Output Path / Result   | 결과 폴더 경로, 추출 파일 수, 열기    |

#### 2.1.1.2 반응형 레이아웃 전략
- **1000px 이상**: Z-패턴 가로 분할 레이아웃
- **800~1000px**: F-패턴(상단→중앙→하단) 레이아웃
- **800px 이하**: 세로 스택 레이아웃
- 로그 영역은 항상 하단, 스크롤 가능

#### 2.1.1.3 Z-패턴 와이어프레임 예시 (텍스트)

```
┌──────────────────────────────────────────────────────────────┐
│ FlashMate           Status: Ready | Files: 2 | Variant: A   │
├──────────────────────────────────────────────────────────────┤
│ [Drag & Drop ZIP]   [Car Variant: ________] [Validate]      │
│ [Selected Files]    [Start] [New Task] [Open Folder]        │
│ [Log/Status]        [Output Path: Database/Variant/Time]    │
└──────────────────────────────────────────────────────────────┘
```

- [x] **2.2 사용자 플로우 정의**
  - 단계별 사용자 여정
  - 에러 상태 UI 처리
  - 성공/실패 피드백 디자인

#### 2.2.1 전체 사용자 플로우 (Z-패턴 기반)

1. **앱 실행 및 초기화**
   - 상태: Ready
   - 로그: "Application started"

2. **ZIP 파일 입력**
   - 사용자는 좌상단 Drag & Drop 영역에 2개의 ZIP 파일을 드롭하거나 [Browse Files] 클릭
   - 실시간 파일 검증 (ZIP, 개수, 손상 여부)
   - 에러 발생 시: "Please select exactly 2 valid ZIP files" (빨간색 메시지)
   - 성공 시: "2 ZIP files selected" (파란색 메시지)

3. **Car Variant 입력**
   - 우상단 입력 필드에 Car Variant 입력
   - [Validate] 클릭 또는 실시간 자동 검증
   - 에러 발생 시: "Car Variant is required" (빨간색 메시지)
   - 성공 시: "Car Variant validated: {variant}" (파란색 메시지)
   - 툴팁: "Will filter files containing '{variant}'"

4. **중복 폴더 감지**
   - [Start] 클릭 시, Database 폴더에서 중복 여부 자동 검사
   - 중복 시: "Duplicate folder already exists: {path}" (오렌지색 메시지)
   - 사용자는 [Start]를 한 번 더 눌러 덮어쓰기 진행 가능

5. **펌웨어 추출 및 처리**
   - 진행률 표시: "Extracting files... (45%)"
   - 성공 시: "Processing completed successfully" (초록색 메시지)
   - 실패 시: "Failed to extract files: {error}" (빨간색 메시지)

6. **결과 확인 및 폴더 열기**
   - 우하단 Output Path에 결과 경로 표시
   - [Open Output Folder] 클릭 시 시스템 파일 탐색기 실행
   - 로그: "Output folder opened: {path}"

7. **새 작업(New Task) 시작**
   - [New Task] 클릭 시 모든 입력/상태 초기화
   - 로그: "Application reset for new task"

#### 2.2.2 예외 및 에러 상태 처리
- 파일 개수/형식 오류: "Please select exactly 2 valid ZIP files"
- Car Variant 미입력: "Car Variant is required"
- 중복 폴더: "Duplicate folder already exists: {path}"
- 폴더 생성 실패: "Failed to create output folder: {error}"
- ZIP 파일 손상: "Corrupted ZIP file detected: {filename}"
- 처리 중단: "Processing aborted by user"

#### 2.2.3 성공/실패 피드백 디자인
- **INFO**: 파란색, 일반 상태 메시지
- **WARN**: 오렌지색, 중복/주의 메시지
- **ERROR**: 빨간색, 치명적 오류
- **SUCCESS**: 초록색, 완료 메시지
- 모든 메시지는 로그 영역에 타임스탬프와 함께 표시

#### 2.2.4 사용자 플로우 다이어그램 (텍스트)

```
[Start]
  ↓
[Select ZIP files] → (Invalid) → [Error: Please select 2 ZIP files]
  ↓
[Input Car Variant] → (Invalid) → [Error: Car Variant is required]
  ↓
[Check Duplicate] → (Duplicate) → [Warn: Duplicate folder exists]
  ↓
[Start Processing] → (Error) → [Error: ...]
  ↓
[Processing] → [Success: Files extracted]
  ↓
[Open Output Folder] / [New Task]
```

- [ ] **2.3 UI 컴포넌트 설계**
  - 로그/상태 표시 영역
  - 진행률 표시 (필요시)
  - 폴더 경로 표시 영역

---

### 🔧 3. 데이터 구조 설계 (Data Structure Design)
- [x] **3.1 폴더 구조 정의**
  - Database 폴더 내부 구조
  - 출력 폴더 명명 규칙
  - 중복 감지 로직

#### 3.1.1 Database 폴더 내부 구조

```
Database/
├── 📁 CarVariant_A/                 # Car Variant별 분류
│   ├── 📁 2024-01-15_14-30-25/      # 생성된 폴더 (타임스탬프)
│   │   ├── 📄 folder_info.json      # 폴더 생성 정보
│   │   ├── 📁 firmware_files/       # 추출된 펌웨어 파일
│   │   │   ├── 📄 firmware.hex
│   │   │   └── 📄 firmware.s19
│   │   └── 📄 extraction_log.txt    # 추출 로그
│   └── 📁 2024-01-16_09-15-42/      # 동일 Variant, 다른 시간
│       ├── 📄 folder_info.json
│       ├── 📁 firmware_files/
│       └── 📄 extraction_log.txt
├── 📁 CarVariant_B/
│   └── 📁 2024-01-15_16-45-10/
└── 📄 database_index.json           # 전체 폴더 인덱스
```

#### 3.1.2 출력 폴더 명명 규칙

| Component | Format | Example | Purpose |
|-----------|--------|---------|---------|
| **Car Variant** | `{variant_name}` | `CarVariant_A` | Car Variant 구분 |
| **Timestamp** | `YYYY-MM-DD_HH-MM-SS` | `2024-01-15_14-30-25` | 생성 시간 구분 |
| **Full Path** | `Database/{variant}/{timestamp}` | `Database/CarVariant_A/2024-01-15_14-30-25` | 고유 식별자 |

**폴더명 생성 로직**:
```python
def generate_folder_name(car_variant: str, zip_files: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{car_variant}_{timestamp}"

def get_full_path(base_path: str, folder_name: str) -> str:
    return os.path.join(base_path, "Database", folder_name)
```

#### 3.1.3 중복 감지 로직

**1. 중복 감지 기준**:
- **정확한 중복**: Car Variant + ZIP 파일명 조합이 동일
- **부분 중복**: Car Variant만 동일 (경고 표시)

**2. 중복 감지 프로세스**:
```python
class DuplicateDetector:
    def check_duplicate(self, car_variant: str, zip_files: List[str]) -> DuplicateResult:
        # 1. Database 폴더 스캔
        existing_folders = self.scan_database_folders()
        
        # 2. 정확한 중복 확인
        exact_match = self.find_exact_match(car_variant, zip_files, existing_folders)
        if exact_match:
            return DuplicateResult.EXACT_MATCH(exact_match)
        
        # 3. 부분 중복 확인 (같은 Car Variant)
        partial_matches = self.find_partial_matches(car_variant, existing_folders)
        if partial_matches:
            return DuplicateResult.PARTIAL_MATCH(partial_matches)
        
        return DuplicateResult.NO_MATCH()

class DuplicateResult:
    def __init__(self, type: str, matches: List[str] = None):
        self.type = type  # "EXACT", "PARTIAL", "NONE"
        self.matches = matches or []
        self.message = self.generate_message()
    
    def generate_message(self) -> str:
        if self.type == "EXACT":
            return f"Duplicate folder already exists: {self.matches[0]}"
        elif self.type == "PARTIAL":
            return f"Found {len(self.matches)} folders with same Car Variant"
        return "No duplicates found"
```

**3. Database 인덱스 구조**:
```json
{
  "version": "1.0",
  "last_updated": "2024-01-15T14:30:25",
  "folders": [
    {
      "id": "CarVariant_A_2024-01-15_14-30-25",
      "car_variant": "CarVariant_A",
      "zip_files": ["build_v1.zip", "build_v2.zip"],
      "created_at": "2024-01-15T14:30:25",
      "path": "Database/CarVariant_A/2024-01-15_14-30-25",
      "file_count": 5,
      "total_size": "2.5MB"
    }
  ],
  "statistics": {
    "total_folders": 15,
    "total_size": "45.2MB",
    "variants": ["CarVariant_A", "CarVariant_B", "CarVariant_C"]
  }
}
```

**4. 중복 처리 플로우**:
```
User Input → Duplicate Detection → Result Display → User Choice → Process Execution
     ↓              ↓                ↓              ↓              ↓
  Car Variant   Database Scan    Warning Message   Overwrite     Folder Creation
  + ZIP Files                   + Path Display     Confirmation  or Overwrite
```

- [ ] **3.2 설정 파일 구조**
  - 애플리케이션 설정 관리
  - 기본 경로 설정
  - 사용자 환경 설정

- [ ] **3.3 로그 데이터 구조**
  - 로그 메시지 형식
  - 타임스탬프 및 레벨 정의
  - 에러 코드 체계

---

### ⚙️ 4. 핵심 로직 설계 (Core Logic Design)
- [ ] **4.1 ZIP 파일 처리 로직**
  - 파일 검증 프로세스
  - 압축 해제 및 임시 저장
  - 펌웨어 파일 필터링 로직

- [x] **4.2 Car Variant 기반 필터링**
  - 필터링 규칙 정의
  - 지원 파일 형식 목록
  - 확장 가능한 필터링 구조

#### 4.2.1 지원 파일 형식 목록

| File Extension | Description | Priority |
|----------------|-------------|----------|
| **.hex** | Intel HEX format firmware files | High |
| **.s19** | Motorola S-record format files | High |
| **.cmm** | Lauterbach debug script files | Medium |

**확장 가능한 구조**:
```python
SUPPORTED_EXTENSIONS = {
    'hex': {'priority': 'high', 'description': 'Intel HEX format'},
    's19': {'priority': 'high', 'description': 'Motorola S-record format'},
    'cmm': {'priority': 'medium', 'description': 'Lauterbach debug script'},
    # Future extensions can be easily added here
}
```

#### 4.2.2 Car Variant 기반 필터링 규칙

**필터링 로직**:
```python
class CarVariantFilter:
    def filter_firmware_files(self, extracted_files: List[str], car_variant: str) -> List[str]:
        """
        Filter firmware files based on Car Variant keywords
        """
        filtered_files = []
        
        for file_path in extracted_files:
            file_name = os.path.basename(file_path).lower()
            file_ext = os.path.splitext(file_path)[1].lower()
            
            # 1. Check if file extension is supported
            if file_ext not in SUPPORTED_EXTENSIONS:
                continue
                
            # 2. Check if Car Variant keyword is in file name or path
            if self._contains_variant_keyword(file_path, car_variant):
                filtered_files.append(file_path)
                
        return filtered_files
    
    def _contains_variant_keyword(self, file_path: str, car_variant: str) -> bool:
        """
        Check if file path contains Car Variant keyword
        """
        # Convert to lowercase for case-insensitive matching
        path_lower = file_path.lower()
        variant_lower = car_variant.lower()
        
        # Check in file name
        file_name = os.path.basename(file_path).lower()
        if variant_lower in file_name:
            return True
            
        # Check in directory path
        dir_path = os.path.dirname(file_path).lower()
        if variant_lower in dir_path:
            return True
            
        return False
```

**필터링 예시**:
```
Car Variant: "CarVariant_A"
Input Files:
├── firmware_generic.hex          ❌ (no variant keyword)
├── CarVariant_A_firmware.hex     ✅ (variant in filename)
├── CarVariant_B_firmware.s19     ❌ (different variant)
├── debug/CarVariant_A/debug.cmm  ✅ (variant in path)
└── common/config.hex             ❌ (no variant keyword)

Output: ["CarVariant_A_firmware.hex", "debug/CarVariant_A/debug.cmm"]
```

#### 4.2.3 확장 가능한 필터링 구조

**설정 기반 필터링**:
```python
class FilterConfig:
    def __init__(self):
        self.variant_keywords = {}  # Car Variant별 키워드 매핑
        self.file_patterns = {}     # 파일명 패턴 규칙
        self.path_patterns = {}     # 경로 패턴 규칙
    
    def add_variant_keyword(self, variant: str, keywords: List[str]):
        """Add keywords for specific Car Variant"""
        self.variant_keywords[variant] = keywords
    
    def get_filter_rules(self, variant: str) -> Dict:
        """Get filtering rules for specific Car Variant"""
        return {
            'keywords': self.variant_keywords.get(variant, [variant]),
            'file_patterns': self.file_patterns.get(variant, []),
            'path_patterns': self.path_patterns.get(variant, [])
        }
```

- [ ] **4.3 폴더 관리 로직**
  - 중복 감지 알고리즘
  - 안전한 덮어쓰기 프로세스
  - 에러 처리 및 복구

---

### 🧪 5. 테스트 전략 설계 (Testing Strategy)
- [ ] **5.1 단위 테스트 계획**
  - 핵심 함수별 테스트 케이스
  - 모킹 전략 (파일 시스템 등)
  - 테스트 데이터 준비

- [ ] **5.2 통합 테스트 계획**
  - 전체 워크플로우 테스트
  - 에러 시나리오 테스트
  - 성능 테스트 기준

---

### 📦 6. 배포 및 패키징 설계 (Deployment Design)
- [ ] **6.1 실행 파일 패키징**
  - PyInstaller 설정
  - 의존성 포함 전략
  - 배포 파일 크기 최적화

- [ ] **6.2 설치 프로그램 설계**
  - Windows 인스톨러 구조
  - 기본 설치 경로 설정
  - 사용자 권한 요구사항

---

## 🎯 설계 완료 기준

각 단계는 다음 기준으로 완료 여부를 판단합니다:
- ✅ **완료**: 구체적인 설계 내용이 문서화됨
- 🔄 **진행중**: 일부 내용만 작성됨
- ❌ **미완료**: 아직 시작하지 않음

---

## 📝 설계 문서 작성 가이드

### 작성 시 고려사항:
1. **구체성**: 추상적이지 않고 구현 가능한 수준으로 작성
2. **완성도**: 각 단계별로 필요한 모든 요소 포함
3. **일관성**: 용어와 표기법 통일
4. **확장성**: 향후 기능 추가를 고려한 설계

### 문서 형식:
- **표**: 구조화된 정보는 표로 정리
- **다이어그램**: 복잡한 구조는 다이어그램 포함
- **코드 예시**: 핵심 로직은 의사코드나 실제 코드 포함
- **참조**: requirements.md와의 연결성 유지
