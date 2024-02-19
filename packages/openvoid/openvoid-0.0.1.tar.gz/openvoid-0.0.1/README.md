# OpenVoid Python Client

The OpenVoid Python Client facilitates interaction with the OpenVoid AI API, which is currently in closed beta. This client enables developers to easily incorporate AI functionalities into Python applications, utilizing the OpenVoid AI platform's robust features.

## Features

- Easy integration with the OpenVoid AI API in closed beta.
- Simplified API response handling.
- Comprehensive examples to jumpstart your application development.

## Getting Started

### Prerequisites

Make sure Python 3.6 or later is installed on your system before installing the OpenVoid Python client.

### Installing

To install the OpenVoid Python client via pip, execute:

```bash
pip install openvoid
```

This command installs the OpenVoid client and all necessary dependencies.

### Installing from Source

For source installations, `poetry` is used for dependency management and packaging:

```bash
pip install poetry
```

After installing poetry, clone the OpenVoid client repository:

```bash
git clone https://github.com/openvoidai/openvoid-python.git
cd openvoid-python
```

Then, install the package and its dependencies:

```bash
poetry install
```

Poetry will create a virtual environment and manage all dependencies for you.

## Configuration

### API Key Setup (Closed Beta)

During the closed beta phase, OpenVoid AI API keys are exclusively available to beta testers.

1. Beta testers can obtain their OpenVoid AI API key as detailed in the [OpenVoid Documentation](https://docs.openvoid.ai/#api-access).
2. Configure your environment with your API key:

```bash
# For zsh users
echo 'export OPENVOID_API_KEY=[your_key_here]' >> ~/.zshenv
source ~/.zshenv

# For bash users
echo 'export OPENVOID_API_KEY=[your_key_here]' >> ~/.bashrc
source ~/.bashrc
```

## Usage

### Running Examples

The `examples/` directory includes scripts that demonstrate the OpenVoid Python client's usage. Run these examples with `poetry run` or within a `poetry shell` environment.

#### Using poetry run

```bash
cd examples
poetry run python chat_no_streaming.py
```

#### Using poetry shell

```bash
poetry shell
cd examples
python chat_no_streaming.py
```

### Usage Example

Here is a simple example that demonstrates how to use the OpenVoid Python client to ask a question and receive an answer:

```python
#!/usr/bin/env python

import os
from openvoid.client import OpenVoidClient
from openvoid.models.chat_completion import ChatMessage

def main():
    api_key = os.environ["OPENVOID_API_KEY"]
    model = "prox"

    client = OpenVoidClient(api_key=api_key)

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content="What is SQL Injection?")],
    )
    print(chat_response.choices[0].message.content)

if __name__ == "__main__":
    main()
```

This script demonstrates initiating a chat session with the OpenVoid AI and asking it to explain SQL Injection. Ensure you have set your `OPENVOID_API_KEY` in your environment variables to use this example.

## Improvements

- **API Key Management for Closed Beta:** Enhanced configuration process for closed beta participants' API keys.
- **Expanded Examples:** More detailed examples demonstrate the OpenVoid AI API's capabilities.
- **Improved Error Handling:** Better error reporting for easier debugging and issue resolution.

## Contributing

Contributions are welcome! Check the repository's contribution guidelines for more information.

## License

This project is licensed under the [MIT License](LICENSE.txt). See the LICENSE file for details.