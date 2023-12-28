import base64
import codecs
from os.path import exists

def encode(value):
    value = str(value)
    value = bytearray(value, "utf8")
    value = base64.b64encode(value)
    value = str(value)[2:-1]
    value = codecs.decode(value, 'rot_13')
    value = bytearray(value, "utf8")
    value = base64.b64encode(value)
    value = str(value)[2:-1]
    value = bytearray(value, "utf8")
    value = base64.b64encode(value)
    value = str(value)[2:-1]
    value = bytearray(value, "utf8")
    value = base64.b64encode(value)
    value = str(value)[2:-1]
    value = bytearray(value, "utf8")
    value = base64.b64encode(value)
    value = str(value)[2:-1]
    value = codecs.decode(value, 'rot_13')
    return value

def decode(value):
    value = codecs.encode(value, 'rot_13')
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = codecs.encode(value, 'rot_13')
    value = str(value)
    value = base64.b64decode(value)
    return str(value)[2:-1]

def createENF():
    content = (encode(0)+'\n')*3
    for i in range(7):
        content += encode(-1) + '\n'
        content += encode(-1) + '\n'
        content += encode(-1) + '\n'
    with open('../lib/ingame_textures/map/ExtremelyNormalFile.png', "w") as f:
        f.write(content)

class Highscore:
    if not exists('../lib/ingame_textures/map/ExtremelyNormalFile.png'):
        createENF()
    
    @staticmethod
    def load_highscore(lvl, difficulty):
        with open('../lib/ingame_textures/map/ExtremelyNormalFile.png', "r") as f:
            content = f.readlines()
        return(int(decode(str(content[lvl*3 + difficulty]))))

    @staticmethod
    def save_highscore(score, lvl, difficulty):
        with open('../lib/ingame_textures/map/ExtremelyNormalFile.png', "r") as f:
            content = f.readlines()
        content[lvl*3 + difficulty] = encode(score) + '\n'
        with open('../lib/ingame_textures/map/ExtremelyNormalFile.png', "w") as f:
            f.writelines(content)

    @staticmethod
    def is_locked(lvl, difficulty):
        return Highscore.load_highscore(lvl, difficulty) == -1

    @staticmethod
    def lock(lvl, difficulty):
        Highscore.save_highscore(-1, lvl, difficulty)

    @staticmethod
    def unlock(lvl, difficulty):
        if Highscore.is_locked(lvl, difficulty):
            Highscore.save_highscore(0, lvl, difficulty)