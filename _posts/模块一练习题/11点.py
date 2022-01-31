import random

fen_shu = {}
ren = ["alex", "吴佩琪", "张哥"]
pai = [("小王", 14), ("大王", 15)]
huase = ["♣", "♦", "♥", "♠"]
# 生成牌
for i in range(1, 14):
    for j in huase:
        ites = (j, i)
        pai.append(ites)
# 发牌+计算
for wanjia in ren:
    indox = random.randint(1, len(pai) - 1)
    poke = pai.pop(indox)
    fen = 0
    v1 = poke[1]
    if poke[1] > 10:
        v1 = 0.5
    fen += v1
    print(f"玩家{wanjia}抽的牌是{poke},总点数为{fen}")
    while True:
        a = input("还要牌吗Y/N")
        a = a.upper()
        if a == "N":
            print(f"{wanjia}结束")
            break
        if a not in {"N", "Y"}:
            print("输入错误重新要牌")
            continue
        indox = random.randint(1, len(pai) - 1)
        poke = pai.pop(indox)
        print(poke)
        v1 = poke[1]
        if poke[1] > 10:
            v1 = 0.5
        fen += v1
        print(f"玩家{wanjia}抽的牌是{poke},总点数为{fen}")

        if fen > 11:
            print(f"玩家{wanjia},牌爆了")
            fen = 0
            break
    fen_shu[wanjia] = fen
print(fen_shu)
