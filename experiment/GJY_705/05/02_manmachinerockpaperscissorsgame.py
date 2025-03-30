import random


class Player_base:
    def __init__(self):
        # 修正手势映射为0-2对应剪刀石头布
        self.dict_gesture = {0: '剪刀', 1: '石头', 2: '布'}

    def gesture(self, input_num):
        return self.dict_gesture.get(input_num, '无效输入')


class AIPlayer(Player_base):
    play_data = []  # 类属性存储玩家历史数据

    def ai_gesture(self):
        # 策略选择逻辑
        if len(AIPlayer.play_data) < 4:
            return random.randint(0, 2)
        else:
            # 统计玩家手势频率
            count = [0, 0, 0]
            for gesture in AIPlayer.play_data:
                count[gesture] += 1
            max_gesture = count.index(max(count))
            # 选择克制玩家最高频手势的策略
            return (max_gesture + 1) % 3  # 剪刀(0)→石头(1), 石头(1)→布(2), 布(2)→剪刀(0)


class Game(Player_base):
    def __init__(self):
        super().__init__()
        self.ai = AIPlayer()  # 创建AI玩家实例

    def game_judge(self):
        # 游戏判断逻辑
        while True:
            try:
                player_input = int(input("请输入手势（0-剪刀 1-石头 2-布）："))
                if player_input not in [0, 1, 2]:
                    raise ValueError
                break
            except:
                print("输入无效，请重新输入！")

        # 记录玩家出拳并获取双方手势
        AIPlayer.play_data.append(player_input)
        ai_choice = self.ai.ai_gesture()

        # 显示双方出拳
        print(f"玩家出：{self.gesture(player_input)}")
        print(f"电脑出：{self.gesture(ai_choice)}")

        # 胜负判断逻辑
        diff = (player_input - ai_choice) % 3
        if diff == 0:
            print("平局！")
        elif diff == 1:
            print("玩家获胜！")
        else:
            print("电脑获胜！")

    def main(self):
        # 主循环逻辑
        print("-----猜拳游戏开始-----")
        self.game_judge()
        while True:
            choice = input("\n是否继续游戏？（y/n）").lower()
            if choice == 'y':
                self.game_judge()
            elif choice == 'n':
                print("游戏结束！")
                break
            else:
                print("无效输入，请输入y或n！")


# 启动游戏
if __name__ == "__main__":
    game = Game()
    game.main()