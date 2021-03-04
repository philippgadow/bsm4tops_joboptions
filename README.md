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



