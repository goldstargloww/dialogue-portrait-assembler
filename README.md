# dialogue portrait assembler!

a simple python script used to turn layers of a dialogue portrait into assembled images!

or, more generally: a tool to take two sets of images and layer one on top of the other, naming the files according to their layers

# installation

1. download [`portraitassembler.py`](portraitassembler.py) and put it somewhere convenient (aka get it out of your downloads folder, put it in its own folder)
2. install [Python](https://www.python.org/downloads/) (make sure to add it to your PATH - there's an option in the installer, or you can look up how to do it later)
3. run `pip install pillow` in a terminal (you can open a terminal by searching for "terminal" in the taskbar)

# usage

this is a command line tool, which, depending on your comfort level, might be a bit scary! but don't worry, it's not as complicated as it might sound

first, open a terminal in the folder you have `portraitassembler.py` in. you can do this by navigating to said folder, right clicking the background of it in your file explorer, and pressing "Open in Terminal".

in order to run the tool, type in `py portraitassembler.py`, and then take a look at the options below, which you can also find by running `py portraitassembler.py --help`:

```
usage: portraitassembler.py [-h] [-b BASE] [-B BASES] [-o OVERLAY] [-O OVERLAYS] [-f FOLDER] [-t TEMPLATE]

options:
  -h, --help            show this help message and exit
  -b, --base BASE       path to a single base image to use, eg. "./character/bases/default.png"
  -B, --bases BASES     path to a directory of bases to use, eg. "./character/bases"
  -o, --overlay OVERLAY
                        single overlay; TBA, not implemented
  -O, --overlays OVERLAYS
                        path to a directory of overlays to use, eg. "./character/overlays"
  -f, --folder FOLDER   the folder to output to. defaults to "./generated"
  -t, --template TEMPLATE
                        naming template for files. defaults to "{base}_{overlay}.png". you can use / for nesting of directories. also you need to write the .png (can't do other file types sorgy)
```

## example usage

- `py portraitassembler.py --base "character/bases/default.png" --overlays "character/overlays"`
- `py portraitassembler.py -b "character/bases/default.png" -O "character/overlays" -t "character/{base}/character_{base}_{overlay}.png"`


example video: https://github.com/user-attachments/assets/1518e65d-0675-4971-94a8-ab03f55d0453

