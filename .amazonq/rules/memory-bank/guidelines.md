# Development Guidelines

## Code Quality Standards

### Python Code Patterns
- **Empty `__init__.py` Files**: Use minimal package initialization files for clean module structure
- **Modular Architecture**: Separate concerns into distinct modules (tools, config, core logic)
- **CLI-First Design**: Implement command-line interfaces as primary interaction method

### C# Code Patterns (External Components)
- **Namespace Organization**: Use hierarchical namespaces (`GitCredentialManager.Diagnostics`)
- **Async/Await Pattern**: Consistent use of async methods with proper Task handling
- **Constructor Injection**: Pass dependencies through constructors for testability
- **StringBuilder for Logging**: Use StringBuilder for efficient string concatenation in logging scenarios

## Structural Conventions

### File Organization
- **Package Structure**: Follow Python package conventions with `__init__.py` files
- **Configuration Separation**: Keep YAML configs in dedicated `config/` directory
- **Tool Modularity**: Organize custom tools in separate `tools/` package
- **Test Isolation**: Maintain separate `tests/` directory for all test files

### Naming Standards
- **Python Modules**: Use lowercase with underscores (`custom_tool.py`, `mcp_tools.py`)
- **C# Classes**: Use PascalCase with descriptive names (`MicrosoftAuthenticationDiagnostic`)
- **Configuration Files**: Use descriptive YAML names (`agents.yaml`, `tasks.yaml`)
- **Output Files**: Use hyphenated naming for generated content (`topic-Learning-Roadmap.md`)

## Implementation Patterns

### Error Handling
- **Exception Propagation**: Use try-catch blocks with meaningful error messages
- **Async Exception Handling**: Properly handle exceptions in async methods
- **Logging Integration**: Include detailed logging for debugging and monitoring

### Configuration Management
- **Environment Variables**: Use `.env` files for sensitive configuration
- **YAML Configuration**: Leverage YAML for structured agent and task definitions
- **Default Values**: Provide sensible defaults with override capabilities

### Dependency Management
- **UV Package Manager**: Use UV for fast, reliable Python dependency management
- **Lock Files**: Maintain `uv.lock` for reproducible builds
- **Version Constraints**: Specify Python version requirements (>=3.10 <3.14)

## API Usage Patterns

### CrewAI Integration
- **Agent Configuration**: Define agents declaratively in YAML files
- **Task Orchestration**: Use CrewAI's built-in task management and execution
- **Tool Integration**: Implement custom tools following CrewAI patterns

### External Service Integration
- **OpenAI API**: Integrate LLM services through environment variable configuration
- **MCP Protocol**: Implement Model Context Protocol for enhanced AI capabilities
- **Async Operations**: Use async/await for external API calls

## Common Code Idioms

### Python Idioms
```python
# CLI argument handling
if len(sys.argv) > 1:
    topic = " ".join(sys.argv[1:])

# Environment variable fallback
topic = os.getenv('TOPIC') or input("Enter topic: ").strip()

# Exception handling with context
try:
    result = crew.kickoff(inputs=inputs)
except Exception as e:
    raise Exception(f"Error occurred: {e}")
```

### C# Idioms
```csharp
// Async method pattern
protected override async Task<bool> RunInternalAsync(StringBuilder log, IList<string> additionalFiles)

// Platform-specific logic
if (PlatformUtils.IsMacOS()) { /* macOS-specific code */ }
else if (PlatformUtils.IsLinux()) { /* Linux-specific code */ }

// String formatting for logging
log.AppendLine($"Property: {value}");
```

## Development Practices

### Testing Approach
- **Separate Test Directory**: Keep all tests in dedicated `tests/` folder
- **Tool Discovery**: Implement tool listing and discovery for debugging
- **Integration Testing**: Test MCP and external service integrations

### Documentation Standards
- **README-Driven**: Maintain comprehensive README with setup instructions
- **Inline Comments**: Use comments sparingly, prefer self-documenting code
- **Configuration Documentation**: Document YAML structure and options

### Version Control
- **Gitignore Patterns**: Exclude build artifacts, logs, and sensitive files
- **Lock File Tracking**: Commit dependency lock files for reproducibility
- **Environment Files**: Keep `.env` files in gitignore, provide `.env.example`