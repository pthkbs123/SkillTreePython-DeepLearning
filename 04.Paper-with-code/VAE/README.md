# Auto-Encoding Variational Bayes

## Abstract
본 연구에서 확률적 변분추론(stochastic variational inference)과 대규모의 데이서셋에 대하여, mild한 미분가능성 조건하에 잘 작동할 수 있는 학습 알고리즘을 제안했다..
본 연구의 주된 기여 2가지는 다음과 같다.
1. Variational lower bound의 reparameterization를 통하여 표준적인 확률적 경사 기반 방법들(SGD 등)을 이용해 직접적으로 손쉽게 최적화할 수 있는 lower bound estimator를 얻을 수 있다.  
2. 연속형 잠재변수가 존재하는 iid 데이터셋에, 본 연구에서 제안하는 lower bound estimator를 사용한 intractable한 사후분포에 근사추론 모델을 피팅함으로써 효율적인 사후추론을 진행하는 것을 보였다.  

## Introduction
Variational Bayesian(VB) 접근은 다루기 힘든 사후분포를 갖는 잠재변수, 파라미터를 가진 유향확률모델에서 어떻게 효율적인 근사추론을 할 수 있을지에서 부터 시작된다. 흔히 사용되는 mean-field 접근은 그 자체도 intractable한 경우가 많은 '근사된 사후분포'의 기댓값에 대한 analytical solution을 요구한다.  

논문의 저자들은 variational lower bound의 reparameterization 트릭을 통해 어떻게 간단히 lower bound에 대한 미분가능한 비편향 추정량을 얻는지 보이는데, 얘를 SGVB(Stochastic Gradient Variational Bayes) 추정량이라고 부르며, SGVB는 연속형 잠재변수/파라미터를 갖는 거의 모든 모델에 사용될 수 있다고 한다. 또한, 표준적인 gradient ascent/descent 방법을 통해 직접 최적화가 가능하다고 하였고, 이 SGVB를 이용하여 목적함수의 최적화를 진행하는 알고리즘으로 AEVB(Auto-Encoding VB)를 제안했다.

## Method

메소드에는 크게 네 가지로, Problem scenario, The variational bound, The SGVB estimator and AEVB algorithm, The reparameterization trick가 있다.

### Problem scenario

데이터셋 X는 N개의 iid 샘플로 이루어져 있고, 데이터 x와 관측불가능한 연속형 잠재변수 z가 어떤 random process에 의해 생성된다고 가정한다.  
프로세스는 2단계로 이루어지는데,  
1. 잠재 변수 z가 어떤 Prior distribution pθ*로부터 생성된다.  
2. dataset xi 가 어떤 conditional distribution pθ*(x|z)로부터 생성된다.  
이 때 이 prior와 likelihood는 parametric한 distribution인 pθ(z) 와 pθ(x|z)로 나타낼수 있다고 생각하고, 이 pdf들은 θ나 z에 관해서 미분 가능하다고 생각하자.  

하지만 문제는 우리는 실제 parameter θ*를 모르고, latent variable z 또한 모른다. 본 연구에서는 marginal 분포, 사후분포에 대해 단순화하는 가정을 하지 않을 것이며, 오히려 현실의 복잡한 상황들에 대해서도 잘 일반화될 수 있는 알고리즘을 찾고자 하는 것 이다.  

본 연구에서 아래의 3가지 문제 상황에 대해 관심있었으며, 해답을 제시하고있다.

1. 파라미터 θ에 대한 효율적인 근사 ML, MAP 추정. 얘를 추정할 수 있다면 Hidden random process를 모방하여 실제를 닮은 인조 데이터를 생성하는게 가능하다
2. 모수 θ 하에 관측된 변수 x의 값이 주어졌을 때 잠재변수 z에 대한 효율적인 근사 사후추론(즉, pθ(z∣x)에 대한 추론). 이는 coding(데이터의 부호화)이나 representation task에 매후 유용할 것이다.
3. x에 대한 효율적인 marginal inference. 즉, 데이터의 마지널한 확률분포 P(X)에 대한 근사추론. 이는 x에 대한 사전분포가 요구되는 모든 추론 테스크에 사용될 수 있다.

