### 대화식 웹 앱 만들기 

### 로컬 컴퓨터에 작업 폴더하나 만들기
  * 이 폴더가 웹 앱을 구동하는 실제 디렉터리가 된다. 여기에서는 chatbot_medi를 생성
```
chatbot_medi 폴더 생성
```

### 사전 아나콘다 환경에 가상환경 구축하기
  * 아나콘다 설치 후, 가상환경에 설치할 때, 이 부분 추가.

<!-- HTML 주석도 사용할 수 있습니다 -->
<p align="center">
  <img src="https://ldjwj.github.io/openAIGPT_kor/image/ch11_01_anaconda.png" width="30%" />
</p>

```
conda create -n myChat python=3.11
conda activate myChat
```
 - conda create의 명령으로 myChat이라는 가상환경을 생성합니다.
 - conda activate의 명령으로 myChat의 가상환경을 활성화합니다.

### Vue.js 설치 및 환경 구축하기
  * Node.js가 설치되어 있어야 npm에 의한 명령이 정상적으로 실행됩니다.

#### 00. openai 설치
```
pip install openai
```
- ChatGPT API를 사용하기 위한 라이브러리 openai를 설치합니다.

#### 01. vue.js 설치
```
npm install -g @vue/cli
```
- Node.js의 패키지 관리자인 npm을 사용하여 Vue.js의 공식 CLI(명령줄 인터페이스)를 전역적으로 설치합니다.

#### 02. 백엔드 프론트엔드를 위한 폴더 만들기 
```
mkdir chatbot_medi\server
cd chatbot_medi
vue create client
```
 - mkdir chatbot_medi\server : 위에서 생성한 chatbot_medi 폴더 안에 server를 생성합니다.
 - cd chatbot_medi : 해당 폴더로 이동합니다.
 - vue create client 명령어는 Vue.js의 공식 CLI(Command Line Interface)를 사용하여 'client'라는 이름의 새 Vue.js 프로젝트를 생성합니다.

* 설치 메뉴
```
Vue CLI v5.0.8
? Please pick a preset: (Use arrow keys)
> Default ([Vue 3] babel, eslint)
  Default ([Vue 2] babel, eslint)
  Manually select features
```
 - 어떤 버전을 설치할지 물어봅니다. 저희는 기본으로 Vue 3을 선택하고 설치를 진행합니다.
 -  Babel은 최신 JavaScript 코드를 오래된 브라우저에서도 실행될 수 있도록 변환해주는 도구이며, ESLint는 코드의 문법적 오류나 스타일 문제를 찾아주는 도구입니다. 이 옵션은 Vue 3를 사용하려는 대부분의 현대적인 프로젝트에 적합합니다.
 -  Manually select features: 이 옵션을 선택하면 사용자가 프로젝트에 포함시킬 기능을 직접 선택할 수 있습니다. Vue 버전, CSS 전처리기, 라우터, 상태 관리 시스템 (Vuex), linter / formatter 설정, unit testing, e2e testing 도구 등을 포함할지 여부를 사용자가 결정할 수 있습니다. 
  
#### 03. 공유기 추가
```
cd client
vue add router
```
- 'vue add router'명령은 Vue CLI를 통해 기존 Vue.js 프로젝트에 Vue Router를 추가하는 과정입니다. Vue Router는 Vue.js 애플리케이션에서 페이지 라우팅을 구현하는 데 사용되는 공식 라이브러리입니다. 이 명령어를 사용하면 프로젝트에 Vue Router가 자동으로 설치되고, 기본적인 라우팅 설정이 프로젝트에 추가됩니다.

