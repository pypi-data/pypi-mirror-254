# Nepali-to-Roman 🌐

[![Downloads](https://img.shields.io/pypi/dm/nepali-to-roman?color=blue&style=flat-square)](https://pepy.tech/project/nepali-to-roman) [![Version](https://img.shields.io/pypi/v/nepali-to-roman?color=blue&style=flat-square)](https://pypi.org/project/nepali-to-roman/) [![License](https://img.shields.io/pypi/l/nepali-to-roman?color=blue&style=flat-square)](LICENSE)

Elegantly transform Nepali text into Romanized English with precision using the powerful `nepali-to-roman` Python package. Overcoming the limitations of existing solutions, this package meticulously maps Nepali literals and words to their precise Romanized counterparts.

## 🚀 Installation

Install `nepali-to-roman` effortlessly using `pip`. Ensure you have [`pip`](https://pip.pypa.io/en/stable/installing/) installed and run:

```bash
pip install nepali-to-roman
```

## 🎨 Usage

Import the `ntr` module into your Python script or interactive environment:

```python
import ntr
```

The `ntr` module exposes the `nep_to_rom` function, designed for transliterating Nepali text. Each word in a sentence is individually transliterated, and the results are seamlessly merged into a single string.

**Syntax:**
```python
ntr.nep_to_rom(text)
```

**Example:**
```python
import ntr
print(ntr.nep_to_rom("म नेपाल मा बस्छु ।"))
# Output: ma nepal ma baschhu .
```

## 🌱 Contributions

This package is licensed under The MIT License (MIT), details of which can be found in the [LICENSE](LICENSE) file. As an open-source project, we enthusiastically welcome contributions and feedback. If you have ideas for improvements or extensions, please feel free to contribute.

## 👥 About Contributors

- [Diwas Pandey](https://www.diwaspandey.com.np)
- [Ishparsh Uprety](https://www.ishparshuprety.com.np/)