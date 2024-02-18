# frills 1.0.4

Helpful utilities for python development

Requires:
- python	3.9
- cv2 		4.9.0.80
- numpy   1.24.3

## maths

- `get_factors()` takes one argument `n` and returns all factors of `n`. This is useful for picking appropriate batch sizes in custom data loaders. 

## graphics

All show functions take the arguments `message` and `image` for the window title and image to be displayed.

- `showw()` waits for user input (any key) before continuing execution. This is useful for checking through a series of images, allowing the user to skip as quickly or slowly as they want. 

- `showx()` shows the specified image, then exits the program entirely once the cv2 window is closed. This is useful for checking the contents of an image dataset are as expected without having to manually halt further execution. 

## debugging

- `printw()` prints a string built from the arguments given and waits for used input (any key) before continuing execution. This is useful for stepping through a program slowly and analysing the contents of variables one at a time. 

- `printx()` prints a string built from the arguments given, then exits the program entirely. This is useful for checking the contents of a variable and breaking there, rather than having to comment the rest of the code or use `sys.exit()` underneath a `print()`. 

- `normalize_to_range()` takes the following arguments:
  - `x` the data (expected to be a numpy array)
  - `min_orig` the original lower bound of the data
  - `max_orig` the original upper bound of the data
  - `min_new` the minimum of the new scale
  - `max_new` the maximum of the new scale