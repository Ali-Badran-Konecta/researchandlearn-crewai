# Project Structure

## Directory Organization

### Core Application (`src/researchandlearn/`)
- **`__init__.py`**: Package initialization and exports
- **`main.py`**: Entry point with CLI commands (run, train, test, replay)
- **`crew.py`**: CrewAI crew configuration and agent orchestration
- **`config/`**: YAML configuration files for agents and tasks
  - `agents.yaml`: Agent definitions, roles, and capabilities
  - `tasks.yaml`: Task specifications and workflows
- **`tools/`**: Custom tools and integrations
  - `custom_tool.py`: Project-specific tool implementations
  - `mcp_tools.py`: Model Context Protocol tool integrations

### Testing (`tests/`)
- **`list_crewai_tools.py`**: CrewAI tools discovery and listing
- **`test_mcp.py`**: Model Context Protocol testing

### Configuration & Dependencies
- **`pyproject.toml`**: Python project configuration and dependencies
- **`uv.lock`**: Dependency lock file for reproducible builds
- **`.env`**: Environment variables (API keys, configuration)
- **`README.md`**: Project documentation and setup instructions

### Knowledge & Output
- **`knowledge/`**: Domain knowledge and user preferences
- **Generated Roadmaps**: Various learning roadmap outputs (`.md` files)

### External Dependencies
- **`git-credential-manager/`**: Large external C# project for Git credential management
- **`cursor_latest_amd64.deb`**, **`cursor.AppImage`**: Development tools

## Core Components

### Agent System
- **Multi-Agent Architecture**: Coordinated AI agents with specialized roles
- **YAML Configuration**: Declarative agent and task definitions
- **CrewAI Framework**: Underlying orchestration and collaboration system

### Tool Integration
- **Custom Tools**: Project-specific functionality extensions
- **MCP Integration**: Model Context Protocol for enhanced AI capabilities
- **Extensible Design**: Modular tool system for easy expansion

### Execution Modes
- **Standard Run**: Basic research and roadmap generation
- **Training Mode**: Iterative improvement of agent performance
- **Testing Mode**: Evaluation and validation of crew capabilities
- **Replay Mode**: Debug and analyze specific task executions

## Architectural Patterns

### Configuration-Driven Design
- YAML-based agent and task configuration
- Environment variable configuration management
- Separation of configuration from implementation

### Modular Tool System
- Plugin-style tool architecture
- Clear separation between core logic and extensions
- Standardized tool interfaces

### CLI-First Approach
- Command-line interface for all operations
- Scriptable and automatable workflows
- Multiple execution modes for different use cases