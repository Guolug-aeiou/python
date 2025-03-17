def vocab():
    # 初始化生词本数据结构
    words_set = set()
    word_dict = {}

    while True:
        print("欢迎使用生词本")
        print("1.查看生词本")
        print("2.背单词")
        print("3.添加新单词")
        print("4.删除单词")
        print("5.清空生词本")
        print("6.退出生词本")
        try:
            choice = int(input("\n请输入功能编号："))
        except ValueError:
            print("请输入有效的数字选项")
            continue
        print("="*20)
        if choice == 1:
            # 查看生词本
            if not word_dict:
                print("生词本内容为空")
            else:
                print(word_dict)
            print("="*20)
        elif choice == 2:
            # 背单词
            if not word_dict:
                print("生词本内容为空")
            else:
                for word in word_dict:
                    user_trans = input(f"请输入{word}的翻译：")
                    if user_trans == word_dict[word]:
                        print("太棒了")
                    else:
                        print("再想想")
            print("="*20)
        elif choice == 3:
            # 添加新单词
            new_word = input("请输入新单词：").strip()
            if new_word in words_set:
                print("此单词已存在")
            else:
                translation = input("请输入单词翻译：").strip()
                words_set.add(new_word)
                word_dict[new_word] = translation
                print("单词添加成功")
            print("="*20)

        elif choice == 4:
            # 删除单词
            if not word_dict:
                print("生词本内容为空")
            else:
                print(word_dict)
                del_word = input("请输入要删除的单词：").strip()
                if del_word in words_set:
                    words_set.remove(del_word)
                    del word_dict[del_word]
                    print("删除成功")
                else:
                    print("删除的单词不存在")
            print("="*20)

        elif choice == 5:
            # 清空生词本
            if not word_dict:
                print("生词本为空")
            else:
                words_set.clear()
                word_dict.clear()
                print("生词本清空成功")
            print("="*20)

        elif choice == 6:
            # 退出
            print("退出成功")
            break
        else:
            print("无效的选项，请重新输入")
            print("="*20)

if '__main__' == __name__:
    vocab()
