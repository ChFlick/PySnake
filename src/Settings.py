class Setting:
    def __init__(self, name, val, reduceFct, increaseFct, min, max):
        self.name = name
        self.val = val
        self.reduceFct = reduceFct
        self.increaseFct = increaseFct
        self.min = min
        self.max = max

    def __str__(self):
        return self.name + ": " + str(self.val)

    def reduceVal(self):
        if self.checkBoundaries(self.reduceFct):
            self.val = self.reduceFct(self.val)

    def increaseVal(self):
        if self.checkBoundaries(self.increaseFct):
            self.val = self.increaseFct(self.val)

    def checkBoundaries(self, fct):
        return self.max >= fct(self.val) >= self.min


class SettingNames:
    SPEED = "Speed"
    LIVES = "Lives"

    ALL_NAMES = [SPEED, LIVES]


__settings = [
    Setting(SettingNames.SPEED, val=500, min=1, max=601, reduceFct=lambda x: x-20, increaseFct=lambda x: x+20),
    Setting(SettingNames.LIVES, val=3, min=1, max=10, reduceFct=lambda x: x-1, increaseFct=lambda x: x+1)
]


def getSettingForName(settingName):
    for setting in __settings:
        if setting.name == settingName:
            return setting

