id_num = int(input('How many users? '))
eph_num = int(input('How many EphID per user? '))

cnt = 1
for i in range(1,id_num+1):
    for j in range(eph_num):
        eph=cnt
        print('{'+str(i)+','+str(eph)+'},')
        cnt += 1
