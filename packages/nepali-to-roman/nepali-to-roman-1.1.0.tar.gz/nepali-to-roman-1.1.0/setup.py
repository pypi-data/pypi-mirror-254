import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nepali-to-roman',
    version='1.1.0',
    description='A PyPi package for converting Nepali words to Romanized English literals. This package performs transliteration, converting Devanagari words into Roman literals.',
    url='https://github.com/Diwas524/Nepali-to-Roman-Transliteration',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Diwas Pandey, Ishparsh Uprety',
    author_email='diwaspandey524@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    keywords=['Nepali to Roman', 'Nepali Transliteration', 'Devanagari to English', 'Devanagari', 'Diwas Pandey',
              'Nepali words to Roman', 'Roman from Nepali', 'Convert Nepali to Roman', 'Romanize Nepali words',
              'How to convert Nepali to Roman', 'Convert Nepali script to Roman', 'Nepali language', 'Romanization'],

    project_urls={
        'Bug Reports': 'https://github.com/Diwas524/Nepali-to-Roman-Transliteration/issues',
        'Source': 'https://github.com/Diwas524/Nepali-to-Roman-Transliteration',
    },
)
