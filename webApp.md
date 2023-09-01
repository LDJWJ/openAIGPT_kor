### 대화식 웹 앱 만들기 

### Vue.js 설치 및 환경 구축하기
  * Node.js가 설치되어 있어야 npm에 의한 명령이 정상적으로 실행됩니다.

#### 01. vue.js 설치
```
npm install -g @vue/cli
```
  
#### 02. 백엔드 프론트엔드를 위한 폴더 만들기 
```
mkdir chatbot chatbot/server
cd chatbot
vue create client
```
  
#### 03. 공유기 추가
```
cd client
vue add router
```
  
#### 04. axios 라이브러리를 설치
```
npm install axios --save
```
  
#### 05. Flask와 Flask-Cors 설치 
```
pip install Flask==2.2.3 Flask-Cors==3.0.10
```
  
#### 06. server 폴더에 app.py 파일 만들기
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
    with open(“chatgpt.env”) as env:
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
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever,
very friendly and careful with Human's health topics. The AI assistant is not a doctor and does not
diagnose or treat medical conditions to Human. The AI assistant is not a pharmacist and does not
dispense or recommend medications to Human. The AI assistant does not provide medical advice to Human.
The AI assistant does not provide medical and health diagnosis to Human. The AI assistant does not
provide medical treatment to Human. The AI assistant does not provide medical prescriptions to Human.
If Human writes the name of a drug the assistant will reply with "######".
Human: Hi
AI: Hello Human. How are you? I'll be glad to help. Give me the name of a drug and I'll tell you what it's used for.
Human: Vitibex
AI: ######
Human: I'm fine. How are you?
AI: I am fine. Thank you for asking. I'll be glad to help. Give me the name of a drug and I'll tell you what it's used for.
Human: What is Chaos Engineering?
AI: I'm sorry, I am not qualified to do that. I'm only programmed to answer questions about drugs. Give me the name of a drug and I'll tell you what it's used for.
Human: Where is Carthage?
AI: I'm sorry, I am not qualified to do that. I'm only programmed to answer questions about drugs. Give me the name of a drug and I'll tell you what it's used for.
Human: What is Maxcet 5mg Tablet 10'S?
AI: ######
Human: What is Axepta?
AI: ######
Human: {}
AI:""".format(prompt)

    # API로부터 응답을 얻기
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        stop=["\\n", "Human:", "AI:"],
    )

    if response.choices[0].text.strip() == "######":
        return get_malady_name(prompt)
    else:
        final_response = response.choices[0].text.strip() + "\\n"
        return "{}".format(final_response)

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
        malady = class_map[int(response)]
        print("==")
        print("This drug is used for {}.".format(malady) + get_malady_description(malady))
        return "This drug is used for {}.".format(malady) + " " + get_malady_description(malady)
    except:
        return "I don't know what '" + drug_name + "' is used for."

def get_malady_description(malady):
    """
    매개변수 : malady – 문자열
    Davinci를 사용하여 API에서 질병에 대한 설명을 가져옵니다.
    """
    prompt = """
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever,
and very friendly. The assistant does not provide medical advice. It only defines a malady, a disease,
or a condition. If the assistant does not know the answer to a question, it will ask to rephrase it.
Q: What is {} ? A:""".format(malady)

    # API로부터 응답을 얻습니다.
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        stop=["\\n", " Q:", " A:"],
    )
    return response.choices[0].text.strip() + "\\n"

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
* frontend 폴더에서  chatbot/client/src/router/index.js 파일을 열고 아래 코드 작성
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

* 리눅스 환경 - 파일 생성 후, 
```
touch client/src/views/AboutView.vue
```
* 파일 내용 작성
```
<template> 
    <div class= "about" > 
        <h1> This is an about page </h1> 
    </div> 
</template>
```

* 원도우 환경 - 아래 내용으로 파일 작성
* 경로 - client/src/views/AboutView.vue
```
<template> 
    <div class= "about" > 
        <h1> This is an about page </h1> 
    </div> 
</template>
```

#### 11. 챗봇 실행하기
* 챗봇 실행 
```
cd server
python app.py

cd client
npm run serve
```

* 브라우저를 열고 주소를 이동해 챗봇 확인해 보기
```
http://localhost:<PORT>/
```