```
? Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n) [Y 선택]
```
- Vue CLI가 Vue Router를 프로젝트에 추가할 때 'history' 모드를 사용할지 여부를 묻는 것입니다. 이 선택은 Vue Router에서 사용할 URL 스타일을 결정합니다.
- History Mode: 'history' 모드를 사용하면, URL에서 # (해시)가 제거됩니다. 이는 더 깔끔하고 전통적인 URL 구조를 제공합니다. 예를 들어, http://example.com/about와 같은 형식입니다. 그러나 이 모드를 사용하려면 웹 서버가 올바르게 설정되어야 합니다. 특히, 사용자가 직접 URL을 입력하거나 새로고침할 때 404 오류가 발생하지 않도록 모든 요청을 index.html로 리디렉션하는 설정이 필요합니다.

#### 04. axios 라이브러리를 설치
```
npm install axios --save
```
- 'npm install axios --save 명령어는 Node.js 프로젝트에 axios라는 HTTP 클라이언트 라이브러리를 설치하고, 이 의존성을 프로젝트의 package.json 파일에 저장


#### 05. Flask와 Flask-Cors 설치 
```
pip install Flask==2.2.3 Flask-Cors==3.0.10
```
- 이 부분은 Flask 웹 프레임워크의 특정 버전인 2.2.3을 설치하도록 지정합니다. Flask는 Python에서 가장 인기 있는 웹 프레임워크 중 하나로, 웹 애플리케이션을 구축하는 데 사용됩니다.
- Flask-Cors==3.0.10: Flask-Cors는 Flask 애플리케이션에서 Cross-Origin Resource Sharing (CORS)를 다루는 데 사용되는 확장입니다. CORS는 웹 페이지가 다른 도메인의 리소스에 접근할 수 있도록 허용하는 보안 메커니즘입니다. 이는 버전 3.0.10을 설치하도록 지정합니다.


#### 06. server 폴더에 app.py 파일 만들기
- server폴더로 이동하기
- server폴더 위치가 'c:\user\chatbot_medi\server'의 경우

* 폴더 이동
'''
cd c:\user\chatbot_medi\server
'''

