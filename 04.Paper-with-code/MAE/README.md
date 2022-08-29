Masked Autoencoders Are Scalable Vision Learners (MAE)

AutoEncoder는 Encoder-Decoder 형태의 아키텍쳐이며, '좋은 인코더' 얻으려고 학습한다. 디코더를 통해 input을 복원하도록 loss를 학습시키면, 
핵심적인 시맨틱을 가지는 좋은 feature를 뽑는 구조를 이용하여 네트워크를 훈련한다. 

## Abstract
MAE의 접근 방법은 간단한데, 입력 이미지의 Patch를 임의로 골라서 마스킹 작업하고, 손실된 픽셀을 재구축하는 방식으로 학습을 진행한다.  
  
본 구조의 첫 번째 핵심 설계는, 비대칭 형태의 Encoder-Decoder 구조로, Encoder는 Masking된 patch를 제외하고 Visible Patches만을 사용한다.  
  
두 번째 핵심 설계는, 높은 masking 비율이다. 본 논문에서는 효과적인 Self Supervisory Task를 수행하기 위해서 75%의 Mask Ratio를 가지고 있다. 너무 작은 Masking 비율을 둘 경우, Image의 각 픽셀은 
그다지 Semantic하지 않기 때문에 단순히 주변 영역을 보고 쉽게 추론할 수 있기 때문에 높은 Masking을 통해 학습을 진행한다.  

이러한 두가지 설계를 합쳐서 구현한 MAE는 3배 이상의 속도 향상을 이뤄냈고, 인코더의 입력 차원이 줄었으므로 정확도 또한 ImageNet 1K 데이터만으로 ViT-Huge에서 87.8%의 정확도를 얻어냈으며, 이는 기존 Supervised Learning 방식의 정확도보다 높다.  

## Introduction

### introduction: ViT (Vision Transformer)
이전에 CNN 구조(ResNet)을 배운 적이 있으나, 최근에는 조금 다른 방법을 사용한다. ViT는 CNN과 다르게 self-attention 모듈을 여러 block으로 쌓아서 표현력을 높이는 구조이다.

<img src ='(https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbbDpDH%2FbtroSsGRwqn%2FV9oXahTZpdQfbCOU3eWzF0%2Fimg.png)'>

CNN 기반 model과는 입력을 사용하는 방법에서 조금 차이가 있는데, Language에서 sequence의 sample 단위는 word token인데 이것을 일정 크기의 patch(16x16)으로 나눠서 입력에 사용한다.  
