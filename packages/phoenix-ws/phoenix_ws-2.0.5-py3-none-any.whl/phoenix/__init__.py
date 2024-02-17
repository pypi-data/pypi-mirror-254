from .serve import run, config, loadextensions, VERSION
import sys, os, shutil

def main():
  pass

if '-p' in sys.argv:
  config['port'] = int(sys.argv[sys.argv.index('-p')+1])

if '--port' in sys.argv:
  config['port'] = int(sys.argv[sys.argv.index('--port')+1])

def phoenix_help():
  print(F"phoenix version {VERSION} help\n\
        help       | Prints this message\n\
        -\n\
        run        | Starts the server\n\
        --host -h  | Allows other devices to access the server\n\
        --port -p  | Specify the port to run on\n\
        -\n\
        install    | Install a package\n\
        remove     | Uninstall a package\n\
        -\n\
        CLEAN      | Remove all PPM files\n\
        ")

if 'help' in sys.argv or '--help' in sys.argv or '-?' in sys.argv or '/?' in sys.argv:
  phoenix_help()

if '-h' in sys.argv or '--host' in sys.argv:
  config['host'] = True

if 'run' in sys.argv:
  run(config)

if 'test-ext' in sys.argv:
  loadextensions()

repo = "https://phoenix-repo.vercel.app"
if '--repo' in sys.argv:
  repo = sys.argv[sys.argv.index('--repo')+1]

if 'install' in sys.argv:
  to_install = sys.argv[sys.argv.index('install')+1:]
  for pkg in to_install:
    pl = pkg.split("==")
    name = pl[0]
    package_len = len(pl)
    version = 'latest'
    ok = True
    if package_len == 2:
      version = pl[1]
    elif package_len != 1:
      print(f"[Error] Improperly formatted package '{pkg}'")
      ok = False
    if ok:
      PPM.i(name, version, repourl=repo)

if 'remove' in sys.argv:
  to_remove = sys.argv[sys.argv.index('remove')+1:]
  for pkg in to_remove:
    PPM.r(pkg)

if 'CLEAN' in sys.argv:
  print("This WILL remove ALL PACKAGE MANAGER FILES (phoenix_files/ and package.phoenix)!")
  print("ANY AND ALL extensions WILL be DELETED, INCLUDING CUSTOM SERVER CODE!")
  confirm = input("Are you SURE you want to proceed? (y/N)").lower()
  if confirm == 'y':
    try:
      shutil.rmtree('phoenix_files/')
    except Exception as e:
      print(str(e))
    try:
      os.remove('package.phoenix')
    except Exception as e:
      print(str(e))
  else:
    print("Operation cancelled.")

