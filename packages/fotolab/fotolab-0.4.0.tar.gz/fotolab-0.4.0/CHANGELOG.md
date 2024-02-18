# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [0-based versioning](https://0ver.org/).

## [Unreleased]

## v0.4.0 (2024-02-04)

### Added

- Add `-o` or `--overwrite` global flag to overwrite modified image

## v0.3.1 (2024-01-28)

### Added

- Add `-w` or `--width` option to `fotolab border` subcommand
- Add `-c` or `--color` option to `fotolab border` subcommand

### Fixed

- Fix border not added to image

## v0.3.0 (2024-01-21)

### Fixed

- Fix incorrect subcommand wording

### Changed

- Ignore `__repr__` in code coverage
- Ignore duplicate code linting rule

### Added

- Add `fotolab border` subcommand to add border for an image
- Test `quiet` flag

## v0.2.0 (2024-01-14)

### Added

- Add `fotolab env` subcommand for debugging and bug reporting purpose

### Fixed

- Fix incorrect metavar for `--font-color`

## v0.1.1 (2024-01-07)

### Added

- Generate project documentation using `sphinx`

### Changes

- Bump project and pre-commit hooks deps

## v0.1.0 (2024-01-01)

### Added

- Initial public release
