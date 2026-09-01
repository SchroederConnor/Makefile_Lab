import os
import subprocess
import re
import sys

REQUIRED_FILES = [
    "main.cpp",
    "calculator.cpp",
    "calculator.h",
    "makefile"
]

EXECUTABLE_NAMES = ["result"]


def print_result(test_name, passed):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")


# ---------------------------
# Check required files
# ---------------------------
def check_files():
    existing_files = {f.lower() for f in os.listdir(".")}
    missing = []
    for file in REQUIRED_FILES:
        if file.lower() not in existing_files:
            missing.append(file)

    if missing:
        print("Missing files:", ", ".join(missing))
        return False
    return True


# ---------------------------
# Check function declarations
# ---------------------------
def check_header():
    with open("calculator.h", "r") as f:
        content = f.read()

    # Remove single-line comments
    content = re.sub(r'//.*', '', content)

    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    required = [
        r"add\s*\(",
        r"subtract\s*\(",
        r"multiply\s*\(",
        r"divide\s*\("
    ]

    for func in required:
        if not re.search(func, content):
            print(f"Missing declaration: {func}")
            return False

    return True


# ---------------------------
# Check implementation
# ---------------------------
def check_cpp_implementation():
    with open("calculator.cpp", "r") as f:
        content = f.read()

    required = [
        r"add\s*\(",
        r"subtract\s*\(",
        r"multiply\s*\(",
        r"divide\s*\("
    ]

    for func in required:
        if not re.search(func, content):
            print(f"Missing implementation: {func}")
            return False

    return True


# ---------------------------
# Run make
# ---------------------------
def check_make():
    try:
        result = subprocess.run(
            ["make"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        if result.returncode != 0:
            print(result.stderr)
            return False

        return True

    except Exception as e:
        print(e)
        return False


# ---------------------------
# Check executable
# ---------------------------
def check_executable():
    for exe in EXECUTABLE_NAMES:
        if os.path.exists(exe):
            return True
    print("exe file name must be result.")
    return False


# ---------------------------
# Run make clean
# ---------------------------
def check_make_clean():
    try:
        subprocess.run(
            ["make", "clean"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        obj_files = [f for f in os.listdir(".") if f.endswith(".o")]
        exe_files = [f for f in EXECUTABLE_NAMES if os.path.exists(f)]

        if obj_files or exe_files:
            return False

        return True

    except Exception:
        return False


# ---------------------------
# Optional: inspect main.cpp
# ---------------------------
def check_main_cpp():
    with open("main.cpp", "r") as f:
        content = f.read()

    # Remove single-line comments
    content = re.sub(r'//.*', '', content)

    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
  
    if "#include" not in content:
        print ("No #include found in the main.cpp.")
        return False

    if "main(" not in content:
        print ("No main method is found in the main.cpp.")
        return False

    if "printf" in content:
        print ("Not all the printf were removed.")
        return False
    
    if "scanf" in content:
        print ("Not all the scanf were removed.")
        return False

    return True


# ---------------------------
# Main test runner
# ---------------------------
def main():
    total = 0
    passed = 0

    tests = [
        ("Required Files Exist", check_files),
        ("Header Declarations", check_header),
        ("CPP Implementations", check_cpp_implementation),
        ("main.cpp Structure", check_main_cpp),
        ("Makefile Builds", check_make),
        ("Executable Created", check_executable),
        ("Make Clean Works", check_make_clean),
    ]

    for name, func in tests:
        total += 1
        result = func()
        print_result(name, result)

        if result:
            passed += 1

    

    if passed == total:
        print("\n======================")
        print("Project Passed")
        print("======================")
        sys.exit(0)
    else:
        print("\n======================")
        print("Project Failed")
        print("======================")
        sys.exit(1)


if __name__ == "__main__":
    main()