# 📘 Project Requirements Document - FlashMate

## 1. Introduction
**Project Purpose**:  
FlashMate is a GUI tool that simplifies the extraction of firmware files from build archives (.zip), making embedded development workflows faster and less error-prone. Your friendly firmware prep assistant

**Target Users**:  
- Embedded developers (HW /SW )
- QA/test engineers  

**Scope**:  
This project aims to support ZIP file processing, firmware file filtering, and user-friendly file export — all within a desktop GUI.

---

## 2. Feature List

| ID | Feature | Priority | Status |
|----|---------|----------|--------|
| F01 | Select 2 ZIP files | High | 🔵 Planned |
| F02 | Input Car Variant | High | 🔵 Planned |
| F03 | Parse ZIP content | High |🔵 Planned |
| F04 | Extract & copy firmware files  by Car Variant| High | 🔵 Planned |
| F05 | Create output folder structure | High | 🔵 Planned |
| F06 | File input area with Drag & Drop | Medium | 🔲 TBD |
| F07 | Input field for Car Variant | Medium | 🔲 TBD |
| F08 | "Start" button to trigger processing | High | 🔲 TBD |
| F09 | Log or status message display (success/fail info) | Medium | 🔲 TBD |
| F10 | Output path display and open folder button | Medium | 🔲 TBD |
| F11 | "New Task" button to reset UI and allow new input | Medium   | 🔲 TBD |
| F12 | Database folder management for output organization | Medium | 🔲 TBD |
| F13 | Duplicate folder detection and warning system | Medium | 🔲 TBD |
| F14 | Overwrite confirmation for existing folders | Medium | 🔲 TBD |



### 2-1 Status Legend
| 마크                     | 의미                          |
| ---------------------- | --------------------------- |
| ✅ Completed            | 기능 개발 완료                    |
| 🔄 In Progress         | 현재 개발 중                     |
| 🔵 Planned             | 구현 예정 (우선순위에 따라 조만간 시작할 예정) |
| 🔲 TBD (To Be Decided) | 구현 여부 또는 방식이 아직 미정          |



## 3. Use Cases

### 🟦 Use Case: Input Files and Variant
**Actor**: Developer  
**Trigger**: User starts the application  

**Main Flow**:
1. User opens the application.
2. Selects or drags & drops **exactly two** `.zip` files.
3. Application verifies file types and counts.
4. User inputs a Car Variant string.
5. Valid files and variant are prepared for processing.

**Exceptions**:
- Less than two or more than two files selected → show validation error.
- Non-ZIP files selected → show validation error.
- Corrupted or unreadable ZIP file → show error message.
- Empty variant input → prompt for required field.

---

### 🟦 Use Case: Process and Extract Firmware Files
**Actor**: Developer  
**Trigger**: User clicks the **Start** button  

**Main Flow**:
1. Application checks for duplicate folders in Database directory.
2. If duplicate detected, shows warning with existing folder path.
3. Application parses the contents of the two ZIP files.
4. Extracts all files into a temporary directory.
5. Filters necessary firmware files (`.hex`, `.s19`, etc.) based on Car Variant.
6. Creates output folder structure under Database folder.
7. If duplicate exists and user clicks Start again, overwrites existing folder.
8. Displays success message and output path.

**Exceptions**:
- No matching firmware files found → show warning.
- Output directory inaccessible → show error and abort.
- Existing folder locked/in use → show error and abort.
- Database folder creation fails → show error and abort.

> ℹ️ Car Variant-based filtering logic is **TBD** and will be implemented later.

---

### 🟦 Use Case: View Results and Manage Output
**Actor**: Developer  
**Trigger**: After processing completes  

**Main Flow**:
1. Output folder path is displayed on the screen.
2. User clicks "Open Folder" button to launch the system file explorer.
3. Log/status area displays process summary, warnings, and any errors.
4. User clicks **"New Task"** button to reset the GUI and clear previous results.

