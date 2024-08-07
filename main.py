from flask import Flask, request, jsonify
from requests import get
from user_agent import generate_user_agent
from re import findall

########## alEX WAS HERE ###########

class VSCode(Flask):
    def __init__(self, name):
        super().__init__(name)
        self.route('/alex/', methods=['GET'])(self.Download_Tool)

    def Download_Tool(self):
        query = str(request.args.get('title'))
        headers = {
            'User-Agent': generate_user_agent(),
            'Referer': 'https://www.youtube.com/'
        }
        
        query_result = get(f"https://www.youtube.com/results?search_query={query}", headers=headers).content.decode('utf-8')
        
        urls = findall(':{"videoId":"(.*?)","', str(query_result))
        titles = findall('"title":{"runs":\[{"text":"(.*?)"}],"accessibility"', str(query_result))

        # إعداد النتيجة الجديدة
        new_result = {"Urls": urls, "Title": titles, "by": "alEx"}
        
        # إرجاع النتيجة الجديدة
        return (new_result)

app = VSCode(__name__)
if __name__ == '__main__':
    app.run()
