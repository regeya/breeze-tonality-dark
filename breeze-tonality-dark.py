# /usr/bin/env python

from typing import ClassVar
from dataclasses import dataclass, field


@dataclass
class WindowColors:
    # 1. The shared data structure (Class Variable)
    myclass = "Window"
    inactive = False
    colors: ClassVar[dict] = {
        "BackgroundAlternate": (22, 22, 27),
        "BackgroundNormal": (33, 33, 40),
        "DecorationFocus": (53, 132, 228),
        "DecorationHover": (53, 132, 228),
        "ForegroundActive": (53, 132, 228),
        "ForegroundInactive": (136, 136, 142),
        "ForegroundLink": (129, 208, 255),
        "ForegroundNegative": (255, 136, 140),
        "ForegroundNeutral": (255, 156, 91),
        "ForegroundNormal": (255, 255, 255),
        "ForegroundPositive": (141, 230, 152),
        "ForegroundVisited": (251, 167, 255),
    }

    def to_commas(self, k):
        r = k[0]
        g = k[1]
        b = k[2]
        return f"{r},{g},{b}"

    def to_hex(self, k):
        r = k[0]
        g = k[1]
        b = k[2]
        return f"#{r:02x}{g:02x}{b:02x}"

    def to_reg(self, k):
        r = k[0]
        g = k[1]
        b = k[2]
        return f"{r} {g} {b}"

    def to_ini(self):
        f = []
        g = f"[Colors:{self.myclass}]"
        if self.inactive:
            g = g + "[Inactive]"
        f.append(g)
        for k, v in self.colors.items():
            f.append(f"{k}={self.to_commas(v)}")
        return "\n".join(f) + "\n\n"


class ButtonColors(WindowColors):
    colors: ClassVar[dict] = WindowColors.colors | {
        "BackgroundAlternate": (4, 97, 190),
        "BackgroundNormal": (52, 52, 55),
        "ForegroundNeutral": (255, 156, 91),
    }
    myclass = "Button"


class ComplementaryColors(WindowColors):
    colors: ClassVar[dict] = WindowColors.colors | {
        "BackgroundAlternate": (26, 67, 114),
        "BackgroundNormal": (39, 39, 39),
    }
    myclass = "Complementary"


class HeaderColors(WindowColors):
    colors: ClassVar[dict] = WindowColors.colors | {
        "BackgroundNormal": (40, 40, 44),
    }
    myclass = "Header"


class InactiveHeaderColors(WindowColors):
    colors: ClassVar[dict] = WindowColors.colors | {
        "BackgroundNormal": (34, 34, 38),
        "BackgroundAlternate": (40, 40, 44),
    }
    myclass = "Header"
    inactive = True


class SelectionColors(WindowColors):
    colors: ClassVar[dict] = WindowColors.colors | {
        "BackgroundAlternate": (26, 67, 114),
        "BackgroundNormal": (53, 132, 228),
        "ForegroundActive": (255, 255, 255),
        "ForegroundInactive": (142, 142, 142),
        "ForegroundLink": (255, 192, 87),
        "ForegroundNegative": (192, 0, 35),
        "ForegroundNeutral": (182, 34, 0),
        "ForegroundPositive": (21, 119, 46),
    }
    myclass = "Selection"


class TooltipColors(WindowColors):
    colors: ClassVar[dict] = WindowColors.colors | {
        "BackgroundNormal": (16, 16, 18),
        "BackgroundAlternate": (7, 7, 7),
    }
    myclass = "Tooltip"


class ViewColors(WindowColors):
    colors: ClassVar[dict] = WindowColors.colors | {
        "BackgroundNormal": (16, 16, 18),
        "BackgroundAlternate": (27, 27, 32),
        "ForegroundInactive": (96, 96, 108),
    }
    myclass = "View"


class ColorFX(WindowColors):
    myclass = "Disabled"
    colors: ClassVar[dict] = {
        "Color": (23, 23, 23),
        "ColorAmount": 0,
        "ColorEffect": 0,
        "ContrastAmount": 0.65,
        "ContrastEffect": 1,
        "IntensityAmount": 0.1,
        "IntensityEffect": 2,
    }

    def to_ini(self):
        f = []
        g = f"[ColorEffects:{self.myclass}]"
        f.append(g)
        for k, v in self.colors.items():
            if k == "Color":
                f.append(f"{k}={self.to_commas(v)}")
            elif v == True:
                f.append(f"{k}=true")
            else:
                f.append(f"{k}={v}")
        return "\n".join(f) + "\n\n"


class InactiveColorFX(ColorFX):
    myclass = "Inactive"
    colors: ClassVar[dict] = {
        "ChangeSelectionColor": True,
        "Color": (112, 111, 110),
        "ColorAmount": 0.025,
        "ColorEffect": 2,
        "ContrastAmount": 0.1,
        "ContrastEffect": 2,
        "Enable": True,
        "IntensityAmount": 0,
        "IntensityEffect": 0,
    }


