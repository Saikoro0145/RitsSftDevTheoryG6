import subprocess
import sys
from importlib.util import find_spec
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]

TOOLS = {
    "pytest": "pytest",
    "pytest-cov": "pytest_cov",
    "ruff": "ruff",
    "radon": "radon",
}

COMMANDS = [
    {
        "title": "Test and Coverage",
        "tools": ["pytest", "pytest-cov"],
        "command": [
            sys.executable,
            "-m",
            "pytest",
            "test",
            "-q",
            "--cov=src",
            "--cov-report=term-missing",
            "--cov-report=html",
        ],
    },
    {
        "title": "Ruff Lint",
        "tools": ["ruff"],
        "command": [sys.executable, "-m", "ruff", "check", "src", "test"],
    },
    {
        "title": "Ruff Format",
        "tools": ["ruff"],
        "command": [sys.executable, "-m", "ruff", "format", "--check", "src", "test"],
    },
    {
        "title": "Raw Metrics",
        "tools": ["radon"],
        "command": [sys.executable, "-m", "radon", "raw", "src"],
    },
    {
        "title": "Cyclomatic Complexity",
        "tools": ["radon"],
        "command": [sys.executable, "-m", "radon", "cc", "src", "-s", "-a"],
    },
    {
        "title": "Maintainability Index",
        "tools": ["radon"],
        "command": [sys.executable, "-m", "radon", "mi", "src", "-s"],
    },
]


def is_installed(tool_name):
    module_name = TOOLS[tool_name]
    return find_spec(module_name) is not None


def run_command(command):
    completed = subprocess.run(
        command,
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (completed.stdout + completed.stderr).strip()
    return completed.returncode, output


def status_text(returncode):
    return "OK" if returncode == 0 else "FAILED"


def print_section(title):
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def main():
    final_status = 0
    missing_tools = sorted(
        tool_name for tool_name in TOOLS if not is_installed(tool_name)
    )

    if missing_tools:
        print("Missing tools:")
        for tool_name in missing_tools:
            print(f"- {tool_name}")
        print()
        print("Install required tools:")
        print("python -m pip install pytest pytest-cov ruff radon")
        print()

    for item in COMMANDS:
        title = item["title"]
        tools = item["tools"]
        missing_for_command = [
            tool_name for tool_name in tools if tool_name in missing_tools
        ]

        print_section(title)

        if missing_for_command:
            print("SKIPPED")
            print("Missing tools: " + ", ".join(missing_for_command))
            continue

        code, output = run_command(item["command"])
        print(status_text(code))
        print(output if output else "(no output)")

        if code != 0:
            final_status = 1

    return final_status


if __name__ == "__main__":
    raise SystemExit(main())
