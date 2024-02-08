from readCompany import comp
from formatEmail import writeToExcel

# function to merge the emails
listCom = comp()

def read(email,profileContent):
    emailDic = {}
    profileDic = {}
    # changed the line number
    lineNum = 0
    lineNum2 = -1
    # Extract data from the profiel scrapped data 
    profileContent = open(profileContent,"r",encoding='utf8')

    for line in profileContent:
        info = line.replace('"','').replace(',','')
        info = info.split("!!")

        lineNum += 1
        if lineNum % 3 == 1:
            companyName = info[0][:-1]

        if lineNum % 3 == 0:
            for person in range(len(info)):
                profile = info[person].split("-")
                profileNameInfo = profile[0].split()
                try:
                    profileDesc = profile[1]
                    try:
                        if " Co" == profile[1]:
                            profileDesc = "Co-"+ profile[2]
                    except:
                        continue

                # print(profileNameInfo)
                # print(profile)

                    firstName = profileNameInfo[0]
                    lastName = profileNameInfo[1]
                    if lastName[-1] == ".":
                        lastName = lastName[:-1]
                    if firstName[-1] ==".":
                        firstName = firstName[:-1]

                    var = [firstName, lastName, profileDesc,companyName]
                    # A profile dictionary with key = company name, and the value being a list of the profile 
                    profileDic[companyName] = var

                except:
                    continue

     
    #Extract data from the company format data, and find the data of the email
    content = open(email, "r", encoding='utf8')

    for line in content:
        lineNum2 += 1

        if lineNum2 % 3 == 0:
                 #  find the company name
            companyName = line.replace(",","")
            companyName = companyName[:-1]

        if lineNum2 % 3 == 2:
            companyEmail = line.replace(",","")
            companyEmail = companyEmail.split("(")
            emailFormat = None

            if "The most common" in companyEmail[0]:
                # If it's the format one
                companyEmail = companyEmail[1].split(")")
                companyEmail[0] = companyEmail[0][4:]
                emailFormat = companyEmail[0]

            if "email formats: 1." in companyEmail[0]:

                companyEmail = companyEmail[0].split("1.")
                emailFormat = companyEmail[1].replace(' ', '').replace("'","")

            if [companyName,emailFormat] not in emailDic:
                # Email dictionary of company as key and email format 
                emailDic[companyName[1:]] = emailFormat

    print(emailDic)
    # Final list automatically checks the 2 dictionaries against each other, and writes to excel to save space complexity
    writeToExcel(emailDic,profileDic)

    return None