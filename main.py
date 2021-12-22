import time
import os

def is_yes(choice):
    return choice in ('Y', 'y')
def is_no(choice):
    return choice in ('N', 'n')

def make_file(filename):
    print("Đang tạo file " + filename + "...")
    file = open(filename, "w", encoding="utf8")
    file.close()
    time.sleep(1.5)
    print("Đã tạo!\n")

    time.sleep(0.5)
    path = os.getcwd()
    print("File được tạo nằm theo đường dẫn:\n" + path + "\\" + filename)
    time.sleep(0.5)
    print("----------------\n")

    return 0

def get_data(filename):
    imported = False
    while (imported != True):
        time.sleep(0.5)

        status = input("\nBạn nhập dữ liệu chưa (Y/N): ")
        if is_yes(status):
            imported = True
        elif is_no(status):
            print("Mời bạn nhập dữ liệu vào file!")
        else:
            print("Không hợp lệ!")

    print("Đang đọc từ file dữ liệu...")

    return open(filename, "r", encoding="utf8").read()

def tokenize(text):
    # Xóa kí tự đặc biệt và khoảng trắng
    for symbol in "()[]{},.;:?!\"“”'":
        text = text.replace(symbol, "")
    for space in ["\n", "\t", "\v", "\f", "\r", "  "]:
        text = text.replace(space, " ")
    text = text.lower()

    # Tách từ
    word_list = text.split(" ")
    return word_list
def word_count(word_list, sort=None):
    words_dict = {}

    #Count words
    for word in word_list:
        if word != "":
            words_dict[word] = word_list.count(word)

    #Sorted words_dict
    if sort.lower() == "ascending":
        words_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=False))
    elif sort.lower() == "descending":
        words_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))

    return words_dict

def run(words_dict):
    print("Danh sách hành động có thể lựa chọn:"
          "\n\t1. Thống kê top N từ được lặp lại nhiều nhất"
          "\n\t2. Tạo biểu đồ tần suất xuất hiện các từ trong văn bản"
          "\n\t3. Tìm nhóm câu văn có sự lặp từ"
          "\n\t4. Thêm các từ ngoại lệ"
          "\n\t5. Thoát")
    time.sleep(0.5)

    valid = False
    while (valid != True):
        action = input("Chọn hành động bạn muốn thực hiện: ")
        if action.isdigit() and int(action) in range(1,6):
            valid = True

    if action == "5":
        return action
    elif action == "1":
        flag = False
        while (flag != True):
            time.sleep(0.5)
            i = input("\nNhập N: ")
            if i == "*":
                N = len(words_dict)
                flag = True
            else:
                try:
                    N = int(i)
                    flag = True
                except ValueError:
                    print("Không hợp lệ!")
                    continue


        print("\nTOP " + str(N) + " TỪ ĐƯỢC LẶP LẠI NHIỀU NHẤT")
        print("\n+{:-^5}+{:-^15}+{:-^12}+".format("-", "-", "-"))
        print("|{:^5}|{:^15}|{:^12}|".format("STT", "Từ", "Số lần lặp"))
        print("|{:-^5}|{:-^15}|{:-^12}|".format("-", "-", "-"))

        num = 0
        for word in words_dict:
            num += 1
            print("|{:^5}|{:<15}|{:^12}|".format(str(num), " " + word, words_dict[word]))
            if num >= N:
                print("+{:-^5}+{:-^15}+{:-^12}+".format("-", "-", "-"))
                break
    elif action == "2":
        print("Tính năng đang được xây dựng. Vui lòng trở lại sau.")
    elif action == "3":
        print("Tính năng đang được xây dựng. Vui lòng trở lại sau.")
    elif action == "4":
        print("Tính năng đang được xây dựng. Vui lòng trở lại sau.")
    return action

if not os.path.exists("input.txt"):
    make_file("input.txt")
    time.sleep(0.5)
    print("Nhập văn bản cần đếm số từ vào file input.txt và lưu lại (Ctrl + S)")
else:
    print("Đã tồn tại file input.txt")
    flag = True
    while(flag):
        time.sleep(0.5)
        want_new = input("\nBạn có muốn tạo mới không (Y/N): ")
        if is_yes(want_new):
            make_file("input.txt")
            time.sleep(0.5)
            print("Nhập văn bản cần đếm số từ vào file input.txt và lưu lại (Ctrl + S)")
            flag = False
        elif is_no(want_new):
            flag = False
        else:
            print("Không hợp lệ!")

doc = get_data("input.txt")
time.sleep(1)
print("Đã đọc!\n")

time.sleep(0.5)
print("Đang xử lý...")

words_dict = word_count(tokenize(doc), "descending")

time.sleep(1)
print("Đã xử lý!")
time.sleep(0.5)
print("----------------\n")

running = True
while (running):
    action = run(words_dict)

    if (action != "5"):
        flag = False
    else:
        running = False
        flag = True
    while (flag != True):
        time.sleep(0.5)
        choice = input("\nBạn có muốn tiếp tục không (Y/N): ")
        if is_yes(choice):
            running = True
            flag = True
        elif is_no(choice):
            running = False
            flag = True
        else:
            print("Không hợp lệ!")

