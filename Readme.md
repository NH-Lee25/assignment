<h3>전시회 분류<br>
이나현, 경제금융학부, nabu98@naver.com </h3>
<hr></hr>

프로젝트 설명에 대한 유튜브 링크 <br>
https://www.youtube.com/watch?v=xalMH-ccysU <br>

※ 4:45의 신경망 -> 뉴런
<hr></hr>


<H3> I. Introduction <br>
- Motivation: Why are you doing this? </H3>

네이버 검색창에 전시회를 검색해보면, 현재 진행 중인 전시회에 대한 정보를 한눈에 알아보기 힘들다는 것을 알 수 있다. <br><br>
위치의 경우 서울(강남구, 종로구, 기타), 경기, 부산, 타지역 같은 식으로 너무 크게 나뉘어있으면서, 장소도 주소값이나 역의 위치가 아닌 전시 장소명만을 적어둬 정확한 위치를 일일이 검색하지 않는 한 확인하기 힘들다는 문제가 있었다. <br>
개요 및 설명에 대한 부분은 영화를 검색했을 때와 상반되게 아무것도 나오지 않아, 오직 조그만 포스터 이미지와 전시회의 이름만 보고 검색하여 내용을 확인해야한다. <br><br>
하지만 네이버 전시회 검색을 제외하고서는 마땅한 아카이브 사이트도 없는 상황이다. 현재로써는 네오룩, 아트바바 정도가 전시회 아카이브 사이트라고 할 수 있겠지만 두 사이트 모두 현재 진행 중인 전시회의 일부만 있다는 점, 과거 전시회는 확인하기 힘들며, 필터링이 장르를 제외한 것들은 알아보기 힘들다, 전시 설명이 난해하다 등의 문제가 있었다. <br><br>

<H3> - What do you want to see at the end?</H3>

그렇다면 이런 상황에서 전시회에 어떤 분류가 가장 시급할까에 대한 주변의 의견을 구한 결과, ‘인스타용 전시회인가, 아닌가’가 가장 큰 수요를 보였다. 인스타용 전시회는 흔히 인생샷을 얻을 수 있는 전시회로 사진 찍는 것을 좋아하는 사람들, 전시회가 처음인 사람들에게는 큰 인기가 있다. 하지만 그만큼 사람이 몰린다는 점, 사진만 찍는 주변 관람객 때문에 전시에 집중하기가 힘들다는 점에서 가장 불호가 심한 전시회이기도 하다.

따라서 이번에 ‘전시회가 인스타용 전시회인가, 아닌가’를 전시회 검색 상위 내용을 통해 분류, 예측하는 프로젝트를 진행하고자 한다. <br><br>

<h3>II. Datasets <br>
- Describing your dataset</h3>
(데이터 수집에 사용했던 전시회_정보_수집.py, 구글 검색.py 코드 업로드)<br>
<b>junsi_description_sudong (junsi_description_sudong.xlsx)</b><br>
row (375개) : 6월 2일을 기준으로 네이버 전시회에 등록된 전국 모든 전시회<br>
Columns (6개) :<br>
junsi_name – 전시회의 이름<br>
start, end – 전시회 시작일과 종료일<br>
place – 전시 장소명<br>
google1 – ‘junsi_name place’로 검색했을 때 나온 검색 상위 내용<br>
☞ 검색 상위 내용의 경우 블로그, 해당 전시 사이트, 페이스북, 뉴스 등 일정한 형식이 없어 크롤링 후 내용을 직접 읽어 전처리를 진행. <br>
Insta – ‘junsi_name place’로 검색했을 때 나온 이미지를 기반으로 인스타용 전시회의 경우 1, 아닌 경우 0의 라벨을 붙임.<br><br>

