# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-01

### Added
- Initial release of Card Brand Identifier
- Support for 8 card brands: Visa, MasterCard, American Express, Diners Club, Discover, JCB, Hipercard, and Elo
- Luhn algorithm validation for card numbers
- Python API with `identify_brand()` and `luhn_check()` functions
- Command-line interface (CLI) with `card-identify` command
- Comprehensive test suite with pytest
- Docker support with Dockerfile and docker-compose.yml
- Pre-commit hooks for code quality
- CI/CD pipeline with GitHub Actions
- Complete documentation
- Usage examples (basic and advanced)
- Makefile for automation
- pyproject.toml for modern Python packaging

### Features
- Automatic card number normalization (removes spaces and hyphens)
- Brand detection based on IIN/BIN ranges
- Luhn validation with clear error messages
- Support for formatted card numbers (e.g., "4111 1111 1111 1111")
- Interactive CLI mode
- Batch processing support
- Detailed card information via `CardInfo` dataclass

### Documentation
- Installation guide
- Usage guide
- API reference
- Troubleshooting guide
- Examples for common use cases

### Testing
- Unit tests for all major functions
- Test coverage reporting
- Multi-version and multi-OS testing in CI/CD
- Fixtures for test data

### Development Tools
- Black for code formatting
- Flake8 for linting
- isort for import sorting
- MyPy for type checking
- Bandit for security scanning
- Pre-commit hooks

## [Unreleased]

### Planned
- Web interface for card validation
- Support for additional card brands
- Performance optimizations for batch processing
- Internationalization (i18n) support
- REST API wrapper
- GraphQL API support
- Mobile app integration examples

## [0.1.0] - 2023-12-01

### Added
- Initial concept and design
- Basic Luhn algorithm implementation
- Brand pattern detection for Visa and MasterCard
- Jupyter notebook for demonstration

## Version History

### Version 1.0.0 (2024-01-01)
- First stable release
- Complete feature set
- Production-ready codebase

### Version 0.1.0 (2023-12-01)
- Initial development version
- Proof of concept

## Links

- [GitHub Repository](https://github.com/Ronbragaglia/identificador_bandeira_cartao)
- [Issue Tracker](https://github.com/Ronbragaglia/identificador_bandeira_cartao/issues)
- [Documentation](./docs/index.md)

## Contributing

To add a new entry to the changelog:

1. Add your changes under the appropriate section (Added, Changed, Deprecated, Removed, Fixed, Security)
2. Follow the format: `- [Category] Description of the change`
3. Update the version number following semantic versioning
4. Add a new `[Unreleased]` section at the top

## Types of Changes

- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability fixes
