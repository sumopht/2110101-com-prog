def mosteller(w, h):
    return ((w * h) ** 0.5) / 60


def du_bois(w, h):
    return 0.007184 * (w**0.425) * (h**0.725)


def fujimoto(w, h):
    return 0.008883 * (w**0.444) * (h**0.663)


def main():
    weight = float(input())
    height = float(input())
    print("Mosteller =", round(((weight * height) ** 0.5) / 60, 5))
    print("Du Bois =", round(0.007184 * (weight**0.425) * (height**0.725), 5))
    print("Fujimoto =", round(0.008883 * (weight**0.444) * (height**0.663), 5)


exec(input())  # DON'T remove this line
