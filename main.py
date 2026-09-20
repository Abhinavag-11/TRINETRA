import sys
import os
from pathlib import Path

# Set application root
if getattr(sys, "frozen", False):
    app_root = Path(sys.executable).resolve().parent
else:
    app_root = Path(__file__).resolve().parent
sys.path.insert(0, str(app_root))

# Disable TorchScript JIT source code inspection for PyInstaller frozen bundles
try:
    import torch
    if hasattr(torch, "jit") and hasattr(torch.jit, "_state"):
        torch.jit._state.disable()
except Exception:
    pass

from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Qt
from config import Config
from app.ui.login_window import LoginDialog
from app.ui.main_window import MainWindow

def main():
    print("==========================================================")
    print("   TRINETRA — AI Video Analytics & Evidence Platform     ")
    print("   SIH 2026 Prototype • Problem Statement ID: SIH26187   ")
    print("==========================================================")

    # 1. Initialize folders
    Config.initialize_directories()

    # 2. Configure Qt application
    app = QApplication(sys.argv)
    app.setApplicationName(Config.APP_NAME)
    app.setOrganizationName("SIH2026_TRINETRA")

    # 3. Launch Login / Authenticator Modal
    login_dialog = LoginDialog()
    if login_dialog.exec() == QDialog.Accepted:
        # 4. Authenticated -> Launch Command & Operations Master Window
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        print("[TRINETRA] Authentication cancelled. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