위 문제를 해결하기 위해 z의 intractable한 실제 사후분포 pθ(z∣x)에 대한 근사분포인 qϕ(z∣x)를 도입한다.  
- qϕ(z∣x) : probabilistic Encoder - 데이터가 주어졌을 때 잠재표현 z의 모든 가능한 값에 대한 분포를 반환.  
- pθ(x∣z) : probabilistic Decoder - 잠재표현 z가 주어졌을 때 대응되는 x값들에 대한 분포를 반환.  

## The variational bound

x의 가능도는 아래와 같은 식으로 나타낼 수 있다.

<img src ='https://velog.velcdn.com/images%2Fchangdaeoh%2Fpost%2Fc10e401f-06d5-4c19-9e6d-91388be7f56e%2Fimage.png'>

DKL(qφ(z|x (i) )||pθ(z|x (i) )) 이 Term 은 항상 Nonnegative 이니까 식은 다음 식들과 같이 변하는데, 

<img src ='https://velog.velcdn.com/images%2Fchangdaeoh%2Fpost%2Ffb6d2181-f95f-4321-8972-acffc81840b6%2Fimage.png'>
여기서의 우변을 variational lower bound라고 부르고, 이 식을 다르게도 풀 수 있는데,

<img src ='https://velog.velcdn.com/images%2Fchangdaeoh%2Fpost%2F19cb6c10-632e-49a9-88b6-57715acdb71f%2Fimage.png'>

이 lower bound를 varaiational parameter 인 φ와 generative parameter인  θ에 대해서 모두 최적화 하고 싶은 것. 하지만 이 lower bound로 gradient 를 흘려보내 주는 것은 약간 문제가 있는데, 이런 경우에 일반적으로 사용하는 monte carlo gradient estimator는 분산이 커서 우리의 목적에는 실용적이지 않다고 한다. 

## The SGVB estimator and AEVB algorithm

최적화 하고 싶은 식은 2.2에서 찾았는데, 이제 이 식을 어떻게 optimize 할 건지 estimator 를 찾아야 한다. 2.4에서와 같은 mild한 조건이 있다면, posterior를 다음과 같이 reparameterize 할 수 있다. 

<img src ='https://velog.velcdn.com/images%2Fchangdaeoh%2Fpost%2F535378f3-13d9-483e-a9f1-828228d5968e%2Fimage.png'>

이제 z에 대한 어떤 함수 f(z)의 기대값의 몬테카를로 추정량은 다음과 같다.

<img src ='https://velog.velcdn.com/images%2Fchangdaeoh%2Fpost%2F87fb6f65-cd1e-4ea3-b7c6-2b52aa8ec86c%2Fimage.png'>

이 estimator를 variational lower bound에 적용하여, 우리의 일반적인, Stochastic Gradient Variational Bayes estimator를 만들어 낼 수 있는 것이다.

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcklwoI%2FbtqOqUcyitW%2FBlvsbTi8AOb1Zm3SJeZNJK%2Fimg.png'>

그런데 종종 Lower Bound에서 첫번째 term인 qϕ(z∣x)와 pθ(z)에 대한 KLD가 분석적으로 직접 구해지는 경우가 있음(부록B에 증명). 이 경우 MC 방법에 의한 근사를 LB의 두번째 term에 대해서만 사용하면 되어 추정량의 분산이 줄어들게 된다. 이런 방식의 두번째 SGVB 추정량은 다음과 같이 표현된다.

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdvaiiE%2FbtqOleXElVW%2FCaeOXe6h9iYwkUfOVMqKsK%2Fimg.png'>

N datapoint 를 가진 dataset X 가 주어진다면, 전체 dataset 에 대한 Lower bound 또한 구할 수 있다. 

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FD5BPy%2FbtqOnyuMkPY%2FNkbMdi3N6O66gmQH2afLik%2Fimg.png'>

이제 우리의 최적화대상인 LB에 대한 gradient가 구해질 수 있고 이것을 이용하는 확률적 최적화방법인 SGD와 그 변종 방법들이 모델 파라미터 업데이트에 이용될 수 있다. 전체 과정은 다음과 같다.

<img src ='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcB9Vu9%2FbtqOhOZI65O%2FgwO8CoBSudgRkXWrAIaKN1%2Fimg.png'>

## The reparametrization trick 
