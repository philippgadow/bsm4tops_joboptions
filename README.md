## Development of BSM4tops job options in Atlas MC Generation releases 21.6.23 and later


### Run this example quickly
Run in release `21.6.58` (CC7)

```
git clone git@github.com:philippgadow/bsm4tops_joboptions.git
source setup.sh
source run.sh
```

### Batch submission
On DESY NAF run:

```
source setup_batch.sh
source run_batch.sh
```

### Modify job option

Take the job option [`150xxx/150000/MadGraphControl_TopPhilicG_4t_v2.py`](https://github.com/philippgadow/bsm4tops_joboptions/blob/master/150xxx/150000/MadGraphControl_TopPhilicG_4t_v2.py) to implement your changes for testing.
All other copies of that job option are symlinks to this file.

### Overview of samples

| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| DSID   | process | mass | width | ct   | theta | decay chain            | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| 150000 | restt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150001 | restt   | 1250 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150002 | restt   | 1500 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150003 | restt   | 2000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150004 | restt   | 2500 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150005 | restt   | 3000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150006 | resjt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150007 | resjt   | 1250 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150008 | resjt   | 1500 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150009 | resjt   | 2000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150010 | resjt   | 2500 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150011 | resjt   | 3000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150012 | reswt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150013 | reswt   | 1250 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150014 | reswt   | 1500 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150015 | reswt   | 2000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150016 | reswt   | 2500 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| 150017 | reswt   | 3000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | yes      |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |

| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| DSID   | process | mass | width | ct   | theta | decay chain            | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| 151000 | restt   | 1000 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151001 | restt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151002 | restt   | 1000 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151003 | restt   | 1000 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151004 | restt   | 1000 | AUTO  |  7.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151005 | restt   | 1000 | AUTO  | 10.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151006 | restt   | 1000 | AUTO  | 20.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151007 | restt   | 1000 | AUTO  | 50.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |

| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| DSID   | process | mass | width | ct   | theta | decay chain            | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| 152000 | resjt   | 1000 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152001 | resjt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152002 | resjt   | 1000 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152003 | resjt   | 1000 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152004 | resjt   | 1000 | AUTO  |  7.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152005 | resjt   | 1000 | AUTO  | 10.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152006 | resjt   | 1000 | AUTO  | 20.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152007 | resjt   | 1000 | AUTO  | 50.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |

| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| DSID   | process | mass | width | ct   | theta | decay chain            | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| 153000 | reswt   | 1000 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153001 | reswt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153002 | reswt   | 1000 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153003 | reswt   | 1000 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153004 | reswt   | 1000 | AUTO  |  7.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153005 | reswt   | 1000 | AUTO  | 10.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153006 | reswt   | 1000 | AUTO  | 20.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153007 | reswt   | 1000 | AUTO  | 50.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |

| ------ | ------- | ---- | ----- | ---- | ----- | -------------------------------- | -------- |
| DSID   | process | mass | width | ct   | theta | decay chain                      | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | -------------------------------- | -------- |
| 154000 | restt   | 1000 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1=2 QED=0 | no       |
| 154001 | restt   | 1000 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1=2 QED=0 | no       |
| 154002 | restt   | 1000 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1=2 QED=0 | no       |
| 154003 | restt   | 1000 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1=2 QED=0 | no       |
| ------ | ------- | ---- | ----- | ---- | ----- | -------------------------------- | -------- |
