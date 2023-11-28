def bold_text(text):
  bold_start = '\033[1m'
  bold_end = '\033[0m'
  return bold_start + text + bold_end

def italic_text(text):
  italic_start = '\033[3m'
  italic_end = '\033[0m'
  return italic_start + text + italic_end


def red_text(text):
  red_start = '\033[91m'
  red_end = '\033[0m'
  return red_start + text + red_end

def yellow_text(text):
  yellow_start = '\033[93m'
  yellow_end = '\033[0m'
  return yellow_start + text + yellow_end


def cyan_text(text):
  cyan_start = '\033[36m'
  cyan_end = '\033[0m'
  return cyan_start + text + cyan_end

def blue_text(text):
  blue_start = '\033[94m'
  blue_end = '\033[0m'
  return blue_start + text + blue_end

def green_text(text):
  green_start = '\033[92m'
  green_end = '\033[0m'
  return green_start + text + green_end

def dim_text(text):
  dim_start = '\033[2m'
  dim_end = '\033[0m'
  return dim_start + text + dim_end

def magenta_text(text):
  magenta_start = '\033[95m'
  magenta_end = '\033[0m'
  return magenta_start + text + magenta_end
