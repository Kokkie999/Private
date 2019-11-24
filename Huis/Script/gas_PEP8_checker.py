import pycodestyle
style_checker = pycodestyle.StyleGuide()
filesresult = style_checker.check_files(["gas.py"])