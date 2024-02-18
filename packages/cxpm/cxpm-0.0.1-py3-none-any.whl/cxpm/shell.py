import subprocess
import threading
import locale


def print_text(text):
    try:
        print(text.strip().decode(locale.getpreferredencoding()))
    except UnicodeDecodeError:
        print(text.strip().decode(locale.getpreferredencoding(), "ignore"))


def read_pipe(process_pipe, echo=True):
    for line in iter(process_pipe.readline, b""):
        print_text(line)


def cmd(command, echo=True):
    if echo:
        print(f"\033[92m cmd: {command} \033[0m")

    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    stdout_thread = threading.Thread(target=read_pipe, args=(process.stdout, echo))
    stderr_thread = threading.Thread(target=read_pipe, args=(process.stderr, echo))
    stdout_thread.start()
    stderr_thread.start()

    process.wait()
    stdout_thread.join()
    stderr_thread.join()

    if process.returncode != 0:
        raise Exception(f"Failed Return Code: {process.returncode}")


def script(script, echo=True, shell=True):
    pass
