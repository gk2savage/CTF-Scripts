from io import BytesIO
from PIL import Image

# Binary data
binary_data = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xdb\x00C\x00\x02\x01\x01\x02\x01\x01\x02\x02\x02\x02\x02\x02\x02\x02\x03\x05\x03\x03\x03\x03\x03\x06\x04\x04\x03\x05\x07\x06\x07\x07\x07\x06\x07\x07\x08\t\x0b\t\x08\x08\n\x08\x07\x07\n\r\n\n\x0b\x0c\x0c\x0c\x0c\x07\t\x0e\x0f\r\x0c\x0e\x0b\x0c\x0c\x0c\xff\xdb\x00C\x01\x02\x02\x02\x03\x03\x03\x06\x03\x03\x06\x0c\x08\x07\x08\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\xff\xc0\x00\x11\x08\x01U\x01\xa4\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xfd\x0c\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa2\x8a(\x00\xaf\r\xff\x00\x82\x95|a\xf1\x1f\xc0\x0f\xd8S\xe2_\x8c\xbc#\xa8\xff\x00d\xf8\x93\xc3\xfaI\xb9\xb0\xbc\xfb<S\xf9\x12y\x88\xbb\xb6J\xac\x8d\xc1<2\x91^\xe5_3\xff\x00\xc1c\x7f\xe5\x18\xdf\x19?\xec\x04\x7f\xf4tu\xcb\x8e\x93\x8e\x1a\xa4\xa3\xa3Q\x7f\x91\xd1\x84JU\xe0\x9e\xd7_\x99\xee\x7f\x06|Aw\xe2\xcf\x83\xfe\x14\xd5/\xe5\xf3\xef\xf5-\x1e\xce\xea\xe6]\xa1|\xc9d\x81\x19\xdb\n\x00\x19$\x9c\x00\x05|\xdd\xff\x00\x04\xfe\xfd\xb35\x7f\x15\xfe\xc4^7\xf8\x9b\xf1O^\xfb|~\x0f\xd7\xb5\xf1sz-!\x80\xc5ae+l@\x90\xa2+\x15E\xc0\xe3s\x1cd\x93\\o\xc1\x9f\xf8$\xc7\xfc$?\x07\xfc)\x7f\xff\x00\r1\xfb[\xd8\xfd\xbbG\xb3\xb8\xfb5\xa7\xc4O*\xde\xdf|\x08\xdb#O\xb3\x9d\xa8\xb9\xc0\x19\xe0\x01^+\xfb5\xfc>\xbe\xd6\x7f\xe0\x81?\x1d\xb4\x1d6\xe2\xfe\xfa\xf2\xd6\xff\x00\xc4\xc1e\x99\xcc\xb77k\x05\xc6\xf6.\xc3\x1b\x9d\xd66\xc9\xeeX\xf1]9\x8c\x9d:\xb8\x89GG\x18M\xa5\xd2\xeap\xf9i\xb7\xa3g.\x05s\xd3\xa1\x17\xaa\x94\xa0\x9b\xea\xd3\x8c\xff\x00=\xfeG\xb1\xfc\x1b\xbd\xfd\xac\x7f\xe0\xa0?\x0e\xec\xfe%\xe8\xff\x00\x15\xbc9\xfb?xO\xc4!\xee\xbc9\xa1ZxB\xdb\xc4W\xd7\x16,\xc7\xc9\x9a\xf2k\xa6\n\xb2:\x80\xc3\xca\x00m`v\x82p;\x8f\xd8\xcb\xf6\xba\xf8\x91i\xfbR\xf8\x97\xf6}\xf8\xe1\x0e\x81s\xe3\xad\x0fH\x8f\xc4\x1a\x17\x88\xf4h\xcd\xbd\xa7\x8at\xd2\xe26\x91\xa1c\xfb\xb9\xd5\x88\xca\xae\x14\xe2L\x00\x103\xfa\x87\xfc\x13\xbb\xe2^\x8b\xf1k\xf6\x19\xf8S\xac\xe87\x10O`\xde\x18\xb0\xb5a\x11\x04A4\x10$3Dq\xd1\x92Du#\xd5k\xc0\xaf5\x1bO\x8b?\xf0_}8\xe8o\r\xdf\xfc+\x1f\x86S[k\xf3\xc5\x86\xfb-\xc5\xcd\xcb\x18\xad\xdc\xf6m\x93+\xe3\'\x86<\x0ek\xa6\xa55K\x17\xf5h\xfc>\xfa\xd7W\xee\xc6M;\xef{\xa5~\x9a\xed\xb5\xa2\x15\x1dL/\xb7\x9e\x92\xf7_o\x8aQM[m\x9b\xf3\xd3s\xa5\xf1\x87\xec\x9b\xfbQ\xc1y\xaajQ\xfe\xd9\xa9\xa4i(\xf2\xdc\xac/\xf0\x9fG\x91l\xa0\x04\xb0R\xed&X"\xf1\xb8\xf2q\x9a\x9b\xfe\x08\xdd\xf1{\xe2\x97\xc7\xff\x00\xd9\xc7[\xf1\x8f\xc4\x8f\x18?\x8d\xac5o\x10\xddC\xe1MJ]\x1a\xd7I\x9a\xefL\x80\xf9"v\x82\xdd\x02\xa7\x99"HB\xb1b1\xf7\x88\xc5V\xff\x00\x82\xc7\xfcV\xd6\x0f\xc1/\x0f\xfc\x18\xf0m\xc7\x95\xe3\xbf\x8f\x9a\xb2xZ\xc9\x95\xc06\x96$\x86\xbe\xb8a\xd7\xcb\x10\x9d\x8cGA)=\xab\xdd.\xbe\x02\xea?\x0e\xbfe(~\x1d|+\xd7\xa1\xf0E\xfe\x87\xa2\xc3\xa4h\x1a\xad\xc5\x82\xea#O\xf2\x95Udx\x9c\x85\x91\x88S\x92\xdd\xdbq\x07\xa1\xe5\xa4\xf9)Ni]/u-\xdd\xd5\xa4\xdd\xde\xb7K\x95-u\xbc\xaf}\r\xaa%)\xc27\xb3~\xf3\xec\x96\xa9m\xd1\xbeg\xb6\x9c\xab\xb9\xf2\xdf\xfc\x13J\x7f\x08\xfc9\xf8I\xf1\xcf\xf6\x84\xf1j\xbbx\x94\xf8\xaf\xc4\xbf\xdb\xba\xec\xf2\xc95\xc7\xf6m\x95\xc11\xdb\xa0f "$J\x11\x00\xec\x07\xa0\xa6\xfc\t\xd6?k/\xf8(\x17\x82-\xfe(\xe9?\x13\xfc;\xf0\x07\xc1\xda\xe3\x1b\x8f\x0c\xf8v/\x08[\xf8\x82\xee\xfa\xcb{ys^\xcbp\xcaQ\xa4\x01H\xf2\xb0\x19H`\xab\xdf\x87\xf8m\xa3\xdc|B\xff\x00\x83|\xbe!xo@\xd0f\xb1\xf1>\x87\xa7\xeb:^\xb9o\x15\xd3\xdd\xc9\xa8\xeaV\xb7n\xf7\xd7\x02B79\x9c\xab\xc9\xb7\xa0\xdf\xb0d(\xaf\xaf?\xe0\x9a\xff\x00\x10\xf4O\x89\xff\x00\xb0O\xc2MO\xc3\xf2\xdb\xc9\xa7\xc7\xe1{\x1b\x12\x90\x91\x8by\xad\xe1X%\x88\x80N\nI\x1b)\x19\xedW\x08$\x9c/u\x08RJ\xdb;\xa9^K\xd7\x955\x7f\xe6wWd\xca^\xf75\xad\xcf:\x8d\xdf}\x1a\xb4~I\xb4\xed\xfc\xaa\xce\xcbZV\x1f\x15~9\xfc9\xfd\x99\xc4\xfe$\xf8{\xa3\xf8\xd3\xe2\xbcz\x9bi6\xf6\x9e\x1b\xbf\x16\xdaV\xa4\xa4\x9f*\xfd\xe4\x98\x96\xb6\x87o2\x06\x05\x83)\xda\xbf2\x8a\xf3/\xf8%g\xed\x15\xf1\x83\xe3\'\xc5?\x8f~\x1c\xf8\xc5\xadhz\x9e\xb1\xe0\x0f\x10\xdai\xd6\xf6\xfa5\xa2Ca\xa7\t"\x95\xe4\x8a\x16\xd8\xb2\xc8\x99\x0b\x86\x98\xb3q\xd7\x9a\xfa\xfbH\xf1\x16\x9f\xe2\x07\xbb[\x0b\xeb;\xd6\xd3\xee\x1a\xd2\xe8[\xcc\xb2\x1bi\x94\x02\xd1>\t\xda\xe02\x92\xa7\x90\x18q\xcd|c\xff\x00\x04\xc2\xff\x00\x93\xdd\xfd\xb2\xbf\xecy\xb3\xff\x00\xd1\x13R\xa5+\xd5\x92z\xde\r\xfd\xd2\xa6\xae\xbakv\xfevVZ\n\xaa\xe5\x84R\xfe{\x7f\xe4\xb5\x1d\xbb\xe9e\xf7+\xdd\xeao~\xd1?\xb4\x07\xc5\x0f\x8e_\xb6\x93|\x02\xf8;\xe2m;\xe1\xe4\xbe\x19\xd0\xa3\xf1\'\x8b|as\xa4\xc5\xabOh\xb2\xb0[{+kY\x7ft]\xf2\x19\x9d\xfa)\xe3\x050\xf0\xfe\xcc?\xb4\x0f\xc5_\x83\xdf\xb7\x16\xa3\xfb?|`\xf1-\x87\xc495_\x0f\x1f\x15\xf8W\xc5\xd6\xfaL:L\xf7P\xac\xbeT\xd6\x97\x16\xf0\xfe\xe8:\x10\xc5Jv\\\x9c\xef\x010\xff\x00f\xc9\x17\xc3_\xf0\\\x9f\xda2\xc2\xed\xd2;\xaf\x12xKA\xd5l#\'\x99\xad\xe1\x8a8$a\xf4\x90\x81\xc7\xadK\xf1\x86U\xf1W\xfc\x17\x7f\xe1\x05\x9d\x8a\xac\xd7\x1e\x15\xf8u\xaa\xeaZ\x99\\\x93\x043\xc8\xf0E\xbb\xb0\xcb\x91\x8e\x07\xde\xeax\xa5\x86\xda\x8b\x7fmT\xbf\xc9Tk\xd2\xce)im\x9d\xf7eb?\xe5\xe5\xbe\xcf\xb3\xb7\xfd\xbd\xec\xef~\xf7\xe6\x96\xff\x00-\x91\xe9\xff\x00\x11\x7f\xe0\xac\x7f\xb3\xd7\xc2V\xd4\x13\xc4?\x12t\xfd6}/\xc4\x17>\x17\xb9\xb7}>\xf1\xee#\xd4-\xf6\xf9\xf1\x88\x96\x12\xed\x1ao@fPb\xcb\x01\xbf5\xf1\x8f\xedG\xff\x00\x05\r\xf07\xed\x1f\xff\x00\x05\n\xb9\xf0.\xa1\xf1\xd7\xe2\xaf\xc3\x7f\x85\xde\x17\xf0\xf1\x8e9\xbc\x0f\x06\xa5\xa6_\xdfk\xe6\xe4\xc4\xe93Gm$\xaf\x12F\xd9\x04\xa0\x88\xb2\xa9\x0c\x7f\x8b\xda\x7f\xe0\x91\xdf\t|7/\xed\x07\xfbWx\xc9\xf4k)|O?\xc5mcFmFD\xdf*\xd9\xab\x89\x04+\x9c\x85R\xf21m\xa0n\xf9wgj\xe3W\xc0\x1f\xf2\x9f\x9f\x1e\xff\x00\xd9%\xb2\xff\x00\xd2\xe8\xe9\xd2I\xcf\x0e\xe5\xf6\xa3\xcc\xfet\x9c\xf4\xf4\xd6\xdd\x9d\xb7\xe5\xf7\xaa\xbb\xe4\xf6\xca\x1bF\\\xab\xbe\x95\x14\x7f\xe1\xfb\xab\xed}>\x9c\xf8g\xf1\xcf\xc2>%\xf8\x8d\xe2\x0f\x86\xda_\x88n\xb5\x8f\x17|=\xb3\xb1\xfe\xdc\x86\xe6\xdeQ4+q\x08x$yLk\x14\x8d"\r\xc7\xcb\'\x04\x9c\x85\xe9V<1\xfbBxG\xc7?\x16\xfc_\xe0\x1d\'W\xfbO\x8b\xbc\x0b\r\xac\xda\xdd\x8f\xd9g\x8f\xec+u\x19\x92\x03\xe62\x08\xdfrs\xf23c\xbe\r|\xd3\xfb&\x0f#\xfe\x0b\x17\xfbW+\xfc\x8d6\x95\xe1Y#\r\xc1u\x16$\x16\x1e\xa3<g\xd6\xab~\xc8\x9a\x84\x1a\x8f\xfc\x15\xf7\xf6\xb9ky\xa2\x9dc\xd3\xfc/\x13\x98\xdc0W[\x06\x0c\xa7\x1d\x08 \x82;\x11Y\xd5n\xa5.g\xbc\xa9\xcaO\xd5\x03\x82\x87:_g\x92\xdf\xf6\xf7%\xff\x00\xf4\xa7oN\xa7G\xff\x00\x04R\xf8\x8f\xe2\x1f\x8a\x9f\xf0O\x1f\x0ck~(\xd7u\x9f\x12k3\xea\x1a\xaaK\x7f\xaa\xde\xc9ys"\xa5\xfc\xea\x81\xa4\x91\x99\x88U\x00\x00O\x00\x00+s\xfe\t?\xfb@\xf8\xb7\xf6\x95\xfd\x91c\xf1G\x8d\xf5\x7f\xed\xadp\xf8\x83V\xb27_e\x86\xdb\xf70]\xc9\x1cK\xb2\x14D\xf9Q@\xce2q\xc9&\xb8\xaf\xf8 \xa9\xc7\xfc\x13\'\xc2\x7f\xf6\x13\xd6?\xf4\xe3q_:\xfc\x10\xf1&\xb1\xa1\xff\x00\xc1\xbb\xdf\x165\x0f\r\xcd2\xde\xfd\xa7\xc4!f\xb69e\xb7}E\x96vR;y-!\xc8\xe82kLeOgR\xac\xed~Zw\xb7\x9d\xe1\xff\x00\x07_SOg\xcfS\x91iz\xcd|\xbfy\xfeKO#\xeb\xed_\xfe\x0b\x11\xfb4\xe8^?o\r\xdc\xfcX\xd0\xd6\xfe;\xaf\xb1=\xc2\xdb]>\x9b\x1c\xdc\xfc\xad|\xb1\x1bQ\xd0\xf2e\xc0\xc7Z\xf5\xff\x00\x8b\x9f\xb4\x7f\x82\xbe\x05\xe8\xde\x1b\xd4|Q\xaeG\xa7\xd8\xf8\xbfW\xb5\xd0ty\xe3\xb7\x9a\xe9/o.C\x18#\x06\x14|\x07\np\xed\x84\x1d\xd8dW\x95\xfc\'\xf8I\xf0\xe6\x1f\xf8%\xde\x8f\xe1\xc5\xd3\xf4\x8f\xf8W\x97~\x00\x8ek\x85\xf2\xd5\xa0\x96\x17\xb2\x12\xc9p\xc4\xf0\\\x92d.y\xdd\xces_\t\xe9\x1a\x96\xb1\xa9\xff\x00\xc1\x1e\xff\x00c\x1b\x9dl\xdc\x97\xb5\xf8\xb3\xa2\xa2Kq\x9c\xa5\x9a^\xdfGnI$\xe1|\xa1\x18\x1c\xe3\x1b@\xe3\x15\xb7\xb2\xe5\xac\xe8I\xeb\x19\xd3\x8b}\xd4\xe4\xe2\xec\xbaZ\xdaj\xff\x00\x03\x96\x13\xe7\xa2\xab\xf4\x94f\xd2\xec\xe3\x0ee\xea\xba=\xbf\x1d?Q~4~\xd0~\x10\xfd\x9elt\x0b\x9f\x18j\xff\x00\xd9\x10\xf8\x9fZ\xb6\xf0\xee\x98\xdfe\x9a\xe3\xed7\xf7\x1b\xbc\x98q\x121]\xdb\x1b\xe6l(\xc7,+\x96\xf8\xe3\xfbw|%\xfd\x9b<_{\xa1x\xeb\xc6v>\x1b\xd54\xfd\x07\xfe\x12i\xa2\xba\xb7\x9fo\xd8<\xff\x00\xb3\x89\x15\xd5\n;\x99~E\x89I\x95\x8fD"\xbc\'\xfe\x0bM\xa8A\x0f\x85?g\xebg\x9a%\xb8\x9f\xe3?\x87\x9e(\x99\xc0y\x15L\xfb\x8a\x8e\xa4\r\xcb\x9ct\xc8\xf5\xacO\x8b\xbf\n\xbc;\xf1G\xfe\x0b\xef\xe0V\xf1\x0e\x91i\xab\xff\x00\xc2;\xf0\xa1\xf5}9.T\xba[\xdd\xa6\xa74i6\xdf\xba\xcc\xab+\xed\xdc\x08\x0cC\x0c2\xa9\x18\xd2Nm-\xaf)\xc7\xe5\x1aJ\x7f}\xdf\xdd\xa6\x9b\x9b\xd4Q\x8c\\\xbbB2\xf9\xba\x8e\x16\xf4\xb7\xf9\xeb\xb1\x8b\xff\x00\x05\x16\xff\x00\x82\x82\xf8\xef\xc5_\n~\x08\xf8\x93\xf6Y\xf1u\xa5\xea\xfcG\xd5\xf5\x18m\xda]%\x1d5\xc5\xb4\x85\xdc\xda\xf9wP\xf9\xa8\xcd$2F\x02\x84fb\x06\xe1\x90k\xdb\xf4\x0f\xdb\x85?h\x1f\xf8%\xe7\x88\xfe3x2\xe5t\xcdj\x0f\x06\xeaw\xe1\x04k#h\xfa\xad\xb5\xac\xa6H\x99$\x04\x1f.d\xe0:\x90\xcb\xb4\xe0\x86\xe7\x8d\xff\x00\x82\x93D\xb0\xfe\xd8\x1f\xb2\x08U\n?\xe1?\xbal\x01\x8eM\xa1$\xfe$\xd7\x81\xfe\xd7\xf6\xaf\xff\x00\x04\xda\xf8\xa3\xf1\xc3\xc3\xa1\x1a\xdb\xe0\xf7\xed/\xe1-sP\xd2\x8e\xf6\xfb6\x85\xe2u\xd3\xe63B\x01\x1bP]\x0c\x15\x19\xe5\xb6(\x18\x8e\xb9g/\xdc\xd7KK\xb9(\xf7N4\xe0\xd2\xbf\xf7\xae\xed\xfd\xe4\x97\xda5\xa2\xbf\xda(\xdf\xa7+\x97f\x9c\xe4\x9b\xb7\xf7l\xaf\xfd\xden\xc8\xfa\xbf\xe1\x0f\x8a\xfe2~\xd1\xdf\xb0\x0f\xc2mk\xc2\xbe.\xf0\xce\x89\xe3_\x16\xe8\xb6\x17\x9a\xf7\x88\xb5\x8d\x1f\xed\x86\x08\xe5\xb5-,\xd6\xf6\x91\x18\xa1i\xcc\xa62\x15\xca\xc6\x06\xee\x0f\x02\xbc\xb3\xc2\xff\x00\x19>:~\xc9?\xf0P\x8f\x85\xff\x00\n~ \xfcM\xd2\xfe2\xf8c\xe2\xe5\x9e\xa0\xf0]?\x87-t]KC\x96\xd2\x03)m\x96\xdf+\xc6\xc4\x01\x96\x07\x82\xdd\n|\xde\xa3\xfb\x13\xfc9o\x8b\x7f\xf0J\x8f\x85^\x1dO\x10\xf8\x97\xc2\x8d\xaax\'K\x8cj\xde\x1f\xbb[MJ\xcb\x10\xc6\xdb\xa1\x95\x91\xc2\xb1\xc6\t*x&\xbei\xf8\x8d\xf0sR\xff\x00\x82]\xfe\xdf\xbf\x07|]k\xe3\x1d{\xe2\xfc?\x18u\x84\xf0M\xf1\xf1\xdc\xd1\xea~"\xd2VF]\xb3Y^*+$*d;\xe3\n\x14\x0c\x0c\x1d\xfb\x93\xd3\xad\x15\x1c\xc1\xc1-\x1c\xda\xf2\xd6\xea+\xcb\xde\xb6\xab\xaf\x91\xc1E\xb9`\xb9\x9f\xc4\xa1\x7fKY\xb9y\xe9}\x1e\xfbu>\x84\x1f\xb4O\x8e~\x08\x7f\xc1Q\xbf\xe1]\xf8\xdb[]K\xe1\xb7\xc5\x9d\x10\xdfx\x12Im \x80\xe9Z\x95\xa0\x1fj\xd3\xfc\xc8\xe3V\x97z\x13(2\xb3\x11\x98\xd5NKf_\x82\x7f\xb4\x8f\x8c?i_\xf8(\x1f\xc4\x1b]\x03Z[/\x82\xff\x00\x08m\x06\x83\xa8"\xda\xc0\xeb\xaf\xeb\xef\x97\x9b\xf7\xec\x86EKd\xf9YQ\xd7\xe7\nNCb\xab\x7f\xc1g\xbe\x19G\xe2\xaf\xd8g_\xf1}\x9d\xec\xda?\x8b>\x14M\x17\x8c\xbc7\xaa\xdb\xa83X\xdeZ\xb0<g\x82\xae\x85\xd4\x83\x91\x92\xa4\x83\xb4\n\xe8\xbf`?\x86\x9e\x1c\xfd\x92\xbf\xe0\x9d\xde\x17\x9eY\x9e{F\xf0\xf9\xf1o\x885\t\x932\xdf\xdc\\\xc3\xf6\xbb\xa9\x9cs\xb8\xfc\xc5FI\xf9QGj\xe3\x84\x94i\xcas\xff\x00\x97i\xaf^k\xf2\xb7\xfe\x14\xa6\xbb\xddFGME\xcd8\xc2\x1b\xd4\xb7\xcb\x96\xdc\xc9z\xbeO+9\xae\xc5\rG\xfe\x0b)\xfb2\xe9~6]\x02_\x8bZ\x19\xbbk\xa5\xb3\xfbLV\x97r\xe9\xab+t\x06\xf9!6\xa0z\x93.\x07r)\xff\x00\xf0T\xaf\xda#\xc5\x7f\xb3\xcf\xec\xeb\xe1\xbf\x10x\x1fY]+P\xd4\xbce\xa3ir\\\xad\xb4\x17K5\xa5\xc4\xfbe@%G\\2\xff\x00\x10\x19\x1d\x88\xaf\x9b\xbe;|g\xf8\xb1\xfbV\x7f\xc10<k\xe2\x0f\x08\xfc\'\xf8I\xe0\xaf\x82:\x8f\x85u\t\xac\xac5mfw\xd5\xcd\x84H\xed\x1d\xcc6\xd6\xb6\xdff\x86O\x93zDd\xf9]FXu\xa7\xfe\xd7\xda\x94\xfa\xc7\xfc\x11\x8f\xf6n\xba\xb9\x91\xa6\xb8\x9e\xfb\xc0\xcf#\xb7V%"\xc9\xad\x14]\xe3\xcd\xa3U)\'\xe6\xa5=\x9a\xe9\xf0\xd9\xa7\xbd\xec\xedfe9{\x92\x94vp\xaa\xd7\xfd\xbb\x1d,\xfa\xef\xbf\x92ks\xee_\x8c\xdf\xb5g\xc3\xcf\xd9\xe3\xc5\x1e\x1d\xd1\xfco\xe2\x9b\x0f\x0c\xdex\xae;\xd9t\xd6\xbeY\x12\xdeT\xb3\x88Mr\xcf>\xdf*\x10\x91\x90s+\xa89\xc0\xc9\xe2\xb9O\xd9\xb7\xfe\n5\xf0W\xf6\xba\xf1\x85\xf7\x87\xfe\x1fx\xf3O\xd7u\xcd:/\xb4K`\xf6\xb76S\xbc\\~\xf2$\xb8\x8e3*`\x82Z=\xca\x03)\'\x0c3\xe0\xbf\xf0S_\x87:\x17\xc5\x8f\xf8(w\xecy\xa1x\x97J\xb2\xd6\xf4k\xadW\xc42Oey\x18\x92\t\xccVv\xf2\xa6\xf4<0\x0e\x8apr\x0e0A\x1cV\xa7\xed\xcd\xa7\xc3\xa6\xff\x00\xc1T\x7fc\xcdB\xde5\x82\xfa\xea\xe3\xc4\x96SO\x18\xda\xf2\xc0\xb6\x11\xb2\xc4\xc4u@]\x8e\x0f\x1f1\xf5\xa2\x87\xbf\xc9\xcd\xf6\xa5(\xfaZ\xf6\x7f\xa3_;\xf45\xad\x16\x93\xe4\xe9\x0e\x7f\xb9\xca\xeb\xcbH\xe8\xf5\xd7\xa1\x81/\xfc\x17?\xe1\xd7\x87\x7fn_\x17x\x17]\xd7\xac\xed>\x1fh:2}\x9bP\x8b\xc3:\xbc\xba\x93\xea\xebq\xe5\xdc[\xba\xa4m\xfb\xa5^C\x88B\x93\x8cH\xd9\xc5z\xb7\xc4\x0f\xda3\xc5Z\x7f\xfc\x15\x13\xe1w\xc3\xfd7X\xf2\xfc\x0f\xe2\x8f\x04jZ\xd5\xe5\x87\xd8\xe1?i\xb8\x8a@"\x93\xccd\xf3W\x00\xfd\xd0\xc0\x1e\xe2\xb8\xff\x00\x86\xb3*\xff\x00\xc1v\xbe%!e\x0e\xdf\n\xb4\xd2\xaaO$\x0b\xd1\x9c\x0f\xc4~t\xff\x00\x8c\xbf\xf2\x9c\x1f\x83?\xf6N\xf5\xaf\xfd\x1c*(\xea\xa8sn\xfd\xa5\xfc\xec\xab/\xce)\xae\xd6[\xb5w\x15\x9f\xf1\xb9v^\xcf\xf1t\xb6\xf96\x9f{\xbd\x93\xb1\xe5\x1f\xf0P\x1d;\xf6\xad\xfd\x8d>\r\xdcx\xee\xdb\xf6\xac\xfe\xda\xb6\x97\\\xb3\xd3b\xd2\xff\x00\xe1Yh\xf6\xdeJ]\\\x08\x94\xf9\xc7\xcc-\xe5\x86\x1dW\xe6\xc7Q\x9c\xd7\xd1\x7f\x08\xff\x00c\x9f\x8a\xf2\xcd\xaf\xe9_\x1b\xbe:[\xfcn\xf0\'\x88t\x89\xb4\xcb\x8f\x0eO\xe0;\r\x0e6y\x19\x0f\x9af\xb7r\xe7\x08\xae\xbb8\x1f\xbc\xcer\xa2\xb8\xaf\xf8.\xcf\xfc\x98\x87\xfd\xcd\xda\x17\xfe\x97G_eUQK\xd9J\xfa\xfb\xd2\x8e\xba\xe9\xc9\x0e\xff\x00\xe2z\xef\xf8\x05I?l\xad\xa7\xba\xa5\xa6\x9a\xf3O\xb7\xa2\xd3c\xe3\xff\x00\xf8"\xe5\xc3i_\xb3\xbf\x8f|)\x1b^.\x95\xe0/\x89:\xff\x00\x87\xb4\x8b[\x89\x1eO\xec\xfb\x18\xae\x15\xa1\xb7Fr\\\xa2\x878\xdcI\xe6\xbe\xc0\xaf\x8b\x7f\xe0\x9a\x16\x1a\xbe\xbb\xfbL~\xd1\x1e \xf0\xe5\xf4:\x1f\xc2e\xf1\xd6\xa3\xa6\xc5\xe1\x99"\xfbM\xc5\xd6\xb9\x1f\x91\xf6\xddP\\6\x1e\x18\xa4`@\xb7\xf9\x97\xe6\xc8\xd9\xb7\xe7\xfbJ\xaa\xeeT\xa9M\xee\xe1\x0f\xfd%k\xf3\xdf\xe7\xad\x9d\xd2,\xa3R\xa4V\xcas\xff\x00\xd2\x9e\x9f-\xbb]iuf\x14QEH\xc2\x8a(\xa0\x02\x8a(\xa0\x02\x8a(\xa0\x02\x8a(\xa0\x02\x8a(\xa0\x02\x8a(\xa0\x02\xb8o\xdaW\xe0\x06\x8f\xfbS|\n\xf1/\xc3\xef\x10\\\xeavz7\x8a\xad>\xc7w6\x9d"Gu\x1anV\xccl\xe8\xea\x0eTuS\xf4\xae\xe6\x8a\x99\xc23\x8b\x84\xb6eFN2R\x8e\xe8\xcc\xf0g\x85\xad\xfc\r\xe0\xfd+D\xb4y\xa4\xb5\xd1\xec\xe1\xb1\x85\xe6 \xc8\xc9\x12\x04R\xc4\x00\t\xc2\x8c\xe0\x01\x9e\xd5\xc2\xfe\xcb\x1f\xb2\x9f\x87?do\x86W\xbe\x14\xf0\xed\xd6\xaf\xa8i\xba\x86\xady\xacJ\xda\xac\xb1K/\x9bu!\x92E\x05#E\xd8\t\xc0\x05s\x8e\xa4\xd7\xa6\xd1W&\xe579n\xee\x9f\xcd\xa6\xff\x00\x14\xbe\xe2#\x15\x18\xa8-\x96\xdf$\xd2\xfc\x1b>B\xd5\xff\x00\xe0\x8c\x1f\x0f4\xef\x15\xea\x9a\x87\x80\xbcy\xf1\xab\xe0\xed\x86\xb7r\xd7\x97\xfa\'\x81<^\xfaV\x95s3}\xe70\x18\xdfnG\x1bP\xaa\xa8\xe1B\x80\x00\xc4\xf0\xbf\xfc\x12\xdb\xc5?\xb1\x9f\x8f\x1f\xc4\xff\x00\xb3O\x8f"\xd1?\xb6L\x03\xc4\xfe\x19\xf1\xb0\x97U\xd3|D\xc8\xd8k\xa3r\xbf\xe9\x10\\a\xe5rS!\xdc\xa8\xf9\x17"\xbe\xd8\xa2\x88\xb7\x1br\xf4\xfc\xbbzyzvA4\xa5~n\xbf\x9f\x7f_=\xcf(\xd4\x7fc\xdf\x0ck\x7f\xb6\x05\x87\xc6\xadB\xf3\\\xbf\xf1F\x8d\xa1\xbe\x83\xa5\xd9O<M\xa6\xe9q;\x16\x92hc\xf2\xc3\xac\xcf\xb9\x95\x9c\xc8r\xacF+\xd5\xe8\xa2\x92\xd1(\xad\x95\xff\x00\x16\xdb\xfc[c\xdd\xb9u\x7f\xa2\xb2\xfc\x11\xf2\x1f\xfc\x12\xc6\xcb_\xf8<\xff\x00\x13~\x17x\x9f\xc1\x9e1\xd1u\r3\xc6Z\xce\xbbk\xab\xddiN\xba.\xb1eut$\x85\xad\xee\xf9\x8d\xdc\xab\xe4\xc6\x0e\xe5\xc1\xcf \x80\xed\x7f\xfe\x08\xcd\xf0\xea\x0f\x19jZ\xa7\x81\xbcm\xf1\x93\xe0\xf5\x9e\xb7?\xdau-\x17\xc0~,}\'J\xbf\x94\xf5w\x83c\xed\xc8\xe3\x08U@\xe0\x01_]QIE%\x05\xd61Q\xf5I%\xfa-;\xea\x17w\x97i7+y\xb6\xdf\xe6\xdd\xbc\x9d\x8f\x0f\xb7\xfd\x82<%\xe0\xff\x00\xd9\xb2\x0f\x85\xfe\x02\xd6\xbci\xf0\xb7F\x86\xf0_\xb6\xa5\xe1]W\xec\xfa\xbc\xf3\x16-#\xc9s2J\xced8\xdeX\x12@P\x08\x00\n\xf3\x0f\x83\x7f\xf0G}\x0b\xe0_\xc5\x0b\xcf\x16\xe8\x9f\x1b\xbfh\x8f\xed-cT\x83V\xd6R\x7f\x14Z\xb4:\xfc\xd16\xe0.\xc2\xda)\x95H%H\xdc\x0e\xd6 \x11__\xd1U\x16\xe3>u\xbf\xfc7\xf9/\xb8\\\xab\x97\x93\xa7\xfc?\xf9\xbf\xbc\xf0\xcf\xda\xab\xfe\t\xff\x00\xe0\xef\xda\xb7\xc6:\x0f\x8a\xae\xb5\x7f\x19x\x1f\xc7>\x1a\x8d\xad\xf4\xff\x00\x14\xf8CU\xfe\xcc\xd5\xa2\xb6bK[4\x85\x1d^"Y\x8e\xd6C\x8d\xcd\x82\x0307\x7fe\x1f\xd8[\xc1\xbf\xb25\xe6\xbb\xaa\xe9W\x9e\'\xf1W\x8b\xbcPc\xfe\xd9\xf1O\x8au6\xd55\xadMc\x18\x8e9\'!@E\x18\x01QTp\xb9\xce\x06=\x9a\x8aQ\xf7~\x1f\xea\xfa\xbf\xbd\xee9{\xdf\x17\xf5m\xbe\xee\x9d\x8f2\xfd\x9d?eO\x0f~\xcc\x9a\xaf\x8f\xee\xf4\x1b\xcdf\xeeO\x88\xde\'\xba\xf1f\xa4/\xe5\x8aE\x82\xea\xe3n\xf4\x87di\xb6!\xb4`6\xe6\xf5cQh\xff\x00\xb2O\x874_\xda\xf7W\xf8\xd3\x15\xee\xb6\xde)\xd6|;\x17\x86g\xb5y\xa2:z\xdbG(\x94:\xa7\x97\xe6\t7(\xc92\x11\x8f\xe1\xef^\xa5E\x0bG\x16\xbe\xca\xb2\xf2V\xe5\xff\x00\xd2t\t{\xd7\xbfWw\xeb~o\xcfS\xe7o\xdaK\xfe\t\xa7\xe0\xdf\xda/\xe3U\xaf\xc4h|O\xf1\x1f\xe1\xd7\x8e"\xd3\xce\x93u\xac\xf8+]\xfe\xca\xb9\xd5,\xf3\x91\x04\xe4\xa3\x86Q\xd8\xa8V\xe1~o\x916\xeb~\xcb\x7f\xf0O?\x87\xbf\xb1\xdf\xc4\x1f\x16x\x87\xc1+\xad[O\xe3;K;]B\xde\xea\xf0\\\xc6\xcdo\xe6\x1f?{/\x9c\xf3J\xd2\xbb\xc8\xf2H\xe5\x98\xf1\xb4q^\xe7E+%\x1eU\xb6\xbf\x8e\xff\x00}\xd8K\xde\xf8\xbc\xbf\x0b[\xee\xb2>T_\xf8$W\x814\xef\xd9\xd7\xc2\xff\x00\x0eto\x1b\xfcZ\xf0\xc4\x1e\x10\xba\xbf\xb8\xb0\xd74O\x10\xa6\x9f\xac\x14\xbd\x90\xc9so$\x91\xc2"x\\\xed\xf9L]\x11y\xeb\x9fe\xf8!\xfb(\xf8\x17\xf6~\xfd\x9d\xac\xbe\x15\xe8\x1a,M\xe0\xab[)\xacd\xb1\xbe?j\x17\xc96\xe3?\x9f\xbf\x872\x17r\xc0\x8d\xbf1\x00\x01\x80=\x1a\x8aoU$\xf6\x96\xfe}\x06\xdbrS{\xab\xb5\xea\xdd\xdf\xe2|qo\xff\x00\x04K\xf8og\xa6\xb7\x87\xe1\xf1\xf7\xc7\x08>\x1bI9\x96O\x00\xc7\xe39W\xc3\x92FN\xe6\xb71\x84\xf3\xfc\xa2y+\xe7g<\xe75\xee\xdf\x1e?co\x87\xbf\xb4_\xec\xe4\xff\x00\n\xb5\xfd\n(\xbc\x18\xb6\xf0[\xd9\xdai\xe7\xec\xa7K\xf2\x00\x105\xb9^#1\xe0m\xe0\x8cpARA\xf5\x1a(z\xaeW\xe4\xfekg\xea\xbav\xe8\t\xda\\\xeb\x7f\xf3\xdf\xef\xeb\xdf\xa9\xf25\xb7\xfc\x11\xab\xe1\xd5\xed\xef\x87u/\x11x\xd3\xe2\xdf\x8e<G\xe1MZ\xcbT\xd2\xb5\xcf\x13x\x8du+\xeb%\xb5\x91dKH\xf7\xc5\xe5G\x03\xb2)\x93dk#\xed\x19\x92\xbd\xb2\xf3\xf6T\xf0\xf5\xf7\xedwg\xf1\xa1\xaf5\x91\xe2\x8b/\x0c7\x84\xd2\xd4K\x17\xd8\r\xab\\\x1b\x82\xe5<\xbf3\xcd\xdeq\x9f3n?\x87<\xd7\xa6\xd1MI\xab[\xa3o\xe6\xd5\x9f\xde\xb7\xff\x002l\xac\xd7{/\xb9\xdd}\xcc\xf3O\x8e\x1f\xb2\xbf\x87\xfe>\xfcI\xf8q\xe2\x8db\xf3Y\xb6\xd4>\x17\xea\xef\xadiQ\xd9\xcb\x1aCq3\xc7\xe5\x95\x9c4lY1\xd9\n\x1c\xf7\xaa\xdf\xb6G\xecu\xe0\xcf\xdb\xa3\xe0}\xe7\x80\xbcs\x05\xebiW3\xc7w\r\xcd\x8c\xab\x15\xe5\x85\xc4y\xdb4.\xca\xca\x1c\x06e\xf9\x95\x81W`A\xcdz\xa5\x15\x0e\x11q\xe5kK\xdf\xe7\xa6\xbf\x82\xfb\x8aRj\\\xcb{[\xe5\xae\x9f\x8b\xfb\xcf\x06\xf1o\xfc\x13\xc3\xc1~*\xfd\x9f\xbc\t\xf0\xfe=k\xc7z\x12|6\xb2\x8e\xcb\xc3\xfa\xfe\x89\xae\xc9\xa6\xebvA \x10\x97\xf3\xe1\n\xac\xce\xa0n\x056\x12\x07\xca0\x05d|\x13\xff\x00\x82a\xf8+\xe1G\xc6+\x0f\x88\x1a\xef\x8a~%\xfcU\xf1\x96\x88\xae\x9a6\xa9\xe3\xaf\x10\x1dQ\xf4Eu\xda\xe2\xda5H\xe2M\xc3\xbe\xc2s\xc8 \xd7\xd2\x14U\xdd\xfbGW\xed=o\xe7\xdf\xd4\x9eU\xc8\xa9\xf4_\x97c\x8c\xfd\xa1\xbe\x07i?\xb4\xb7\xc1\x0f\x13\xf8\x07]\xb8\xd4m4\x7f\x15\xd8I\xa7]\xcda"Gs\x1co\xd4\xc6\xce\x8e\xa1\xbe\xaaG\xb5h\xf8G\xe1\x8e\x97\xe1\x1f\x85\x1ag\x83\x02>\xa1\xa2i\x9aLZ(K\xcd\xb25\xcd\xbcp\x88q.\x00V,\x83\xe6\xc0\x00\xe4\xf0:WEEM\x93N/iZ\xfev\xbd\xbf7\xf7\x8f\xaa\x97U{|\xed\x7f\xc9}\xc7\xc7W_\xf0E\x1f\x877\xde\x03\xbf\xf0\\\xde<\xf8\xd1/\xc3\x9b\x94\x9dm|\x1a\xfe*\xce\x8b\xa5\x992Q\xa1\x8f\xca\xf3\x1b\xc9r$\x8df\x92D\x0e\xaa\xcc\xad^\xa9\xf1\x07\xf6\x02\xf0w\xc4\x8f\xd9\x7f\xc0\xff\x00\t\xaf\xb5/\x13E\xe1\xcf\x00K\xa5K\xa7\xdc\xc1q\x02\xde\xcct\xe0\xa2\x0f5\x8c%\x0e\xed\xa3~\xd4\\\xf3\x8d\xb5\xee4U\xf3;[\xcd?\x9c]\xd3\xf5]\xc5\xca\xbbtk\xe5-\xd7\xa3<\xcb\xe2\xdf\xec\xa9\xe1\xef\x8c\xdf\x1d~\x19\xfcA\xd5/5\x985\x9f\x85S\xdfO\xa4\xc3k,Kkp\xd7p\xac2y\xea\xd1\xb30\n\xa0\xae\xc6L\x1c\xe7=(\xf8\xb7\xfb*x{\xe37\xc7_\x86\x7f\x10uK\xcdf\rg\xe1T\xf7\xd3\xe90\xda\xcb\x12\xda\xdc5\xdc+\x0c\x9ez\xb4l\xcc\x02\xa8+\xb1\x93\x079\xcfJ\xf4\xda*c\xee\xda\xdd\x1d\xd7\xab\xdc\xa6\xdb\xdf\xb5\xbeZ\xe9\xf8\xbf\xbc\xf9\xfb\xf6\x97\xff\x00\x82sxS\xf6\x92\xf8\xcb\xa6\xfcBO\x16\xfcJ\xf8y\xe3;\r0\xe8\xb3j\xde\x0b\xd7\xbf\xb2\xae5\x1b\x12\xe6Ao9(\xfb\x909,\n\xedl\xe3\x9f\x95v\xf6Z\xe7\xec\x9f\xe1\xef\x10~\xd3\xfe\x15\xf8\xb3=\xf6\xb9\xff\x00\t\x1f\x844;\x9d\x02\xce\x01q\x19\xb3\x9a\t\xd83\xbc\xa0\xc6di28"@=A\xafO\xa2\x88\xfb\xb6K\xa5\xda\xf9\xa6\x9f\xdfw\xf7\xb1K\xdew\x97\x97\xe1f\xbe\xeb/\xb9\x1eg\xfbX\xfe\xca\xde\x1e\xfd\xb1\xbe\x12\xff\x00\xc2\x1b\xe2k\xcdf\xc7L\xfe\xd1\xb4\xd4\xfc\xdd.X\xe2\x9f\xcc\xb6\x95eA\x99#\x91v\x96Q\x91\xb78\xe8GZ\xec\xbe"x\xd6?\x87\x1e\x05\xd5u\xe9\xb4\xedgV\x8fI\xb6{\x96\xb2\xd2,d\xbe\xbe\xba\xda3\xb2\x18\x10\x16\x91\xcf@\xa2\xb6\xa8\xa5\xaa\x8b\x8c}~vJ\xff\x00r_pi\xcd\xcc\xfd>Wn\xdf\x8b\xfb\xcf\x95\x7f\xe0\x90\xdf\x0c\xfcC\xe0O\xd9\xdf\xc5\x9a\xbf\x89|7\xabxN\xf7\xc7\xfe;\xd6\xbcUo\xa5\xea\xb0\x98/\xed\xadng\x1eH\x9e#\xccRmNT\xf3\x82\x0fz\xfa\xaa\x8a*\x9b\xd1El\x92K\xd2)%\xf8!%f\xdfv\xdf\xcd\xb6\xdf\xe6\x14QE!\x85\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x05\x14Q@\x1f\xff\xd9'

# Convert binary data to image
image = Image.open(BytesIO(binary_data))

# Save image to file
image.save("image.png")