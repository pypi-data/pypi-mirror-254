# Base Template CLI

[![Test](https://github.com/haru52/base_template_cli/actions/workflows/test.yml/badge.svg)](https://github.com/haru52/base_template_cli/actions/workflows/test.yml)
[![Release](https://github.com/haru52/base_template_cli/actions/workflows/release.yml/badge.svg)](https://github.com/haru52/base_template_cli/actions/workflows/release.yml)
[![CodeQL](https://github.com/haru52/base_template_cli/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/haru52/base_template_cli/actions/workflows/github-code-scanning/codeql)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://commitizen.github.io/cz-cli/)
[![semantic-release: conventionalcommits](https://img.shields.io/badge/semantic--release-conventionalcommits-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

## Overview

CLI tool of [Base Template Repository](https://github.com/haru52/base_template#readme).

## Requirements

| Tool                                                                                                                                      | Version               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [Base Template Repository](https://github.com/haru52/base_template) or its [Japanese version](https://github.com/haru52/base_template_ja) | ^7.8.0 or ^6.8.0 (ja) |

You have to clone either `base_template` or `base_template_ja` repo to your machine before using Base Template CLI.

```sh
git clone git@github.com:haru52/base_template.git
# or
git clone git@github.com:haru52/base_template_ja.git
```

## Installation

```sh
pip install base-template-cli
```

## Usage

```console
Usage: base-template-cli [OPTIONS] COMMAND [ARGS]...

  Base Template CLI.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  apply  Apply (Copy) Base Template boilerplates to the destination repo.
```

```console
Usage: base-template-cli apply [OPTIONS]
                         BASE_TEMPLATE_ROOT_PATH

  Apply (Copy) Base Template boilerplates to the destination repo.

Options:
  -d, --dst TEXT          Destination repo root path.
  -t, --target-dirs TEXT  Target directories to copy (e.g., .husky,
                          .github/ISSUE_TEMPLATE). If you don't specify this
                          option, this command copies all files of Base
                          Template to the destination repo. If you want to
                          copy only root files, use --only-root option.
  -r, --only-root         Copy only root directory files of Base Template
                          repo.
  -l, --lang TEXT         Language of Base Template. `en` or `ja`.
  -h, --help              Show this message and exit.
```

## Update

```sh
pip install -U base-template-cli
```

## Uninstall

```sh
pip uninstall base-template-cli
```

## Versioning policy

[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)

## License

[MIT](https://github.com/haru52/base_template_cli/blob/main/LICENSE)

## Contributing

[Contributing Guideline](https://haru52.github.io/base_template_cli/CONTRIBUTING.html)

<!-- vale Microsoft.Vocab = NO -->

## Documentation

[Documentation | base_template_cli](https://haru52.github.io/base_template_cli/)

## Author
<!-- vale Microsoft.Vocab = YES -->

[haru](https://haru52.com/)
