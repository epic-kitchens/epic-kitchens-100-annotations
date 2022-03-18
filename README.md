# EPIC KITCHENS-100 Dataset

<!-- start badges -->
[![CircleCI](https://img.shields.io/circleci/build/github/epic-kitchens/epic-kitchens-100-annotations.svg)](https://circleci.com/gh/epic-kitchens/epic-kitchens-100-annotations)
[![GitHub release](https://img.shields.io/github/release/epic-kitchens/epic-kitchens-100-annotations.svg)](https://github.com/epic-kitchens/epic-kitchens-100-annotations/releases/latest)
[![arXiv-2006.13256](https://img.shields.io/badge/arXiv-2006.13256-red.svg)](https://arxiv.org/abs/2006.13256)
<!-- end badges -->

> [EPIC-KITCHENS-100](https://epic-kitchens.github.io/) is the largest dataset in first-person (egocentric) vision; itself an extension of the [EPIC-KITCHENS-55 dataset](https://github.com/epic-kitchens/annotations) (formally known as EPIC-KITCHENS-2018).

## Authors
Dima Damen (1)
Hazel Doughty (1)
Giovanni Maria Farinella (2)
Antonino Furnari (2)
Evangelos Kazakos (1)
Jian Ma (1)
Davide Moltisanti (1)
Jonathan Munro (1)
Toby Perrett (1)
Will Price (1)
Michael Wray (1)

* (1 University of Bristol)
* (2 University of Catania)

**Contact:** [uob-epic-kitchens@bristol.ac.uk](mailto:uob-epic-kitchens@bristol.ac.uk)

## Citing
When using the dataset, kindly reference:
```
@article{damen2022rescaling,
   title={Rescaling Egocentric Vision},
   author={Damen, Dima and Doughty, Hazel and Farinella, Giovanni Maria  and and Furnari, Antonino 
           and Ma, Jian and Kazakos, Evangelos and Moltisanti, Davide and Munro, Jonathan 
           and Perrett, Toby and Price, Will and Wray, Michael},
           journal={International Journal of Computer Vision},
           volume={130},
           number={1},
           pages={33--55},
           year={2022},
           publisher={Springer}
} 
```

## Erratum

**Important:** We have recently detected an error in our pre-extracted RGB and Optical flow frames for two videos in our dataset. This does not affect the videos themselves or any of the annotations in this github. However, if you've been using our pre-extracted frames, we below detail how you can fix the error at your end, until we publish replacement frames for downloading.

Download the videos `P01_109.MP4` and `P27_103.MP4`. Then set up a directory like so:

    $ mkdir -p rgb/{P01_109,P27_103}
    $ mkdir -p flow/{P01_109,P27_103}
    $ mkdir videos
    $ mv /path/to/{P01_109,P27_103}.MP4 videos

You will need docker setup on your machine to extract the frames and flow.

**RGB**

    $ docker run --gpus "device=0" \
         -it \
         --rm \
         -v "$PWD:/workspace" \
         willprice/nvidia-ffmpeg \
         -hwaccel cuvid \
         -c:v hevc_cuvid \
         -i /workspace/videos/P27_103.MP4 \
         -vf 'scale_npp=-2:256:interp_algo=super,hwdownload,format=nv12' \
         -qscale:v 4 \
         -r 50 /workspace/rgb/P27_103/frame_%010d.jpg
    
    $ docker run --gpus "device=0" \
         -it \
         --rm \
         -v "$PWD:/workspace" \
         willprice/nvidia-ffmpeg \
         -hwaccel cuvid \
         -c:v hevc_cuvid \
         -i /workspace/videos/P01_109.MP4 \
         -vf 'scale_npp=-2:256:interp_algo=super,hwdownload,format=nv12' \
         -qscale:v 4 \
         -r 50 /workspace/rgb/P01_109/frame_%010d.jpg


**Flow**


    $ docker run --gpus "device=0" \
         -it \
         --rm \
         -v "$PWD/rgb/P01_109:/input" \
         -v "$PWD/flow/P01_109:/output" \
         willprice/furnari-flow \
         frame_%010d.jpg -g 0 -s 1 -d 1 -b 8
    
    $ docker run --gpus "device=0" \
         -it \
         --rm \
         -v "$PWD/rgb/P27_103:/input" \
         -v "$PWD/flow/P27_103:/output" \
         willprice/furnari-flow \
         frame_%010d.jpg -g 0 -s 1 -d 1 -b 8


## Index
* [Dataset Details](#dataset-details)
* [Quick start Guides](#quick-start)
* [Important Files](#important-files)
* [File Structure](#file-structure)
* [Additional Information](#additional-information)
* [License](#license)

## Dataset Details
The EPIC-KITCHENS-100 dataset is an extension of the EPIC-KITCHENS-55 dataset. Videos are distinguished as follows:

* `PXX_YY.MP4` videos originate from EPIC-KITCHENS-55.
* `PXX_1YY.MP4` videos originate from the extension collected for EPIC-KITCHENS-100 (thus represent new videos).



The dataset currently has 6 active benchmarks:

* [Action Recognition](#action-recognition-challenge)
* [Weakly Supervised Action Recognition](#weakly-supervised-action-recognition-challenge)
* [Action Detection](#action-detection-challenge)
* [Action Anticipation](#action-anticipation-challenge)
* [Unsupervised Domain Adaptation](#unsupervised-domain-adaptation-challenge)
* [Multi-Instance Retrieval](#multi-instance-retrieval-challenge)

We provide csv files for the train/val/test sets of each benchmark detailed below for ease of use, see [Important Files](#important-files) for more information.

Ground truth is provided for action segments as action/verb/noun labels along with the start and end times of the segment.

We also provide automatic annotations in the form of object masks and hand/object BBoxes. See [automatic annotations](#automatic-annotations-download) for more details.

[back to top](#index)

## Quick Start

Here you can download the annotation files for all of the challenges. For more information on each challenge, please see the paper [here]().
A download script is provided for the videos, RGB Frames and Flow frames [here](https://github.com/epic-kitchens/download-scripts-100).

### Action Recognition Challenge
1. Download the videos/RGB/Flow frames [here](https://github.com/epic-kitchens/download-scripts-100) with the following command: 

```bash
python epic_downloader.py --videos --rgb-frames --flow-frames
```

2. Download the Action Recognition [train](EPIC_100_train.csv)/[val](EPIC_100_validation.csv)/[test](EPIC_100_test_timestamps.csv) files.
3. Enjoy the EPIC-KITCHENS-100 dataset in your favourite action recognition model, see [the paper](#citing) for details on the models we used for this baseline. Models trained on EPIC-KITCHENS-55 can be found [here](https://github.com/epic-kitchens/action-models) as a starting point.

### Weakly Supervised Action Recognition Challenge
1. Download the videos/RGB/Flow frames [here](https://github.com/epic-kitchens/download-scripts-100) with the following command: 

```bash
python epic_downloader.py --videos --rgb-frames --flow-frames
```

2. This challenge uses the Action Recognition files, download the [train](EPIC_100_train.csv)/[val](EPIC_100_validation.csv)/[test](EPIC_100_test_timestamps.csv) files.
3. The weakly supervised challenge uses the narration timestamp, not the the start/end times of the action. Therefore a simple baseline would be to modify an action recognition model to use the surrounding 5s worth of frames. See [the paper](#citing) for details on the models we used for this baseline.

### Action Detection Challenge
1. Download the videos/RGB/Flow frames [here](https://github.com/epic-kitchens/download-scripts-100) with the following command: 

```bash
python epic_downloader.py --videos --rgb-frames --flow-frames
```

2. This challenge uses the Action Recognition files, download the [train](EPIC_100_train.csv)/[val](EPIC_100_validation.csv)/[test](EPIC_100_test_timestamps.csv) files.
3. Train an action proposal network on the EPIC-KITCHENS-100 train set, for example [this model](https://github.com/JJBOY/BMN-Boundary-Matching-Network). This model predicts action-agnostic segments which still need to be classified.
4. Use your favourite action recognition model to classify the proposals ([example models](https://github.com/epic-kitchens/action-models)).

### Action Anticipation Challenge
1. Download the videos/RGB/Flow frames [here](https://github.com/epic-kitchens/download-scripts-100) with the following command: 

```bash
python epic_downloader.py --videos --rgb-frames --flow-frames
```

2. This challenge uses the Action Recognition files, download the [train](EPIC_100_train.csv)/[val](EPIC_100_validation.csv)/[test](EPIC_100_test_timestamps.csv) files.
3. A simple baseline for this task is to train an action recognition model (example models [here]()) on the 5 seconds that precede an action with a 1 second gap. For example, an action that starts at 20.00s in a video would see frames between 14.00s and 19.00s.

### Unsupervised Domain Adaptation Challenge
The unsupervised domain adaptation challenge tests how models can cope with similar data collected 2 years later on the task of action recognition.

1. Download the videos/RGB/Flow frames [here](https://github.com/epic-kitchens/download-scripts-100) with the following command: 

```bash
python epic_downloader.py --videos --rgb-frames --flow-frames --domain-adaptation
```

2. Download the Unsupervised Domain Adaptation [source train](UDA_annotations/EPIC_100_uda_source_train.csv)/[target train](UDA_annotations/EPIC_100_uda_target_train_timestamps.csv)/[source_test](UDA_annotations/EPIC_100_uda_source_test_timestamps.csv)/[target test](UDA_annotations/EPIC_100_uda_target_test_timestamps.csv)/[source val](UDA_annotations/EPIC_100_uda_source_val.csv)/[target val](UDA_annotations/EPIC_100_uda_target_val.csv) files.
3. Extract video features (for all six splits) using an off-the-shelf model trained on **EPIC-KITCHENS-55** ([example model](https://github.com/epic-kitchens/action-models)).
4. A simple baseline is using a domain discriminator (prediciting whether a video came from the source, EPIC-KITCHENS-55, or the target, EPIC-KITCHENS-100) to align the two domains. See [the paper](#citing) for details on the models we used for this baseline.

IMPORTANT NOTE ON HYPER-PARAMETER TUNING. As the target domain is unlabelled, the training splits cannot be used for hyper-parameter tuning. You must use the validation splits to choose hyper-parameters. The procedure for hyper-parameter tuning and training is as follows:

1. Train your model on [source val](UDA_annotations/EPIC_100_uda_source_val.csv) with unlabelled data from [target val](UDA_annotations/EPIC_100_uda_target_val.csv).
2. Evaluate your model on [target val](UDA_annotations/EPIC_100_uda_target_val.csv) using the labels provided (these labels should not be used during training).
3. Select hyper-parameters based on the performance on [target val](UDA_annotations/EPIC_100_uda_target_val.csv).
4. Re-train your model on [source train](UDA_annotations/EPIC_100_uda_source_train.csv)/[target train](UDA_annotations/EPIC_100_uda_target_train_timestamps.csv) with selected hyper-parameters.
5. Evaluate the re-trained model on [target test](UDA_annotations/EPIC_100_uda_target_test_timestamps.csv) to produce action predictions for the challenge leaderboard.

It is optional but highly ecouraged to evalute the performance on [source_test](UDA_annotations/EPIC_100_uda_source_test_timestamps.csv) to compare source domain performances.

### Multi-Instance Retrieval Challenge

**NOTE** *30/09/2020* There was an error in the creation of the sentence files for the retrieval challenge. Please download the new sentence dataframes.

1. Download the videos/RGB/Flow frames [here](https://github.com/epic-kitchens/download-scripts-100) with the following command: 

```bash
python epic_downloader.py --videos --rgb-frames --flow-frames --action-retrieval
```
2. Download the Multi-Instance Retrieval [train](retrieval_annotations/EPIC_100_retrieval_train.csv)/[test](retrieval_annotations/EPIC_100_retrieval_test.csv) files.
3. Extract video features (for both the train and test set) using an off-the-shelf model trained on **EPIC-KITCHENS-55** ([example model](https://github.com/epic-kitchens/action-models)).
4. Extract word2vec features for the captions from both the train and test set ([example models](https://github.com/mmihaltz/word2vec-GoogleNews-vectors)).
5. Enjoy the EPIC-KITCHENS-100 dataset in your favourite video retrieval model, see [the paper](#citing) for details on the models we used for this baseline.


[back to top](#index)

## Important Files

For ease of use, download scripts are [provided](https://github.com/epic-kitchens/download-scripts-100) to download the videos and RGB/Flow frames. (see [file downloads](#file-downloads) for more details). We direct the reader to [RDSF](https://data.bris.ac.uk/data/dataset/2g1n6qdydwa9u22shpxqzp0t8m) for the full release of videos and RGB/Flow frames. 
We provide html and pdf alternatives to this README which are auto-generated.

* `README.md (this file)`
* `README.pdf`
* `README.html`
* [`license.txt`](#license)
* [`EPIC_100_train.csv`](EPIC_100_train.csv) ([info](#epic_100_traincsv)) ([Pickle](EPIC_100_train.pkl))
* [`EPIC_100_validation.csv`](EPIC_100_validation.csv) ([info](#epic_100_validationcsv)) ([Pickle](EPIC_100_validation.pkl))
* [`EPIC_100_test_timestamps.csv`](EPIC_100_test_timestamps.csv) ([info](#epic_100_test_timestampscsv)) ([Pickle](EPIC_100_test_timestamps.pkl))
* [`EPIC_100_noun_classes.csv`](EPIC_100_noun_classes.csv) ([info](#epic_100_noun_classescsv))
* [`EPIC_100_verb_classes.csv`](EPIC_100_verb_classes.csv) ([info](#epic_100_verb_classescsv))

### Additional Files

* [`UDA_annotations/EPIC_100_uda_source_train.csv`](UDA_annotations/EPIC_100_uda_source_train.csv) ([info](#epic_100_uda_source_traincsv)) ([Pickle](UDA_annotations/EPIC_100_uda_source_train.pkl))
* [`UDA_annotations/EPIC_100_uda_source_test_timestamps.csv`](UDA_annotations/EPIC_100_uda_source_test_timestamps.csv) ([info](#epic_100_uda_source_test_timestampscsv)) ([Pickle](UDA_annotations/EPIC_100_uda_source_test_timestamps.pkl))
* [`UDA_annotations/EPIC_100_uda_target_train_timestamps.csv`](UDA_annotations/EPIC_100_uda_target_train_timestamps.csv) ([info](#epic_100_uda_target_train_timestampscsv)) ([Pickle](UDA_annotations/EPIC_100_uda_target_train_timestamps.pkl))
* [`UDA_annotations/EPIC_100_uda_target_test_timestamps.csv`](UDA_annotations/EPIC_100_uda_target_test_timestamps.csv) ([info](#epic_100_uda_target_test_timestampscsv)) ([Pickle](UDA_annotations/EPIC_100_uda_target_test_timestamps.pkl))
* [`UDA_annotations/EPIC_100_uda_source_val.csv`](UDA_annotations/EPIC_100_uda_source_val.csv) ([info](#epic_100_uda_source_valcsv)) ([Pickle](UDA_annotations/EPIC_100_uda_source_val.pkl))
* [`UDA_annotations/EPIC_100_uda_target_val.csv`](UDA_annotations/EPIC_100_uda_target_val.csv) ([info](#epic_100_uda_target_valcsv)) ([Pickle](UDA_annotations/EPIC_100_uda_target_val.pkl))
* [`retrieval_annotations/EPIC_100_retrieval_train.csv`](retrieval_annotations/EPIC_100_retrieval_train.csv) ([info](#epic_100_retrieval_traincsv)) ([Pickle](retrieval_annotations/EPIC_100_retrieval_train.pkl))
* [`retrieval_annotations/EPIC_100_retrieval_test.csv`](retrieval_annotations/EPIC_100_retrieval_test.csv) ([info](#epic_100_retrieval_testcsv)) ([Pickle](retrieval_annotations/EPIC_100_retrieval_test.pkl))
* [`retrieval_annotations/EPIC_100_retrieval_train_sentence.csv`](retrieval_annotations/EPIC_100_retrieval_train_sentence.csv) ([info](#epic_100_retrieval_train_sentencecsv)) ([Pickle](retrieval_annotations/EPIC_100_retrieval_train_sentence.pkl))
* [`retrieval_annotations/EPIC_100_retrieval_test_sentence.csv`](retrieval_annotations/EPIC_100_retrieval_test_sentence.csv) ([info](#epic_100_retrieval_test_sentencecsv)) ([Pickle](retrieval_annotations/EPIC_100_retrieval_test_sentence.pkl))
* [`EPIC_100_train_missing_timestamps_narrations.csv`](EPIC_100_train_missing_timestamps_narrations.csv) ([info](#epic_100_train_missing_timestamps_narrationscsv)) 
* [`EPIC_100_validation_missing_timestamps_narrations.csv`](EPIC_100_validation_missing_timestamps_narrations.csv) ([info](#epic_100_validation_missing_timestamps_narrationscsv)) 
* [`EPIC_100_unseen_participant_ids_test.csv`](EPIC_100_unseen_participant_ids_test.csv) ([info](#epic_100_unseen_participant_idscsv))
* [`EPIC_100_unseen_participant_ids_validation.csv`](EPIC_100_unseen_participant_ids_validation.csv) ([info](#epic_100_unseen_participant_idscsv))
* [`EPIC_100_tail_verbs.csv`](EPIC_100_tail_verbs.csv) ([info](#epic_100_tail_verbscsv))
* [`EPIC_100_tail_nouns.csv`](EPIC_100_tail_nouns.csv) ([info](#epic_100_tail_nounscsv))
* [`EPIC_100_video_info.csv`](EPIC_100_video_info.csv) ([info](#epic_100_video_infocsv))

[back to top](#index)

## File Structure

#### EPIC_100_train.csv

This CSV file contains the action annotations for the training set and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_01_0`     | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_01`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:01.089` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:00.14`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:03.37`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `8`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `202`          | End frame of the action.                                                      |
| `narration`           | string                     | `open door`    | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `open`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `3`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `door`         | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `3`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[door]`       | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[3]`          | Numeric ID of all of the parsed noun's classes.                               |

[Back to Important Files](#important-files)


#### EPIC_100_validation.csv

This CSV file contains the action annotations for the validation set and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_01_11`    | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_11`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:00.560` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:00.00`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:01.89`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `1`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `113`          | End frame of the action.                                                      |
| `narration`           | string                     | `take plate`   | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `take`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `0`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `plate`        | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `2`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[plate]`      | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[2]`          | Numeric ID of all of the parsed noun's classes.                               |

[Back to Important Files](#important-files)


#### EPIC_100_test_timestamps.csv

This CSV file contains the action annotations for the testing set and contains 9 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_101_0`    | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_101`      | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:02.851` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:02.86`  | Start time in `HH:mm:ss.SSS` of the action segment.                           |
| `stop_timestamp`      | string                     | `00:00:03.87`  | End time in `HH:mm:ss.SSS` of the action segment.                             |
| `start_frame`         | int                        | `143`          | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `193`          | End frame of the action.                                                      |

[Back to Important Files](#important-files)


#### EPIC_100_noun_classes.csv

This CSV file contains information on the 300 noun classes and contains 4 columns.

| Column Name | Type                       | Example                  | Description                                                                   |
| ----------- | -------------------------- | ------------------------ | ----------------------------------------------------------------------------- |
| `id`        | int                        | `222`                    | Unique ID for the noun class.                                                 |
| `key`       | string                     | `label`                  | Key used for the noun class (all keys are a member of their own class).       |
| `instances` | list of string (1 or more) | `"['label', 'sticker']"` | All nouns within the class, including the key.                                |
| `category`  | string                     | `materials`              | Name of the higher-level noun category that this noun class belongs to.       |

[Back to Important Files](#important-files)


#### EPIC_100_verb_classes.csv

This CSV file contains information on the 97 verb classes and contains 4 columns.

| Column Name | Type                       | Example               | Description                                                                   |
| ----------- | -------------------------- | --------------------- | ----------------------------------------------------------------------------- |
| `id`        | int                        | `79`                  | Unique ID for the verb class.                                                 |
| `key`       | string                     | `let-go`              | Key used for the verb class (all keys are a member of their own class).       |
| `instances` | list of string (1 or more) | `"['let', 'let-go']"` | All verbs within the class, including the key.                                |
| `category`  | string                     | `leave`               | Name of the higher-level verb category that this verb class belongs to.       |

[Back to Important Files](#important-files)


#### EPIC_100_uda_source_train.csv

This CSV file contains the action annotations for the **source training set** used for **Unsupervised Domain Adaptation** and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_01_0`     | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_01`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:01.089` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:00.14`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:03.37`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `8`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `202`          | End frame of the action.                                                      |
| `narration`           | string                     | `open door`    | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `open`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `3`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `door`         | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `3`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[door]`       | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[3]`          | Numeric ID of all of the parsed noun's classes.                               |

Note that this file contains only videos from EPIC-KITCHENS-55 which is used as the source domain.

See [here](#unsupervised-domain-adaptation-challenge) for more details on the unsupervised domain adaptation challenge.

[Back to Important Files](#important-files)

#### EPIC_100_uda_source_test_timestamps.csv

This CSV file contains the action annotations for the **source testing set** used for **Unsupervised Domain Adaptation** and contains 9 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_11_0`     | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_11`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:00.560` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:00.00`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:01.89`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `1`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `113`          | End frame of the action.                                                      |

Note that this file contains only videos from EPIC-KITCHENS-55 which is used as the source domain.

See [here](#unsupervised-domain-adaptation-challenge) for more details on the unsupervised domain adaptation challenge.

[Back to Important Files](#important-files)


#### EPIC_100_uda_target_train_timestamps.csv

This CSV file contains the action annotations for the **target training set** used for **Unsupervised Domain Adaptation** and contains 9 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_102_0`    | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_102`      | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:01.100` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:00.54`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:02.23`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `27`           | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `111`          | End frame of the action.                                                      |

Note that this file contains only videos from EPIC-KITCHENS-100 which is used as the target domain.

See [here](#unsupervised-domain-adaptation-challenge) for more details on the unsupervised domain adaptation challenge.

[Back to Important Files](#important-files)


#### EPIC_100_uda_target_test_timestamps.csv

This CSV file contains the action annotations for the **target testing set** used for **Unsupervised Domain Adaptation** and contains 9 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_101_0`    | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_101`      | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:02.851` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:02.86`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:03.87`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `143`          | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `193`          | End frame of the action.                                                      |

Note that this file contains only videos from EPIC-KITCHENS-100 which is used as the target domain.

See [here](#unsupervised-domain-adaptation-challenge) for more details on the unsupervised domain adaptation challenge.

[Back to Important Files](#important-files)

#### EPIC_100_uda_source_val.csv

This CSV file contains the action annotations for the **source validation set** used for **Unsupervised Domain Adaptation** and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P03_02_0`     | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P03`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P03_02`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:04.310` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:03.29`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:04.26`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `197`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `255`          | End frame of the action.                                                      |
| `narration`           | string                     | `put lunch box`    | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `put`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `1`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `box:lunch`         | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `23`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[box:lunch]`       | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[23]`          | Numeric ID of all of the parsed noun's classes.                               |

Note that this file contains only videos from EPIC-KITCHENS-55 which is used as the source domain for validation.

See [here](#unsupervised-domain-adaptation-challenge) for more details on the unsupervised domain adaptation challenge.

[Back to Important Files](#important-files)

#### EPIC_100_uda_target_val.csv

This CSV file contains the action annotations for the **target validation set** used for **Unsupervised Domain Adaptation** and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P03_101_0`     | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P03`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P03_101`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:02.877` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:02.60`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:03.86`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `130`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `193`          | End frame of the action.                                                      |
| `narration`           | string                     | `turn on tap`    | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `turn-on`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `6`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `tap`         | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `0`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[tap]`       | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[23]`          | Numeric ID of all of the parsed noun's classes.                               |

Note that this file contains only videos from EPIC-KITCHENS-100 which is used as the target domain for validation.

See [here](#unsupervised-domain-adaptation-challenge) for more details on the unsupervised domain adaptation challenge.

[Back to Important Files](#important-files)

#### EPIC_100_retrieval_train.csv

This CSV file contains the action annotations for the **action retrieval** training set and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_01_0`     | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_01`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:01.089` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:00.14`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:03.37`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `8`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `202`          | End frame of the action.                                                      |
| `narration`           | string                     | `open door`    | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `open`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `3`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `door`         | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `3`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[door]`       | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[3]`          | Numeric ID of all of the parsed noun's classes.                               |

[Back to Important Files](#important-files)


#### EPIC_100_retrieval_train_sentence.csv

This CSV file contains the caption annotations for the **action retrieval** training set and contains 6 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_01_0`     | Unique ID for the caption (corresponding to the original action).             |
| `narration`           | string                     | `open door`    | Transcribed description of the English narration provided by the participant. |
| `verb_class`          | int                        | `3`            | Numeric ID of the verb's class.                                               |
| `noun_classes`        | list of int (1 or more)    | `[3]`          | Numeric ID of the all noun classes in the narration.                          |
| `verb`                | string                     | `open`         | Parsed verb from the narration.                                               |
| `nouns`               | list of string (1 or more) | `[door]`       | All parsed nouns in the narration.                                            |

[Back to Important Files](#important-files)


#### EPIC_100_retrieval_test.csv

This CSV file contains the action annotations for the **action retrieval** testing set and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_11_0`     | Unique ID for the segment as a string with participant ID and video ID.       |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_11`       | ID of the video where the segment originated from (unique per video).         |
| `narration_timestamp` | string                     | `00:00:00.560` | Timestamp of when the original narration was recorded in `HH:mm:ss.SSS`.      |
| `start_timestamp`     | string                     | `00:00:00.00`  | Start time in `HH:mm:ss.SS` of the action segment.                            |
| `stop_timestamp`      | string                     | `00:00:01.89`  | End time in `HH:mm:ss.SS` of the action segment.                              |
| `start_frame`         | int                        | `8`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `113`          | End frame of the action.                                                      |
| `narration`           | string                     | `take plate`   | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `take`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `0`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `plate`        | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `2`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[plate]`      | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[2]`          | Numeric ID of all of the parsed noun's classes.                               |

[Back to Important Files](#important-files)


#### EPIC_100_retrieval_test_sentence.csv

This CSV file contains the caption annotations for the **action retrieval** testing set and contains 2 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_11_0`     | Unique ID for the caption (corresponding to the original action).            |
| `narration`           | string                     | `take plate`   | Transcribed description of the English narration provided by the participant. |

[Back to Important Files](#important-files)

#### EPIC_100_train_missing_timestamps_narrations.csv

This CSV file contains the narration IDs of all EPIC-KITCHENS-55 videos in the training set which do not have a narration timestamp (see [here]() for more details). This file has one column:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_09_660`   | Unique ID for the segment as a string with participant ID and video ID.       |

[Back to Important Files](#important-files)

#### EPIC_100_validation_missing_timestamps_narrations.csv

This CSV file contains the narration IDs of all EPIC-KITCHENS-55 videos in the validation set which do not have a narration timestamp (see [here]() for more details). This file has one column:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P02_12_293`   | Unique ID for the segment as a string with participant ID and video ID.       |

[Back to Important Files](#important-files)

#### EPIC_100_unseen_participant_ids.csv

This CSV file contains the list of participant IDs who are unseen during training for use in evaluating the unseen participant metrics.

We have two files for both the validation and test set:

- `EPIC_100_unseen_participant_ids_test.csv` - The unseen participants in the test set.
- `EPIC_100_unseen_participant_ids_validation.csv` - The unseen participants in the validation set.

| Column Name           | Type   | Example        | Description                                                                   |
| --------------------- | ------ | -------------- | ----------------------------------------------------------------------------- |
| `participant_id`      | string | `P33`          | ID of the participant (unique per participant).                               |

[Back to Important Files](#important-files)

#### EPIC_100_tail_verbs.csv

This CSV file contains the list of verb classes which are considered part of the tail classes.
These are the set of smallest classes (i.e. those with fewest instances) that account for 20% of the total number of instances in the training set.

| Column Name           | Type   | Example        | Description                                                                   |
| --------------------- | ------ | -------------- | ----------------------------------------------------------------------------- |
| `verb`                | int    | `10`           | Numeric ID representing the verb class.                                       |

[Back to Important Files](#important-files)

#### EPIC_100_tail_nouns.csv

This CSV file contains the list of noun classes which are considered part of the tail classes.
These are the set of smallest classes (i.e. those with fewest instances) that account for 20% of the total number of instances in the training set.

| Column Name           | Type   | Example        | Description                                                                   |
| --------------------- | ------ | -------------- | ----------------------------------------------------------------------------- |
| `noun`                | int    | `56`           | Numeric ID representing the noun class.                                       |

#### EPIC_100_video_info.csv

This CSV file contains information about each video in the dataset.

| Column Name           | Type   | Example        | Description                                                                   |
| --------------------- | ------ | -------------- | ----------------------------------------------------------------------------- |
| `video_id`            | str    | `P01_01`       | ID of the video.                                                              |
| `duration`            | float  | `201.134`      | Duration of the video in seconds.                                             |
| `fps`                 | float  | `50.0`         | FPS of the video.                                                             |
| `resolution`          | str    | `1920x1080`    | Resolution of the video `width x height`.                                     |

[Back to Important Files](#important-files)

[back to top](#index)

## Additional Information

### Frame indexing

All frame indices are 0 indexed.

### File Downloads

Due to the size of the dataset we provide a script for downloading parts of the dataset which can be found [here](https://github.com/epic-kitchens/download-scripts-100).
If you wish to download the extension only (i.e. you have already downloaded EPIC-KITCHENS-55) the following command can be run:
```bash
python epic_downloader.py --extension-only
```

If you wish to download the whole dataset, the following command can be run:
```bash
python epic_downloader.py
```

See the [README](https://github.com/epic-kitchens/download-scripts-100/blob/master/README.md) for more information.

#### Automatic Annotations Download

We also provide automatic annotations in the form of object masks extracted through the use of MaskRCNN and hand-object BBoxes from [ddshan/Hand_Object_Detector](https://github.com/ddshan/Hand_Object_Detector)
([CVPR
2020](https://openaccess.thecvf.com/content_CVPR_2020/html/Shan_Understanding_Human_Hands_in_Contact_at_Internet_Scale_CVPR_2020_paper.html)).

The masks can be downloaded from [data.bris](https://data.bris.ac.uk/data/dataset/3l8eci2oqgst92n14w2yqi5ytu) and a supporting library is available from [this repo](https://github.com/epic-kitchens/epic-kitchens-100-object-masks).

The hand-object bboxes can be downloaded from [data.bris](https://data.bris.ac.uk/data/dataset/3l8eci2oqgst92n14w2yqi5ytu) and a supporting library is available from [this repo](https://github.com/epic-kitchens/epic-kitchens-100-hand-object-bboxes).

### Differences to EPIC-Kitchen-55

#### Updated Annotations

Whilst videos from EPIC-KITCHENS-55 are used within EPIC-KITCHENS-100 some of the annotations have been modified to improve the quality of the annotations. Additionally, with EPIC-KITCHENS-100, the verb/noun classes have been updated to cover the annotations from the new videos. Because of this, the annotations from EPIC-KITCHENS-55 cannot be used for EPIC-KITCHENS-100.


#### Missing Narration Timestamps

Due to the differences in the annotation pipeline between EPIC-KITCHENS-100 and EPIC-KITCHENS-55, it was impossible to assign the narration timestamp to every action. Because of this, there are actions within [EPIC_100_train.csv](#epic_100_traincsv) and [EPIC_100_validation.csv](#epic_100_validationcsv) which do not have timestamp narrations and are thus marked with NaN within the dataframes.

### Pickle Files

We also provide pickle files for all of the main train/val/test csvs for ease of use. These files require python 3.5+ and pandas 1.0.0+ to read.
The pickle files are automatically tagged with the commit hash and version for version control purposes which can be found in python using the following commands:

```
>>> import pandas as pd
>>> train = pd.read_pickle('EPIC_100_train.pkl')
>>> train._metadata
{'commit_hash': 'ce7a0fb', 'version_number': '1.0.0'
```

showing that this version of the `EPIC_100_train.pkl` came from commit hash ce7a0fb and version number 1.0.0.

[back to top](#index)

## License
All files in this dataset are copyright by us and published under the 
Creative Commons Attribution-NonCommerial 4.0 International License, found 
[here](https://creativecommons.org/licenses/by-nc/4.0/).
This means that you must give appropriate credit, provide a link to the license,
and indicate if changes were made. You may do so in any reasonable manner,
but not in any way that suggests the licensor endorses you or your use. You
may not use the material for commercial purposes.

[back to top](#index)

## Disclaimer
EPIC-KITCHENS-55 and EPIC-KITCHENS-100 were collected as a tool for research in computer vision, however, it is worth noting that the dataset may have unintended biases (including those of a societal, gender or racial nature).

[back to top](#index)

## Changelog
Please see the [release history](https://github.com/epic-kitchens/EPIC-KITCHENS-100-Annotations/releases) for the changelog.

Current Version 1.1.0.

[back to top](#index)
