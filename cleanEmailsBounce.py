def clean():
    content = open("emailsBounce.csv", "r", encoding='utf8')
    emails = []
    for line in content:
        info = line.split()
        for i in range(len(info)):
            if "@" in info[i]:
                print(info[i])
                if info[i][-1] != ".":
                    emails.append(info[i])

    return emails
clean()
