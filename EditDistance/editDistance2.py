def editDistance(str1, str2):
    
    length_str1 = len(str1)
    length_str2 = len(str2)
    
    dp = []
    for i in range(length_str1 + 1):
        dp.append([0]*(length_str2 + 1))
    
    for i in range(length_str1 + 1):
        for j in range(length_str2 + 1):
            if (i == 0):
                dp[i][j] = j
            elif (j == 0):
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
          
    return dp[i][j]
    
str1 = "sunday"
str2 = "saturday"

print(editDistance(str1, str2))
        