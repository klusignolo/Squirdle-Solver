# Squirdle-Solver
A simple Python utility for narrowing down guesses on Squirdle.
#  ![](https://i.ibb.co/0j5mbBy/Squirdle.png)
A simple Python utility for narrowing down guesses on [Squirdle](https://squirdle.fireblend.com/). Example usage:

![Squirdle Solver](https://i.ibb.co/DYmGPCF/Squirdle-Solver.gif)

Yes, this is technically cheating. But hey, who wants to lose a streak when it comes down to the 6/6 wire?

## Compiling

Everything should run out of the box by running main.py. Instructions below for compiling into an executable.

## Building Executable

If you'd like to build the standalone executable, I've included the PyInstaller .spec file to accomplish that for you. To build a new .exe, open a command prompt window in the project directory and run the following:

```python
pyinstaller build.spec
```
When PyInstaller finishes running, the new .exe file will be located in /dist. You may need to run 'pip install pyinstaller' if you don't already have it.


## Contributing
Contributions are welcome! This is already pretty light weight. If there are any words that need to be removed from five_letter_words.txt, just open a PR and I'll approve.

## License
[MIT](https://choosealicense.com/licenses/mit/)
