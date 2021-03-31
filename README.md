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



| DSID   | process | mass | width | ct    | theta | decay chain            | reweight |
| ------ | ------- | ---- | ----- | ----- | ----- | ---------------------- | -------- |
| 151000 | restt   | 1000 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151001 | restt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151002 | restt   | 1000 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151003 | restt   | 1000 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151004 | restt   | 1250 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151005 | restt   | 1250 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151006 | restt   | 1250 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151007 | restt   | 1250 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151008 | restt   | 1500 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151009 | restt   | 1500 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151010 | restt   | 1500 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151011 | restt   | 1500 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151012 | restt   | 2000 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151013 | restt   | 2000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151014 | restt   | 2000 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151015 | restt   | 2000 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151016 | restt   | 1000 | AUTO  |  1.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151017 | restt   | 1000 | AUTO  |  2.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151018 | restt   | 1000 | AUTO  |  3.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151019 | restt   | 1250 | AUTO  |  1.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151020 | restt   | 1250 | AUTO  |  2.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151021 | restt   | 1250 | AUTO  |  3.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151022 | restt   | 1500 | AUTO  |  1.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151023 | restt   | 1500 | AUTO  |  2.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151024 | restt   | 1500 | AUTO  |  3.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151025 | restt   | 2000 | AUTO  |  1.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151026 | restt   | 2000 | AUTO  |  2.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 151027 | restt   | 2000 | AUTO  |  3.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |


| DSID   | process | mass | width | ct   | theta | decay chain            | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| 152000 | resjt   | 1000 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152001 | resjt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152002 | resjt   | 1000 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 152003 | resjt   | 1000 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |



| DSID   | process | mass | width | ct   | theta | decay chain            | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | ---------------------- | -------- |
| 153000 | reswt   | 1000 | AUTO  |  0.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153001 | reswt   | 1000 | AUTO  |  1.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153002 | reswt   | 1000 | AUTO  |  2.5 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |
| 153003 | reswt   | 1000 | AUTO  |  5.0 |  pi/4 | p > v1 t t~, v1 > t t~ | no       |



| DSID   | process | mass | width | ct   | theta | decay chain                       | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | --------------------------------- | -------- |
| 154000 | tttt    | 1000 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154001 | tttt    | 1000 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154002 | tttt    | 1000 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154003 | tttt    | 1000 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154004 | tttt    | 1250 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154005 | tttt    | 1250 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154006 | tttt    | 1250 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154007 | tttt    | 1250 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154008 | tttt    | 1500 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154009 | tttt    | 1500 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154010 | tttt    | 1500 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154011 | tttt    | 1500 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154012 | tttt    | 2000 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154013 | tttt    | 2000 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154014 | tttt    | 2000 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154015 | tttt    | 2000 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154016 | tttt    | 1000 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154017 | tttt    | 1000 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154018 | tttt    | 1000 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154019 | tttt    | 1250 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154020 | tttt    | 1250 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154021 | tttt    | 1250 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154022 | tttt    | 1500 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154023 | tttt    | 1500 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154024 | tttt    | 1500 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154025 | tttt    | 2000 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154026 | tttt    | 2000 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |
| 154027 | tttt    | 2000 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=2 Qv1<=2 QED=0 | no       |



| DSID   | process | mass | width | ct   | theta | decay chain                       | reweight |
| ------ | ------- | ---- | ----- | ---- | ----- | --------------------------------- | -------- |
| 155000 | ttttsm  | 1000 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155001 | ttttsm  | 1000 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155002 | ttttsm  | 1000 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155003 | ttttsm  | 1000 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155004 | ttttsm  | 1000 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155005 | ttttsm  | 1000 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155006 | ttttsm  | 1000 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155007 | ttttsm  | 1250 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155008 | ttttsm  | 1250 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155009 | ttttsm  | 1250 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155010 | ttttsm  | 1250 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155011 | ttttsm  | 1250 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155012 | ttttsm  | 1250 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155013 | ttttsm  | 1250 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155014 | ttttsm  | 1500 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155015 | ttttsm  | 1500 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155016 | ttttsm  | 1500 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155017 | ttttsm  | 1500 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155018 | ttttsm  | 1500 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155019 | ttttsm  | 1500 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155020 | ttttsm  | 1500 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155021 | ttttsm  | 2000 | AUTO  |  0.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155022 | ttttsm  | 2000 | AUTO  |  1.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155023 | ttttsm  | 2000 | AUTO  |  1.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155024 | ttttsm  | 2000 | AUTO  |  2.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155025 | ttttsm  | 2000 | AUTO  |  2.5 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155026 | ttttsm  | 2000 | AUTO  |  3.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
| 155027 | ttttsm  | 2000 | AUTO  |  5.0 |  pi/4 | p > t t~ t t~ QCD<=4 Qv1<=2 QED=0 | no       |
