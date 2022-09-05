# Transfomer

## Abstract
Transfomer란 2017년 구글에서 발표한 논문 'All attention is All you need'에서 나온 구조로 기존 구조를 따르면서도 발전시킨 모델로,  BERT, GPT-3, T5 등과 같은 아키텍처가 발전하는 기반이 마련한 모델이다.  
Machine translation 작업에 대한 실험 결과에 따르면, 이 모델은 병렬 처리가 가능하고 학습시간이 훨씬 덜 소요되며 WMT Englishto-German 번역 대회에서 28.4 BLEU를 달성하면서 기존 최고 모델보다 2 BLEU 이상 향상하며 SOTA를 달성함을 보여줬고 또한 다른 task에서도 잘 일반화됨을 보여준다.

## Introduction
<img src ='https://velog.velcdn.com/images%2Ftobigs-nlp%2Fpost%2F87d61430-3608-409e-b816-2f3b584e3651%2Fimage.png'>
위를 보면, 기존의 인코딩/디코딩 구조를 따르면서도 attention만을 사용하여 구현한 것을 확인할 수 있다.



<img src ='https://velog.velcdn.com/images%2Fguide333%2Fpost%2Ff1e8fe2a-2391-4d3e-8092-e2a17ef3eaea%2FScreenshot%20from%202021-04-15%2013-20-27.png'>
* 기존 구조의 경우.

<img src ='https://velog.velcdn.com/images%2Ftobigs-nlp%2Fpost%2F6c68245c-4175-4f62-b4cd-f05099c9fa73%2Fimage.png'>
두 구조를 비교를 해보면, sequential한 데이터 input이 들어왔을 때, transformer를 통과해서 ouput이 나오는데 RNN의 encoder-decoder 구조와 틀은 비슷하지만 transformer의 내부를 보면 encoding component와 decoding component가 존재하고 이 둘을 어떻게 연결시키는지가 다르다.

이외에도, 해당 논문에 자료와 함계 자세한 설명이 개제되어 있으나 간략하게만 정리하고 넘어가겠다.

## Model Architecture

### Encoder
총 6개의 stack으로 구성되어 있고, 하나의 인코더는 Self-Attention Layer와 Feed Forward Neural Network로 이루어져있으며 2개의 Sub-layer가 있다.  
이 때 인코더의 내부 구조를 보자. 
<img src ='https://miro.medium.com/max/1400/0*e_UzrRKgRYBP6bPY'>

Self-Attention Layer의 내부 구조는 다음과 같다.
<img src ='https://miro.medium.com/max/1370/0*s0dkdBvKmAz1MNd6'>

### Decoder
인코더의 가장 상단에 있는 출력은 key와 value 벡터로 바뀐다. 이 key, value 벡터가 decoder의 각 encoder-decoder attention layer에 사용된다.
<img src ='https://miro.medium.com/max/1400/0*qSQNPa9uImuf1vWR'>

다음 time-step에서는 decoder의 직전 output을 input으로 다시 받아, Decoder stacks를 거쳐 Linear+Softmax를 한 뒤, 다시 output을 뱉는 과정을 거친다.
<img src ='https://miro.medium.com/max/1400/0*xB9EX8ua0Gw-hNsP'>

