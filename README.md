# EPIC Kitchens 100 Dataset

<!-- start badges -->

<!-- wnd badges -->

> [EPIC-Kitchens-100](https://epic-kitchens.github.io/) is the largest dataset in first-person (egocentric) vision; itself an extension of the [EPIC-Kitchens-55 dataset](https://github.com/epic-kitchens/annotations).

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

**Contact:** [uob-epic-kitchens2018@bristol.ac.uk](mailto:uob-epic-kitchens2018@bristol.ac.uk) <!-- TODO, should this be changed/renamed? -->

## Citing
When using the dataset, kindly reference:

TBA

## Dataset Details
The EPIC-Kitchens-100 dataset is an extension of the EPIC-Kitchens-55 dataset. Videos are distinguished as follows:

* `PXX_YY.MP4` videos originate from EPIC-Kitchens-55.
* `PXX_1YY.MP4` videos originate from the extension collected for EPIC-Kitchens-100 (thus represent new videos).


The dataset currently has 6 active benchmarks:

* Action Recognition
* Weakly Supervised Action Recognition
* Action Detection
* Action Anticipation
* Unsupervised Domain Adaptation
* Action Retrieval

We provide csv files for the train/val/test sets of each benchmark detailed below for ease of use.

Ground truth is provided for action segments as action/verb/noun labels along with the start and end times of the segment.


## Quick Start

Here you can download the annotation files for all of the challenges. For more information on each challenge, please see the paper [here]().
Download scripts are provided for the [videos](), [RGB Frames]() and [Flow frames]().

### Action Recognition Challenge
Download the Action Recognition [train]()/[val]()/[test]() files.

### Weakly Supervised Action Recognition Challenge
This challenge uses the Action Recognition files, download the [train]()/[val]()/[test]() files.

### Action Detection Challenge
This challenge uses the Action Recognition files, download the [train]()/[val]()/[test]() files.

### Action Anticipation Challenge
This challenge uses the Action Recognition files, download the [train]()/[val]()/[test]() files.

### Unsupervised Domain Adaptation Challenge
Download the Unsupervised Domain Adaptation [source train]()/[target train]()/[target test]() files.

### Action Retrieval Challenge
Download the Action Retrieval [train]()/[test]() files.


## Important Files

We direct the reader to [RDSF]() for the videos and RGB/Flow frames. For ease of use, download scripts are [provided]() (see [here](#file_downloads) for more details).
We provide html and pdf alternatives to this README which are auto-generated.

* `README.md (this file)`
* `README.pdf`
* `README.html`
* [`license.txt`](#license)
* [`EPIC_100_train.csv`](EPIC_100_train.csv) ([info](#epic_100_traincsv)) ([Pickle](EPIC_100_train.pkl))
* [`EPIC_100_val.csv`](EPIC_100_val.csv) ([info](#epic_100_valcsv)) ([Pickle](EPIC_100_val.pkl))
* [`EPIC_100_test.csv`](EPIC_100_test.csv) ([info](#epic_100_testcsv)) ([Pickle](EPIC_100_test.pkl))

### Additional Files

* [`EPIC_100_UDA_source_train`](EPIC_100_UDA_source_train.csv) ([info](#epic_100_UDA_source_traincsv)) ([Pickle](epic_100_source_train.pkl))
* [`EPIC_100_UDA_target_train`](EPIC_100_UDA_target_train.csv) ([info](#epic_100_UDA_target_traincsv)) ([Pickle](epic_100_target_train.pkl))
* [`EPIC_100_UDA_target_test`](EPIC_100_UDA_target_test.csv) ([info](#epic_100_UDA_target_testcsv)) ([Pickle](epic_100_target_test.pkl))
* [`EPIC_100_retrieval_train`](EPIC_100_retrieval_train.csv) ([info](#epic_100_retrieval_traincsv)) ([Pickle](epic_100_retrieval_train.pkl))
* [`EPIC_100_retrieval_test`](EPIC_100_retrieval_test.csv) ([info](#epic_100_retrieval_testcsv)) ([Pickle](epic_100_retrieval_test.pkl))

## File Structure

#### EPIC_100_train.csv

This CSV file contains the action annotations for the training set and contains 15 columns:

| Column Name           | Type                       | Example        | Description                                                                   |
| --------------------- | ---------------------------| -------------- | ----------------------------------------------------------------------------- |
| `narration_id`        | string                     | `P01_01_0`     | Unique ID for the segment which includes participant ID and video ID.         |
| `participant_id`      | int                        | `P01`          | ID of the participant (unique per participant).                               |
| `video_id`            | string                     | `P01_01`       | ID of the video where the segment originated from (unique per video).         |
| `start_timestamp`     | string                     | `00:00:00.14`  | Start time in `HH:mm:ss.SSS` of the action segment.                           |
| `stop_timestamp`      | string                     | `00:00:03.37`  | End time in `HH:mm:ss.SSS` of the action segment.                             |
| `start_frame`         | int                        | `8`            | Start frame of the action.                                                    |
| `stop_frame`          | int                        | `202`          | End frame of the action.                                                      |
| `narration_timestamp` | string                     | `00:00:01.089` | Timestamp of when the original narration was recorded in `HH:mm:ss:SSS`.      |
| `narration`           | string                     | `open door`    | Transcribed description of the English narration provided by the participant. |
| `verb`                | string                     | `open`         | Parsed verb from the narration.                                               |
| `verb_class`          | int                        | `3`            | Numeric ID of the verb's class.                                               |
| `noun`                | string                     | `door`         | First parsed noun from the narration.                                         |
| `noun_class`          | int                        | `3`            | Numeric ID of the first noun's class.                                         |
| `all_nouns`           | list of string (1 or more) | `[door]`       | List of all parsed nouns within the narration.                                |
| `all_noun_classes`    | list of int (1 or more)    | `[3]`          | Numeric ID of all of the parsed noun's classes.                               |


## Additional Information

### File Downloads

Due to the size of the dataset we provide scripts for downloading parts of the dataset:

* [videos]() (GB)
* [frames]() (GB)
  * [rgb-frames]() (GB)
  * [flow-frames]() (GB)

*Note: These scripts will work for Linux and Mac. For Windows users a bash 
installation should work.*

These scripts replicate the folder structure of the dataset release on RDSF, found 
[here]().

If you wish to download part of the dataset instructions can be found
[here]().

## License
All files in this dataset are copyright by us and published under the 
Creative Commons Attribution-NonCommerial 4.0 International License, found 
[here](https://creativecommons.org/licenses/by-nc/4.0/).
This means that you must give appropriate credit, provide a link to the license,
and indicate if changes were made. You may do so in any reasonable manner,
but not in any way that suggests the licensor endorses you or your use. You
may not use the material for commercial purposes.

## Changelog
Please see the [release history]() for the changelog.
