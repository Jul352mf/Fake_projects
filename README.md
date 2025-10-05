# Fake Projects - Test Project Collection

A collection of test projects for validating Dev Wizard and other development tools.

## Purpose

This repository contains multiple test projects designed to validate various features and frameworks:

- **Multi-framework support**: TypeScript, Python, React, FastAPI, LangGraph
- **Project management tools**: Dev Wizard, MCP tools
- **CI/CD pipelines**: Testing automated workflows
- **Development patterns**: Monorepos, microservices, agent architectures

## Projects

### Test_Project_1

**Status**: ✅ Complete  
**Type**: Monorepo with 3 applications  
**Location**: `test_project_1/`

A comprehensive test monorepo containing:
- **Frontend**: React + TypeScript + Vite (weather dashboard)
- **API Server**: FastAPI + Python (weather data API)
- **LangGraph Agent**: Python + LangGraph (simple echo agent)

**Stats**:
- 24 files, 1,150 lines of code
- 3 frameworks, 3 services
- Full documentation included

**Purpose**: Validate all 18 Dev Wizard MCP tool handlers

[View Full Documentation →](test_project_1/PROJECT_SUMMARY.md)

---

## Adding New Test Projects

To add a new test project:

1. Create a new directory: `test_project_N/`
2. Add project files and documentation
3. Update this README with project details
4. Include PROJECT_SUMMARY.md in project directory
5. Add .gitignore for project-specific ignores
6. Commit and push to repository

## Structure

```
Fake_projects/
├── README.md                    # This file
├── test_project_1/              # Test Project 1 (monorepo)
│   ├── apps/                    # Applications
│   ├── PROJECT_SUMMARY.md       # Full documentation
│   ├── QUICK_REFERENCE.md       # Quick start guide
│   └── README.md                # Project overview
├── test_project_2/              # Future: Another test project
└── test_project_N/              # Future: More test projects
```

## Usage

Each test project is self-contained and can be used independently. Refer to the project's README.md and PROJECT_SUMMARY.md for specific setup instructions.

## Contributing

These are test projects for development and validation purposes. Feel free to:

- Add new test projects
- Improve existing projects
- Update documentation
- Report issues or suggest enhancements

## License

MIT License - See individual project directories for specific licensing if different.

---

**Repository**: https://github.com/Jul352mf/Fake_projects  
**Created**: October 5, 2025  
**Maintainer**: Jul352mf
