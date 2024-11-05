# DA 421M Multi-modal Data Processing and Learning Course Project

## Project Title:
Video Captioning with Transformer-Based Models: An Exploration from VideoBERT to UniVL
This repository contains the code for the 

## Environment Setup
```bash
pip install -r requirements.txt
```

## VideoBERT: A Joint Model for Video and Language Representation Learning
- **Step 1**: **Collection of Data**
    Video and text annotations are sourced from the HowTo100M dataset, a large-scale
    dataset for video-language tasks. We use a subset of this dataset, containing 47,470 videos,
    identified in the file _step1/ids.txt_. Annotations are accessed through the official dataset
    source, ensuring high-quality text aligned with instructional videos.
  <hr>
- **Step 2**: **Transforming the Data**
    Video frame rates are standardized to 10 frames per second (fps) for consistency and
    computational efficiency. Additionally, punctuation is added to text annotations to maintain
    coherence in language structure. Pre-trained models available for punctuation restoration are
    referenced to ensure accurate punctuation alignment.
  <hr>
- **Step 3**: **Extraction of Features**
    I3D (Inflated 3D) network features are extracted from the processed frames.The I3D model, known
    for its proficiency in capturing spatiotemporal information, is applied to each video segment,
    yielding a set of features that encode motion and object-level details. The pre-trained I3D model
    checkpoint is utilized to streamline this process, located in the step3/checkpoint directory.
  
    Captions are processed using a BERT model to create token embeddings for each word or phrase.
  <hr>
- **Step 4**: **Clustering the I3D Features**
    To bridge the gap between continuous visual data and the discrete nature of language tokens,
    we cluster the I3D features using hierarchical k-means clustering with a cluster size
    k = 12 and hierarchy level h = 4. This clustering reduces feature dimensionality while
    retaining essential information.
  <hr>
- **Step 5**: **Converting BERT to VideoBERT**
    To adapt BERT for video-language tasks, we make modifications to the original BERT model.
    A new vocabulary is introduced to capture visual features, and a custom class, VideoBertForPreTraining,
    is created to handle the unique input modalities and training regimes of VideoBERT. This customized
    model structure allows for the inclusion of both text and video inputs, ensuring VideoBERT can learn
    joint representations that bridge the two modalities.
  <hr>
- **Step 6**: **Training the Model**
    The final step involves training VideoBERT on the transformed and clustered data.Training is conducted
    with two model variations: one that excludes the alignment task and another that incorporates it. By
    evaluating both configurations, we assess the impact of the alignment task on model performance. The
    processed training data required for this step is made available through a designated source, allowing
    for reproducibility and comparison with baseline results.
- **Step 7**: **Evaluation**
    To evaluate the trained model, we use the YouCookII validation dataset, a benchmark dataset for video
    captioning and classification tasks. VideoBERT’s performance is assessed on a zero-shot classification
    task, comparing generated captions with ground truth annotations. The evaluation lists for verbs and
    nouns are stored in _evaluation/verbs.txt_ and _evaluation/nouns.txt_, used to verify the model’s captioning
    accuracy and language coherence.

## Modification of VideoBERT: UniVL (A Unified Video and Language Pre-Training Model for Multimodal Understanding and Generation)


## Group Members:
* Rasesh Srivastava
* Vidya Sagar G
