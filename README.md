# CS202: Software Tools & Techniques for CSE 🚀  

_**Note**: Please find bandit analysis and other files of Lab 7-8 in the below OneDrive Link:_
- [https://iitgnacin-my.sharepoint.com/:f:/g/personal/22110187_iitgn_ac_in/EnECtzFbUNZKkBWY6aa8QJYBp6liTXfpuYRtJNMd1TwR6A?e=nsND4y](https://iitgnacin-my.sharepoint.com/:f:/g/personal/22110187_iitgn_ac_in/EnECtzFbUNZKkBWY6aa8QJYBp6liTXfpuYRtJNMd1TwR6A?e=nsND4y)

Welcome to my CS202 repository! This repository contains all lab assignments, reports, analysis, and code developed throughout the course. The course focused on essential software tools and techniques used in software engineering research, with extensive hands-on experience in version control, repository mining, code analysis, debugging, testing, and automation.

## 📌 Course Overview  
CS202 explores software tools and techniques fundamental to modern software engineering and research practice. The course emphasizes practical experience with industry-standard tools through 12 comprehensive lab assignments spanning version control systems, continuous integration, software repository mining, code quality analysis, testing automation, vulnerability assessment, and event-driven programming.

**Instructor:** Prof. Shouvick Mondal (IIT Gandhinagar)  
**Course Duration:** January 2025 - April 2025  
**Status:** ✅ Complete - All 12 labs submitted

## 🛠️ Topics Covered  

### Version Control & CI/CD
- Git workflows and GitHub Actions
- Agile development methods and DevOps practices
- CircleCI integration for continuous integration

### Software Repository Mining
- Mining software repositories for bug fixes
- Commit analysis and bug fix tracking using Pydriller
- LLM-based bug type inference using CommitPredictorT5
- Code complexity metrics with Lizard
- Code similarity analysis (BLEU, crystalBLEU, CodeBERTScore)

### Diff Algorithms & Source Code Analysis
- Git diff algorithms: Myers, Minimal, Patience, and Histogram
- SZZ algorithm for bug-introducing change detection
- Comparative analysis of diff algorithms on open-source repositories

### Code Complexity & Quality Metrics
- McCabe's Cyclomatic Complexity (MCC) analysis
- Control Flow Graph (CFG) generation with py2cfg
- Call graph visualization with cflow and cflow2dot

### Testing & Code Coverage
- Static and dynamic program analysis
- Code coverage analysis with coverage.py and gcov
- Automated test generation using Pynguin
- Test parallelization with pytest-xdist and pytest-run-parallel
- Regression test prioritization strategies

### Vulnerability & Security Analysis
- Common Weakness Enumeration (CWE) framework
- Vulnerability detection using Bandit
- Security analysis on open-source repositories

### Module Dependencies & Software Design
- Module dependency analysis with modulegraph and pydeps
- Cohesion metrics: LCOM{1-5} and YALCOM
- Coupling and cohesion principles in software design

### .NET Development & Debugging
- Visual Studio and C# console application development
- Visual Studio debugger for C# applications
- Exception handling and inheritance in C#
- Bug analysis in C# console games

### Event-Driven Programming
- Event-driven programming concepts and architecture
- Windows Forms applications in C#
- Event handling and control management
- Data binding and connectivity mechanisms

### Build Automation
- Makefiles: dependency rules, macros, and suffix rules
- Build tools: Gradle and Apache Maven

### Profiling & Performance Analysis
- GNU Debugger (GDB)
- Linux perf: stat, trace, sampling, and off-CPU profiling
- Hotspot UI frontend for performance visualization

## 🔧 Tools & Technologies Used  

**Python Tools:**  
coverage.py, pynguin, pytest, pytest-cov, pytest-xdist, pylint, lizard, bandit, pydriller, py2cfg, pycflow2dot, radon, cohesion, lcom, LCOM, minecraft, minecpp

**.NET/C# Tools:**  
Visual Studio Community 2022, Visual Studio Debugger

**CI/CD & Version Control:**  
Git, GitHub Actions, CircleCI

**Machine Learning & Analysis:**  
CodeBERTScore, BLEU/crystalBLEU

**Build Automation:**  
Make, Gradle

## 📂 Repository Structure 
```
├── Lab 1/          # Version Control, Git Workflows & GitHub Actions
├── Lab 2/          # Mining Software Repositories for Bug Fixes
├── Lab 3/          # Diff Algorithms Exploration
├── Lab 4/          # McCabe's Cyclomatic Complexity Analysis
├── Lab 5/          # Code Coverage Analysis & Test Generation
├── Lab 6/          # Python Test Parallelization
├── Lab 7-8/        # Vulnerability Analysis with Bandit
├── Lab 9/          # Module Dependency & Cohesion Analysis
├── Lab 10/         # C# Console Application Development
├── Lab 11/         # Bug Analysis in C# Console Games
├── Lab 12/         # Event-Driven Programming with Windows Forms
└── Lab Reports/    # Structured reports and documentation
```

Each lab directory contains:
- Source code and implementation files
- Analysis results and outputs
- Screenshots and visualizations
- Insights and observations

## 📚 Learning Outcomes  

Through this course, I gained:
- Comprehensive understanding of software engineering tools used in academic and industrial research
- Hands-on experience with version control systems and CI/CD pipelines
- Proficiency in mining and analyzing software repositories for research insights
- Skills in automated testing, test generation, and code coverage analysis
- Expertise in code quality metrics, complexity analysis, and vulnerability assessment
- Practical knowledge of debugging tools and performance profiling techniques
- Experience with event-driven programming and rapid application development in C#
- Understanding of build automation and dependency management systems

## ✨ Acknowledgments  

Special thanks to Prof. Shouvick Mondal for his comprehensive instruction and guidance throughout the course. The hands-on approach and extensive tool exposure provided invaluable practical experience in software engineering research methodologies.
