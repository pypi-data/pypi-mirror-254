# PLCT CLI App

This Command-Line Interface (CLI) app, named PLCT (Petlja Learning Content Tools), provides a set of commands to streamline the management and generation of learning content using Sphinx.

## Installation

1. Clone the repository:

    ```bash
    pip install plct-cli
    ```

## Commands

### `build`

Generate learning content using Sphinx-build.

```bash
plct build [-so <sphinx-options>] [-sf <sphinx-files>]
```

- `-so`, `--sphinx-options`: Specify additional options for Sphinx-build.
- `-sf`, `--sphinx-files`: Specify filenames for Sphinx-build.

### `preview`

Preview learning content using Sphinx-autobuild.

```bash
plct preview [-so <sphinx-options>]
```

- `-so`, `--sphinx-options`: Specify additional options for Sphinx-autobuild.

### `publish`

Publish learning content.

```bash
plct publish
```

### `clean`

Clean the generated output directory.

```bash
plct clean
```

### `get_markdown`

Generate markdown files from the source directory.

```bash
plct get_markdown
```

## Configuration

The app tries to determine the command arguments (source and output directories) of the sphinx command based on the project file structure. You can also specify these configurations `plct config.yaml`.

## Usage

For detailed information about each command, use the `--help` option:

```bash
plct [COMMAND] --help
```

## Examples

### Build Command

```bash
plct build
```

This command generates learning content using Sphinx with additional options and specific filenames.

### Preview Command

```bash
plct preview
```

This command previews learning content with additional Sphinx-autobuild options.

### Publish Command

```bash
plct publish
```

This command publishes learning content, copying it to the "docs" directory.

### Clean Command

```bash
plct clean
```

This command cleans the generated output directory.

### Get Markdown Command

```bash
plct get_markdown
```

This command zips all markdown files from the source directory.

## License

This CLI app is licensed under the [MIT License](LICENSE). Feel free to customize and extend it according to your needs.