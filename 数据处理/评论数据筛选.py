import csv,time
count=0
with open('美团评论汇总2.csv','r',encoding='utf-8') as op:
    reader = csv.reader(op)
    for rows in reader:
        if not rows[0] == '区域' and not rows[0] =='用户':
            if rows[1] == '1':
                count+=1
                #print(count)
count1=[count,count,count,count,count]
count2 = [0,0,0,0,0]
out = open('./清洗后美团评论2.csv', 'a', newline='', encoding='utf-8')
csv_write = csv.writer(out)
with open('美团评论汇总2.csv', 'r', encoding='utf-8') as op:
    reader = csv.reader(op)
    for rows in reader:
        if rows[0] =='区域':
            count2=[300,300,300,300,300]
        if not rows[0] == '区域' and not rows[0] =='用户' and  len(rows[2])>=9 and rows[2].find('号') ==-1:
            if rows[1] == '1' and count1[0]>=0 and count2[0]>=0:
                count1[0]-=1
                csv_write.writerow((rows[0],rows[1],rows[2]))
            elif rows[1] == '2'and count1[1]>=0 and count2[1]>=0:
                count1[1] -= 1
                count2[1] -= 1
                csv_write.writerow((rows[0], rows[1], rows[2]))
            elif rows[1] == '3'and count1[2]>=0 and count2[2]>=0:
                count1[2] -= 1
                count2[2] -= 1
                csv_write.writerow((rows[0], rows[1], rows[2]))
            elif rows[1] == '4'and count1[3]>=0 and count2[3] >= 0:
                count1[3] -= 1
                count2[3] -= 1
                csv_write.writerow((rows[0], rows[1], rows[2]))
            elif rows[1] == '5'and count1[4]>=0 and count2[4] >= 0:
                count1[4] -= 1
                count2[4] -= 1
                csv_write.writerow((rows[0], rows[1], rows[2]))
out.close()