class General(ColorFX):
    myclass = "General"
    colors: ClassVar[dict] = {
        "ColorScheme": "BreezeTonalityDark",
        "Name": "Breeze Tonality Dark",
        "shadeSortColumn": True,
    }

    def to_ini(self):
        f = []
        g = f"[{self.myclass}]"
        f.append(g)
        for k, v in self.colors.items():
            if k == "Color":
                f.append(f"{k}={self.to_commas(v)}")
            elif v == True:
                f.append(f"{k}=true")
            else:
                f.append(f"{k}={v}")
        return "\n".join(f) + "\n\n"


class KDEstuff(General):
    myclass = "KDE"
    colors: ClassVar[dict] = {
        "Contrast": 0,
        "frameContrast": 0.1,
    }


class WM(General):
    myclass = "WM"
    colors: ClassVar[dict] = {
        "activeBackground": (46, 46, 50),
        "activeBlend": (255, 255, 255),
        "activeForeground": (255, 255, 255),
        "inactiveBackground": (39, 39, 39),
        "inactiveBlend": (142, 142, 142),
        "inactiveForeground": (142, 142, 142),
    }


my_colors = {}

my_colors["window"] = WindowColors()
my_colors["button"] = ButtonColors()
my_colors["header"] = HeaderColors()
my_colors["inactive_header"] = InactiveHeaderColors()
my_colors["selection"] = SelectionColors()
my_colors["Tooltip"] = TooltipColors()
my_colors["View"] = ViewColors()
my_colors["ColorFXDisabled"] = ColorFX()
my_colors["ColorFXInactive"] = InactiveColorFX()
my_colors["General"] = General()
my_colors["KDE"] = KDEstuff()
my_colors["WM"] = WM()

my_wm = my_colors["WM"].colors
my_window = my_colors["window"].colors
my_button = my_colors["button"].colors
my_header = my_colors["header"].colors
my_selection = my_colors["selection"].colors

wine_colors = {
    "ActiveTitle": my_wm["activeForeground"],
    "AppWorkSpace": (63, 63, 66),
    "Background": my_header["BackgroundNormal"],
    "ButtonAlternativeFace": my_button["BackgroundAlternate"],
    "ButtonDkShadow": my_window["BackgroundNormal"],
    "ButtonHilight": (23, 23, 26),
    "ButtonText": my_wm["activeForeground"],
    "GradientActiveTitle": my_window["BackgroundNormal"],
    "GrayText": my_wm["inactiveForeground"],
    "Hilight": my_selection["BackgroundNormal"],
    "HilightText": my_selection["ForegroundActive"],
    "InactiveTitle": (54, 54, 56),
    "InactiveTitleText": (230, 230, 230),
    "Scrollbar": (14, 14, 14),
}
print(wine_colors["Background"])
wine_colors["ButtonFace"] = wine_colors["Background"]
wine_colors["ActiveBorder"] = wine_colors["ActiveTitle"]
wine_colors["InactiveBorder"] = wine_colors["ActiveBorder"]
wine_colors["ButtonShadow"] = wine_colors["ButtonHilight"]
wine_colors["GradientInactiveTitle"] = wine_colors["GradientActiveTitle"]
wine_colors["InfoText"] = wine_colors["InactiveTitleText"]
wine_colors["InfoWindow"] = wine_colors["InactiveTitleText"]
wine_colors["Menu"] = wine_colors["Background"]
wine_colors["MenuBar"] = wine_colors["Menu"]
wine_colors["MenuHilight"] = wine_colors["Background"]
wine_colors["MenuText"] = wine_colors["ActiveTitle"]
wine_colors["TitleText"] = wine_colors["ActiveTitle"]
wine_colors["Window"] = wine_colors["Scrollbar"]
wine_colors["WindowFrame"] = wine_colors["Window"]
wine_colors["WindowText"] = wine_colors["ActiveTitle"]


def to_reg_format(my_tuple):
    return f"{my_tuple[0]} {my_tuple[1]} {my_tuple[2]}"


def to_reg(my_dict):
    f = []
    print(my_dict)
    for k, v in my_dict.items():
        f.append(f'"{k}"="{to_reg_format(v)}"')
    return "\n".join(f) + "\n\n"


with open("breeze-tonality-dark.colors", "w") as f:
    for i in my_colors.keys():
        f.write(my_colors[i].to_ini())

with open("breeze-tonality-dark.reg", "w") as f:
    f.write("Windows Registry Editor Version 5.00\n\n")
    f.write("[HKEY_CURRENT_USER\\Control Panel\\Colors]\n")
    f.write(to_reg(wine_colors))
