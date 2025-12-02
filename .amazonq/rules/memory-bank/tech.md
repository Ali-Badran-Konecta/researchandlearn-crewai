# Technology Stack

## Programming Languages
- **Python**: Primary language (>=3.10 <3.14)
- **C#**: External Git Credential Manager component
- **YAML**: Configuration files for agents and tasks

## Core Dependencies
- **CrewAI**: Multi-agent AI framework for orchestration
- **UV**: Modern Python package manager and dependency resolver
- **OpenAI API**: LLM integration for agent capabilities

## Development Tools
- **UV Package Manager**: Fast dependency management and virtual environments
- **PyProject.toml**: Modern Python project configuration
- **Environment Variables**: Configuration management via `.env` files

## Build System
- **UV-based workflow**: Streamlined dependency management
- **Lock file support**: Reproducible builds with `uv.lock`
- **CrewAI CLI**: Built-in commands for project management

## Development Commands

### Setup
```bash
# Install UV package manager
pip install uv

# Install project dependencies
crewai install
```

### Execution
```bash
# Run the research crew
crewai run

# Train the crew (requires iterations and filename)
python -m researchandlearn.main train <iterations> <filename>

# Test crew performance
python -m researchandlearn.main test <iterations> <eval_llm>

# Replay specific task execution
python -m researchandlearn.main replay <task_id>
```

### Configuration
- **API Keys**: Set `OPENAI_API_KEY` in `.env` file
- **Agent Configuration**: Modify `src/researchandlearn/config/agents.yaml`
- **Task Configuration**: Modify `src/researchandlearn/config/tasks.yaml`
- **Custom Logic**: Edit `src/researchandlearn/crew.py`

## Architecture Components
- **Agent Framework**: CrewAI for multi-agent coordination
- **Tool System**: Extensible custom tools and MCP integration
- **Configuration Layer**: YAML-based declarative setup
- **CLI Interface**: Command-line driven execution model

## External Integrations
- **OpenAI API**: Language model services
- **Model Context Protocol (MCP)**: Enhanced AI tool capabilities
- **Git Credential Manager**: Secure credential handling (C# component)

## Development Environment
- **Python Version**: 3.10+ (< 3.14)
- **Package Management**: UV for fast, reliable dependency handling
- **Configuration**: Environment-based settings with `.env` support
- **Output Format**: Markdown files for generated content