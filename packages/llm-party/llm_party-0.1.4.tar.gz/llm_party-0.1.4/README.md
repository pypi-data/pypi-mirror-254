# llm_party

llm_party offers a chat session conducted by multiple AI agents with simple but flexible configuration scheme. It is designed to be used by people who are eager to develop high-quality AI services with quick and many iterations.

## Requirements

`Python>=3.9`

## Installation

```bash
pip install llm_party
```

## Demo

See notebooks in `demo` directory.

## Conduct a chat session with multiple agents

### Initial Setup

Before starting a chat session with multiple agents (a party with LLMs🎉), you need to prepare the following.

#### Attendees

The attendees are the AI agents or humans that participate in the chat session. You need to decide what attendees you want to include in the chat session. You can choose from the following attendees:

- RawLLMAgent: A simple AI agent that sends messages based on default LLM API responses.
- FacilitatorAgent: An AI agent that can terminate the chat session.

You can create your own attendees by mixing various attendees and mixin classes. In [`custom`](./llm_party/attendee/custom) directory, you can see some examples of custom attendees.

#### configuration file

The configuration file defines the initial state of the chat session. It includes fields such as `title`, `purpose`, `status`, `attendees`, `settings`, and `chat_history`. For a detailed explanation of each field and an example of a valid JSON configuration file, refer to [initial_config_sample.yaml](./tests/data/initial_config_sample.yaml)
For the specification, refer to the [specification document](./doc/dev/#6_start_session/spec_start_session.md).

#### Start Session

Now, you are ready to start a chat session with multiple agents. You can start a chat session with a simple configuration by using `initiate_session` function.

```python
from llm_party import initiate_session

chat_session, saved_file_path = initiate_session(
    config, # path to configuration file
    save_dir="save_dir",
    save_file_name="save_file_name.yaml",
    save_yaml=True,
    output=print
)
```

You will see agents' chat in the standard output because we set `output=print`.

## Technical things

### Error Handling

The `start_session` function validates the configuration file and handles errors related to invalid configuration files and failed message delivery. If an error occurs, the function raises a `ValueError` with a descriptive error message.

### Testing

Unit tests for the `start_session` function are included in the `test_session_service.py` file. You can run these tests to verify the functionality of the `start_session` function.

### Troubleshooting

If you encounter any issues while using the `start_session` function, refer to the error message for clues about the problem. Common issues include invalid configuration files and failed message delivery.

### Future Work

Future enhancements for the start session functionality are planned, including support for human attendees and a free-for-all chat mode.

### Contact

If you encounter any issues or need further help, please feel free to create an issue in the GitHub repository.
