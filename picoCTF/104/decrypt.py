flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"

ans = "".join([chr((int(hex(ord(flag[i]))[j : j + 2], 16))) for i in range(len(flag)) for j in range(2, 5, 2)])
print(ans)
