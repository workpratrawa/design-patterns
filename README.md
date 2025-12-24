# Design Patterns — Examples and Practice (Python)

This repository contains short explanations and Python example code for several classic design patterns, plus a small practice exercise. The materials are organized by pattern and include both theory (Markdown) and runnable example code (Python), plus diagrams and images where helpful.

## Repository structure

- 3_decorator_pattern/
  - `1_Decorator_Basics.md` — explanation and examples of the decorator pattern concepts.
  - `2_Logging_Decorator.py` — runnable Python example demonstrating a logging decorator.
  - `basic_uml_diagram.png`, `beverage_example.png` — diagrams and illustrations.

- 7_adapter_pattern/
  - `1_Adapter_Basics.md` — explanation of the adapter pattern and when to use it.
  - `2_Question_Payment_Adapter.md` — a problem statement / example scenario.
  - `2_Solution_Payment_Adapter.py` — Python implementation of the adapter solution.
  - `basic_idea.png`, `basic_uml_diagram.png` — diagrams to illustrate the pattern.

- 9_proxy_pattern/
  - `1_Proxy_Basics.md` — explanation and variants of the proxy pattern.
  - `2_Question_Document_Service.md` — problem statement / scenario for practice.
  - `2_Soln_Document_Service.py` — Python example implementing the proxy solution.
  - `image.png` — diagram / illustration.

- pratice/1_notification_system/
  - `question.md` — practice problem describing a notification system to implement.
  - `solution.py` — a sample Python solution for the practice exercise.

- `README.md` (this file) — repository overview and usage instructions.

## What you will find in each pattern folder

- A short theory document describing the pattern, problem context, UML/diagrams, and trade-offs.
- A small, focused Python implementation that demonstrates the pattern in code.
- Images illustrating class relationships or example flows.

## Requirements

- Python 3.8+ (examples are plain Python and aim to avoid external dependencies).
- No external packages required for the included examples (unless a specific example states otherwise).

## How to run the examples

From the repository root, run the Python example files with your Python interpreter. Examples:

- Decorator pattern example
  - python3 3_decorator_pattern/2_Logging_Decorator.py

- Adapter pattern example
  - python3 7_adapter_pattern/2_Solution_Payment_Adapter.py

- Proxy pattern example
  - python3 9_proxy_pattern/2_Soln_Document_Service.py

- Practice: Notification system
  - python3 pratice/1_notification_system/solution.py

Note: The examples are small scripts intended for demonstration. If you need them structured into importable modules or packaged for testing, I can help refactor.

## Suggested improvements / TODOs

- Add tests for each example (pytest or unittest) to verify behavior and make refactoring safer.
- Add a LICENSE file (no license detected in the repository). If you want a permissive license, consider adding an MIT or Apache-2.0 license.
- Add a CONTRIBUTING.md with contribution guidelines and coding standards.
- Normalize folder naming (e.g., `practice` instead of `pratice`) if desired.
- Provide a small Makefile or scripts to run all examples and all tests.

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repository.
2. Create a branch for your change: `git checkout -b feat/my-change`
3. Make changes and add tests where appropriate.
4. Open a pull request describing your change.

If you'd like, I can create branches and push the new README.md for you.

## License

No LICENSE file was found in the repository at the time this README was created. Please add a license file to make the repository licensing explicit (e.g., MIT, Apache-2.0).

## Contact

If you want me to:
- Commit this README to the repository,
- Add a LICENSE file (I can suggest an MIT template),
- Create tests or refactor examples into a package,

tell me which action to take and I'll create the branch and push the changes.
