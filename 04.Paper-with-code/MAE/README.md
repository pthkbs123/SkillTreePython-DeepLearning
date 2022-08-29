Masked Autoencoders Are Scalable Vision Learners (MAE)

AutoEncoder는 Encoder-Decoder 형태의 아키텍쳐이며, '좋은 인코더' 얻으려고 학습한다. 디코더를 통해 input을 복원하도록 loss를 학습시키면, 
핵심적인 시맨틱을 가지는 좋은 feature를 뽑는 구조를 이용하여 네트워크를 훈련한다. 

## Abstract
MAE의 접근 방법은 간단한데, 입력 이미지의 Patch를 임의로 골라서 마스킹 작업하고, 손실된 픽셀을 재구축하는 방식으로 학습을 진행한다.  
본 구조의 첫 번째 핵심 설계는, 비대칭 형태의 Encoder-Decoder 구조이다. Encoder는 Masking된 patch를 제외하고 Visible Patches만을 사용한다.  
두 번째 핵심 설계는, 높은 masking 비율이다. 본 논문에서는 효과적인 Self Supervisory Task를 수행하기 위해서 75%의 Mask Ratio를 가지고 있다. 너무 작은 Masking 비율을 둘 경우, Image의 각 픽셀은 
그다지 Semantic하지 않기 때문에 단순히 주변 영역을 보고 쉽게 추론할 수 있기 때문에 높은 Masking을 통해 학습을 진행한다.

