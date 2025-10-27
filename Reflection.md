# Static-code-analysis
Easiest vs Hardest Issues

Easiest: Function naming and adding docstrings – only required editing names and text.

Hardest: Removing the global statement and fixing mutable default arguments – required refactoring functions and passing stock and logs explicitly.

False positives

Pylint flagged broad exception handling in remove_item as a potential issue, even though it is necessary to safely catch unexpected errors.

Integration into workflow

Integrate Pylint, Flake8, and Bandit in CI/CD pipelines to automatically validate code quality, style, and security.

Can also run locally before commits to enforce coding standards early.

Tangible improvements

Code readability improved due to snake_case naming and docstrings.

Robustness improved by removing unsafe patterns (eval, bare excepts, mutable defaults).

Security and maintainability increased, reducing potential bugs and runtime errors.