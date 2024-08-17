# Simple Demo

## Quick Start

1. Clone the repo

```bash
git clone https://github.com/coleYab/proto
cd proto
```

2. setup your virtual enviroment and install flask on it
```
virtualenv .venv
source .venv/bin/activate
pip3 install flask
```

3. Run the application like this
```bash
python3 main.py
```

## Documentation
1. To get all users go to chrome and request
http://127.0.0.1:5000/users/

2. To get individual users got to chrome and request to this url
http://127.0.0.1:5000/users/<id>

3. to get the data of lost id replace user with
http://127.0.0.1:5000/lostIds

4. to get individual ids
http://127.0.0.1:5000/lostIds/<id>
