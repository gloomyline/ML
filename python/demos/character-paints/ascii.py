# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-17 17:46:32
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 18:18:53
import argparse
from PIL import Image

# cli args
parser = argparse.ArgumentParser()

# input image file
parser.add_argument('file')
# output file path
parser.add_argument('-O', '--output')
# the width of output character paint
parser.add_argument('--width', type=int, default=64)
# the height of output character paint
parser.add_argument('--height', type=int, default=64)

# get the args from cli
args = parser.parse_args()

# some constants
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
# character list
ASCII_CHS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|\\()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# establish a mapping between characters and grayscale
def get_char(r, g, b, alpha=256):
  if alpha == 0:
    return ' '
  chs_length = len(ASCII_CHS)
  gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
  unit = (256.0 + 1) / chs_length
  return ASCII_CHS[int(gray / unit)]

if __name__ == '__main__':
  # crate im instance with the input image file
  im = Image.open(IMG)
  # resize the image file size by input width and height
  im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

  # construct the characters paint
  txt = ''
  for y in range(HEIGHT):
    for x in range(WIDTH):
      txt += get_char(*im.getpixel((x, y)))
    txt += '\n'

  print(txt)

  # write the paint into output file
  output_f = ''
  if OUTPUT:
    output_f = OUTPUT
  else:
    output_f = 'ascii.txt'
  with open(OUTPUT, 'w') as f:
    f.write(txt)
