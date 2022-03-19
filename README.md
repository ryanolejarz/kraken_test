# Kraken Test

This repository contains a test suite for testing the public [Kraken REST API](https://www.kraken.com/features/api).

## Dependencies

The following python packages are required for running these tests:

`json`
`pytest`
`requests`
`time`

To install these packages run:
`pip3 install <package_name>`

## Running Tests Locally
The test suite uses `pytest`.

### Run All Tests
To run all tests, from the root directory run: `pytest tests/ -v`

### Run Only Certain Test Types
Tests are marked as one of the following test types: smoke, errors, regression. To run just the smoke tests run: `pytest tests/ -v -m smoke`

You can also run more than one type of test. To run smoke tests and regression tests run: `pytest tests/ -v -m "smoke or regression"`

### Run A Test File
To run just a specific file run: `pytest tests/test_system_and_server.py -v`

## Running Tests via GitHub
A GitHub Action `Run Tests` is configured to run tests right from GitHub. To run this workflow click on the `Actions` tab. In the `Workflows` list click on `Run Tests`. Click on the `Run Workflow` dropdown and click on `Run Workflow`. By default this is set to run against `main`. To run against your branch select it from the list.

![image](https://user-images.githubusercontent.com/47618456/159128996-8559858d-ee3e-4853-aae6-f1fba2848aef.png)

Example Test Run: https://github.com/ryanolejarz/kraken/runs/5612238688?check_suite_focus=true