**Exceptions**:
- Output folder not found or permission denied → show error message.
- Reset fails due to locked resources → show error and suggest app restart.

---

### 🟦 Use Case: Real-time Status and Logging
**Actor**: Developer  
**Trigger**: During any major operation  

**Main Flow**:
1. Application shows real-time status messages (validation, extraction, success/failure).
2. Errors and warnings are clearly displayed in the log area.
3. Status text is color-coded and timestamped for better readability.
4. Duplicate folder warnings include existing folder path and modification date.

**Exceptions**:
- Log display fails → continue processing with minimal feedback.


## 4. Non-Functional Requirements

| Category      | Description                                                        |
|---------------|--------------------------------------------------------------------|
| Platform      | Windows 10 or higher                                               |
| Framework     | Python (PySide6)                                                   |
| Performance   | Process ZIP files (avg 500MB) within 5 seconds                     |
| Usability & UX| Intuitive drag-and-drop GUI, no tutorial required, clear feedback  |
| Localization  | English only (v1)                                                  |
| Storage & File Handling | Organized database folder, duplicate detection, safe overwrite |
| Error Handling & Logging | Clear error messages, real-time color-coded logs with timestamps |
| Security      | Safe file operations with permission checks                        |
| Scalability & Reliability | Efficient handling of 2 ZIP files/session, robust against file/folder issues |

---

## 5. Project Milestones (Initial MVP)

| Date | Goal | Description |
|------|------|-------------|
| Jul 13 | Initial Setup | Repo, basic GUI, ZIP loader |
| Jul 20 | Core MVP | Extract, filter, export |
| Jul 31 | Demo Ready | Clean UI, simple installer |

## 🎉 프로젝트 구조 생성 완료!

FlashMate 프로젝트의 모든 폴더와 파일이 성공적으로 생성되었습니다!

### 📁 생성된 구조 요약:

```
FlashMate/
├── 📁 src/                          # 소스 코드
│   ├── 📁 main.py                   # 🚀 메인 애플리케이션
│   ├── 📁 ui/                       # UI 관련 모듈
│   │   ├── 📁 ui_files/             # Qt Designer .ui 파일들
│   │   ├── 📁 ui_classes/           # UI 클래스들
│   │   └── 📁 resources/            # 리소스 (아이콘, 스타일 등)
│   ├── 📁 core/                     # 핵심 비즈니스 로직
│   ├── 📁 utils/                    # 유틸리티 (constants.py 포함)
│   └── 📁 models/                   # 데이터 모델
├── 📁 build/                        # 빌드 관련
│   ├── 📁 scripts/                  # 빌드 스크립트
│   ├── 📁 config/                   # 빌드 설정
│   └── 📁 dist/                     # 빌드 결과물
├── 📁 scripts/                      # 관리 스크립트
│   └── 📁 clean.py                  # 정리 스크립트
├── 📁 sample_data/                  # 테스트용 샘플 데이터
├── 📁 .vscode/                      # VS Code 설정
├── 📁 env_config.bat               # 🚀 환경 설정
├── 📁 run.py                       # 🎯 통합 실행 관리자
├── 📁 requirements.txt              # Python 의존성
├── 📁 pyproject.toml               # 프로젝트 설정
├── 📁 setup.py                     # 패키지 설정
├──  .pre-commit-config.yaml      # 코드 품질 관리
└── 📁 README.md                    # 프로젝트 설명
```

###  다음 단계:

1. **환경 설정 실행:**
   ```cmd
   env_config.bat
   ```

2. **개발 시작:**
   ```cmd
   python run.py
   ```

3. **메뉴에서 선택:**
   - [1] Run Program - 애플리케이션 실행
   - [2] Build - 실행파일 빌드
   - [3] Clean - 프로젝트 정리
   - [4] Exit - 종료

이제 Qt Designer로 UI를 만들고, 각 모듈을 구현하면 됩니다! 모든 기본 구조가 준비되었습니다. 🎯

