```markdown
# maldinio_ai

The `maldinio_ai` package is a comprehensive utility toolset designed to streamline AI prompt management and processing. Developed by Mehdi Nabhani, this package offers a robust foundation for handling various NLP (Natural Language Processing) tasks, memory management, response processing, and project folder organization for AI-related projects.

## Features

- **Prompt Management:** Generate, manage, and process AI prompts efficiently.
- **Memory Management:** A custom-built module to handle memory operations, aiding in data retention across different operations.
- **NLP Processing:** Utilize NLP techniques to process and analyze text data.
- **API Key Management:** Securely manage your API keys for various AI services.
- **Project Folder Creation:** Automate the creation of structured project folders for organized development.

## Installation

To install `maldinio_ai`, ensure you have Python 3.6 or later installed, then run:

```bash
pip install maldinio_ai-0.1.7.5-py3-none-any.whl
```

Alternatively, you can install from source:

```bash
pip install .
```

from the root directory of the package.

## Dependencies

`maldinio_ai` depends on the following packages:

- `tiktoken>=0.4.0`
- `openai>=1.3.7`

Ensure these are installed in your environment to fully utilize `maldinio_ai`.

## Usage

Before using the package, configure your environment with the necessary API keys, especially for OpenAI services.

### Creating a Project Folder

```python
from maldinio_ai.tools.create_project_folder import CreateProjectFolder
from maldinio_ai.memory_management import ModuleMemory

memory = ModuleMemory()
create_folder = CreateProjectFolder(memory)
create_folder.execute()
```

This will set up a new project directory with subdirectories for prompts, responses, and outputs.

### Loading a Project

```python
from maldinio_ai.tools.load_project import LoadProject

load_project = LoadProject(memory)
load_project.execute()
```

### Processing Prompts with NLP

```python
from maldinio_ai.nlp.nlp_processor import NLPProcessor
from maldinio_ai.prompt.prompt_context import PromptContext

prompt_context = PromptContext()
nlp_processor = NLPProcessor()
response = nlp_processor.process("Your prompt here", prompt_context)
```

## Modules Overview

### API Key Loader
The `api_key_loader` module securely loads API keys from your environment, enabling safe access to external AI services.

### Memory Management
`memory_manager` provides structured memory storage solutions, facilitating data persistence across various operations within your project.

### NLP Client and Processor
- `nlp_client` interacts directly with NLP services to process prompts.
- `nlp_processor` serves as a bridge between your application and the NLP client, providing additional processing and handling of NLP tasks.

### Prompt Management
- `prompt_context` allows for the dynamic creation and manipulation of prompt contexts.
- `prompt_generator` offers tools for generating prompts based on predefined contexts.
- `response_processor` processes and formats responses from the AI models.

### Tools for Project Management
- `create_project_folder` automates the setup of a structured project directory.
- `load_project` assists in loading existing project configurations and details.

### Utilities
Utility modules (`verification_utils`, `json_utils`, `helpers`) offer various support functions, such as JSON validation and string manipulation, enhancing overall functionality and ease of use.

## Development

To contribute to `maldinio_ai`, clone the repository, create a new branch for your feature or bug fix, and submit a pull request.

## License

`maldinio_ai` is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, reach out to Mehdi Nabhani at [mehdi@nabhani.de](mailto:mehdi@nabhani.de).