<h3>III. Methodology
- Explaining your choice of algorithms (methods)</h3>
1. 적은 데이터 양임에도 모델을 학습시키고 성능을 확인 – (TF-IDF + Sequential model)<br>
TF-IDF는 문서에서 단어의 빈도수에 따라 문서 전체를 벡터화 시키는 방법이다. 예를 들어 전시회 설명 1과 2를 비교할 때, 각각에 대해 설명 1에만 많이 나온 단어, 설명 2에만 많이 나온 단어에 가중치를 두어 나타내는 것이다. 이것을 이용해 전시회 설명 하나를 하나의 벡터로 표현해 낼 수 있게 된다.<br>
<img src="https://user-images.githubusercontent.com/84369886/121608833-9e4d5600-ca8d-11eb-8746-f87e3d132ffe.png" width="70%">
<br>
Sequential model은 keras에 있는 모델로, 신경망의 Input layer, Hidden layer, Output Layer를 구성하기 위해 사용된다. 이 때 Input ~ Output의 방향은 일방향으로 레이어에 하나의 입력 텐서와 하나의 출력 텐서가 있는 경우에 적합하다. 이번 주제의 경우, 전시 설명의 각각 문장에 집중하는 것이 아닌 전시 설명 전체를 하나로 인스타 전시회를 분류한다는 점에서 위 모델을 사용하는 것은 적절할 것이라고 판단했다.<br>

<br>2. 데이터가 적기 때문에 미리 훈련된 모형을 사용 – Sktbrain KoBert<br>
단어를 벡터로 표현하는 방법으로 원-핫 인코딩과 Word Embedding이 있다. 일반적으로 n개의 단어 중 i번째에 존재하는 ‘전시회’라는 단어를 표현하려면, n차원의 벡터에서 i번째 숫자만 1을 넣고, 나머지는 0을 넣는 식으로 표현할 수 있다. 이것을 원-핫 인코딩이라고 하는데, 문제는 전체 n개의 단어가 커지면 커질수록 벡터의 차원이 커진다는 것이다. 하지만 Word Embedding경우 벡터 안의 값들을 실수로 넣어, 저차원의 벡터로 단어의 표현이 가능하며 단어 사이의 유사성도 나타낼 수 있게 된다. 또한 이미 학습된 모델이 있어 훈련 없이 사용이 가능하다는 것도 큰 장점이었다<br>
2018년 처음 나온 ELMo(Embeddings from Language Mode)는 단어가 문장 안에서 갖는 의미를 고려해가며 word embedding을 시킨다는 것에 큰 의의가 있었다. 예를 들면 ‘배를 먹다’ 라는 문장의 ‘배’를 일반적으로 읽었을 때‘먹는 거면 과일 배구나’라는 걸 알지만, Word2Vec이나 GloVe 같은 방법들은 이게 사람 배인지, 과일 배인지, 타는 배인지 구분없이 전부 똑같은 벡터를 사용했다. 하지만 ELMo는 문장 안에서의 단어의 의미에 따라 벡터를 사용한다는 장점이 있었다. 그 이후 앞의 단어를 가지고 뒤의 단어를 예측한다는 ELMo의 일방향적인 단점을 보완해서, 양방향성을 가진 같은 Bert가 등장하게 됐다. 그리고 SKT가 한국어 Bert, KoBert를 깃허브에 공개해두어, 이를 활용해보고자 했다.<br><br>

<h3>- Explaining features (if any)</h3>
1번 방법의 경우, 전시회 설명들을 Konlpy의 KKma를 활용해 형태소 분석을 진행하였다. 이 때 위에서 말했던 것처럼 TF-IDF 방법으로 벡터화 시키는 것을 고려해 가장 간단한 명사만을 사용하여 분석을 진행했다. 그 이후 Train, Test, Validation을 각각 60%, 20%, 20%로 나눠 준비한 뒤, Sequential model로 각각 64개의 layer를 가진 hidden layer를 통과시킨 뒤, 하나의 output layer로 결과를 내도록 구성했다. Hidden layer의 경우 relu를 활성화 함수로 썼고, output layer의 경우 라벨이 0, 1이므로 sigmoid를 사용했으며, loss 함수는 mse를 사용했다. 이렇게 생성한 모델을 train에 대해 학습을 50번 시키고(epochs=50), validation에 대해 예측하여 성능을 확인했다.<br><br>
2번 방법의 경우, Train과 Test를 70%, 30%로 나눠 준비한 뒤, Bert의 tokenizer로 문장을 tokenizing한다. Parameter의 경우 max_len을 64, batch_size를 32, num_epochs를 5로 잡았다. 그 후 dataloader로 batch_size만큼씩 모델에 값을 넣게 하고, 학습을 시킨다.

