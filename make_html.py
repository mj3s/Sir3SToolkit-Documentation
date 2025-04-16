import subprocess
import os

def make_html_docs():
    # Add Sphinx to PATH
    sphinx_path = r"C:\Users\jablonski\AppData\Local\anaconda3\Scripts\sphinx-build"
    os.environ["PATH"] += os.pathsep + sphinx_path

    # Run the make.bat file
    subprocess.run(["cmd", "/c", ".\\make.bat html"])

    print("docs built")

make_html_docs()