* app.py 파일 생성
```
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import openai

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def init_api():
    with open("chatgpt.env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value
    openai.api_key = os.environ.get("API_KEY")
    openai.organization = os.environ.get("ORG_ID")

init_api()

def regular_discussion(prompt):
    """
    params: prompt - a string
Davinci를 사용하여 API로부터 응답을 반환합니다. 사용자가 약명에 대해 묻는 경우, get_malady_name() 함수를 호출합니다.
    """
    prompt = """

	다음은 AI 비서와의 대화입니다. 이 비서는 유용하고, 창의적이며, 영리하고, 매우 친절하며 인간의 건강 주제에 대해 주의를 기울입니다.
	AI 비서는 의사가 아니며 인간에게 의학적 상태를 진단하거나 치료하지 않습니다.
	AI 비서는 약사가 아니며 인간에게 약을 조제하거나 추천하지 않습니다.
	AI 비서는 인간에게 의학적 조언을 제공하지 않습니다.
	AI 비서는 인간에게 의학 및 건강 진단을 제공하지 않습니다.
	AI 비서는 인간에게 의학적 치료를 제공하지 않습니다.
	AI 비서는 인간에게 의학적 처방을 제공하지 않습니다.
	사용자가 약물의 이름을 쓰면, 비서는 "######"으로 답할 것입니다.
	User: 안녕하세요.
	AI: 안녕하세요, 사용자님. 어떠신가요? 도와드릴게요. 약물의 이름을 말씀해 주시면 그것이 무엇에 사용되는지 알려드리겠습니다.
	User: Vitibex
	AI: ######
	User: 저는 괜찮아요. 당신은 어떠세요?
	AI: 저는 괜찮습니다. 물어봐 주셔서 감사합니다. 도와드릴게요. 약물의 이름을 말씀해 주시면 그것이 무엇에 사용되는지 알려드리겠습니다.
	User: 카오스 엔지니어링이 무엇인가요?
	AI: 죄송합니다, 그것을 말할 자격이 없습니다. 저는 약물에 대한 질문에만 답하는 것으로 프로그래밍되었습니다. 약물의 이름을 말씀해 주시면 그것이 무엇에 사용되는지 알려드리겠습니다.
	User: 카르타고는 어디에 있나요?
	AI: 죄송합니다, 그것을 말할 자격이 없습니다. 저는 약물에 대한 질문에만 답하는 것으로 프로그래밍되었습니다. 약물의 이름을 말씀해 주시면 그것이 무엇에 사용되는지 알려드리겠습니다.
	User: Maxcet 5mg Tablet 10'S는 무엇인가요?
	AI: ######
	User: ACGEL CL NANO Gel 15gm는 무엇인가요?
	AI: ######
	User: Axepta는 무엇인가요?
	AI: ######
 	User: ALAN Gel 15gm는 무엇인가요?
	AI: ######        
    User: {} 
    AI:
    """.format(prompt)

    # API에서 응답 얻기
    next = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ],
    temperature=0,
    max_tokens=256,
    stop = [ " \n " , " User:" , " AI:" ],
    )

    if next.choices[0].message.content.strip() == "######": 
        return get_malady_name(prompt)
    else: 
        final_response = next.choices[0].message.content + " \n " 
        return("{}".format(final_response))

def get_malady_name(drug_name):
    """
    params: drug_name - a string
    Fine-tuned 모델에서 약 이름에 해당하는 질병 이름을 반환합니다.
    이 함수는 get_malady_description() 함수를 호출하여 질병에 대한 설명을 얻습니다.
    """
# 모델 ID 설정. 여기서는 모델 ID를 변경해 주세요.
    model = " ada:ft-personal:drug-data-2023-08-15-09-58-51"
    class_map = {
        0: "Acne",
        1: "Adhd",
        2: "Allergies",
        # ...
    }

    # 각 약물에 대한 클래스를 반환
    prompt = "Drug: {}\\nMalady:".format(drug_name)
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=1,
    )
    response = response.choices[0].text.strip()

    try: 
        malady = class_map[ int(next)] 
        print("==")
        print ( "AI: 이 약물은 {} 에 사용되고 있어요.".format(malady) + get_malady_description(malady))
        return "AI: 이 약물은 {} 에 사용되고 있어요.".format(malady) + get_malady_description(malady) 
    except:  
        return "AI: 저도 '" + drug_name + "' 이 어디에 사용되는지 모르겠어요."
       
def get_malady_description(malady):
    """
    매개변수 : malady – 문자열
    Davinci를 사용하여 API에서 질병에 대한 설명을 가져옵니다.
    """
    prompt = """
    다음은 AI 비서와의 대화입니다.
    이 비서는 유용하고, 창의적이며, 영리하고, 매우 친절합니다.
    비서는 의학적 조언을 제공하지 않습니다.
    비서는 병, 질병 또는 상태를 정의하는 데에만 집중합니다.
    비서가 질문에 대한 답을 모를 경우, 다시 표현해달라고 요청할 것입니다.
    Q: {}는 무엇입니까?
    A:""".format(malady)

    # API로부터 응답을 얻습니다.
    next = client.chat.completions.create(
        model="gpt-3.5-turbo" ,
        messages=[
          {"role": "user", "content": prompt}
        ],
        temperature = 1,
        max_tokens = 256,
        stop = [ " \n " , " Q:" , " A:" ]
    )
    
    return next.choices[0].message.content.strip() + "\n"

@app.route('/', methods=['GET'])
def reply():
    m = request.args.get('m')
    chatbot = regular_discussion(m)
    print("chatbot: ", chatbot)
    return jsonify({'m': chatbot})

if __name__ == '__main__':
    app.run()
```

#### 07. server 폴더에 .env 파일 생성
```
API_KEY=sk-xxxx
ORG_ID=org-xxx #optional
```

#### 08. 프론트엔드 폴더에 index.js 파일 생성
* frontend 폴더에서  chatbot_medi/client/src/router/index.js 파일을 열고 아래 코드 작성
```
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

```

