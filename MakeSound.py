import numpy as np
from scipy.io import wavfile
import sys



def makeSound(name, freq, sec=1.0, rate=44100):
    # freq: 生成するsin波の周波数
    # sec: 生成する音の秒数
    # rate: 出力するwavファイルのサンプリング周波数(アナログ音をデジタル音に変換するための処理頻度)

    name = name + "(" + str(freq) + "Hz)" + ".wav"

    try:
        phases = np.cumsum(2.0 * np.pi * freq / rate * np.ones(int(rate * sec)))

        # 波形を生成
        wave = np.sin(phases)

        # 16bitのwavファイルに出力
        wave = (wave * float(2 ** 15 - 1)).astype(np.int16) # 値域を16bitにする
        wavfile.write(name, rate, wave)
    except ZeroDivisionError:
        print("ZeroDivisionError: 変数rateが0である可能性があります")
    except ValueError:
        print("ValueError: 入力値に誤りがあります")
    else:
        print(f"{name}が正常に出力されました")



# 実行
freq = input("生成するsin波の周波数を入力(float) =>")
if (freq == ""):
    sys.exit()
freq = float(freq)

sec = input("生成する音の秒数を入力(default:1.0, float) =>")
if (sec == ""):
    sec = 1.0
else:
    sec = float(sec)

rate = input("出力するwavファイルのサンプリング周波数を入力(default:44100, float) =>")
if (rate == ""):
    rate = 44100
else:
    rate = float(rate)

name = input("出力するwavファイルの名前を入力 =>")
if (name == ""):
    name = "名無し"

if __name__ == "__main__":
    makeSound(name, freq, sec, rate)
