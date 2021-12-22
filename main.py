import time
import os

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
        if action in [str(i) for i in range(0, 6)]:
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

def make_file():
    print("Đang tạo file input.txt...")
    file = open("input.txt", "w", encoding="utf8")
    file.close()
    time.sleep(1.5)
    print("Đã tạo!\n")

    time.sleep(0.5)
    path = os.getcwd()
    print("File được tạo nằm theo đường dẫn:\n" +
          path + "\input.txt")
    time.sleep(0.5)
    print("----------------\n")

    time.sleep(0.5)
    print("Nhập văn bản cần đếm số từ vào file input.txt và lưu lại (Ctrl + S)")

    return 0

def get_input():
    status = input("\nBạn nhập dữ liệu chưa (Y/N): ")
    if status in ('Y', 'y'):
        return True
    elif status in ('N', 'n'):
        print("Mời bạn nhập dữ liệu vào file!")
    else:
        print("Không hợp lệ!")
    return False



if not os.path.exists("input.txt"):
    make_file()
else:
    print("Đã tồn tại file input.txt")
    flag = True
    while(flag):
        time.sleep(0.5)
        isMade = input("\nBạn có muốn tạo mới không (Y/N): ")
        if isMade in ('Y', 'y'):
            make_file()
            flag = False
        elif isMade in ('N', 'n'):
            flag = False
        else:
            print("Không hợp lệ!")

status = False
while (status != True):
    time.sleep(0.5)
    status = get_input()

print("Đang đọc từ file dữ liệu...")
file = open("input.txt", "r", encoding="utf8")
doc = file.read()
time.sleep(1)
print("Đã đọc!\n")

time.sleep(0.5)
print("Đang xử lý...")
words_dict = {}

# Xóa kí tự đặc biệt và khoảng trắng
for symbol in "()[]{},.;:!\"“”":
    doc = doc.replace(symbol, "")
for space in ["\n", "\t", "\v", "\f", "\r", "  "]:
    doc = doc.replace(space, " ")
doc = doc.lower()

# Tách từ, đếm số lượng và sắp xếp
words = doc.split(" ")
for w in words:
    if w != "":
        words_dict[w] = words.count(w)
words_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))

time.sleep(1)
print("Đã xử lý!")
time.sleep(0.5)
print("----------------\n")

running = True
while (running):
    action = run(words_dict)
    # print(type(action))

    if (action != "5"):
        flag = False
    else:
        running = False
        flag = True
    while (flag != True):
        time.sleep(0.5)
        choose = input("\nBạn có muốn tiếp tục không (Y/N): ")
        if choose in ('Y', 'y'):
            running = True
            flag = True
        elif choose in ('N', 'n'):
            running = False
            flag = True
        else:
            print("Không hợp lệ!")

