RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"  # This resets the color back to default

order = ["NO_SIGN", "RSA", "ECDSA", "EDDSA"]
algorithms = {
    "NO_SIGN": {"marker": "o", "color": "blue"},
    "RSA": {"marker": "s", "color": "red"},
    "ECDSA": {"marker": "^", "color": "green"},
    "EDDSA": {"marker": "D", "color": "purple"},
}
color_alpha = 0.8
