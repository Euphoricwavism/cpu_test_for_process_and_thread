# -*- coding: utf-8 -*-
import multiprocessing
import threading
import time
import sys

class sample_thread(object):
    def __call__(self,count,name):
        result = 0
        print(name + ":処理開始")
        start = time.time()
        for i in range(count):
            result += i
        elapsed_time = time.time() - start
        print(name + ":処理完了")
        print(name + ":処理時間:{0}[sec]".format(elapsed_time))

if __name__ == "__main__":
    argvs = sys.argv 
    argc = len(argvs)
    num_of_thread = multiprocessing.cpu_count()
    amount_of_calc = 150000000
    if (argc > 3):
        print("引数が多すぎます")
        quit()
    elif (argc == 2):
        try:
            num_of_thread = int(argvs[1])
            if (num_of_thread < 1):
                print("引数の数字は1以上で入力してください")
                quit()
            else:
                print("スレッド数は{0}で処理します".format(num_of_thread))
                print("int加算計算量はデフォルトの{0}回で処理します".format(amount_of_calc))
        except ValueError:
            print("引数は数字で入力してください")
            quit()
    elif (argc == 3):
        try:
            num_of_thread = int(argvs[1])
            amount_of_calc = int(argvs[2])
            if (num_of_thread < 1) or (amount_of_calc < 1):
                print("引数の数字は1以上で入力してください")
                quit()
            else:
                print("スレッド数は{0}で処理します".format(num_of_thread))
                print("int加算計算量は{0}回で処理します".format(amount_of_calc))
        except ValueError:
            print("引数は数字で入力してください")
            quit()
    else:
        print("スレッド数はCPU数と同じ{0}で処理します".format(num_of_thread))
        print("int加算計算量はデフォルトの{0}回で処理します".format(amount_of_calc))

    print("全体処理開始")
    start = time.time()

    test_thread = sample_thread()
    test_threads = []
    for i in range(num_of_thread):
        thread_name = "sample_thread" + str(i + 1)
        thread = threading.Thread(target=test_thread, args=(amount_of_calc,thread_name))
        thread.start()
        test_threads.append(thread)
    for thread in test_threads:
        thread.join()
    elapsed_time = time.time() - start
    print("全体処理完了")
    print("全体処理時間:{0}[sec]".format(elapsed_time))


