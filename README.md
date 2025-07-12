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



### 2-1 Status Legend
| 마크                     | 의미                          |
| ---------------------- | --------------------------- |
| ✅ Completed            | 기능 개발 완료                    |
| 🔄 In Progress         | 현재 개발 중                     |
| 🔵 Planned             | 구현 예정 (우선순위에 따라 조만간 시작할 예정) |
| 🔲 TBD (To Be Decided) | 구현 여부 또는 방식이 아직 미정          |



## 3. Use Cases

### 🟦 Use Case: Load Two ZIP Files
**Actor**: Developer  
**Trigger**: User selects or drags & drops ZIP files into the application  

**Main Flow**:
1. User opens the application.
2. Selects or drags & drops **exactly two** `.zip` files.
3. Application verifies file types and counts.
4. Valid files are temporarily prepared for extraction.

**Exceptions**:
- Less than two or more than two files selected → show validation error.
- Non-ZIP files selected → show validation error.
- Corrupted or unreadable ZIP file → show error message (via log/status area).

---

### 🟦 Use Case: Input Car Variant
**Actor**: Developer  
**Trigger**: After selecting ZIP files  

**Main Flow**:
1. User selects or types in a Car Variant string.
2. Application stores the selected variant for use in filtering logic.

**Exceptions**:
- Empty input → prompt for required field.
- (Optional) Unsupported variant value → show warning (validation rule TBD).

---

### 🟦 Use Case: Start Processing and Extract Firmware Files
**Actor**: Developer  
**Trigger**: User clicks the **Start** button  

**Main Flow**:
1. Application parses the contents of the two ZIP files.
2. Extracts all files into a temporary directory.
3. Based on the selected Car Variant, the program filters necessary firmware files (`.hex`, `.s19`, etc.).
4. Extracted files are saved to a structured output folder under the predefined path.
5. A log/status message is displayed in the GUI showing success.

**Exceptions**:
- No matching firmware files found → show warning.
- Output directory inaccessible → show error and abort.

> ℹ️ Car Variant-based filtering logic is **TBD** and will be implemented later.

---

### 🟦 Use Case: View Result and Open Output Folder
**Actor**: Developer  
**Trigger**: After processing completes  

**Main Flow**:
1. Output folder path is displayed on the screen.
2. User clicks “Open Folder” button to launch the system file explorer at the output path.
3. Log/status area displays process summary and any warnings.
4. User clicks **“New Task”** button to reset the GUI and clear previous results.

**Exceptions**:
- Output folder not found or permission denied → show error message.
- Reset fails due to locked resources or UI state → show error and suggest app restart.


---

### 🟦 Use Case: Log and Status Display
**Actor**: Developer  
**Trigger**: During or after any major operation  

**Main Flow**:
1. Application shows real-time status messages (ZIP validation, extraction steps, success/failure).
2. Errors and warnings are clearly shown in a log area.
3. Status text is optionally color-coded or timestamped.


## 4. Non-Functional Requirements

| Category | Description |
|----------|-------------|
| Platform | Windows 10+ |
| Performance | Process ZIP < 5 sec (avg 500MB build) |
| Framework | Python (PySide6)
| Usability | GUI should work without tutorial |
| Localization | English only (for v1) |

---

## 5. Project Milestones (Initial MVP)

| Date | Goal | Description |
|------|------|-------------|
| Jul 15 | Initial Setup | Repo, basic GUI, ZIP loader |
| Jul 20 | Core MVP | Extract, filter, export |
| Jul 25 | Demo Ready | Clean UI, simple installer |
