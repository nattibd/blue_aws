#Create an empty list
awslist = []

#Populate the list using append or insert
awslist.append('S3')
awslist.append('Lambda')
awslist.append('EC2')
awslist.append('DynamoDB')
awslist.append('RDS')
awslist.append('Cognito')
awslist.append('CloudFront')
awslist.append('EFS')
awslist.append('CodeBuild')
awslist.append('CloudTrail')
awslist.append('CodeStar')
awslist.append('Neptune')

#Print the list and the length of the list
print(awslist)
print(len(awslist))

#Remove two specific services from the list by name or by index
del awslist[7]
del awslist[10]

#Print the new list and the new length of the list
print(awslist)
print(len(awslist))
