# Google Translate Text-To-Speech

[![PyPI - Version](https://img.shields.io/pypi/v/google-text-to-speech)](https://pypi.org/project/google-text-to-speech)

![Pylint Score](https://labsoft-ai.gitlab.io/google-translate-tts/badges/pylint.svg)

---

The `google_text_to_speech` package is a Python-based solution designed to provide versatile and user-friendly text-to-speech (TTS) capabilities. Leveraging the Google Translate TTS API, it enables users to convert written text into spoken words in various languages.

```
.
├── clean_up_ws.sh
├── coverage.sh
├── docs
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   ├── prepare_plantuml.sh
│   ├── requirements.txt
│   ├── resources
│   │   └── LabSoft2.png
│   └── src
│       ├── architecture.md
│       └── user_stories.md
├── images
│   └── TransparentLogo.png
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── src
│   └── google_text_to_speech
│       ├── google_translate_tts.py
│       ├── __init__.py
│       └── _version.py
└── tests
    ├── test_google_translate_tts.py
    └── test-reports

8 directories, 20 files
```

## Table of Contents

- [Google Translate Text-To-Speech](#google-translate-text-to-speech)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
  - [Features](#features)
  - [Documentation and Reports](#documentation-and-reports)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

```bash
pip install google_text_to_speech
```

## Quick Start

```python
from google_text_to_speech import play_tts

# Text to be converted to speech
text = "Hello World!"
language = "en"  # Language code (e.g., "en" for English)

# Calling the text-to-speech function
play_tts(text, language)
```

## Features

* Multiple Language Support: Utilizes Google's TTS service to offer speech synthesis in numerous languages.
* Handling of Large Texts: Splits long texts into sentences to avoid limitations related to URL length and TTS service constraints.
* Real-Time Audio Playback: Converts text to speech in real-time, with the capability to play the audio immediately.

## Documentation and Reports

* [Documentation](https://labsoft-ai.gitlab.io/google-translate-tts)
* [GitLab](https://gitlab.com/labsoft-ai/google-translate-tts)
* [Pylint report](https://labsoft-ai.gitlab.io/google-translate-tts/lint/index.html)
* [Test coverage report](https://labsoft-ai.gitlab.io/google-translate-tts/coverage_html_report/index.html)
* The code quality report - Navigate to the [Pipelines page](https://gitlab.com/labsoft-ai/google-translate-tts/-/pipelines), select the latest pipeline, and open the `Code Quality` tab.
* The test results report - Navigate to the [Pipelines page](https://gitlab.com/labsoft-ai/google-translate-tts/-/pipelines), select the latest pipeline, and open the `Tests` tab.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](https://gitlab.com/labsoft-ai/google-translate-tts/-/wikis/home) for more information.

## License

This project is licensed under the [MIT License](LICENSE).

---

Developed with ❤️ by

 [![labsoft.ai](images/TransparentLogo.png)](https://labsoft.ai)
