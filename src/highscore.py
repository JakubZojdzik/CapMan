import base64
import codecs

def encode(value):
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

class Highscore:
    @staticmethod
    def load_highscore(lvl, difficulty):
        with open('../lib/ExtreamlyNormalFile.png', "r") as f:
            w = f.readlines()
        return(decode(str(w[lvl + 9 * difficulty])))

    @staticmethod
    def save_highscore(score, lvl, difficulty):
        with open('../lib/ExtreamlyNormalFile.png', "r") as f:
            w = f.readlines()
        w[lvl + 9 * difficulty] = encode(score) + '\n'
        with open('../lib/ExtreamlyNormalFile.png', "w") as f:
            f.writelines(w)

    @staticmethod
    def reset_highscore():
        for i in range(9):
            Highscore.save_highscore('0', i)
        
