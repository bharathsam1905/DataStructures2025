# AI Assistant Instructions for DataStructures2025

This repository contains coursework and implementations for the ND256 Data Structures and Algorithms course. Follow these guidelines when assisting with this codebase.

## Project Structure

The repository is organized into four main sections:
- `introduction/` - Introductory problems analyzing CSV data
- `data-structures/` - Core data structure implementations
- `basic-algorithms/` - Standard algorithm problems and solutions
- `advanced-algorithms/` - Complex algorithmic challenges like A* pathfinding

## Coding Standards

### Type Annotations
- Use Python type hints for all function parameters and return values
- Example pattern:
```python
def function_name(param1: type1, param2: type2) -> return_type:
    """Docstring with Args and Returns sections"""
    pass
```

### Testing Pattern
- Test files use `test_function()` pattern with descriptive test cases
- Include edge cases, normal cases, and error cases
- Example pattern:
```python
def test_function(test_case):
    """Test docstring describing inputs and expected behavior"""
    # Edge cases
    test_case([[]])  # Empty input
    # Normal cases
    test_case([[1, 2, 3]])  # Standard input
    # Error cases
    test_case([None])  # Invalid input
```

### Documentation Requirements
- Every problem solution requires:
  1. Implementation file (e.g., `problem_N.py`)
  2. Explanation file (e.g., `explanation_N.md`) with:
     - Reasoning behind decisions
     - Time complexity analysis 
     - Space complexity analysis

## Key Files and Patterns

### Route Planner Project
- Entry: `advanced-algorithms/route-planner/project_notebook.ipynb`
- Tests: `project_test.py` contains test cases and validation logic
- Key function: `shortest_path(map_40, start, goal)` implementing A* search

### Data Structures Project
- Directory: `data-structures/show-me-the-data-structures/`
- Each problem has implementation (.py) and explanation (.md) files
- File traversal pattern in `problem_2.py` shows standard recursive approach

### CSV Data Analysis
- Location: `introduction/unscramble-computer-science-problems/`
- Uses Python's csv module to process text/call data
- Standard pattern: read CSVs into lists, then analyze data

## Common Tasks

### Running Tests
- Each algorithm/data structure has its own test suite
- Test functions print "Pass" or "Fail" based on output comparison
- Run individual tests using Python directly: `python problem_N.py`

### Adding New Solutions
1. Create implementation file following type annotation standards
2. Add corresponding explanation.md with complexity analysis
3. Include comprehensive test cases following the established pattern

## Prerequisites
- Python 3.9+
- No external dependencies required - standard library only
- VS Code or similar IDE for Python development

Remember to maintain the educational focus of this repository - solutions should be clear, well-documented, and following the established patterns for consistency.