<h3>IV. Evaluation & Analysis
- Graphs, tables, any statistics (if any)</h3>
1번 방법의 경우 0.5이상을 Insta 라벨 1, 0.5 미만을 Insta 라벨 0이라고 했을 때 25개의 Validation data 중에 22개를 제대로 분류해내어, 정확도 88% 로 나타났다.
<img src= "https://user-images.githubusercontent.com/84369886/121610594-5f210400-ca91-11eb-963e-62e0aee2dbaa.png" width="30%">
<br>
2번 방법의 경우 값을 GPU를 사용한 경우 마지막 셀에서<br>
RuntimeError: CUDA out of memory. Tried to allocate 96.00 MiB (GPU 0; 14.76 GiB total capacity; 13.66 GiB already allocated; 13.75 MiB free; 13.71 GiB reserved in total by PyTorch) <br>
메모리가 부족하다는 오류가 발생하였고, 이를 해결하기 위해 TPU를 사용해 실행을 해보았다.<br>
Ran out of memory in memory space hbm. Used 17.01G of 7.48G hbm. Exceeded hbm capacity by 9.53G. TPU <br>
여전히 메모리가 부족하다는 오류가 발생하였고, 결국 이를 해결하기 위해 batch_size를 2까지 줄이고, 코랩 프로를 결제하였지만 여전히 메모리가 부족하다는 오류가 생겼다.
15만건의 영화 리뷰 데이터 분석 메모리가 부족하지 않지만, 370여개의 전시회 설명 데이터 분석에는 메모리가 부족한 것은 문제가 있다고 판단했다. 그리고 영화 리뷰 분석과 차이를 찾아본 결과 추측한 원인으로는 영화 리뷰의 경우는 한줄 정도의 짧은 데이터로 15만개가 있었지만, 전시회 설명 데이터는 아주 긴 설명이 370개라는 적은 양이 존재했다는 점이었다. 전시회 분석의 토큰을 보면 밑에와 같이 배열에 모두 값이 들어간 것을 확인할 수 있다.
<<img src= "https://user-images.githubusercontent.com/84369886/121612682-d5c00080-ca95-11eb-8327-a28e45eac15c.PNG" width="70%">
그러나 정상적으로 KoBert를 실행시킨 결과값을 보면 data_train[0]의 토큰이 64개를 모두 채우지 않은 것을 확인했다 (https://moondol-ai.tistory.com/241) <br>

<h3>V. Related Work (e.g., existing studies)
- Tools, libraries, blogs, or any documentation that you have used to do this project.</h3>
https://www.tensorflow.org/guide/keras/sequential_model?hl=ko <br>
https://wikidocs.net/book/2155 <br>
https://yngie-c.github.io/nlp/2020/07/03/nlp_elmo/<br>
https://github.com/SKTBrain/KoBERT
<br>
<h3>VI. Conclusion: Discussion</h3>
긍정적인 이야기와 부정적인 이야기가 모두 가능할 것 같다. 처음 목표점으로 삼았던 ‘전시회가 인스타용 전시회인가, 아닌가’를 분류, 예측하는 것에 대해서는 굉장히 적은 데이터에 대해서 실행한 것을 고려하면 TF-IDF + Sequential model 로 긍정적인 예측 결과가 나왔다고 생각한다. 하지만 KoBert의 경우 성능이나 결과값을 볼 수도 없이 메모리가 부족하다는 문장으로 그만둘 수 밖에 없었던 것에는 아쉬움으로 남는다. 
앞으로 추가적인 분석이 가능하다면, 주제적으로는 단순 인스타용 전시회인가 아닌가가 아닌 전시회의 장르 및 주제 등을 분류해내거나 추출해낼 수 있는 프로그램을 생각해 볼 수 있을 것 같다. 또한 과거의 전시회 데이터를 찾기 힘들었다는 점을 감안하여 긴 시간동안 충분한 데이터를 모아 성능을 더 좋게 만드는 것 또한 개선할 부분이라고 생각한다.




