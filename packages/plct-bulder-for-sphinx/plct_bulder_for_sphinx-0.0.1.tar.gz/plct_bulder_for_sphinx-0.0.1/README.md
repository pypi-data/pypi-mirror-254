# Petlja Builder for Sphinx

This custom Sphinx builder, named `PLCTBuilder`, extends the functionality of the `StandaloneHTMLBuilder` to meet specific requirements for packaging content into various formats, such as bare HTML, Moodle backup, or SCORM.

## Key Features

### Bare HTML Content

The builder provides the ability to generate HTML content suitable for hosting as standalone pages

### Moodle Backup

The builder supports packaging content in a format suitable for Moodle. Key features include:

### SCORM

The builder facilitates the creation of SCORM-compliant packages. Noteworthy features include:

## Usage

### Bare HTML Content

```python 
# conf.py

# Import the Petlja Builder extension
extensions = ['plct-bulder-for-sphinx.builder.plct_builder']

```

To generate content, use the following command:

```bash
sphinx-build -b plct_builder source output
```
## Configuration

Customize the behavior of the builder by updating the Sphinx configuration:

```python
# conf.py

# Set the content URI
content_uri = 'your_content_uri'

# Specify additional build targets (e.g., 'moodle', 'scorm')
additional_build_targets = ['moodle', 'scorm']
```

## License

This custom Sphinx builder is licensed under the [MIT License](LICENSE). Feel free to adapt and extend it based on your specific requirements.