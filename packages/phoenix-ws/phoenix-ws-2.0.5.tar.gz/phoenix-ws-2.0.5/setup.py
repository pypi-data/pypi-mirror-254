import pathlib
from setuptools import setup
from phoenix import VERSION

print(f"Packaging Phoenix version {VERSION}...")

setup(
  name="phoenix-ws",
  version=VERSION,
  description="Speedy alternative web server",
  long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
  long_description_content_type="text/markdown",
  url="https://codeberg.org/novaandromeda/phoenix",
  author="Nova",
  author_email="froggo8311@proton.me",
  license="UNLICENSE",
  classifiers=[
    "Programming Language :: Python :: 3"
  ],
  packages=[
    "phoenix"
  ],
  include_package_data=True,
  install_requires=[
    "flask",
    "waitress"
  ],
  entry_points={
    "console_scripts": [
      "phoenix=phoenix.__init__:main"
    ]
  },
  license_files = ("UNLICENSE",),
  keywords=[
    "Phoenix",
    "Website",
    "Web",
    "Webserver",
    "Server",
    "Package Manager",
    "HTML",
    "CSS",
    "JavaScript",
    "JS",
    "Fast"
  ]
)
