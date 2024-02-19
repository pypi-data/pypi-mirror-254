<a href="https://www.falu.io">
    <img src="https://cdn.falu.io/tools/logo.png" alt="Falu Logo" title="Falu" width="120" height="120" align="right">
</a>

# Falu Python

The official Falu Python library, supporting Python 3.7+.

## Installation

### pip

```shell
pip install --upgrade falu
```

### Source

```shell
python setup.py install
```

## Requirements

- Python 3.7+

## Documentation

For a comprehensive list of examples, check out the [API documentation][api-docs].

## Usage

This library requires your workspace's secret key which is located in [Falu's Dashboard][dashboard].

```python
import os

import falu

falu.api_key = os.environ.get('YOUR_FALU_SECRET_KEY', "fskt_test_...")

# list of messages
messages, error = falu.Messages.get_messages()

print(messages[0].id)

# retrieve a single message

message, error = falu.Messages.get_message(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ')

print(message.id)
```

### Per-request Configuration

```python
import falu

# list messages
messages, error = falu.Messages.get_messages(api_key="fskt_test_...", workspace="wksp_...", live=False)

# retrieve a single message
message, error = falu.Messages.get_messages(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ', api_key="fskt_test_...",
                                            workspace="wksp_...", live=False)

```

## Development

For any requests, bug or comments, please [open an issue][issues] or [submit a pull request][pulls].

The Library is licensed under
the [MIT](http://www.opensource.org/licenses/mit-license.php "Read more about the MIT license form") license. Refer to
the [LICENSE](./LICENSE) file for more information.

[dashboard]: https://dashboard.falu.io

[api-docs]: https://docs.falu.io/api?lang=python

[issues]: https://github.com/faluapp/falu-python/issues/new

[pulls]: https://github.com/faluapp/falu-python/pulls