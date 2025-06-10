# 주제
- MCP on AWS: Hands-on Lab

## 내용
- 데스크톱에 Python 기반 MCP 서버를 구축하고 Claude Desktop, Amazon Q Developer CLI, Smithery에서 제공하는 오픈소스 MCP 서버를 연동해 도구 호출 기능을 구현해 봅니다. 
- AWS CDK를 사용하여 MCP 서버를 AWS 환경에 배포하는 방법도 살펴봅니다.
- 참가자들은 실습을 위해 노트북을 필수로 지참하셔야 합니다.

## 일정
- 2025.06.04

## 메모
- HTTP + SEE vs Steamable HTTP (스터디 필요)
- 애플리케이션이 LLM에 컨텍스트를 제공하는 방법을 표준화하는 개방형 프로토콜
- [Anthropic 나무위키](https://namu.wiki/w/Anthropic)
- https://norahsakal.com/blog/mcp-vs-api-model-context-protocol-explained/
- MCP 가 등장 하기전에는 클라이언트에서 각 LLM 에 맞춰서 개발을 해야됬다 하지만 현재 MCP Server 를 개발하면 어떤 LLM 을 사용해도 제약이 없다.
- https://github.com/awslabs/mcp aws 가 제공해주는 MCP 서버 목록 (credentials 가 필요한게 있고 아닌게 잇다.)
- Notino 에 있는 데이터 나 google calendar 등 데이터 를 통해서 LLM 에 물어볼때 MCP 서버만 구성하면 프로토콜에 맞춰 사용할수있다. (?)
- tools 가 q 를 끌때 킬떄마다 신뢰하는지 여부를 물어보는거는 서버를 사용하는것을 사용자에게 위임하는거다.

### 실습1 MCP 에 대한 이해를 하고 MCP 서버와 연결 한다.
- weather 파이썬 애플리케이션을 로컬에 가상환경을 구성하여 사용한다.
- Smithery는 개발자가 AI 에이전트와 통신하도록 설계된 AI 네이티브 서비스를 찾고 배포할 수 있도록 지원하는 플랫폼입니다
  - 내가 직접 python 등으로 서버를 구성하고 사용해도 되고 Smithery에서 받아와서 사용할수있다.
  - 예를 들어 도커 대표 이미지만 사용하는게 아니라 Docker Hub 에서 특정 이미지를 찾아 쓰는 느낌
  - 개인이 만든 서비스 같은 경우는 데이터 를 조심해야한다.

### 실습2 MCP 환경을 AWS 에 올려서 각각 연결한다.
- 실습 1은 내 로컬에 호스트 애플리케이션을 통해서 사용하면된다.
- 하지만 팀으로 사용할때는 AWS 에 MCP 서버를 구성하고 원격으로 붙어서 사용할수있다.
- weather 파이썬 애플리케이션을 ECS 에 올려서 실습한다.
- oauth 를 사용하여 특정 사용자만 MCP 만 사용할수있게 구성할수있다.

### 실습3 우리만의 MCP 클라이언트와 MCP 서버를 연결한다.
- MCP 클라이언트를 만드는 이유는 cluade 등 AI 는 데이터를 가져가지 않는다고 하지만 믿을수가 없다.
- 그래서 우리가 클라이언트를 구성해서 사용하여 믿을수있는 사용자만 사용하게 하는식으로 한다.
- 그런 니즈를 가진 사람을 위한 실습
