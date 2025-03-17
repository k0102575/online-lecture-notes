# 주제
- AWS Network Firewall, 이제는 써봐야하지 않을까요

## 내용 
- 나날이 발전하는 AWS 네트워킹 기능과 더불어 AWS 자원을 보호하기 위한 AWS Network Firewall 서비스의 기능도 빠르게 좋아지고 있습니다. 이 세션에서는 금융 고객을 포함한 여러 영역에서 사용하고 계시는 AWS Network Firewall 의 주요 기능에 대한 설명과 함께 AWS Network Firewall 을 사용할 때 권장하는 주요 설정들에 대해 공유 드립니다. 아래는 이번 세션에서 다루게 될 주요 내용입니다.
  - AWS Network Firewall Deployment 구성 별 고려 사항
  - Stateful Rule Group 적용 팁
  - AWS Network Firewall 주요 모범 사례
  - AWS Network Firewall 모니터링 방안

## 일정
- 2024.12.03

## 메모
- Gateway Load Balancer
  - Network Firewall 을 사용하면 내부적으로 Gateway Load Balancer 를 사용중이다 그래서 Gateway Load Balancer 개념을 알고가자
  - 출발지 => GWLB Endpoint => GWLB => Firewall => GWLB => GWLB Endpoint => 목적지 (Endpoint 라우팅 세팅이 필요하다)
  - Gateway Load Banlancer는 주요목적이 트래픽 보안 을 위하여 사용된다.

- ANF 구성
  - ALB, ELB 보다 장점은 Transparent 하다?
    - 출발지, 목적지 IP 가 바뀌지 않는다
  - ANF 를 사용하면 AWS 에서 모든걸 관리한다 (내부 EC2 크기 및 위치 등)
  - 단일 Firewall 을 사용하면 외부로 나가는 아이피가 NAT 를 경유하려 소스가 1개로 보일수밖에없다 그러면 Firewall 을 2개로 구성한다. (단일 VPC 이미지 2번 참조)
  - ANF 는 멀티 엔드 포인트를 지원하지 않는다 그래서 필요에따라 갯수를 늘려야된다.

- ANF 엔진
  - Stateless Rule 엔진 에서 룰에 맞춰 검사를 하고 Stateful 엔진으로 넘어간다 (아무런 룰을 설정하지 않으면 기본적으로 Forward 만 있게 패싱된다.)
  - Stateful 엔진에서 Action Order 는 Pass, Drop, Reject, alert 4가지 규칙을 어떤순으로 하는지 정할수있다 하지만 권장하지 않는다.
  - Strict Order 는 룰을 위에서 아래로 검사한다 하고 생각하자 (가장 Firewall 스럽게 쓰는법)
  - Action Order 는 Default 가 PASS 다
  - Strict Order 는 Default 를 설정 할수있다.

- ANF 모범사례 (발표자료 참고 필요)
  - ANF 는 수리카타 엔진을 써서 IPS를 만들었다 라고 생각하면 이해하기 좋다.
  - Stateless 규칙 보다는 Stateful 규칙을 사용해라 
    - Stateless 는 로깅이 지원 안된다. 단 Stateful 도 Pass 는 로깅이 남지 않는다.
  - 적은수의 규칙 그룹을 사용하자
    - 가독성 향상 및 상용 되는 규칙 에 대한 검사가 용이 하다
  - $HOME_NET 변수
    - 기본적으로 생성되었을떄의 VPC 를 잡지만 따로 설정할수있다. 환경에 따라 바꾸거나 하자
  - 허용 트래픽에 대한 로깅을 위해 Alert 규칙 사용
    - Pass 는 로깅을 하지 않는다, alert 는 로깅일뿐 pass 하지 않는다. 그래서 pass 규칙 위에 똑같은 alert 규칙을 위에 적용해서 alert, pass 둘다 적용될수있게 해야한다.
  - 로깅 및 모니터링 설정
    - CloudWatch Contributor Insights에서 확인하면 좋다.
  - 비용 최적화
    - 불필요한 트래픽을 라우팅 테이블을 설정하여 적절하게 예외 처리 하자
    - S3 와 DynamoDB 와 같은 트래픽 통신은 VPC Endpoint 를 활용하여 경유하지 않게 하여 구성하자
    - ANF 는 시간당 과금, 트래픽당 과금 이 발생한다.
      - 개인 계정에 세팅하고 아무것도 안해도 백만원정도 날아간다.

- 기타
  - 수리카타는 이해했다고 생각되면 이해를 못한거다