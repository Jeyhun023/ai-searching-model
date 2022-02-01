from xml.dom import minidom
import csv
xmldoc = minidom.parse('/var/www/python/searching/Posts.xml')
itemlist = xmldoc.getElementsByTagName('row')
title = []
text = []
Id = []
PostTypeId = []
AcceptedAnswerId = []
CreationDate = []
Score = []
ViewCount = []
OwnerUserId = []
LastEditorUserId = []
LastEditorDisplayName = []
LastEditDate = []
LastActivityDate = []
Tags = []
AnswerCount = []
CommentCount = []
FavoriteCount = []
CommunityOwnedDate = []
ContentLicense = []
x = 0
for s in itemlist:
    if(s.attributes.get('Title') and s.attributes.get('Body') and s.attributes.get('PostTypeId') and x <= 200000):
        if( s.attributes['PostTypeId'].value == '1' ): 
            title.append( s.attributes['Title'].value )
            text.append( s.attributes['Body'].value )
            if(s.attributes.get('Id')):
                Id.append( s.attributes['Id'].value )
            else: 
                Id.append( " " )
            if(s.attributes.get('PostTypeId')):
                PostTypeId.append( s.attributes['PostTypeId'].value )
            else: 
                PostTypeId.append( " " )
            if(s.attributes.get('AcceptedAnswerId')):
                AcceptedAnswerId.append( s.attributes['AcceptedAnswerId'].value )
            else: 
                AcceptedAnswerId.append( " " )
            if(s.attributes.get('CreationDate')):
                CreationDate.append( s.attributes['CreationDate'].value )
            else: 
                CreationDate.append( " " )
            if(s.attributes.get('Score')):
                Score.append( s.attributes['Score'].value )
            else: 
                Score.append( " " )
            if(s.attributes.get('ViewCount')):
                ViewCount.append( s.attributes['ViewCount'].value )
            else: 
                ViewCount.append( " " )
            if(s.attributes.get('OwnerUserId')):
                OwnerUserId.append( s.attributes['OwnerUserId'].value )
            else: 
                OwnerUserId.append( " " )
            if(s.attributes.get('LastEditorUserId')):
                LastEditorUserId.append( s.attributes['LastEditorUserId'].value )
            else: 
                LastEditorUserId.append( " " )
            if(s.attributes.get('LastEditorDisplayName')):
                LastEditorDisplayName.append( s.attributes['LastEditorDisplayName'].value )
            else: 
                LastEditorDisplayName.append( " " )
            if(s.attributes.get('LastEditDate')):
                LastEditDate.append( s.attributes['LastEditDate'].value )
            else: 
                LastEditDate.append( " " )
            if(s.attributes.get('LastActivityDate')):
                LastActivityDate.append( s.attributes['LastActivityDate'].value )
            else: 
                LastActivityDate.append( " " )
            if(s.attributes.get('Tags')):
                Tags.append( s.attributes['Tags'].value )
            else: 
                Tags.append( " " )
            if(s.attributes.get('AnswerCount')):
                AnswerCount.append( s.attributes['AnswerCount'].value )
            else: 
                AnswerCount.append( " " )
            if(s.attributes.get('CommentCount')):
                CommentCount.append( s.attributes['CommentCount'].value )
            else: 
                CommentCount.append( " " )
            if(s.attributes.get('FavoriteCount')):
                FavoriteCount.append( s.attributes['FavoriteCount'].value )
            else: 
                FavoriteCount.append( " " )
            if(s.attributes.get('CommunityOwnedDate')):
                CommunityOwnedDate.append( s.attributes['CommunityOwnedDate'].value )
            else: 
                CommunityOwnedDate.append( " " )
            if(s.attributes.get('ContentLicense')):
                ContentLicense.append( s.attributes['ContentLicense'].value )
            else: 
                ContentLicense.append( " " )
            x = x + 1
with open('Posts.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Id','PostTypeId','Title','Body','AcceptedAnswerId','CreationDate','Score','ViewCount','OwnerUserId','LastEditorUserId','Score','ViewCount','OwnerUserId','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Tags','AnswerCount','CommentCount','FavoriteCount','CommunityOwnedDate','ContentLicense'])
    for x in range( len(title) ):
        writer.writerow([ Id[x], PostTypeId[x], title[x], text[x], AcceptedAnswerId[x], CreationDate[x],Score[x],ViewCount[x],OwnerUserId[x],LastEditorUserId[x],LastEditorDisplayName[x],LastEditDate[x],LastActivityDate[x],Tags[x],AnswerCount[x],CommentCount[x],FavoriteCount[x],CommunityOwnedDate[x],ContentLicense[x] ])
print(x)