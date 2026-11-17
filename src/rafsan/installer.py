
import subprocess
import sys
import shutil

VERSION = "1.0.0"

PACKAGES = [
    "requests",
    "httpx",
    "aiohttp",
    "aiogram",
    "pyrogram",
    "telethon",
    "pyTelegramBotAPI",
    "flask",
    "fastapi",
    "uvicorn",
    "beautifulsoup4",
    "lxml",
    "pillow",
    "numpy",
    "pandas",
    "openpyxl",
    "protobuf",
    "cryptography",
    "pycryptodome",
    "bcrypt",
    "rich",
    "colorama",
    "tabulate",
    "tqdm",
    "python-dotenv",
    "PyYAML",
    "python-dateutil",
    "APScheduler",
    "pytz",
    "psutil",
    "packaging",
    "pydantic",
    "jinja2",
    "orjson",
]

def banner():
    print("=" * 45)
    print("       RAFSAN AUTO PYTHON INSTALLER")
    print("       Developer: RAFSAN VAI")
    print("       Version:", VERSION)
    print("=" * 45)


def install_packages():
    total = len(PACKAGES)
    success = []
    failed = []

    print("\nStarting automatic installation...\n")

    for index, package in enumerate(PACKAGES, 1):
        print(f"\n[{index}/{total}] Installing {package}")

        command = [
            sys.executable, "-m", "pip",
            "install", "--prefer-binary", package
        ]

        try:
            result = subprocess.run(command)

            if result.returncode == 0:
                print(f"[SUCCESS] {package}")
                success.append(package)
            else:
                print(f"[FAILED] {package}")
                failed.append(package)

        except Exception as error:
            print(f"[ERROR] {package}: {error}")
            failed.append(package)

    print("\n" + "=" * 45)
    print("         INSTALLATION REPORT")
    print("=" * 45)
    print("Total:", total)
    print("Successful:", len(success))
    print("Failed:", len(failed))

    if failed:
        print("\nFailed packages:")
        for package in failed:
            print("-", package)

    print("\nRAFSAN INSTALLATION PROCESS FINISHED!")


def main():
    banner()

    print("\n1. Install all Python modules")
    print("2. Check Python")
    print("3. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        install_packages()

    elif choice == "2":
        print(sys.version)
        print("Python:", sys.executable)

    elif choice == "3":
        print("Goodbye RAFSAN USER!")

    else:
        print("Invalid option!")


if __name__ == "__main__":
    main()

