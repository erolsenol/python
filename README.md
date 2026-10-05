# Windows desktop and image experiments

This repository contains separate Python experiments: a BlueStacks desktop automation script (`app.py`), OpenCV image matching helpers, and Kivy drawing and Pong examples. The automation entry point depends on Windows, BlueStacks, Android Debug Bridge, and locally installed Python libraries; it is not a cross-platform application.

## Run the Kivy Pong example

Install Kivy using its platform-specific instructions, then run:

```sh
python pong/pong.py
```

The BlueStacks automation code has machine-specific paths and image coordinates in `app.py`. Review and adjust those values before running it. It can move and click the desktop and launch commands through ADB.

## Checks

```sh
python -m compileall -q app.py control.py image.py window_ss.py paint pong ui.py
```

No dependency lockfile is supplied because the Windows-only libraries depend on platform and Python version. No license is granted unless a `LICENSE` file is present.