#### 09. HomeView.vue 파일 생성
* client/src/views에서 HomeView.vue 파일을 만들고 아래 코드를 추가
* 내용 : Vue.js를 사용하여 간단한 메시징 인터페이스를 구현했습니다. 주요 기능은 사용자의 메시지를 입력 받고, 그 메시지를 서버로 보낸 다음, 서버의 응답을 화면에 표시합니다.

```
<template>
    <div>
        <h2>DrugBot</h2>
        <div v-if="messages.length">
            <div v-for="message in messages" :key="message.id">
                <strong>{{ message.author }}:</strong> {{ message.text }}
            </div>
        </div>
        <form @submit.prevent="sendMessage">
            <input type="text" v-model="newMessage" placeholder="Type your message">
            <button type="submit">Send</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            messages: [
                {
                    id: 1,
                    author: "AI",
                    text: "Hi, how can I help you?"
                },
            ],
            newMessage: "",
        };
    },
    methods: {
        sendMessage() {
            if (this.newMessage.trim() === "") {
                return;
            }
            this.messages.push({
                id: this.messages.length + 1,
                author: "Human",
                text: this.newMessage.trim(),
            });

            const messageText = this.newMessage.trim();
            axios.get(`http://127.0.0.1:5000/?m=${encodeURI(messageText)}`)
                .then(response => {
                    const message = {
                        id: this.messages.length + 1,
                        author: "AI",
                        text: response.data.m
                    };
                    this.messages.push(message);
                })
                .catch(error => {
                    console.error(error);
                    this.messages.push({
                        id: this.messages.length + 1,
                        author: "AI",
                        text: "I'm sorry, I don't understand.",
                    });
                });
            this.newMessage = "";
        },
    },
};
</script>
```

#### 10. AboutView.vue 파일 생성
* 파일 내용 작성
* 경로 - client/src/views/AboutView.vue
```
<template> 
    <div class= "about" > 
        <h1> This is an about page </h1> 
    </div> 
</template>
```

#### 11. Python 기반의 웹 서버 실행
* 챗봇 실행 
```
cd server
python app.py
```

* 실행 결과
```
(myChat) C:\Users\user\chatbot_medi\server>python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 685-908-876
```

* 에러 발생시
* 에러 발생 1 : chatgpt.env부분을 불러올 때, "" 쌍따옴표를 문자를 이해못할때,
* 해결
```
with open("chatgpt.env") as env:
```

* 에러 발생 2 : chatgpt.env부분을 불러올 때, "" 쌍따옴표를 문자를 이해못할때,
* 에러 및 원인
```
ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (C:\Users\user\anaconda3\envs\myChat\Lib\site-packages\werkzeug\urls.py)
Flask가 werkzeug.urls에서 url_quote를 가져오려고 시도했으나 실패했습니다. 이는 일반적으로 Flask 또는 Werkzeug 버전 간의 호환성 문제로 발생
```

* 해결 방법1
* 내용 : 최신 버전으로 업데이트합니다. 특정 버전을 설치해야 한다면 pip install flask==x.x.x werkzeug==y.y.y 형식으로 설치하세요.
```
pip install --upgrade flask werkzeug
```

#### 12. Vue.js 프로젝트를 로컬 개발 서버에서 실행
* 맨처음 실행했던 anaconda prompt를 새롭게 하나 실행 후, 아래 명령으로 실행합니다.
* client 폴더로 이동
```
cd chatbot_medi\client
npm run serve
```
- Vue.js 프로젝트를 로컬 개발 서버에서 실행하기 위해 사용합니다.

* 실행 결과
```
 DONE  Compiled successfully in 4341ms                                                                     오후 12:13:56


  App running at:
  - Local:   http://localhost:8080/
  - Network: http://192.168.120.122:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
```

#### 13. 브라우저에서 실행 확인
* 브라우저를 열고 앞에서 확인한 주소를 이동해 챗봇 확인해 보기
```
Local:   http://localhost:8080/
Network: http://192.168.120.122:8080/
```
